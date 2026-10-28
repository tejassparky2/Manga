# LIAR GAME (Shinobu Kaitani): how its games work

Research notes for *Dead Man's Algorithm*. Compiled 2026-10-28.

**Rule for these notes:** every rule, solution and quote below names the source it came from (URL next to it). Anything I could not open and check is marked **UNVERIFIED**. Wherever I give my own synthesis rather than a source, I mark it **[my synthesis]**.

---

## 0. Sources and how reliable they are

| Key | Source | What it gave me | Reliability |
|---|---|---|---|
| JAWP | Japanese Wikipedia, "LIAR GAME": https://ja.wikipedia.org/wiki/LIAR_GAME (raw wikitext read in full) | Full written rules for every manga game; character outcome notes; the "house only profits from selfishness" design note | High for rules (very detailed). Weaker on step-by-step solutions. |
| ENWP | English Wikipedia, "Liar Game", episode summaries of the 2026 Madhouse anime: https://en.wikipedia.org/wiki/Liar_Game | Step-by-step solutions for Round 1 → Revival Round 2 (anime eps 1–26 follow the manga) | High for the arcs it covers. Note that the summaries call Fukunaga "Fuji"/"Yuji". The anime renames the Contraband countries "Day/Night" (the manga uses North/South, per JAWP). |
| ENWP-CH | "List of Liar Game chapters": https://en.wikipedia.org/wiki/List_of_Liar_Game_chapters | Per-volume plot summaries (vols 1–19) | Medium (short summaries) |
| PLANETA | Planeta Cómic (official Spanish publisher) volume synopses, e.g. vol 11: https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275505/liar-game-n-1119.pdf (vols 9–18 are the same URL pattern; IDs 275503–275513) | Official outcome statements for Pandemic, Musical Chairs, Bid Poker, Human Auction | High (publisher), but brief |
| JAWP-DR | Japanese Wikipedia, "LIAR GAME (テレビドラマ)": https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E) | Full rules of the film-only Eden Game and the spin-off Taboo Game | High for rules |
| ENWP-FS | "Liar Game: The Final Stage": https://en.wikipedia.org/wiki/Liar_Game:_The_Final_Stage | Eden Game plot and resolution | Medium-high |
| CIATR | ciatr.jp drama/film game round-up: https://ciatr.jp/topics/323364 | Drama-only games (Angels & Demons, Gold Rush) | Medium (entertainment site; secondary) |
| REALSOUND | Real Sound Book editorial, 2025-09-01: https://realsound.jp/book/2025/09/post-2141135.html | Critical analysis of why the games work | Medium-high (professional critique) |
| WPBLOG | Fan blog "The 'Power Play' Solution" (2010): https://liargame.wordpress.com/2010/07/01/the-power-play-solution/ | Analysis of the Musical Chairs ending | Fan opinion |
| CORNELL | Cornell INFO 2040 course blog: https://blogs.cornell.edu/info2040/2022/10/27/game-theory-in-liar-game/ | Game-theory reading of Musical Chairs | Student blog |
| Reddit | r/liargame, r/manga threads (URLs inline) | Fan rankings, praise and criticism, some plot details | Fan opinion; plot details from fans are labelled |

**Blocked or not used:**
- liargame.fandom.com and liarsgame.fandom.com returned HTTP 402. TV Tropes, namu.wiki and nicovideo returned 403. I did not get around these blocks, so nothing below comes from fandom wikis.
- explorism.blog and mystiqora.com "all games explained" pages were vague or wrong. For example, explorism describes 17 Poker as "a poker variant with a target of 17". I discarded both.
- Variety's interview with the Squid Game director was paywalled.

---

## 1. The tournament's skeleton: where the "everyone survives" loophole lives

These are the meta-rules that every game inherits. They are the most important design idea in the series.

- **The house has no rake; only selfishness pays the house.** JAWP (rules section, "その他のルール") says the tournament has no 寺銭 (house cut) and is basically zero-sum. The rules are built so that **"the organizers profit only when some player acts purely for their own gain"** (ゲーム中いずれかのプレイヤーが自分の利益だけを考えた行動をしたときのみ主催者側に利益が出る). The mechanism is the drop-out fee: a winner may leave by paying **half** of their winnings to the organizers. So "**if all players cooperate, and the winner gives up dropping out and shares the prize with the losers, the organizers cannot profit at all**". The flip side: "**players as a whole basically cannot profit**; if everyone tries to survive together, they must give up on profit." — https://ja.wikipedia.org/wiki/LIAR_GAME
- JAWP's overview states the theme directly. If every player colluded, nobody would gain and nobody would lose. In reality players can't be sure they can trust each other, so they fall into a **prisoner's dilemma**: "このジレンマにどのように対処するかが、本作品の主題の一つである" ("how to deal with this dilemma is one of the work's themes"). — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Forced loans become debt.** At the start of each game the organizers forcibly lend every player cash: ¥100M in most rounds, ¥400M in Round 3, ¥150M in Revival 2, ¥300M in Revival 3 and the Final. Anything you lose becomes debt, which the office says it will collect "by any means". Winnings only become yours once you leave the game. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Anything not explicitly forbidden is legal.** There is an implicit rule that a player may do anything not explicitly banned. Lies, threats, cheating and fraud all count as valid play if they don't break the stated rules. Violence carries instant elimination or a heavy penalty, so "forming groups and cooperating with many people is comparatively advantageous". — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Winning ≠ profiting.** "金銭的な損得はゲームの勝敗に必ずしも一致しない" (financial gain/loss does not necessarily match winning/losing). In Contraband and Bid Poker you can lose and still take home big money. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **"Bonus" revival rounds hide a house sink.** Revival rounds may be "bonus games" in which the players collectively gain. They come paired with "rules that let the office unilaterally seize money", so the players as a whole can actually end up negative. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **A legal trap keeps people from going to the police.** In Round 1 most players commit what would normally be crimes to take money. If anyone later sues claiming the Liar Game "isn't a game", those Round 1 thefts become real crimes and the people who committed them get arrested. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Proxies are allowed.** A player may send someone else in their place, but the prize or debt belongs to whoever actually plays. This is how Akiyama enters Rounds 2 and 3. — https://ja.wikipedia.org/wiki/LIAR_GAME
- Nao's stated "winning method" (from the synopsis): if players cooperate and everyone is honest, so that nobody tries to trap another for profit, nobody gets rich but nobody ends up in debt either. She keeps playing in order to save the other players. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **The reveal.** The LGT turns out to be a documentary-film project restaging an unfinished novel. The Final Stage film has its own version, where the tournament was a bet among investors on whether an all-red vote would ever happen. — https://ja.wikipedia.org/wiki/LIAR_GAME and https://en.wikipedia.org/wiki/Liar_Game:_The_Final_Stage

**[my synthesis]** This is exactly the structure *Dead Man's Algorithm* wants. Make the "everyone survives" outcome a **fixed point of the rules**: the house only collects when somebody defects. Then make that outcome **unverifiable from the inside**, so fear and greed break it.

---

## 2. The games (manga order), with adaptation-only games after

For each game: **Rules → Hidden insight / protagonist's solution → Antagonist's layer → How money/debt creates tension → Fan reception.**

### 2.1 Round 1: Money Tug-of-War / "¥100 Million Game" (manga vol 1)

