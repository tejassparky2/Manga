"""Check the numbers for a locker/loop game: 19 lockers, 10 opens each."""
import random
from fractions import Fraction
from math import comb

N, K = 19, 10

def cycles(perm):
    seen, out = set(), []
    for s in range(len(perm)):
        if s in seen: continue
        c, x = [], s
        while x not in seen:
            seen.add(x); c.append(x); x = perm[x]
        out.append(c)
    return out

def follow(perm, p, k):
    """Loop strategy: start at own locker. Return opens used if found within k, else None."""
    x = p
    for n in range(1, k + 1):
        card = perm[x]
        if card == p: return n
        x = card
    return None

# 1. Random opening: each player finds own name with prob K/N.
print("random: expected deaths =", Fraction(N - K, N) * N)

# 2. Loop strategy on a random arrangement (exact): P(no cycle > K) = 1 - sum_{L=K+1..N} 1/L
p_long = sum(Fraction(1, L) for L in range(K + 1, N + 1))
print("loop strategy: P(all live) =", float(1 - p_long), " P(a long loop) =", float(p_long))
print("loop strategy: expected deaths =", sum(Fraction(1, L) * L for L in range(K + 1, N + 1)))

# Monte Carlo cross-check
rng = random.Random(1)
trials, alive_all = 200000, 0
for _ in range(trials):
    perm = list(range(N)); rng.shuffle(perm)
    if max(len(c) for c in cycles(perm)) <= K: alive_all += 1
print("  monte carlo P(all live) =", alive_all / trials)

# 3. Momo's single 19-loop: plain loop strategy kills everyone.
order = list(range(N)); rng.shuffle(order)
single = [0] * N
for i in range(N): single[order[i]] = order[(i + 1) % N]
assert len(cycles(single)) == 1
print("single loop, plain loop strategy: deaths =", sum(follow(single, p, K) is None for p in range(N)))

# 4. Split rule: if you fail after 10 opens, swap the card in your own locker
#    with the card in the last locker you opened. Check on every possible long loop length.
def play(perm, entry, plan_split=True, saboteur=None, sab_swap=None, sight=None):
    perm = perm[:]; log = []
    for who in entry:
        if who == sight:                           # sees everything with tokens, splits any long loop
            for c in cycles(perm):
                if len(c) > K:                     # split c into a 9 and the rest
                    a, b = c[0], c[9]                  # loops c1..c9 (9) and c0,c10.. (L-9 <= 10)
                    perm[a], perm[b] = perm[b], perm[a]
            log.append((who, 'SIGHT')); continue
        n = follow(perm, who, K)
        if n is None:
            log.append((who, 'NOT FOUND'))
            if plan_split:                         # first locker = own, last = 10th opened
                path = [who]; x = who
                for _ in range(K - 1): x = perm[x]; path.append(x)
                a, b = path[0], path[-1]
                perm[a], perm[b] = perm[b], perm[a]
        else:
            log.append((who, n))
            if who == saboteur:
                a, b = sab_swap(perm)
                perm[a], perm[b] = perm[b], perm[a]
    return log, perm

ok = True
for L in range(K + 1, N + 1):
    for _ in range(300):
        perm = list(range(N)); rng.shuffle(perm)
        # force one cycle of length L containing a random start, rest random small
        nodes = list(range(N)); rng.shuffle(nodes)
        cyc, rest = nodes[:L], nodes[L:]
        perm = [None] * N
        for i in range(L): perm[cyc[i]] = cyc[(i + 1) % L]
        rp = rest[:]; rng.shuffle(rp)
        for a, b in zip(rest, rp): perm[a] = b
        # rest may contain cycles; keep only arrangements with exactly one long loop
        if max(len(c) for c in cycles(perm)) != L: continue
        entry = list(range(N)); rng.shuffle(entry)
        log, _ = play(perm, entry)
        deaths = sum(r == 'NOT FOUND' for _, r in log)
        if deaths != 1: ok = False; print("FAIL split", L, deaths)
print("split rule: exactly one death for every long-loop length 11..19:", ok)

