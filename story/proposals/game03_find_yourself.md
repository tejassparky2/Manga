# DEAD MAN'S ALGORITHM — Game 3 proposal v3: "Find Yourself"

**Status: PROPOSAL — NOT CANON.** None of it is canon until you approve it in this chat. Nothing gets drawn before that.

- **Replaces:** v1/v2 "The Verdict" (`game03_the_verdict.md`). You said that game was too simple and its escape was written into a rule ("if tied, nobody dies"). This version has no escape rule. The way out is hidden in what the rules *allow*.
- **Requested:** 2026-10-28. "The loophole should be hard and clever to find… more tension, more dark, more psychology, more clever, more hard", with references like Tomodachi Game, Alice in Borderland and The Genius. Then: "Both game and story should be psychological, hard, thrilling, tension, clever, good plots, mysterious, human emotions, playing with mind."
- **Would become:** two chapters (Ch4 + Ch5, about 40 pages), as story Parts 7–12. Each part ends on a hook, so each one can be its own video.

---

## 0. What the research says, and how this game uses it

Five research passes, each with a source link beside every claim, are saved in `research_notes/death_games/` (`alice_in_borderland.md`, `liar_game.md`, `the_genius.md`, `tomodachi_and_others.md`, `craft_and_theory.md`).

| What makes the best games work (source) | How "Find Yourself" uses it |
|---|---|
| Hide the way out in a *permission* or a definition, never in a rule that states it (Alice in Borderland). | The rules only *allow* two things: spending tokens to open more lockers, and swapping two cards. Together they save everyone. No rule says so. |
| Hide each player's most vital fact from themselves (Alice in Borderland, Jack of Hearts). | You can't see where your own name is. |
| Arithmetic or object loopholes, with the numbers planted early (The Genius). | 19 lockers and 10 opens. One counting fact (a loop of 9 or 10 leaves no room for a loop over 10) proves who betrayed whom. |
| One person in the room at a time; cooperation possible but never provable (Liar Game, Pandemic). | You go in alone, and afterwards you can't tell anyone anything. |
| Private, uneven temptations (Tomodachi Game's secret bribe cards). | Inside, Momo makes each player a private offer. The rules say this up front. |
| Any one player can wreck the group (Tomodachi Game). | One swap by anyone can doom the next person in line. |
| The weakest moment is the hand-off, when one person holds everyone's fate (Tomodachi Game). | The first player can see every locker, and with one swap can save or doom anyone. |
| Show 2–3 wrong answers before the right one; let the hero test a theory on the page; no luck; plant every needed fact twice (craft). | Four answers fail on the page. Ren tests his idea on paper. Momo's arrangement is deliberate, not random. Each key fact appears twice. |
| Hide the betrayer inside the reader's pity; make the betrayal's *why* the payoff (craft, from Squid Game). | The betrayer is the funny best friend, acting out of fear. The reader is steered toward suspecting Riku and Kota. |
| Make deaths land: show the person's want and bond, foreshadow with a line, show the cost to the living (craft). | Gō promises to "be the one who cuts it", and dies doing exactly that. Kota is next in line. |

**The maths behind it:** the "100 prisoners problem", a published puzzle (Gál and Miltersen, 2003; [Wikipedia](https://en.wikipedia.org/wiki/100_prisoners_problem)). We use its known core: follow the chain, and one swap by someone who has seen everything saves all. The death game around it is original:
- Momo arranges one deliberate loop.
- The sacrifice swap is the "cut".
- Tokens buy sight.
- Private bribes tempt each player.
- A results board lets Ren expose the traitor.

**Every number in this document was checked by simulation** (19 lockers, 10 opens, thousands of arrangements).

---

## 1. Where Game 3 starts (canon)

| Fact | Source |
|---|---|
| 19 survivors. Saki is dead. | v5, Part 6 |
| Riku has 69 tokens. Every other survivor has 0. | v5 |
| Saki's one token is lying on the floor. | v5: "Her token lay on the floor." |
| Momo holds 1,899 tokens. | *Derived:* 2,000 − 31 spent − 69 − 1 |
| Momo: "Tokens are precious! You'll want them later!" Mio: "And walk into game three with nothing?" | v5, Game 2 |
| Riku took Kota's notebook in Ch1; Gō stopped him. Haruto joked he copies homework: "I'm building a sustainable business model." | Bible, Ch1 |

---

## 2. GAME 03 — FIND YOURSELF: the rules

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

## 3. The logic, layer by layer

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

## 4. The script (Parts 7–12), in v5's format

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

## 5. Why each person does what they do

| Character | What they do | Why (want, fear) |
|---|---|---|
| **Ren** | Finds the chain, then the cut, then the nine-token sight. Trusts Riku. Proves Riku honest and exposes Haruto. | He wants everyone alive and can do the maths. His limit: he can't make 18 frightened people resist a private offer, and Rule 6 means he can't warn them. |
| **Riku** | Refuses to hand over tokens, goes first, cuts honestly, refuses Momo's 50. | He wants control, not corpses: "Dead people don't owe me anything." Cruel, but rational and consistent. He mistakes cruelty for strength (bible 3.4), yet keeps his word: not a one-dimensional villain. |
| **Haruto** | Takes Momo's 30 tokens and swaps. | Fear: he walked into Game 3 with nothing ("You'll want them later"). He tells himself Riku fixed everything, so one swap can't matter. He even tells himself it's for Ren and Yui. His humour hides the fear until it breaks (bible 3.3). **New material (PROPOSAL).** |
| **Gō** | Volunteers to cut. Tells Kota "stay behind me". Cuts the loop when he fails. | Watchful, loyal, protects Kota since Ch1 (bible 3.6). He keeps his promise to the last move. |
| **Kota** | Took Saki's token. Gives Ren a page but keeps the notebook shut. Walks in right after Gō dies. | He wants to be left alone (bible 3.5); his reason for taking the token stays ambiguous ("It was hers"). |
| **Yui** | Notices Haruto's fake smile. | She notices when someone is hiding something (bible 3.2). |
| **Aoi** | Gives every number; states the "no room for a long loop" fact. | Analytical; reads exactly (bible 3.7). |
| **Mio** | Distrusts Riku, then accuses him. Remembers Kota's notebook. | Socially perceptive and cautious. She has no secret identity (bible 3.8). |

---

## 6. State after Game 3 (if approved)

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

## 7. Reader questions, answered

1. **Why can't Riku open everything and tell everyone where their names are?** Rule 6: no communication of any kind after you've been inside.
2. **Why not leave lockers open, or mark cards, as a signal?** Lockers close themselves, cards never leave, and "in any way" covers marks.
3. **Why not refuse to go in?** Rule 7.
4. **Why does following the chain work?** Your locker sits in a loop, so the card that leads back to it is your own name (the toy example).
5. **How did Ren know it was one loop before anyone went in?** Momo's "Everyone's connected!" plus the unbroken floor line. The plan is safe either way: the cut fixes any long loop, and nineteen lockers can never hold two loops over ten.
6. **Why does cutting first and tenth work?** It splits off a loop of 9, and leaves at most 19 − 9 = 10.
7. **Why must the cutter die?** They've used their ten opens without finding their name. Their name is in the other part of the loop.
8. **Why not give the first player nine tokens?** Riku refuses (9.12). Rule 2 allows giving; he chooses not to.
9. **Couldn't Riku buy certainty for others?** Full sight costs 9 tokens each. 69 covers seven people, not eighteen. Nine tokens on the first player covers everyone, which is why the deal is about the first player.
10. **Why trust Riku?** Nine deaths on average, or one certain, against none if he's honest (9.17). Ren goes second so he'll know immediately (10.5–10.6).
11. **How did Ren know Riku was honest?** He found his name in 9, and the counting fact did the rest.
12. **Why did Riku refuse Momo's 50?** "Dead people don't owe me anything." He wants debtors.
13. **How could Momo name lockers in different loops?** It arranged the lockers and watches every swap. Its offers were announced in Rule 5. Nothing is hidden from the reader.
14. **Couldn't Haruto have swapped harmlessly?** Only by swapping two lockers from his own chain, and Momo pays only for *its* pair.
15. **Why did Haruto's swap kill the next person?** Joining the 9 and the 10 makes one loop of 19, so whoever goes in next can't reach their name in ten.
16. **Why didn't everyone swap their own card into their own locker, to make it safer?** Ren chose "touch nothing" because every swap is a chance to get it wrong. Either way, simulation shows a joining swap at position 9 still kills exactly one person.
17. **How do we know Gō cut the loop?** Kota, right after him, found his name in 9. Without the cut, Kota would have died too.
18. **Is anything left to luck?** No. Momo's loop is deliberate, the plan is fixed, and the death follows from one choice.
19. **Who took Saki's token?** Kota. A small question answered; *why* stays open.
20. **Where did Haruto's 30 tokens come from?** Momo's 1,899, the tokens the class gave up in Game 2.
21. **Did anyone know something they couldn't?** No. Ren deduces everything from the board and the rules. Riku's honesty is proved by numbers, not trust.
22. **How does Gō die?** The same as Saki: lights out, then gone. Nothing new is revealed.

---

## 8. Flaw check

| Check | Result |
|---|---|
| No escape written into a rule | ✓ The way out uses two permissions (Rules 2 and 4) plus a deduction. |
| Every lethal rule shown before play; timers defined | ✓ Seven rules, 30 minutes, 10 opens, 1 swap. |
| Momo bound by its rules | ✓ Offers are announced in Rule 5. |
| Shortcut strategies tested | ✓ Telling, signalling, refusing, buying certainty for others, self-fixing (Q1–3, 9, 16). |
| 2–3 wrong answers shown first | ✓ Four. |
| Hero tests the idea on the page | ✓ The toy example on Kota's page. |
| Each key fact planted twice | ✓ The one-loop clue (Momo's line + the floor line); the counting fact (Aoi in 8.10 + Ren in 10.5). |
| No luck | ✓ The arrangement is deliberate and the outcomes are fixed. |
| Betrayal clue shown before the reveal | ✓ Rule 5; Ren's own offer; Haruto's silence and Yui noticing it. |
| All numbers exact | ✓ 9 average deaths; 61.9%; 19 > 10; 9 + 10; 9 tokens; one death; ledger totals 2,000. All simulated. |
| Narration knows only what Ren knows | ✓ The hand and notebook are shown, not narrated. |
| Momo or the meteor revealed? | ✓ No. |
| Q3 or Q6 settled? | ✓ No. The game never uses "eliminated". |
| Strength solves it? / Kota as the solver? | ✓ No / no. |
| Roster | ✓ 18 alive: 7 named + 11 unnamed. Saki and Gō dead. |
| At least one death | ✓ Gō. |

---

## 9. Mysteries kept open on purpose

- **The unbroken circle on the floor and "Everyone's connected".** Momo designed the game around one loop of everyone. Why that idea matters to the system stays unknown.
- **Momo pays for betrayal with the class's own tokens.** The system *wants* them to turn on each other. Why stays unknown.
- **Saki's sealed locker.** It stays shut.
- **Why Kota took Saki's token.** "It was hers."
- **Momo's nature, the meteor's shape, why Class 3-B, the teacher, and what "eliminated" means.** All untouched.

---

## 10. Your decisions

1. **Approve Game 3 v3** ("Find Yourself"), or tell me what to change.
2. **The betrayer.** I recommend **Haruto**: the strongest emotional hit, and the "business model" callback. Alternatives: Mio, Kota, or an unnamed student.
3. **The victim.** I recommend **Gō**: his promise to cut the loop, and his bond with Kota. Whoever stands right after the betrayer dies, so any name works.
4. **Kota took Saki's token**, revealed here. Keep it, or hold the reveal for later?
5. **Saki's sealed locker.** Keep or drop.
6. **Two chapters** (about 40 pages). OK?

Once you approve, I'll record it in the continuity ledger and write the page scripts. Then I'll draw them with the same full-size checks, push the pages to `video/ch04/` and `video/ch05/`, and tell the video session.