- **Rules:** Each player is forcibly lent ¥100M and paired 1-on-1 with an opponent. After 30 days, whoever holds more of the combined ¥200M wins. Winner's prize = holdings minus the ¥100M repayment; the loser's shortfall becomes debt. You must return the *original banknotes* (serial numbers are checked). If neither side takes a single yen, both can leave debt-free. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **What happened:** Fujisawa, Nao's former teacher, persuades her that they're both being scammed and that they should hide the money in his care, which takes all of it. Akiyama spots that day 30 is a Sunday, so Fujisawa must take the cash out of the bank by Friday and guard it at home. Akiyama then announces they will steal it and keeps him under constant surveillance. That breaks Fujisawa down and shows the cash is in a safe in his house (anime eps 1–2). — https://en.wikipedia.org/wiki/Liar_Game
- **Hidden insight:** **Akiyama never opens the safe.** He puts a fake LGT letter in Fujisawa's mailbox saying the game ends at 5 pm instead of 6 pm, then turns up disguised as the LGT collector at 5 and walks off with the money. At 6 pm Nao holds it, so she wins. Nao and Akiyama then give their winnings to Fujisawa so he ends up with no debt (ep 3). — https://en.wikipedia.org/wiki/Liar_Game
- **Design note:** Akiyama attacks the opponent's **belief about the rules** (the deadline), not the thing being guarded. The "both take nothing and leave debt-free" clause is the first hidden cooperative solution, and Nao's later doctrine grows out of this round (JAWP note on Fujisawa: "ナオの語るLIAR GAME必勝法のある種の引き分け戦術の原案は、この出来事が発端"). — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Fans:** Widely called the weakest arc ("Everyone hates this arc", ranked #12 of 12). — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/ and https://www.reddit.com/r/liargame/comments/1uigdd0/briefly_explaining_what_makes_each_arc_of_liar/

### 2.2 Round 2: Minority Rule (少数決) (vol 2)

- **Rules:** 22 players. Each round, one player poses a yes/no question. Everyone who voted with the **majority** is eliminated. Voting repeats until 1–2 players remain. Answers need not be truthful, so the question is decoration and "vote manipulation decides everything". There are 6 hours to negotiate per question. Ballots are pre-printed YES/NO slips with your player number on them. A tie, or a unanimous vote, is void and re-voted. Each player wears a nameplate with a ¥100M jewel. Losers leave the jewel, and the winner(s) split the losers' jewels. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Stakes:** The prize is the losers' plates, about ¥2.1 billion. A winner who wants to quit before Round 3 pays half, ¥1.05bn (anime ep 3; ep 7 calls the full pot ¥2.2bn). — https://en.wikipedia.org/wiki/Liar_Game
- **Akiyama's plan (layer 1):** Form an **8-person team, half voting Yes and half No**. Every question then eliminates half the team but always leaves part of it in the minority: 8 → 4 → 2, so the last survivor is almost certainly one of the 8. The survivor pays ¥1.05bn to quit, ¥700M to clear the other 7's debts, and the team splits the remaining ¥350M (¥43.75M each). The danger is recruiting **"X"**, the player who stole another woman's ¥100M cheque. X can use that money to cover their own debt, so X has no reason to stay loyal (ep 4). — https://en.wikipedia.org/wiki/Liar_Game
- **Antagonist layer (Fukunaga = X):** Fukunaga, disguised as "Hitomi", joins Akiyama's team. **She organizes the other 14 players into two more 8-person teams, putting herself in all three teams.** That lets her steer every vote to be as close to a tie as possible, with herself always in the minority (ep 6). — https://en.wikipedia.org/wiki/Liar_Game
- **Clues planted for the reader:**
  - The first vote is 12–10, "the closest possible vote to avoid a draw", and the second is 6–4.
  - Player 1 stays in the mansion after being eliminated (ep 5).
  - Only Akiyama and X knew the stolen money was a *cheque*, and "Hitomi" knew it (ep 6).
  — https://en.wikipedia.org/wiki/Liar_Game
- **Akiyama's endgame trap (layer 2):** With 4 left, Akiyama announces his vote (No) openly. Then: if all three others vote Yes, Akiyama is the minority and wins. If two vote No, the No side (three, counting Akiyama) is the majority, so the single Yes voter wins and the two No voters lose alongside Akiyama. If only one votes No, it's a 2–2 tie. So beating him requires two people to **sacrifice themselves**, and nobody will (ep 6). Player 15 had secretly sided with Akiyama after Akiyama told him Fukunaga was betraying everyone. The final vote comes out Yes/Yes/Yes vs Akiyama's No, and Akiyama wins (ep 7). — https://en.wikipedia.org/wiki/Liar_Game
- **Money resolution:** Akiyama pays ¥1.1625bn to No. 15 (for No. 15's teammates' debts plus profit), clears his own team's debts (minus Fukunaga), and stays in the tournament to hunt the organizers (ep 7). — https://en.wikipedia.org/wiki/Liar_Game. JAWP: No. 15 left with about ¥140M. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Fans:** "When I'm trying to sell anyone on the Strategies of this franchise, I tell them this"; "the first time the viewer's mind gets blown". — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/
- **Drama variant (2007):** The "15" role is played by Ishida, who betrays Fukunaga and Etou to Akiyama. — https://en.wikipedia.org/wiki/Liar_Game_(2007_TV_series)

### 2.3 Revival Round 1: Downsizing / Restructuring Game (リストラゲーム) (vol 3)

- **Rules:** 9 players vote 10 times. Each ballot (the "L-ticket") must name 5 *other* players (repeats allowed). After 10 votes, the player with the **fewest** total votes is "downsized" and loses ¥100M. Everyone else wins and splits the loser's ¥100M (¥12.5M each). Players hold **M-tickets**: written contracts of the form "I will do Y for ¥X". Breaking a contract costs a ¥100M penalty to the office. Each player may bring any legal personal belonging, *including a person*. The office loses ¥100M in this game because the loser's money goes to the players, so the players as a whole come out +¥100M. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Antagonist layer (Fukunaga):** Fukunaga privately offers Nao a vote-swap (they control 100 of the 450 votes, so "we can't be downsized"). Then he sells everyone else, for ¥5M of M-tickets each, a guarantee that Nao will lose. Nao ends up with 0 votes. Because the M-tickets are enforceable, everyone is now *contractually bound* to vote Fukunaga's way (anime ep 8). — https://en.wikipedia.org/wiki/Liar_Game
- **Mini-game "Light and Darkness":** Fukunaga offers Nao 30 votes against ¥30M. A bag holds a double-sided black card and a Joker. Whichever card is drawn 10 times first wins, and a card drawn "face up" is redrawn. **A double-sided card has no face, so it can never be drawn face-up and redrawn**, which gives the Joker about a 94% chance of losing. In the rematch Nao marks the black card with her fingernail (ep 9). — https://en.wikipedia.org/wiki/Liar_Game
- **Nao's counter:** Akiyama joins as **Nao's "possession"** (JAWP: "敗者復活戦ではナオの私物として参加"). — https://ja.wikipedia.org/wiki/LIAR_GAME
  - Nao secretly makes the *same* deal with every player: their 10 votes for her M-ticket money, telling each one she only needs 20 votes to claim a spare Round 3 seat. She ends up with 80 votes.
  - Akiyama then auctions off her surplus votes, and Nao ends up holding the whole ¥900M.
  - Final tally: Nao 51, everyone else 50, Miura 49. **She chooses Miura to "lose" because he was the only one kind to her.** She pays him ¥200M so he leaves debt-free, and returns ¥700M to the others (eps 9–10).
  - Her stated insight: if players agree to let one player win everything in every round, the winner can pay everyone's debts at once and the LGT earns nothing (ep 10).
  — https://en.wikipedia.org/wiki/Liar_Game
- **Design note:** The losing slot is reframed as a lifeboat. Fans: Downsizing is where Nao realizes "it's about choosing someone to save". — https://www.reddit.com/r/liargame/comments/1uigdd0/briefly_explaining_what_makes_each_arc_of_liar/
- **Side note:** Sato tries to undercut Akiyama by selling his own votes more cheaply; Akiyama sees through it. — https://ja.wikipedia.org/wiki/LIAR_GAME

### 2.4 Round 3: Contraband / Smuggling Game (密輸ゲーム) (vols 4–6). The fan-favourite peak.

- **Rules (JAWP):**
  - Two 9-player "countries". Each player has a **third-country (neutral) account** holding ¥100M and an **enemy-country account** holding ¥300M. All ¥400M is borrowed.
  - 50 "games", in each of which both sides smuggle once, so 100 bouts in all.
  - In a bout, the smuggler puts ¥0–100M from the enemy-country account into a briefcase. The inspector gets 10 minutes in a soundproof room with a one-way mirror, then calls "Doubt, ¥X" or "Pass".
  - **Case empty and inspector doubted:** the inspector pays **half of X** in "compensation" to the smuggler.
  - **X ≥ contents > 0:** the inspector takes all the contents.
  - **X < contents:** the smuggler keeps the contents *and* is paid compensation.
  - **Pass:** the smuggler keeps it all.
  - An inspector can only doubt up to 2× their own third-country balance.
  - **The team with more total in members' third-country accounts wins, but money is paid per individual.** Unsmuggled cash left in enemy-country accounts is split among the *opposing* team as prize, though it doesn't count toward winning.
  - Bank cards can withdraw beyond ¥100M, deposit cash, and be used by other people; the card's owner gets the credit. Every account movement is audited.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Layer 1 (Yokoya's "clairvoyance"):** Yokoya guesses exact odd amounts (¥50.01M, ¥90.01M). Nao exposes the trick by smuggling a teddy bear. Akiyama tests a theory by changing a planned ¥91.11M to ¥91.12M without telling the suspect. Yokoya guesses ¥91.11M, which proves that Kikuzawa, a Day-team member, has been signalling him through the windows. Kikuzawa was Yokoya's high-school victim (anime eps 12–14). — https://en.wikipedia.org/wiki/Liar_Game
