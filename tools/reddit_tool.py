"""Search Reddit and read threads via Reddit's official OAuth API (redditwarp).

Run with the mcp-reddit tool's Python:
  /root/.local/share/uv/tools/mcp-reddit-server/bin/python tools/reddit_tool.py search "ai manga workflow" --sr StableDiffusion --sort top --time year -n 10
  /root/.local/share/uv/tools/mcp-reddit-server/bin/python tools/reddit_tool.py post 1abc23 --comments 15 --depth 2
Use --sr "" (default) to search all of Reddit.
"""
import argparse
import asyncio
import os

from redditwarp.ASYNC import Client
from redditwarp.models.submission_ASYNC import LinkPost, TextPost, GalleryPost

creds = [v for v in (os.getenv("REDDIT_CLIENT_ID"), os.getenv("REDDIT_CLIENT_SECRET"), os.getenv("REDDIT_REFRESH_TOKEN")) if v]


def body_of(s, limit):
    if isinstance(s, TextPost):
        return (s.body or "")[:limit]
    if isinstance(s, LinkPost):
        return f"[link] {s.link}"
    if isinstance(s, GalleryPost):
        return "[gallery]"
    return ""


def header(s):
    sr = getattr(getattr(s, "subreddit", None), "name", "?")
    date = s.created_at.date().isoformat() if getattr(s, "created_at", None) else "?"
    return (f"id={s.id36} r/{sr} {date} score={s.score} comments={s.comment_count}\n"
            f"title: {s.title}\nurl: {s.permalink if s.permalink.startswith('http') else 'https://www.reddit.com' + s.permalink}")


async def search(a):
    client = Client(*creds)
    async with client:
        async for s in client.p.submission.search(a.sr, a.query, a.n, sort=a.sort, time=a.time):
            print(header(s))
            text = body_of(s, a.chars).replace("\n", " ")
            if text:
                print(f"body: {text}")
            print("---")


def walk(node, depth, out, chars):
    c = node.value
    out.append(f"{'  ' * depth}- [{c.score}] {c.author_display_name or '[deleted]'} "
               f"({c.created_at.date().isoformat()}): {c.body[:chars].replace(chr(10), ' ')}")
    for child in node.children:
        walk(child, depth + 1, out, chars)


async def post(a):
    client = Client(*creds)
    async with client:
        s = await client.p.submission.fetch(a.id)
        print(header(s))
        print(f"body: {body_of(s, 20000)}\n\nComments (top):")
        tree = await client.p.comment_tree.fetch(a.id, sort="top", limit=a.comments, depth=a.depth)
        out = []
        for node in tree.children:
            walk(node, 0, out, a.chars)
        print("\n".join(out) or "No comments.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--sr", default="", help="subreddit name; empty = all of Reddit")
    s.add_argument("--sort", default="relevance", choices=["relevance", "hot", "top", "new", "comments"])
    s.add_argument("--time", default="all", choices=["all", "hour", "day", "week", "month", "year"])
    s.add_argument("-n", type=int, default=10)
    s.add_argument("--chars", type=int, default=400)
    p = sub.add_parser("post")
    p.add_argument("id", help="post id36, e.g. 1abc23")
    p.add_argument("--comments", type=int, default=15)
    p.add_argument("--depth", type=int, default=2)
    p.add_argument("--chars", type=int, default=800)
    a = ap.parse_args()
    asyncio.run(search(a) if a.cmd == "search" else post(a))


if __name__ == "__main__":
    main()
