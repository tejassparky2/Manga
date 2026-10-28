# DEAD MAN'S ALGORITHM — approved continuation (v6): Game 3 "Find Yourself"

**Status: CONFIRMED CANON.**

- **Approved:** by the author on 2026-10-28 in this chat ("Approved, go with Haruto and Gō, draw it").
- **Source:** `story/proposals/game03_find_yourself.md` (v3), approved as written. Haruto is the betrayer and Gō the victim. Kota's possession of Saki's token is revealed in Part 12. Saki's locker stays sealed. Game 3 spans two chapters (Chapter 4 = Parts 7–9, Chapter 5 = Parts 10–12).
- **Derived figures** (Momo's 1,899 and the ledger) are arithmetic from canon numbers, marked as such.
- **The game's mathematical core** is the published "100 prisoners problem" (Gál and Miltersen, 2003).

## GAME 03 — FIND YOURSELF: the rules

**The rooms:**
- **Waiting room:** where everyone starts.
- **Locker room:** 20 lockers stand in a ring, each with a student's name plate. A painted line on the floor runs past every locker in one unbroken circle. Saki's locker is sealed.
- **Finished room:** where you go after your turn.

**The board:** a screen in every room shows each player's result as they finish: FOUND or NOT FOUND, and how many lockers they opened.

1. Nineteen lockers each hold one card with one player's name. Every name is in exactly one locker. Cards never leave the lockers.
2. Go in alone. Open up to ten lockers. Each token you spend opens one more, and spent tokens are gone. You may give tokens to anyone before they go in.
3. Find the card with your own name, and you live. If you don't, you die.
4. Before you leave, you may swap the cards in two lockers. Once.
5. Inside, Momo may make you a private offer.
6. Once you have been inside, you may not communicate with anyone who hasn't, in any way. Lockers close themselves when you leave.
7. Anyone who hasn't gone in when thirty minutes are up dies.

The death condition is literally true and invites panic. "Swap" looks like a weapon; it is the cure. Momo is bound by its own rules: its offers are announced in Rule 5 before anyone goes in.

---

## The logic, layer by layer

### Four answers fail on the page
1. **Open any ten** (Aoi). Each person has ten chances in nineteen. **On average, nine of us die.**
2. **"I'll open all nineteen"** (Riku). His 69 tokens make him safe, and nobody else. **The rich can't lose this game; only the poor can.**
3. **Follow the chain** (Ren's first idea, tested on Kota's notebook with five names; see below). It works only if no loop is longer than ten.
   - On a random arrangement, about six times in ten there is a long loop, and everyone in it dies together (exact: 61.9%).
   - Then the clue lands: Momo says "Everyone's connected!" and the floor line runs in one unbroken circle. **It's one loop of nineteen. Following the chain kills all nineteen.**
4. **Cut the loop** (Ren's second idea). Whoever opens ten without finding their name knows they're in the long loop. They swap the card in their **first** locker with the card in their **tenth**.
   - The loop breaks into one loop of 9 and one of at most 10 (19 − 9 = 10). Everyone after them lives.
   - **But the cutter dies, and with one big loop, the first person in is certain to be the cutter.** Gō volunteers: "If it's one loop, I'll be the one who cuts it."

### The real answer: tokens buy sight (Rules 2 + 4)
Ten free opens plus **nine tokens = all nineteen lockers.**
- **Going first:** whoever goes first with nine tokens sees the whole loop, finds their own name, and cuts the loop into 9 and 10.
- **Everyone after:** they follow the chain and find their name in 9 or 10. **Nobody dies.**
- **The catch:** only Riku has nine tokens.

**The toy example Ren draws** (five lockers A–E):
- **The arrangement:** locker A holds C, C holds E, E holds B, B holds D, D holds A.
- **B follows the chain:** B → D → A → C → E, and locker E holds "B".
- **Why it always works:** "Start at your own locker. The card that leads back to your locker is your own name."

### The deal, and its danger
Ren asks Riku for nine tokens so Gō, the volunteer, can go first with full sight. Riku refuses: "My tokens don't leave my hands. I go first."
- **Ren states the danger aloud:** whoever sees every locker can cut the loop wherever they like. They could deliberately leave a loop of eleven and choose who dies.
- **Riku's price:** "Eighteen lives for nine tokens. Every one of you owes me."
- **The class trusts him because the alternatives are worse:** nine deaths on average, or one certain death (the volunteer cutter), against none if Riku keeps his word.

### Ren's plan for everyone after Riku
1. Follow the chain.
2. If you find your name: touch nothing, take nothing, leave.
3. If you open ten and don't: cut, first locker with tenth.
4. Whatever Momo offers, say no.

### How it breaks
- **The offers:** inside, Momo shows each player a private offer, e.g. "Swap TACHIBANA and HAYASHI. Thirty tokens! Nobody will know!"
- **Momo picks the lockers.** It arranged the lockers and watches every swap, so it can name two lockers in different loops. Swapping them joins the two loops back into one loop of nineteen.
- **Haruto takes it.**
- **Gō, next in line, opens ten and doesn't find his name.** He cuts the loop as promised, and dies.
- **Everyone behind Gō lives because of his cut.**

### Ren's proof (the counting fact, planted twice)
**The fact:** if anyone finds their name in **9 or 10** opens, no loop longer than 10 exists at that moment. Their loop uses 9 or 10 of the 19 lockers; a second loop of 11 would need 20 or 21.

**What the board showed:**
- **Riku:** opened all 19.
- **Ren (2nd):** found in 9. *So Riku kept his word.*
- **Everyone from 3rd to 9th, Haruto included:** found in 9 or 10. *So there was still no long loop when Haruto went in.*
- **Gō (10th):** not found. *So there was a long loop when Gō went in.*
- **Kota (11th) and everyone after:** found in 9 or 10. *So Gō cut it before he died.*

The only person inside between "no long loop" and "long loop" was Haruto. Haruto's pockets hold 30 tokens.

*(All of this was confirmed by simulation: a cross-loop swap at position 9 gives exactly one death, at position 10, and every success shows 9 or 10.)*

---

## The script (Parts 7–12), in v5's format

### Chapter 4

#### Part 7: "Find Yourself"
1. A door opened in the white room. Nobody moved first.
2. *(Panel, no words: a hand in a black sleeve picks up Saki's token and slides it between the pages of a small notebook.)*
3. Nobody saw who took it. *(Ren narrates. The reader sees the notebook; Ren doesn't.)*
4. Three rooms. In the middle one, twenty lockers stood in a ring. Every one had a name on it.
5. One said NISHIDA SAKI. It was sealed shut.
6. A line was painted on the floor. It ran past every locker, all the way around, without a break.
7. (Momo) Game three! Find Yourself!
8. (Momo) Nineteen lockers! Each one holds one card, with one of your names!
9. (Momo) Go in alone. Open ten lockers. Find your own name, and you live! Don't, and you die!
10. (Momo) Each token you spend opens one more! You can give tokens away before someone goes in!
11. (Momo) Before you leave, you may swap the cards in two lockers. Once!
12. (Momo) Inside, Momo might whisper you an offer!
13. (Momo) After you go in, no talking to anyone who hasn't. No signs, no notes, nothing! Thirty minutes!
14. (Momo) And Momo set them up special. Everyone's connected!
15. *(The board lights up: 19 names, all blank.)*
16. (Aoi) Ten lockers out of nineteen. On average, nine of us die.
17. (Haruto) Great. Half a class.
18. (Riku) Speak for yourselves. Sixty-nine tokens. I open all nineteen.
19. Riku couldn't lose this game. Only we could.

#### Part 8: "The Chain"
1. (Mio) Then he walks out, and we flip coins.
2. I needed paper.
3. (Ren) Kota. Can I have a page?
4. *(Kota hesitates. He tears one out carefully, keeping the notebook shut.)*
5. *(Ren draws five lockers, A to E, and arrows.)*
6. (Ren) Start at your own locker. The card tells you which locker to open next.
7. (Ren) Every card points somewhere. Follow them and you go round in a loop.
8. (Ren) And the card that leads back to your own locker... is your name.
9. (Haruto) So we just follow the arrows?
10. (Aoi) If your loop is ten or shorter, you find it. If it's longer, everyone in that loop dies together.
11. (Aoi) Random lockers... About six times in ten, there's a long loop.
12. "Everyone's connected." I looked at the line on the floor. One circle. No breaks.
13. (Ren) It's not random. It's one loop. All nineteen of us.
14. (Aoi) Then everyone opens ten... and nobody gets there.
15. Nineteen is longer than ten.
16. Every one of us would die.

#### Part 9: "Cut the Loop"
1. Then I read rule four again. Swap two cards.
2. (Ren) Whoever opens ten and doesn't find their name knows it's the long loop.
3. (Ren) Swap the card in your first locker with the card in your tenth. The loop breaks in two.
4. (Ren) One loop of nine. The other is what's left. Nineteen minus nine is ten.
5. (Aoi) Ten or shorter. Everyone after you finds their name.
6. (Ren) Except the one who cuts it.
7. Silence.
8. (Gō) Then I go first. If it's one loop, I'll be the one who cuts it.
9. *(Kota grabs Gō's sleeve.)* (Gō, quietly) Stay behind me.
10. Ten free. Nine more makes nineteen. Whoever goes first with nine tokens sees everything.
11. (Ren) Nobody has to die. Riku. Give Gō nine tokens.
12. (Riku) My tokens don't leave my hands. I go first.
13. (Mio) Then he decides who dies.
14. (Ren) If he sees every locker, he can cut the loop anywhere. He could leave a loop of eleven. On purpose.
15. (Riku) Or I save all of you.
16. (Riku) Eighteen lives for nine tokens. Every one of you owes me.
17. Nine of us dead on average. One of us dead for sure. Or none of us, if he keeps his word.
18. (Ren) He goes first. I go second. I'll know if he lied.
19. (Riku) You'll know.
20. (Ren) Everyone else: follow the chain. Find your name, touch nothing. Fail, cut first and tenth.
21. (Ren) And whatever Momo offers you... say no.
22. *(Riku walks to the locker-room door and looks back.)* (Riku) Remember. You owe me.

### Chapter 5

#### Part 10: "The Offer"
1. *(Board: KANZAKI RIKU — OPENED 19 — FOUND)*
2. My turn.
3. My locker. A card. A name. The next locker. Another name.
4. Seven. Eight. Nine. KURODA REN.
5. Nine. A loop of nine leaves ten lockers. There's no room left for a loop longer than ten.
6. He kept his word.
7. *(A small screen in the locker room lights up.)* (Momo) Psst! Swap TACHIBANA and HAYASHI. Thirty tokens! Nobody will know!
8. I didn't touch anything.
9. Then I understood. Momo wasn't only asking me.
10. *(The finished room. Riku is sitting alone.)*
11. (Riku) Disappointed?
12. (Ren) It offered you something.
13. (Riku) Fifty. To leave the loop whole.
14. (Ren) Why didn't you take it?
15. (Riku) Dead people don't owe me anything.
16. *(Board: KURODA REN — FOUND — 9)*
17. Seventeen people were waiting to be offered a price for someone's life.
18. And I couldn't say a word.

#### Part 11: "Not Found"
1. *(Board: TACHIBANA YUI — FOUND — 10)*
2. (Yui, arriving) It offered me tokens. I said no.
3. *(Board: FUJIMOTO AOI — FOUND — 9. AOYAMA MIO — FOUND — 10.)* (Aoi) Me too. (Mio) Same.
4. Everyone said no. Nobody could prove it.
5. *(Three more students arrive. Nines and tens on the board.)*
6. *(Board: SAKURAI HARUTO — FOUND — 10)*
7. Haruto came in and sat by the wall. He didn't make a joke.
8. (Yui) Haruto?
9. *(Haruto smiles. It doesn't reach his eyes.)*
10. *(Board: SHIBATA GŌ — NOT FOUND — 10)*
11. *(The waiting room. Kota stares at the board. Students shout: "Riku lied!" "It's still one loop!")*
12. Gō had told him to stay behind him. Kota was next.
13. *(Kota walks in alone.)*
14. *(Board: HAYASHI KOTA — FOUND — 9)*
15. *(The finished room. Every head turns to Riku.)*
16. (Riku) Don't look at me. Look at the board.
17. *(Momo, on every screen.)* (Momo) Momo knows who swapped! Do you?

#### Part 12: "Thirty Tokens"
1. *(Board, final: 18 FOUND. 1 NOT FOUND.)*
2. *(Everyone back in the ring. Two lockers dark now.)*
3. (Mio, at Riku) You left a long loop.
4. (Ren) No. He didn't.
5. (Ren) I found mine in nine. A loop of nine leaves ten lockers. No room for a loop longer than ten.
6. (Ren) Everyone up to the ninth person found theirs in nine or ten. Still no long loop.
7. (Ren) Gō went in tenth. He didn't find his in ten. Now there was a long loop.
8. (Ren) Only one person went in between them.
9. *(Everyone turns.)*
10. (Ren) Haruto. Turn out your pockets.
11. *(Thirty coins spill onto the floor.)*
12. (Mio) And Kota. You always hold that notebook.
13. *(Kota opens it. One coin.)* (Kota) It was hers.
14. (Haruto) Momo said nobody would know.
15. (Haruto) Riku had fixed everything. One swap. I thought... maybe they were in the same loop.
16. (Haruto) Next game, I'd have something. I could've kept you and Yui alive.
17. Momo paid him with the tokens we gave it for Saki.
18. (Ren) Kota found his in nine. Gō cut the loop before he died.
19. Gō's last swap saved the nine people behind him.
20. (Riku) Eighteen alive. Nine tokens. You all owe me.
21. On the first day, Haruto said he was building a sustainable business model.
22. Today he sold Gō for thirty tokens.
23. The boy who killed Saki kept his word. My best friend broke his.
24. I didn't know anyone in this room anymore.
25. (Momo) Eighteen players! Momo loves a smaller loop!

---

## State after Game 3 (if approved)

| | |
|---|---|
| **Survivors** | 18 (Gō dead) |
| **Riku** | 60 tokens |
| **Haruto** | 30 tokens |
| **Kota** | 1 token (Saki's) |
| **Everyone else** | 0 |
| **Momo** | 1,869 (paid 30 to Haruto) |
| **Spent so far** | 40 (31 in Game 1 + Riku's 9) |
| **Total check** | 1,869 + 60 + 30 + 1 + 40 = **2,000** ✓ |
| **Relationships** | The class owes Riku. Ren and Haruto are broken. Kota has lost Gō. |

---