- **Layer 2 (winning vs profiting):** The Day team leads, but Akiyama and Leronira warn that winning does not guarantee profit. Because of how the accounts settle, **the winning team can end up in debt while the losers profit** (ep 14). — https://en.wikipedia.org/wiki/Liar_Game
- **Layer 3 (Akiyama's plan):** Use bank cards to withdraw the Night ATM's entire ¥2.3bn and have a Night traitor deposit it in the Day ATM, so Day "loses the game but walks away with the cash" (ep 15). — https://en.wikipedia.org/wiki/Liar_Game
- **Layer 4 (Yokoya got there first):** Night players *pretending to betray Yokoya* pitched the *exact same plan* to three Day players, who then moved ¥1.91bn **into** the Night ATM (ep 15). — https://en.wikipedia.org/wiki/Liar_Game
- **Layer 5 (turning Yokoya's team):** Akiyama recruits "Bandana" (Akagi). Yokoya rules Night through debt (everyone owes him ¥200M from the revival round) and a points ranking in which the bottom two get nothing. Akiyama sets out to drain balances deliberately through planned confiscations (eps 16–17). Yokoya responds with a **prisoner's-dilemma interrogation**: whoever confesses first is rewarded. Long Hair confesses, and Yokoya sets up a counter-plan (ep 17). — https://en.wikipedia.org/wiki/Liar_Game
- **Layer 6 (triple agents):** The traitors stayed loyal to Akiyama even after the "confession". Baldy handed Yokoya ¥1.91bn in physical cash *withdrawn from the Day ATM*, presented as Night money. Yokoya's smuggling therefore achieved nothing, and the final audit shows Night's accounts empty and Day holding ¥3.35bn (eps 18–19). — https://en.wikipedia.org/wiki/Liar_Game
- **Money resolution:** Day profits ¥1.23bn, which lets the three traitors leave debt-free. **Akiyama and Nao refuse to repay their own ¥400M loans so they can clear everyone else's debts**, and go on to the next Revival in debt. Yokoya alone pockets ¥1.03bn by depositing his teammates' smuggled cash into his own account (eps 19–20). — https://en.wikipedia.org/wiki/Liar_Game
- **Fans:**
  - Praise: "Literally the Peak of Chess Masters… after this Arc, the author decided to have the masked dudes in the backroom explain everything to the audience." — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/
  - Praise: "peak intensity in terms of deception and one-on-one manipulation." — https://www.reddit.com/r/liargame/comments/1n770i8/contraband_game_is_the_best_display_of/
  - Criticism: hard to follow. Anime-only viewers: "I'm so confused what the fuck is going on" (same thread). Another fan calls Contraband "incomprehensible" compared with Musical Chairs. — https://www.reddit.com/r/liargame/comments/1xafydu/the_enemy_of_my_enemy_is_my_friend_how_the/
  - Criticism: Yokoya losing because he overlooked a voice recorder he had handed out himself feels contrived (fan claim). — https://www.reddit.com/r/liargame/comments/1lqqky9/yokoya_needs_justice/
- **Thematic reading (fan):** The arc models currency flight; the three Day players "were making a decision that looked rational from their position without understanding the larger system". — https://www.reddit.com/r/liargame/comments/1vo5b36/liar_game_is_much_deeper_than_a_psychological/

### 2.5 Revival Round 2: three 1-on-1 matches, team of 3 vs 3 (vols 7–8)

**Frame:** Each player is lent ¥150M in chips but repays only ¥100M, so cooperating would net everyone +¥50M. **But every sub-game has a rule that lets the dealer confiscate chips.** — https://ja.wikipedia.org/wiki/LIAR_GAME. Per ENWP-CH vol 7, "Nao realizes the true opponent is the LGT itself." — https://en.wikipedia.org/wiki/List_of_Liar_Game_chapters

**(a) Spearhead: 24-chamber Russian roulette**
- **Rules:**
  - Each player secretly picks 3 of 24 chambers for live rounds. If the picks overlap, they pick again.
  - Firing a "bullet" (a harmless bang) costs 50 chips, paid to the other team.
  - A player may pass by paying 1 chip into the pot. Consecutive passes double the cost (1, 2, 4, 8…).
  - After 5 consecutive passes the dealer pulls the trigger, and **the 31 accumulated chips go to the dealer**.
  - The game ends at the 6th shot; fewer bangs wins.
  - The cylinder "is fully affected by weight imbalance from bullet positions".
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Insight:** Gravity. When the cylinder is spun, the heavier bullet-loaded side settles at the bottom, so the first chambers are almost surely empty. Akiyama leaked false advice to the other team to load their bullets consecutively, which makes the imbalance worse. Fukunaga fakes "gunpowder marks" with eyeliner (anime eps 20–21). — https://en.wikipedia.org/wiki/Liar_Game
- **Nao's layer:** She realises continuous passing feeds the LGT, which collects ¥310M as bullets go off. She **lies to Fukunaga** to get her to fire the last two bullets herself, forcing a **tie** (ep 22). Later, Akiyama explains he wanted the tie because Nao absorbing every player's debt would push the LGT toward bankruptcy (ep 26). — https://en.wikipedia.org/wiki/Liar_Game
- **Fans:** Ranked low after Contraband ("a huge step down"). — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/

**(b) Core: 17 Poker**
- **Rules:**
  - The deck is 17 cards: A, K, Q, J of each suit plus a wild Joker, which can also be a 10, making straights possible.
  - 10 hands. The winner is whoever gains more chips than they started with.
  - 5-chip ante. If both players check, the hand is void and **the dealer takes the pot**. If a player folds, the dealer takes the antes.
  - Special cut rule: each player calls "Nth card from the top".
  - A new deck is used every hand, always in the same factory order (players aren't told). The fastidious dealer always does **perfect riffle shuffles**.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Opponent's edge:** Kikuchi, an ex-boxer with exceptional kinetic vision, follows the Joker and the bottom Ace through the shuffle and uses the cut to deal them to himself (eps 23–24). — https://en.wikipedia.org/wiki/Liar_Game
- **Akiyama's insight:** Kikuchi tracked one card; **Akiyama tracked all 17**. He spotted the perfect riffles and asked for 2 and then 4 consecutive shuffles, which put a Four-of-a-Kind among the undealt cards. He then drew it by discarding his entire hand. Final hand: four Queens vs Kikuchi's Aces-high full house (eps 24–25). — https://en.wikipedia.org/wiki/Liar_Game
- **Fans:** "Literally the most underrated arc. Akiyama pushes himself to the literal limit." — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/. "[Akiyama] uses actual math in some cases (like calculating card placements based on a perfect shuffle)… [but] Too often he explains the solution and I'm like… 'Yeah, sure… I totally get that'." — https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/

**(c) General: Stationary ("non-spinning") Roulette**
- **Rules:**
  - A wheel with 4 pockets. The dealer secretly sets the ball and bets on 1–4 pockets, not necessarily the true one.
  - The other player may bet on at most 2 pockets and must stake at least as much as the dealer.
  - If only one is right, they take everything. If both are right, they split pro rata. **If both miss, the dealer takes all.**
  - The roles alternate, 5 times each.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Solution (double-cross):** Fukunaga sells Kosaka "winning advice" for ¥300M of her prize: that Nao blinks when she lies. Fukunaga had also primed Kosaka to choose 3. Nao bets 90 chips on every pocket (360 total). Kosaka, "seeing" a blink, puts 360 on pocket 2; the ball is in 3. Kosaka can no longer catch up. Nao then pays the losing team's debts as she promised (eps 25–26). — https://en.wikipedia.org/wiki/Liar_Game
- **Fans:** "Her monologue at the End is literally the Peak of Liar Game"; also the source of Akiyama's "'Humans SHOULD be Doubted' Speech". — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/
- REALSOUND quotes the idea behind that speech: "疑わないのはたんなる無関心であり、「他人を知ることの放棄」" (not doubting is mere indifference, "giving up on knowing others"). — https://realsound.jp/book/2025/09/post-2141135.html

### 2.6 Round 4 qualifier: Pandemic / Infection Game (感染ゲーム) (vols 9–10)

- **Rules (JAWP):**
  - 12 players, each wearing a non-removable watch. The watch secretly stores two things: Normal or Infected, and a vaccine count.
  - **You can only see your own status alone inside a locked examination booth.** There are only 4 booths, and if two people enter together the status isn't shown and a buzzer sounds. So **you can never prove your status to anyone.**
  - 2 players start infected (not announced). Players "touch" watches, which gives off a bright flash, so contacts are visible.
  - Normal + Normal: both gain 1 vaccine. This works only once per pair.
  - Normal without a vaccine + Infected: the normal player becomes infected.
  - Vaccine-holder + Infected: the vaccine-holder loses 1 vaccine and *becomes infected*; the infected player becomes normal.
  - Infected + Infected: no change.
  - An infected player with a vaccine can press the switch to spend one and become normal.
  - **Win condition:** if **6 or more** players finish with ≥4 active vaccines, **all of them qualify**; otherwise the top 6 by vaccines qualify.
  - The game lasts 3 × 30-minute periods. At each interval only the *counts* of normal and infected players are announced.
  - A 15-minute mock game comes first. The top 3 in the mock are excluded from the initial infected draw, which works as public proof that they are clean.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Hidden cooperative solution:** The "≥6 players with ≥4 vaccines → all qualify" clause means **everyone can qualify**, and the official synopsis confirms that **"thanks to Nao, all the players in the pandemic game qualify for the final"** ("Gracias al buen hacer de Nao, todos los jugadores que participan en el 'juego de la pandemia'… logran clasificarse para la final"). — PLANETA vol 11: https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275505/liar-game-n-1119.pdf
- **Antagonist layer:** Yokoya deliberately spreads the infection during the *mock* game and has his followers lie about being infected, planting the idea that "no one can be trusted" (fan explanation). — https://www.reddit.com/r/liargame/comments/1tyat07/why_dont_they_just_look_at_the_vaccine_count_to/. Official synopsis for vol 10: with Yokoya manipulating everyone, "distrust sinks deep". Akiyama seemed to have broken a stalemate in which nobody trusted anybody, but Yokoya made him look like a crook. — https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275504/liar-game-n-1019.pdf. ENWP-CH vol 10: "Yokoya tries to eliminate Nao but is thwarted and forced to cooperate." — https://en.wikipedia.org/wiki/List_of_Liar_Game_chapters
- **Akiyama's counters (fan reports; partly confirmed):**
  - **Booth lockout.** Akiyama's side occupies or locks the examination booths. Fans call it the "lockout plan", and one fan's ranking notes "Akiyama locking himself in the Booth… is the moment that marks Chapter 100". — https://www.reddit.com/r/liargame/comments/1hv7ddv/make_akiyama_great_again_akiyamas_most_underrated/ and https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/
  - **Voice impersonation.** Yokoya goes booth to booth offering bribes while "Akiyama and their friend Akagi literally just impersonate the voices of the would-be-traitors". — https://www.reddit.com/r/liargame/comments/18wab50/pandemic_game/. JAWP's rule text notes that booth doors are thick and muffle sound, so voices are hard to identify from outside. A hidden editor's comment in the JAWP source adds that Akiyama and Akagi used this to take ¥300M from Yokoya. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Fans:**
  - Praise: "Pandemic and musical chairs were the absolute sweet spot for people interested in game theory to follow along and make their own strategies." — https://www.reddit.com/r/liargame/comments/1uigdd0/briefly_explaining_what_makes_each_arc_of_liar/
  - Rules hole: couldn't players simply infer their status from whether their vaccine count went up? — https://www.reddit.com/r/liargame/comments/1tyat07/why_dont_they_just_look_at_the_vaccine_count_to/ and https://www.reddit.com/r/liargame/comments/172wpl2/the_pandemic_game/ ("I think that part isn't really explained well")
  - Criticism: Yokoya "made… look like a clown" by falling for the bribe trick repeatedly. — https://www.reddit.com/r/liargame/comments/1lqqky9/yokoya_needs_justice/

### 2.7 Round 4 main: Musical Chairs (イス取りゲーム) (vols 10–14). Most often named the best game.

- **Rules (JAWP):**
  - The game is played on a bankrupt resort island 1.5 km around. 25 numbered chairs are hidden across it.
  - On an alarm, a player must touch the totem pole and then sit in any chair within 10 minutes. Sitting means both hands and buttocks touching; the right hand must stay on the chair. **You can't sit in the same numbered chair twice in a row.** Anyone without a seat is out.
  - After each seating, **all 24 people, including eliminated players, vote anonymously by majority for a "Parent" (親)**. The Parent removes one chair by number. Only active players can be Parent, and voting for yourself is allowed. Ties go to a run-off.
  - Up to 24 periods. The last one standing wins.
  - Eliminated players and qualifier losers become **"Gaya" (extras)**. They may do anything except violence: guard chairs, block, and vote. Blocking someone's path doesn't count as violence.
  - **Money:** each active player gets 23 **medals engraved with their own name**, nominally ¥100M each. **Only the final survivor's medals can be cashed**; everyone else's become worthless as the game goes on. Medals can be handed to anyone.
  - The alarm sound isn't unique to the watches; other devices can make it.
  - A mock game gives 3 winners an envelope they may not open but *may peek into*. It contains a map of 3 chairs, and all 3 maps are identical.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Structure:** A three-way war between Akiyama, Yokoya and the cult leader Harimoto. The dealers liken it to the Three Kingdoms, and Akiyama calls it a "country-taking game". — https://ja.wikipedia.org/wiki/LIAR_GAME. Yokoya and Harimoto keep forming alliances against Akiyama, but they collapse because "They both want Akiyama to lose, Yes, but they also Both want to Win". — https://www.reddit.com/r/liargame/comments/1xafydu/the_enemy_of_my_enemy_is_my_friend_how_the/
- **Key moves (official / JAWP):**
  - Akiyama's group makes a surprise move by **abstaining from the Parent vote**, which flips the situation. Yokoya and Harimoto break their alliance, and a fourth power, the "league of extras", emerges. — PLANETA vol 12: https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275506/liar-game-n-1219.pdf
  - Akiyama runs a Gaya alliance through a **dummy leader, Shima ("Young Jump")**, to control the Parent votes. Yokoya spots this and **buys Shima**, which takes over the Gaya alliance and eliminates Akiyama's team. — https://ja.wikipedia.org/wiki/LIAR_GAME
  - Yasukawa ("Baldy") is cut from Akiyama's team and defects to Yokoya "in revenge", but **that was part of Akiyama's plan**. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Ending:**
  - **Ikezawa ("Debu"), Yokoya's front man, is made the final winner by Akiyama's scheme.** But Ikezawa had **given away every one of his own medals as the team's "throwaway medals" (捨てメダル)**, so he got no prize money. — https://ja.wikipedia.org/wiki/LIAR_GAME. The official synopsis confirms the game "concludes with the victory of Ikezawa, the fat one". — https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275508/liar-game-n-1419.pdf
  - Yokoya himself is stopped by a **"scrum" blockade** from the Gaya-alliance members who hadn't received Yokoya medals. He couldn't break through because he hadn't slept the night before, after staying up on watch. — https://ja.wikipedia.org/wiki/LIAR_GAME
  - Fans: "the trash medals were with akiyama"; Yokoya "hadnt known abt the trash medals". — https://www.reddit.com/r/liargame/comments/1lqqky9/yokoya_needs_justice/
  - WPBLOG: "No one in Yokoya's group has any [of Ikezawa's medals]"; "in the sense of achieving Akiyama and Nao's goals, Ikezawa's winning is actually better than Nao's winning." — https://liargame.wordpress.com/2010/07/01/the-power-play-solution/
  - JAWP: Akiyama "turned the flow of the game around, made a profit *while losing*, and fully repaid his debts" (四回戦本選ではゲームの流れを逆手に、敗北しながら収益を上げ、これまでの負債を完済した). — https://ja.wikipedia.org/wiki/LIAR_GAME
- **The hidden insight [my synthesis, from the sources above]:** The medal design makes **"who wins" a separate question from "who gets paid"**. Bribes paid in a likely loser's medals are worthless, so a team throws away its *front man's* medals as cheap bribes. Akiyama then makes the front man win, which turns the discarded medals (now held by the extras) into the real money.
- **Fans:**
  - "Absolutely nothing will ever beat Musical Chairs." — https://www.reddit.com/r/liargame/comments/pqdcnt/ranking_every_game_in_liar_game/
  - "the best example of a 3 way chess match in anything ever." — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/
  - "unlike the Contraband Game, they are not incomprehensible. They have very little to do with actual math, and entirely to do with understanding the mindsets." — https://www.reddit.com/r/liargame/comments/1xafydu/the_enemy_of_my_enemy_is_my_friend_how_the/
  - "the first Liar Game game to introduce a physical element." — https://www.reddit.com/r/liargame/comments/1wu7tfe/jus_completed_musical_chairs/
  - Criticism: "when it comes to the end of the game it turns out the solution is just an insatisfactory cheat." — https://www.reddit.com/r/liargame/comments/1n770i8/contraband_game_is_the_best_display_of/
  - Sympathy for the antagonist: "He genuinely 'won' the game fair and square, just through pure strategy, and still lost lol." — https://www.reddit.com/r/liargame/comments/1wu7tfe/jus_completed_musical_chairs/
- **Game-theory reading:** "this game requires alliances to be made in order to play optimally"; "Having many extras supporting an active player is essential to controlling the game"; "players are unlikely to cooperate unless offered security or compensation". — https://blogs.cornell.edu/info2040/2022/10/27/game-theory-in-liar-game/
- **Film adaptation:** *Liar Game: Reborn* (2012) is based on this arc: 20 players and ¥2bn in total. — https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E). A fan says the manga version "feels like one of the longest… due to how much thinking it requires", while the film "breezes through everything". — https://www.reddit.com/r/liargame/comments/pqdcnt/ranking_every_game_in_liar_game/

### 2.8 Revival Round 3: Bid Poker (入札ポーカー) (vols 14–16)

- **Rules (JAWP):**
  - 11 players get 300 virtual gold coins each (1 coin = ¥1M, so ¥300M) and must return only 100 coins. That makes it a nominal **+¥200M "super bonus game"** per person.
  - **Dealing stage:** 10 card-sets go up for one-shot sealed auctions. Each set has no hand on its own, but any two sets combined make one. **Coins paid in this stage go to the dealer**, so they are a loss for the players as a whole. **If players spend an average of ¥200M each, the bonus is gone. "This is the game's trap."**
  - **Change stage:** players put unwanted cards up for auction among themselves; that money stays among the players.
  - **Payout:** last place, including everyone tied for last, pays 150 coins each. 1st place takes 2/3 of that pool, 2nd 4/15, 3rd 1/15. Anyone holding fewer than 5 cards has "no hand", and all no-hands tie for last.
  - **A guaranteed play exists: buy nothing.** You are sure to lose, but you receive ¥300M and pay ¥250M, a guaranteed +¥50M. It only helps players whose existing debt is ≤ ¥50M; heavily indebted players are forced to fight.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Plot (official/ENWP):**
  - Nao calls on everyone to cooperate so all can be saved, but **Harimoto's group** blocks it. When everyone is about to fall into Harimoto's trap, Akiyama counter-attacks. — PLANETA vol 15: https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275509/liar-game-n-1519.pdf
  - The real brain of the cult is **Kimura**. After **Kawai's betrayal**, she builds a "cold, cruel plan based on the information he leaked". — PLANETA vol 16: https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275510/liar-game-n-1619.pdf
  - "Nao and Akiyama defeat Kimura's strategy by uniting the players. Harimoto forfeits and uses his earnings to clear others' debts." — https://en.wikipedia.org/wiki/List_of_Liar_Game_chapters
  - JAWP: Kawai's spying for Harimoto "was Akiyama's plan, having read Harimoto's moves". Shimoharada's revenge bid during Yasukawa's auction collapsed the **bid-rigging pact (談合協定)**. Nao's honesty united "almost all participants on the single point that 'Kanzaki Nao will not betray me'". — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Fans:**
  - Seen as mixed or underrated. One favourite moment is when Nao turns out to understand what Akiyama was doing when he "ruined" her plan. — https://www.reddit.com/r/liargame/comments/1nmt8wz/how_would_you_rate_bid_poker/
  - "I think Bid Poker is a little too complex. Most people just couldnt follow what was going on AT ALL." — https://www.reddit.com/r/liargame/comments/1uigdd0/briefly_explaining_what_makes_each_arc_of_liar/
  - "I can't be bothered to try and understand all the Card exchanging crap." — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/
  - On why players didn't just take the guaranteed +¥50M: "most of the Players had a greater debt than just 200 Million." — https://www.reddit.com/r/liargame/comments/1kup6lt/why_did_people_play_bid_poker/

### 2.9 Final round (vols 17–19)

**(a) Group Amidakuji (合作アミダクジ):** 19 players each secretly draw 10 rungs on a shared 19-line ladder (190 rungs in total) and claim a start line first-come-first-served. The result sets each player's order number. Because the players build it themselves, each branch is a 50/50, so you are most likely to land near the spot directly below your start. — https://ja.wikipedia.org/wiki/LIAR_GAME

**(b) Human Auction (人間オークション):**
- **Rules:**
  - Everyone is lent ¥300M.
  - In order-number sequence, each player stands on stage while the others bid in ¥10M steps. **The winning bidder's team absorbs that player, who can't refuse.** Teams bid with their pooled money.
  - The auction stops when there are 4 teams of 4. **The 3 left over are eliminated, and each also pays a ¥200M special penalty (¥600M total), which goes to the eventual champion.**
  - Final confirmation of a bid needs a fingerprint, but every other tablet operation works for anyone. You can therefore grab someone's tablet and force their thumb onto it.
  - A player already holding ≥ ¥200M in profit can drop out here with no debt.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Nao's proposal:** The ¥200M+ holders drop out and pay the penalty, so *nobody* enters the final in debt. Sakuma and Takashima oppose it, and Kaneko drags them out with her. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Yokoya's counter:** He makes sure Nao and Akiyama end up on opposing teams for the first time and torpedoes their plan to save everyone. Akiyama then produces "an elaborate plan that upends Yokoya's objective". — PLANETA vol 18: https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/275513/liar-game-n-1819.pdf
- **Fans:** A fan says Akiyama "basically eliminate[d] the three wealthiest players". — https://www.reddit.com/r/liargame/comments/1hkww2g/i_created_a_100_winning_strategy_to_defeat_akiyama_in_human_auction/. One reader calls it "a great exploration of character… the bidding war over Nao was excellent"; another, "the NPC's lack of character development and intelligence Peaks here." — https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/ and https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/

**(c) Record of the Four Kingdoms (四国志ゲーム):**
- **Rules:**
  - 4 teams of 4. Each team has 100 LP and ¥1.2bn pooled.
  - Each round, a "commander" inside the team's command tower enters up to 3 of 6 actions (attack or defend vs each other country). **Each action costs 1 LP.** An attack that isn't defended deals 3 LP.
  - Teams may negotiate freely during the 20-minute planning time.
  - A team at 0 LP is out and forfeits all its money. The last country standing takes **¥5.4bn**: the losers' ¥4.8bn plus the ¥600M auction penalties.
  — https://ja.wikipedia.org/wiki/LIAR_GAME
- **The designed-in loophole:** "実はこのゲームには大きな欠陥がある" (in fact this game has a major flaw). **If every surviving team is at exactly 1 LP, any action at all eliminates whoever takes it, so no one can act and the game deadlocks.** — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Plot:**
  - Yokoya turns the other two teams on Akiyama's team, "sacrificing his own team's win to destroy Akiyama and Nao" (vol 18). Nao and Akiyama are disqualified. "Akiyama, however, exploits a loophole that ends the game with no winners or losers. The executives then reveal the game's true objective" (vol 19). — https://en.wikipedia.org/wiki/List_of_Liar_Game_chapters
  - JAWP: Akiyama planted the stalemate beforehand. Akiyama invented a **fictional "rich player"** (someone who wants to win at any cost because his parents will cover his debts) who supposedly runs a **spy** on another team. Yokoya didn't deny it, so the players believed it. In the end Yokoya **bribes a white-mask staffer to destroy the system and its backups**, and the LGT, unable to continue, admits defeat. — https://ja.wikipedia.org/wiki/LIAR_GAME
- **Fans (mostly negative):**
  - "players just pushing buttons without any real opening for the mind games." — https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/
  - "The development of the stalemate is not facilitated by any change in the other players, but by Akiyama lying and finessing them." — https://www.reddit.com/r/liargame/comments/1uiw66j/final_thoughts_after_finishing_the_manga_spoilers/
  - "the author conveniently shoved the whole thing into an infinite loop just to avoid an actual loss." — https://www.reddit.com/r/liargame/comments/1lqqky9/yokoya_needs_justice/
  - "ending felt a bit rushed… all info dumbed in like one chapter." — https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/
  - In its defence: "If Akiyama doesn't force a stalemate… 12 are guaranteed to lose… the stalemate is a necessary (and temporary) condition." — https://www.reddit.com/r/liargame/comments/1uuaaiv/spoiler_akiyamas_latest_plan_makes_no_sense_given/
  - It is "the most 'warlike' game". — https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/

### 2.10 Adaptation-only games (secondary)

**Garden of Eden Game: film *Liar Game: The Final Stage* (2010)**
- **Rules (JAWP-DR):**
  - 13 rounds. Each player brands their name on one apple: red, gold or silver. Gold and silver are the "forbidden fruit" (betrayal).
  - **All red: everyone +¥100M.**
  - Exactly 1 forbidden: that player +¥200M, the reds −¥100M each.
  - 2+ forbidden: forbidden voters +¥100M, reds −¥100M.
  - **Only one red: that player is named publicly and loses ¥1bn.**
  - No reds: the majority colour +¥100M, the minority −¥100M. All the same forbidden colour: everyone −¥100M.
  - Anyone reaching −¥500M is expelled, unless someone pays their debt.
  - **The scoreboard shows balances anonymously as A–K.** Only one person may be in the voting room at a time.
  - **No written contracts may force someone's vote.** **No money transfers between players after the game**, which is meant to stop sharing the ¥5bn prize afterwards.
  - Apples are judged by the brand and an internal chip, not by how they look. You may vote using someone else's brand.
  — https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E)
- **Plot:**
  - Nao urges all-red; people betray. Fukunaga forms a voting bloc and then betrays it. A hidden saboteur "X" (Sendou) drives Akiyama to −¥1bn. Akiyama returns, exposes X, and disguises a red apple as silver so Sendou loses ¥1bn.
  - Last round: Nao asks Sendou to vote silver (to pay off his debt) and everyone else to vote red. **Sendou instead votes red "because he would not listen to instruction", so the result is all-red.**
  - The reveal: investors had been betting on whether an all-red vote would ever happen.
  — https://en.wikipedia.org/wiki/Liar_Game:_The_Final_Stage
  - CIATR's version: Akiyama melted the red resin off truth apples so they looked silver, and put them at the front, because Sendou always takes the first apple. — https://ciatr.jp/topics/323364
- **Fans:** "the game shows the meaning of Liar Game I think is Garden Of Eden"; it ranks #2 in one complete ranking. — https://www.reddit.com/r/liargame/comments/pqdcnt/ranking_every_game_in_liar_game/

**Angels & Demons (drama Season 2's version of Pandemic; renamed because of the swine-flu scare)** and **Gold Rush (drama-original)**: CIATR summarizes Gold Rush as two nations moving gold bars between vaults as couriers and sheriffs, with gold depositable in enemy vaults via shared cards. Nao's side won 41–6. — https://ciatr.jp/topics/323364. The renaming is from https://ja.wikipedia.org/wiki/LIAR_GAME. *Treat these details as secondary.*

**Taboo Game (spin-off drama "Fukunaga vs Yokoya"):**
- Two players alternate attack and defence.
- The defender writes up to 3 "taboos" (forbidden actions) on a public card but secretly marks only one as real; the others are dummies.
- The attacker has 15 minutes to move money into their own trunk.
- Whoever breaks the real taboo, attacker *or* defender, loses ¥100M. Two outs in a row means an instant loss.
- A taboo can't be reused, and any taboo that directly forbids taking money counts as the same single "protect money" taboo.
— https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E)

**Korean drama (tvN 2014)**
- Reframed as a reality show with a ₩10bn prize. — https://en.wikipedia.org/wiki/Liar_Game_(2014_TV_series)
- Episode games: 500-Million Game, Minority Game, Layoff Game, "President Game", Smuggling Game, Losers' Revival + "Last Man Standing". — https://thetvdb.com/series/liar-game-kr/seasons/official/1
- Rules of the President Game: **UNVERIFIED** (I could not find them).
- Critic Aju News: it "couldn't escape the frame of *The Genius*", and its tension felt "manufactured" (만들어진 긴장감). It praised Nam Da-jung's line "사람이 사람을 믿는 것이 죄인가" ("Is it a sin for people to trust people?"). — https://www.ajunews.com/view/20141126082526193

### 2.11 Names in the brief that I could NOT verify

- **"Pirate Game": UNVERIFIED / not found.** No source I opened mentions a pirate game in the manga, the Japanese drama (S1, S2, films, spin-offs) or the Korean drama episode list. The JAWP game list, JAWP-DR, the thetvdb Korean list and English web search all came up empty. It may be confused with the classic game-theory "pirate game" puzzle.
- **"Lies and Truth": UNVERIFIED / not found** under that name. Possibly it means the Downsizing mini-game **"Light and Darkness" (光と闇)** (§2.3), or the drama's "Angels and Demons".

---

## 3. Fan consensus: rankings, praise and complaints

- **Most-praised games:** Contraband and Musical Chairs at the top, then 17 Poker and Minority Rule. — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/, https://www.reddit.com/r/liargame/comments/pqdcnt/ranking_every_game_in_liar_game/, https://www.reddit.com/r/liargame/comments/1n770i8/contraband_game_is_the_best_display_of/
- **Least-praised:** Round 1, Human Auction (split opinion), 24-chamber roulette, Four Kingdoms. — same threads, plus https://www.reddit.com/r/liargame/comments/1uiw66j/final_thoughts_after_finishing_the_manga_spoilers/
- **Praise for the formula:** "誰でも理解できるシンプルなゲームを前提として、高度な読み合いや騙し合いが行われる" (sophisticated mind games on top of simple games anyone can understand). The protagonist's refusal to give in to cynicism is "very unconventional for a death-game protagonist, but that is precisely why it may have great appeal." — https://realsound.jp/book/2025/09/post-2141135.html
- **Praise for the theme:** The games are "social experiments based on real economic and political systems… Take a real system → turn it into a game → give people incentives → see how people behave → show the consequences." — https://www.reddit.com/r/liargame/comments/1vo5b36/liar_game_is_much_deeper_than_a_psychological/
- **Recurring complaints:**
  1. **Comprehensibility.** Bid Poker is "too complex"; Contraband confuses anime-only viewers; "Too often he explains the solution and I'm like… 'Yeah, sure'." — https://www.reddit.com/r/liargame/comments/1uigdd0/briefly_explaining_what_makes_each_arc_of_liar/, https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/
  2. **Antagonist nerfed at the payoff.** "Every time there was a one-on-one match between Akiyama and Yokoya, the author made Yokoya lose for absurd or illogical reasons." — https://www.reddit.com/r/liargame/comments/1lqqky9/yokoya_needs_justice/
  3. **NPC sameness.** Background players are interchangeable ("could have been replaced by literally anyone else"). Others defend this: "the Liar Game… is structured to have a large pool of ordinary people… to serve as prey/fodder for a smaller group of elite players." — https://www.reddit.com/r/liargame/comments/1wfr8cj/liar_game_and_the_curse_of_the_npc_characters/
  4. **Premise plausibility.** "an unpayable debt with no legal basis." — https://www.reddit.com/r/manga/comments/3fjr41/liar_game_is_a_truly_horrific_manga/
  5. **Rushed ending and info-dump reveal.** — https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/, https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/
  6. **Over-explaining.** Too much LGT-staff commentary in the finale ("10 chapters primarily composed of indistinguishable LGT guys commenting"). — https://www.reddit.com/r/liargame/comments/1uiw66j/final_thoughts_after_finishing_the_manga_spoilers/. A drama reviewer complained of "overdone explanations" of betrayals. — https://jamaipanese.com/liar-game-japanese-drama-review/ (reader comment)
- **Influence:** English Wikipedia lists *Squid Game* as "influenced by *Liar Game*", citing a Variety interview with Hwang Dong-hyuk. I could not open Variety, so the exact quote is **UNVERIFIED**. — https://en.wikipedia.org/wiki/Liar_Game

---

## 4. Design patterns: how Liar Game hides cooperation inside competition

Each pattern lists its sources. The "For DMA" lines are **[my synthesis]**.

1. **The house's profit is the only thing defection creates.** The rake fires only on selfish acts: the drop-out fee, or dealer confiscation when both pass, both check or both miss. So the cooperative outcome is "starve the house". — https://ja.wikipedia.org/wiki/LIAR_GAME
   - Revival 2 confiscation rules: Russian roulette's 31 chips to the dealer after 5 passes, the 17 Poker void pot, Stationary Roulette's double-miss. Nao's realization that "the true opponent is the LGT itself". — https://en.wikipedia.org/wiki/List_of_Liar_Game_chapters
   - *For DMA:* every game should have a visible "algorithm tax" that only triggers on betrayal or panic.
2. **Cooperative clauses hidden in the win condition.**
   - Pandemic: "if ≥6 qualify, all who meet the bar qualify".
   - Round 1: if neither side takes money, both leave debt-free.
   - Bid Poker: buying nothing guarantees +¥50M.
   - Downsizing: the house loses ¥100M.
   — https://ja.wikipedia.org/wiki/LIAR_GAME
   - *For DMA:* hide the loophole in a quantifier ("all of them", "at least N", "if no one…").
3. **Separate "winning" from "getting paid".**
   - Contraband: team victory vs individual accounts, and unsmuggled money goes to the *opponents*.
   - Musical Chairs: only the winner's *named* medals are worth anything.
   - Bid Poker: losing with nothing bought still profits.
   — https://ja.wikipedia.org/wiki/LIAR_GAME, https://en.wikipedia.org/wiki/Liar_Game
   - This one split produces most of the big twists.
4. **Unverifiability as the engine of fear.**
   - Pandemic: status is visible only alone in a locked booth, and you can't prove it.
   - Eden: anonymous A–K scoreboard, one person in the voting room at a time.
   - Minority: secret paper ballots. Musical Chairs: anonymous Parent vote.
   — https://ja.wikipedia.org/wiki/LIAR_GAME, https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E)
   - Cooperation is *possible* but can never be *confirmed*, which is exactly the prisoner's dilemma JAWP names.
5. **Tradeable instruments turn abstract trust into leverage.**
   - Downsizing: M-tickets are enforceable contracts with a ¥100M penalty, and Fukunaga uses them to *lock* everyone into persecuting Nao.
   - Bank cards that work for anyone (Contraband). Named medals (Musical Chairs). Cheques (the X reveal). Fingerprint-only-at-confirmation tablets (Human Auction).
   — https://ja.wikipedia.org/wiki/LIAR_GAME, https://en.wikipedia.org/wiki/Liar_Game
   - Counter-pattern: Eden *bans* coercive contracts and post-game transfers to make trust harder. — https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E)