# 5. Full sight (9 tokens) first, then plain loop strategy + split rule: zero deaths.
ok = True
for _ in range(2000):
    perm = list(range(N)); rng.shuffle(perm)
    entry = list(range(N)); rng.shuffle(entry)
    log, _ = play(perm, entry, sight=entry[0])
    if any(r == 'NOT FOUND' for _, r in log): ok = False
print("full sight first: zero deaths in 2000 random arrangements:", ok)
print("tokens needed for full sight:", N - K)

# 6. Story run: single 19-loop, Riku (sight) first, then a merging swap by player at position h,
#    the next player dies and splits, everyone after lives. Steps of every success are 9 or 10.
riku = order[0]
entry = [riku] + [p for p in order if p != riku]
rng.shuffle(entry[1:])
entry = [riku] + entry[1:]
h = 8                                            # saboteur position (0-based) in entry
saboteur = entry[h]
def merge(perm):                                 # swap two lockers on different loops
    cs = cycles(perm)
    big = sorted(cs, key=len)[-2:]
    return big[0][0], big[1][0]
log, final = play(single, entry, saboteur=saboteur, sab_swap=merge, sight=riku)
for i, (who, r) in enumerate(log):
    print(f"  {i+1:2}. player {who:2} -> {r}")
print("deaths:", sum(r == 'NOT FOUND' for _, r in log),
      "| final loop sizes:", sorted(len(c) for c in cycles(final)))
# Pigeonhole: a loop of 9 or 10 leaves at most 10 or 9 other lockers, so no loop over 10 can exist.
print("pigeonhole: 9 + 11 =", 9 + 11, "> 19 and 10 + 11 =", 10 + 11, "> 19")

# 7. Pigeonhole proof check: whenever a loop-follower finds their name in 9 or 10 opens,
#    no loop longer than 10 exists at that moment.
viol = 0
for _ in range(20000):
    perm = list(range(N)); rng.shuffle(perm)
    for p in range(N):
        n = follow(perm, p, K)
        if n in (9, 10) and max(len(c) for c in cycles(perm)) > K: viol += 1
print("pigeonhole check violations:", viol)

# 8. Reader question: if every player who finds their name then swaps it into their own
#    locker (taking themselves out of the loop), does a merge at position 9 still kill?
def play_selffix(perm, entry, saboteur_pos, sight):
    perm = perm[:]; log = []
    for i, who in enumerate(entry):
        if who == sight:
            for c in cycles(perm):
                if len(c) > K:
                    a, b = c[0], c[9]; perm[a], perm[b] = perm[b], perm[a]
            log.append((who, 'SIGHT')); continue
        n = follow(perm, who, K)
        if n is None:
            log.append((who, 'NOT FOUND'))
            path = [who]; x = who
            for _ in range(K - 1): x = perm[x]; path.append(x)
            perm[path[0]], perm[path[-1]] = perm[path[-1]], perm[path[0]]
            continue
        log.append((who, n))
        if i == saboteur_pos:                       # merge the two largest open loops
            cs = sorted([c for c in cycles(perm) if len(c) > 1], key=len)
            if len(cs) >= 2:
                a, b = cs[-1][0], cs[-2][0]; perm[a], perm[b] = perm[b], perm[a]
        else:                                       # self-fix: put own card in own locker
            holder = next(j for j in range(N) if perm[j] == who)
            perm[who], perm[holder] = perm[holder], perm[who]
    return log
deaths = []
for _ in range(500):
    o = list(range(N)); rng.shuffle(o)
    single = [0] * N
    for i in range(N): single[o[i]] = o[(i + 1) % N]
    entry = o[:]; rng.shuffle(entry)
    log = play_selffix(single, entry, 8, entry[0])
    deaths.append(sum(r == 'NOT FOUND' for _, r in log))
print("self-fix plan, merge at position 9: deaths min/max =", min(deaths), max(deaths))

# 9. Ledger for the story: start 2,000; Game 1 spent 31; Riku spends 9 to open all 19;
#    Momo pays 30 from its 1,899 for the merging swap.
momo, riku, kota, haruto, spent = 1899, 69 - 9, 1, 30, 31 + 9
momo -= 30
print("ledger: Momo", momo, "Riku", riku, "Haruto", haruto, "Kota", kota, "spent", spent,
      "total", momo + riku + haruto + kota + spent)