6. **Votes as currency; majority and minority inverted.** Minority Rule punishes the majority. Downsizing turns votes into goods that can be bought. Musical Chairs gives the eliminated a vote. — https://ja.wikipedia.org/wiki/LIAR_GAME. A fan reads Minority Rule as asking why a numerical majority doesn't turn into power. — https://www.reddit.com/r/liargame/comments/1vo5b36/liar_game_is_much_deeper_than_a_psychological/
7. **Eliminated players stay on the board.** Musical Chairs' Gaya vote, guard and block, and they decide the ending with a human wall. In Minority Rule, an eliminated player lingering in the mansion is the clue that one person controls the votes. — https://ja.wikipedia.org/wiki/LIAR_GAME, https://en.wikipedia.org/wiki/Liar_Game
   - *For DMA:* "dead" students as a kingmaker bloc.
8. **The antagonist uses the hero's own insight first (mirror layering).**
   - Fukunaga runs Akiyama's 8-person team plan *three times over* with herself in every team.
   - Yokoya runs Akiyama's "drain their ATM" plan before Akiyama does.
   — https://en.wikipedia.org/wiki/Liar_Game
   - The reader learns the clever solution and then learns it has already been turned against the hero. That gives at least three layers: plan, counter-plan, counter-counter-plan via triple agents.
9. **Literal-rule and physical exploits that were fairly disclosed.**
   - A double-sided card has no "face". The revolver is weight-biased, which is stated in the rules.
   - A perfect-shuffling dealer with a fixed starting order. Thick booth doors muffle voices.
   - The alarm sound can be reproduced. You may peek into an envelope you may not open. Apples are judged by chip, not colour.
   - A "personal belonging" can be a person (Akiyama as Nao's possession).
   — https://ja.wikipedia.org/wiki/LIAR_GAME, https://en.wikipedia.org/wiki/Liar_Game, https://ja.wikipedia.org/wiki/LIAR_GAME_(%E3%83%86%E3%83%AC%E3%83%93%E3%83%89%E3%83%A9%E3%83%9E)
   - The exploit-enabling fact is always printed in the rules or shown early.
10. **Mock or tutorial games are part of the battle.**
    - Pandemic mock: the top 3 are certified clean, and Yokoya uses the mock to seed distrust.
    - Musical Chairs mock: the map envelopes.
    - Bid Poker mock: winnings carry over.
    — https://ja.wikipedia.org/wiki/LIAR_GAME, https://www.reddit.com/r/liargame/comments/1tyat07/why_dont_they_just_look_at_the_vaccine_count_to/
11. **Structural deadlock as the ultimate "nobody loses" ending.** In Four Kingdoms, all teams at 1 LP means nobody can act. — https://ja.wikipedia.org/wiki/LIAR_GAME
    - Fans found it the least satisfying payoff because it is reached by lying, not by players changing, and the gameplay is "pushing buttons". — https://www.reddit.com/r/liargame/comments/1uiw66j/final_thoughts_after_finishing_the_manga_spoilers/, https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/
    - *For DMA:* if the loophole is a deadlock, the climax must still be a test of *character* (someone has to choose not to act).
12. **Moral reputation as a coordination device.**
    - Bid Poker unites nearly everyone on "Kanzaki Nao will not betray me". — https://ja.wikipedia.org/wiki/LIAR_GAME
    - Nao's honesty is also *weaponized*: she lies to Fukunaga to force the roulette tie, and Fukunaga sells a fake "Nao blinks when lying" tell. — https://en.wikipedia.org/wiki/Liar_Game
    - REALSOUND: the heroine grows into a "shrewd good person" who keeps her ideal while learning to read people. — https://realsound.jp/book/2025/09/post-2141135.html
13. **The antagonist rules by debt and rank.**
    - Contraband: Yokoya's loyalty points, bottom 2 get nothing, everyone owes him ¥200M.
    - Prisoner's-dilemma interrogation: reward the first to confess.
    — https://en.wikipedia.org/wiki/Liar_Game
    - The hero answers with trust plus verification (triple agents, and Akiyama's ¥91.12M test).
14. **Making the solution legible step by step** (techniques visible in the sources):
    - (a) Plant countable anomalies early, such as the "12–10, the closest possible vote" and "6–4" tallies. — https://en.wikipedia.org/wiki/Liar_Game
    - (b) Run on-page experiments that test a hypothesis (¥91.11M vs ¥91.12M). — https://en.wikipedia.org/wiki/Liar_Game
    - (c) Show the ledger: per-player money after Contraband (Nao ¥100M, Akiyama ¥422M, other Day players ¥472M each, Yokoya ¥1.03bn). — https://en.wikipedia.org/wiki/Liar_Game
    - (d) Masked dealers in a back room explain the stakes to the audience. Fans saw this as Kaitani's response to Contraband's difficulty, but in the finale it became too much. — https://www.reddit.com/r/liargame/comments/1svuyi8/ranking_liar_game_manga_arcs_again_cause_why_not/, https://www.reddit.com/r/liargame/comments/1uiw66j/final_thoughts_after_finishing_the_manga_spoilers/
    - (e) Use simple base rules (yes/no vote, musical chairs, poker) so complexity sits in the *social* layer rather than the arithmetic. Fans rate Pandemic and Musical Chairs "the absolute sweet spot" and call Bid Poker too complex. — https://realsound.jp/book/2025/09/post-2141135.html, https://www.reddit.com/r/liargame/comments/1uigdd0/briefly_explaining_what_makes_each_arc_of_liar/

---

## 5. Instructive games, short form (for the summary)

| Game | Core rule | Hidden insight | Why it works |
|---|---|---|---|
| Minority Rule | Majority eliminated each yes/no vote | A team split evenly always keeps someone in the minority; X places herself in *all* teams; the final public-vote trap forces two people to sacrifice | Simple rule, three levels of the same idea, clues the reader can count |
| Downsizing | Fewest votes in 10 rounds loses; votes are tradeable; contracts enforceable | Corner the vote market, then pick who "loses" in order to rescue them | Turns the loss slot into a lifeboat; contracts become a trap |
| Contraband | Smuggle ≤¥100M past an inspector; team score, individual payouts | Winning ≠ profit; bank cards move money between "countries"; plan, counter-plan, triple agents | Two layers of win conditions plus team betrayal incentives |
| 17 Poker | 17-card deck, perfect-shuffling dealer | Track all cards through deterministic shuffles; ask for extra shuffles | Fair-play physical exploit; disclosed but overlooked |
| Pandemic | Hidden infected status, unverifiable; ≥6 at 4 vaccines → all pass | Everyone can pass; the fight is over verification and control of the booths | Pure trust problem with a cooperative fixed point |
| Musical Chairs | Hidden chairs, Parent vote includes eliminated players; only the winner's named medals pay | Abstain, use a dummy leader, then make the enemy's front man win so his discarded medals pay out | Three-way war plus kingmaker losers plus a winner/payout split |
| Bid Poker | Auction stage money goes to the house; bottom places pay the top | Don't feed the house; buying nothing guarantees profit; unity through trusting Nao | Shows the "starve the house" lesson, at a high cost in complexity |
| Eden (film) | All red = everyone gains; lone red loses ¥1bn; anonymous board; no side-payments | Pure trust game; the all-red result arrives through a saboteur's stubbornness | The cleanest "everyone wins if…" design |
