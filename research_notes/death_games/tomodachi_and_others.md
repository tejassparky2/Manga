# Death-game reference research: TOMODACHI GAME, KAIJI, KAKEGURUI, SQUID GAME, ZERO ESCAPE

Prepared for: *Dead Man's Algorithm* (game-design research only; nothing here is canon for the manga).
Compiled: 2026-10-28.

## 0. Method and how to read these notes

- Every rule, solution, plot fact or quote below names the source it came from. Where I could only find a fan's reading, it is marked **[Fan claim]**. Where sources disagree, it is marked **[Conflict]**. Where I could not verify something, it is marked **UNVERIFIED** or left out.
- My own synthesis and design takeaways are marked **[Analysis]**. They are not claims about the works.
- **Access notes:**
  - Fandom wikis (tomodachi-game, kaiji, kakegurui, squidgame, zeroescape) refused the normal page fetch (HTTP 402/403). I read the same pages' wikitext through each wiki's MediaWiki API (`/api.php?action=parse&page=<Title>&prop=wikitext`). The citations give the normal page URL, `https://<wiki>.fandom.com/wiki/<Title>`.
  - Reddit posts were read with the local Reddit API tool (`tools/reddit_tool.py`).
  - Wikipedia pages and some articles were read through a web-fetch tool that summarises and quotes. Quotes from those pages are as that tool returned them.
  - Anime News Network's "This Week in Anime" column on Tomodachi Game (https://www.animenewsnetwork.com/this-week-in-anime/2022-05-05/.185340) returned 403. **Not used.** A search-engine snippet said it criticised cutting to observers, but I could not open the page, so treat that as UNVERIFIED.
- Most TOMODACHI GAME plot detail comes from fan-wiki episode summaries of the 2022 anime, which covers manga ch. 1–25 (arc table: https://tomodachi-game.fandom.com/wiki/Tomodachi_Game_Story-Arcs). Detail on the manga-only adult games is thinner and leans on fans.

---

## 1. TOMODACHI GAME (manga: Mikoto Yamaguchi, concept/story; Yuki Sato, art; anime 2022)

### 1.1 Basic facts
- The manga ran in Kodansha's *Bessatsu Shōnen Magazine* from 9 Dec 2013 to 8 Aug 2024 and was collected in 26 volumes. Mikoto Yamaguchi is credited as author and Yuki Sato as author and illustrator. Source: https://en.wikipedia.org/wiki/Tomodachi_Game
- The TV anime (Okuruto Noboru; director Hirofumi Ogura; writer Kenta Ihara) has 12 episodes and aired 6 Apr to 22 Jun 2022. Source: https://en.wikipedia.org/wiki/Tomodachi_Game
- Wikipedia's premise: the class trip funds are stolen, and the five friends are "dragged into the mysterious Tomodachi Game as a result of someone's debt. The friendship of the five will be put to the ultimate test against the promise of wealth there." Source: https://en.wikipedia.org/wiki/Tomodachi_Game

### 1.2 The core system: debt, entry fee, name plates, anonymity
The system itself is a suspicion engine, before any single game starts.

- **Debt as the hook.** The games are "organized as a business, mainly for debtors to pay their own debts." The participation fee is "presumably 10% of the players' total incurred debt", and the debt is then divided among the players. Source: https://tomodachi-game.fandom.com/wiki/Tomodachi_Game
  - Japanese Wikipedia agrees. Entry requires a debt above a threshold, and the applicant pays one-tenth of the debt as the entry fee. Each cleared game pays ¥2 million. If you don't join, the original debtor keeps the debt; if you join, it is split equally. Source: https://ja.wikipedia.org/wiki/トモダチゲーム
- **The opening set-up (Group C).**
  - The class's ¥2 million trip money is stolen.
  - The five friends are lured by forged letters, tasered, and wake in a white room.
  - Manabu tells them one of them owes ¥20 million and that the ¥2 million entry fee is already paid.
  - Yuichi realises the trip money must have paid the fee.
  - If they refuse to play, the fee is lost and the debtor alone keeps the debt. If they play, each carries ¥4 million.
  - Source: https://tomodachi-game.fandom.com/wiki/Episode_1
- **The "don't ask" moment.** Shiho argues they should not try to find out who the debtor is. Everyone agrees, but Yuichi stays unsure. Manabu presses him on whether he wants to know "who he shouldn't trust." Source: https://tomodachi-game.fandom.com/wiki/Episode_1
- **Name plates (the anonymity rule).**
  - Each player's plate shows their current debt.
  - Showing the number to anyone doubles your debt. This applies even outside the games.
  - But "players are allowed to say their numbers out loud."
  - Source: https://tomodachi-game.fandom.com/wiki/Tomodachi_Game
  - **[Analysis]** Anyone can claim a debt, and nobody can prove one. That one rule makes every statement about money unverifiable.
- **The audience ("Gods").** The funders watch live, and their chat floats in the sky during Backbiting Sugoroku. Source: https://tomodachi-game.fandom.com/wiki/Tomodachi_Game
- **The quit option.** Players can withdraw and are freed at once, but the fee is not refunded, so the original debtor carries it alone. Source: https://tomodachi-game.fandom.com/wiki/Tomodachi_Game

### 1.3 The games, one by one

#### Game 1: "Kokkuri-san" Game (manga ch. 1–3; anime ep. 1–2)
**Rules.** Source: https://tomodachi-game.fandom.com/wiki/%22Kokkuri-San%22_Game
- Five rounds, one yes/no question each. Getting at least one round "correct" clears the game.
- All five players keep a finger on a ten-yen coin and push it to YES or NO.
- If all five agree, the coin moves to that answer. If answers split, **the coin moves to the option with the fewest votes.**
- A questioner reads sealed question cards in order. The answer is printed on the questioner's card.
- Only the questioner may speak. Anyone else who speaks has their debt doubled.
- If the game is not cleared, **the player with the largest debt takes on everyone else's debt.**
- Cards 1–4 read: "Move the ten yen coin to 'yes' to win the round. Move the ten yen coin to 'no' to half the questioner's debt."
- Card 5 reads: "We, after all of this, will still be friends forever." It carries no debt clause.

**What happened.** Source: https://tomodachi-game.fandom.com/wiki/Episode_1 and https://tomodachi-game.fandom.com/wiki/Episode_2
- Q1 is about Mt. Fuji and Q2 is "is 1+1=2". The coin goes to NO both times.
- Yuichi's own card (Q4) has no question. In small print it offers YES = clear the game, NO = halve the reader's debt.
- From this he deduces that earlier readers had been privately offered the same bribe. "His friends chose easy answers and gave incorrect answers themselves to halve their debt."
- On his own question he chooses YES, but the coin still goes to NO.
- He realises the fifth reader, Yutori, has no halving clause. If round 5 fails, the player with the largest debt (likely Yutori) takes everyone's debt.
- The observers note that "no team had cleared the Kokkuri-san game after reaching the fifth question." Source: https://tomodachi-game.fandom.com/wiki/Episode_1

**Yuichi's solution (the hidden insight).** Source: https://tomodachi-game.fandom.com/wiki/Episode_2
- Yuichi deliberately speaks ("do you know what color is Shiho's underwear today"). This breaks the talking rule, doubles his own debt and makes him the largest debtor.
- He then bluffs that his card changed the rules, so the penalty now goes to the player with the **least** debt.
- Anyone who secretly halved their debt is now the "hunted". They cannot speak to object, because objecting would reveal that they halved.
- He says he is "joking", but his expression is read as a final threat. The coin goes to YES and the game is cleared.
- The cost: Yuichi pays the doubling, and he has "plant[ed] the seed of doubt that one of them is a traitor" (episode summary wording).

**Aftermath.**
- The question cards were printed in **disappearing ink**, so the bribe clauses cannot be checked later. Source: https://tomodachi-game.fandom.com/wiki/Episode_2
- Shiho privately admits her debt is ¥7.6 million rather than the ¥3.6 million everyone claimed, because a small noise she made counted as speaking. Source: https://tomodachi-game.fandom.com/wiki/Episode_2
- Much later, the revealed total debt (¥10.8M) shows that several people lied about their debts after Kokkuri. Tenji admits he halved his. Source: https://tomodachi-game.fandom.com/wiki/Episode_7

**Why it works [Analysis].**
- The **minority-wins** rule gives every single player a veto over the cooperative outcome. The cooperative answer is trivially "correct", yet it can be secretly sabotaged by one person.
- The bribes are **private and asymmetric**: each player only sees their own card.
- The final question turns the game's question ("will we be friends forever?") into a literal vote on trust after four rounds of evidence of betrayal.
- Yuichi wins not by finding the traitor but by **changing who is afraid**: he reverses the incentive with a believable, unverifiable threat.

#### Game 2: Backbiting Sugoroku (Kageguchi Sugoroku; manga ch. 4–11; anime ep. 2–6)
**Rules.** Source: https://tomodachi-game.fandom.com/wiki/Backbiting_Sugoroku
- Each round, each player spends three minutes alone in a locked booth writing "backbiting cards" that expose other players' secrets.
- A player may target several people or hand in a blank card.
- The audience votes on which secret is "most unforgivable". 1st place moves 5 spaces, 2nd moves 4, and so on.
- If **everyone hands in blank cards**, there is no vote and everyone moves one space.
- If a card is proven to be a lie, **the liar is moved in front of the player closest to the goal.**
- Spaces carry penalties, rewards or special chances. **All debt accumulated during the game falls on whoever reaches the goal first.**
- **[Conflict]** The prize terms differ by source:
  - The game page says players who do not reach the end get a ¥1 million bonus each and may skip Game 3.
  - Japanese Wikipedia says the others get ¥1 million bonuses.
  - The Episode 2 page words it as "anyone remaining in the game will receives an additional 1 million debt."
  - The game page and Japanese Wikipedia agree, so a **bonus** looks right.
  - Sources: https://tomodachi-game.fandom.com/wiki/Backbiting_Sugoroku, https://ja.wikipedia.org/wiki/トモダチゲーム, https://tomodachi-game.fandom.com/wiki/Episode_2

**The obvious cooperative path is a trap.** Sources: https://tomodachi-game.fandom.com/wiki/Episode_2 and https://tomodachi-game.fandom.com/wiki/Episode_5
- The friends hand in blanks and move one space at a time, but early spaces cost ¥100k and then ¥500k. Yuichi estimates 60 spaces.
- Later Yuichi reasons that the game "isn't fair at all": they lost ¥3 million in a game worth ¥2 million.
- He argues, "Since there is an audience, it means there is management too. And an unfair game isn't fun to watch."
- He concludes that, as in normal sugoroku, positive and negative squares balance over the whole board.
- Maria confirms the designers put "the negatives mostly in the first half" to discourage moving together.

**The traitor.** Sources: https://tomodachi-game.fandom.com/wiki/Episode_3, https://tomodachi-game.fandom.com/wiki/Episode_4
- Tenji wrote most of the bad-mouthing cards.
- He stole the trip money and applied for the game.
- He had bugged Shiho through a gifted anti-theft keychain to collect secrets.
- His goal was to isolate Shiho.

**Yuichi's three traps.** Sources: https://tomodachi-game.fandom.com/wiki/Episode_5, https://tomodachi-game.fandom.com/wiki/Episode_6
1. **Card-passing tests.** Yuichi secretly passed instruction cards to test people.
   - Shiho was told to write a secret that only Yuichi had told her. Once that card appeared, every other card that round was the traitor's.
   - Yutori was told to write a secret about Shiho that only Yutori knew. The other card that round ("Tenji lies about his age") could only have come from Tenji or Makoto.
   - He passed one card while tapping Shiho, and one during a staged slap.
2. **Controlled order plus volunteering.**
   - Yuichi controlled the order people entered the booth.
   - When the "special chance" space let Shiho name someone, Makoto volunteered to be exposed. Yuichi reasoned that volunteering would be too risky for the traitor, so this cleared Makoto.
3. **A self-identifying card.**
   - Everyone was told to write "I am the one who applied to the Tomodachi Game." Only the traitor would be telling the truth, and everyone else would take the liar's penalty.
   - Yuichi told the others to hand in blanks while Tenji was in the booth. Tenji alone wrote the card.
   - The friends proved loyalty by handing Yuichi their name plates. Yuichi had worked out that **giving** a plate does not double debt; only **showing** the number does. He had tested this by lending Shiho his own plate.
   - Yuichi also read Tenji's behaviour as out of character. Tenji is normally a calm mediator, yet he started a fight with Makoto and blamed him for secrets Makoto could not have known.

**Ending the game by self-sacrifice through the lie rule.** Source: https://tomodachi-game.fandom.com/wiki/Episode_6
- Shiho is one space from the goal. Yuichi confesses that the card "Makoto killed a person" was his own deliberate lie.
- The liar penalty jumps him in front of Shiho, so he reaches the goal, clears the game and takes the debt.
- He reveals that he himself has killed people. Manabu says three.
- Tenji confesses his own lie and follows Yuichi into Game 3.

**Why it works [Analysis].**
- **Anonymous accusations** make every secret a weapon, and only the writer knows who wrote it.
- The audience vote turns **shame into movement**, so being hated means losing.
- The "everyone blank" truce is available but deliberately **made expensive early**, which tests patience and trust.
- The **lie penalty**, built as a deterrent, doubles as the escape hatch, but only for someone willing to sacrifice.
- The solution needs **exact reading of the rules** (giving versus showing a plate) and **reasoning about the designers' incentives** (the game must be watchable).

#### Side story: Friendship Janken (Tomodachi Janken; special omake chapter)
Source: https://tomodachi-game.fandom.com/wiki/Friendship_Janken

**Rules.**
- Five friends each hold one Rock, one Paper and one Scissors card, and each card can be used once.
- If all three rounds end in a **draw**, the game is cleared.
- Talking is allowed.
- Each win lets the winner move ¥500k of debt onto the losers. If the game isn't cleared, remaining debt is doubled.

**What happened.**
- Kenji proposes they all play the same card.
- He secretly plans to defect with Rock while the others play Scissors.
- The other four all play Paper. They later claim they were trying to lose to him on purpose.
- Kenji is now at ¥3M and the others at ¥500k.
- In round 2 they promise to throw Rock so Kenji can win with Paper. He agonises, decides "they are his friends", plays Paper, and they betray him with Scissors.
- Final debts: Kenji ¥10M, the others ¥0.

**Why it works [Analysis].**
- The simplest possible cooperative loophole ("everybody show the same thing") is fully public. It fails purely because each player can profit from defecting and fears the others will.
- It is a clean model of "everyone can survive, but greed and fear break it."

#### 72-hour preparation and Game 3: Friendship Hide-and-Seek (manga ch. 12–20; anime ep. 7–11)
**Rules.** Sources: https://tomodachi-game.fandom.com/wiki/Friendship_Hide-And-Seek and https://tomodachi-game.fandom.com/wiki/Episode_7, https://tomodachi-game.fandom.com/wiki/Episode_8
- Two teams play in a huge forest: Group C (Yuichi, Tenji and the "solo" Maria) against Group K (five basketball players).
- Each team has one hider. Everyone else is a seeker, and the first team to find the other team's hider wins.
- Violence **against the opposing team** is prohibited. The hider cannot move once settled. Giving or taking name plates is forbidden.
- Breaking a rule doubles the team's debt and loses the game.
- Everyone gets a phone that can reach every player.
- Food sits at the central station, and **seekers must carry food to their hider.**
- Only the hider holds a **give-up button**, which loses the game for their team.
- **Switching sides:**
  - A seeker may defect once. They must announce it at the food station, and one member of the new team must accept.
  - If the new team wins, the defector skips Game 4 and their debt is pushed onto their old team.
  - If the new team loses, the defector takes a share of the losing debt and returns to the old team.
  - With only two original members on Group C, a defection would end the game immediately.
- The preceding 72 hours were spent in a cave with rations based on team size; Yuichi and Tenji got only one bottle of water. Source: https://tomodachi-game.fandom.com/wiki/Episode_7

**Hidden insight and play.** Sources: https://tomodachi-game.fandom.com/wiki/Episode_8, https://tomodachi-game.fandom.com/wiki/Episode_9, https://tomodachi-game.fandom.com/wiki/Episode_10, https://tomodachi-game.fandom.com/wiki/Episode_11
- Juuzou (Group K's captain) sees that in a huge forest **the food rule is the real game**: whoever carries food leads you to the hider.
  - Group K parks members at the food station to follow Group C's seekers.
  - They chose the biggest, most patient man as hider.
- Yuichi deliberately **does not feed Tenji for days**, so he never leads anyone to him. This also tests whether Tenji will press the give-up button.
- Yuichi offers to defect to Group K as a probe and studies Group K's relationships.
- He pushes Maria (secretly from management) off a cliff to split pursuers, then uses her as a "honey trap" to set Hyakutarou and Chisato against each other.
- Hyakutarou defects to Group C to protect Maria.
- The genius Kei (Group K's real leader) counters. Hyakutarou becomes a "time bomb": if he strikes a Group K member, Group C loses. Kei then turns Maria and finds Tenji.
- **Yuichi's final key:** the violence ban covers **opponents only**; violence against your own teammate is allowed. Hyakutarou is now on Group C.
  - Yuichi phones Juuzou, the hider with the give-up button, and makes him listen to "Hyakutarou" being beaten and a finger being broken.
  - Juuzou presses give-up. Group C wins.
  - Afterwards Juuzou finds Hyakutarou's fingers intact: Yuichi had broken **his own** finger. Yuichi had also promised that Juuzou could hit him as much as he had hit Hyakutarou.
- Yuichi also infers that the debtor in Group K is Juuzou, not Kei.

**Why it works [Analysis].**
- A logistics rule (feed your hider) quietly becomes the information leak.
- The give-up button gives the **opponent's friendship** a lever: the hider loses if he cares about his teammate.
- The side-switch rule creates a live "traitor market".
- The decisive loophole is a narrow rule scope (*opponent* violence) combined with an emotional bluff.
- Fans single this game out as showing Yuichi's trial and error (see §1.6).

#### Special games: "The Weak Win" and Rock-Paper-Fingers (manga ch. 23–25; anime ep. 11–12)
Sources: https://tomodachi-game.fandom.com/wiki/Episode_11, https://tomodachi-game.fandom.com/wiki/Episode_12

**The Weak Win.**
- Kuroki, a thug impersonating the Tomodachi Game, kidnaps Yutori.
- There are three rounds of physical pain. Yutori chooses who takes each round, and if she picks herself her version is lighter (for example 1 punch against Yuichi's 3).
- Yuichi may not speak while she decides.
- Yuichi takes every round: punches, three nails pulled, and his hand stabbed three times.

**Rock-Paper-Fingers.** Yuichi then challenges Kuroki.
- If Kuroki wins, he gets ¥10M.
- If Yuichi loses, he cuts fingers off depending on his own throw: Paper costs 5, Scissors costs 2, Rock costs 0.
- Yuichi announces that his bandaged right hand can only make Rock or Paper. Kuroki throws Paper, the "safe" counter.
- Yuichi throws Scissors **with his left hand**. He never said he couldn't use it.
- Kuroki's men refuse to take his place when offered "only one finger" instead of his five. The observer sums up that the game exposed that Kuroki had "no brains, no guts and he would easily betray his friends."

**Why it works [Analysis].**
- A self-imposed constraint that is announced but **narrowly worded** is the loophole.
- The real objective was social: break the loyalty of Kuroki's gang.
- Fans called the left-hand trick "a bit *too* obvious" (§1.6). Keep this kind of trick as a garnish, not a main course.

#### Game 4: Friend-Sin Trial (Tomo-zai Saiban; manga ch. 26–34; not animated)
**Rules.** Source: https://tomodachi-game.fandom.com/wiki/Friend-Sin_Trial
- An optional "special" game: players may decline it and go to Game 5.
- To save Makoto Shibe, charged with murdering his father, they have one week to win "votes" from 28 classmate jurors in the form of money.
- ¥1.96M was handed to the jurors as a "school trip fee refund", and must be collected back **from classmates**; the players may not supply it.
- There is no prize money. If cleared, Shibe's ¥500M debt is added to the group's total.

**Resolution.** Only fan descriptions are available, so these are **[Fan claim]**s:
- Tenji fakes a confession in front of the class to buy time.
- Yuichi blackmails a teacher, using a recording.
- A reply says Tenji's actions made the class concerned with the money, "which resulted in them giving it to the teacher."
- Sources: https://www.reddit.com/r/TomodachiGame/comments/1qumn6y/need_explanation_chapter_33/ and https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/
- The full step-by-step is UNVERIFIED.

**Why it matters [Analysis].** It recasts "trust" as **money that third parties must voluntarily hand back**: a vote you can't buy yourself.

#### Adult Game 1: Friends Prison Game (manga ch. 35–47)
**Rules.** Sources: https://tomodachi-game.fandom.com/wiki/Friend%27s_Prison_Game and https://ja.wikipedia.org/wiki/トモダチゲーム
- 12 prisoners.
- **Two ways to clear:**
  - Serve the 20-year sentence.
  - Or, as prison labour, **stand up all 120,000 dominoes**, which clears the game at once.
- Clearing pays ¥100M each.
- Violence is banned (+¥100M debt and game over).
- Somewhere there is a key to the back gate. Whoever holds it can escape when no guard is around, one person per key.
  - An escapee gets a ¥200M bonus.
  - **Each remaining prisoner has ¥400M added to their debt.**
- "Secret betrayal" (密告) is an anonymous nightly vote of all 12. Anyone named by more than half of all votes is exiled the next morning, takes +¥100M debt, and does not clear.

**What happened.**
- Kenji was exiled by the secret vote. Source: https://ja.wikipedia.org/wiki/トモダチゲーム
- Yuichi and Kei escaped together. **[Fan claim]**s on how:
  - They found the real keys and worked together.
  - Yuichi made and planted fake keys "to create chaos", which made people "paranoid, suspicious, and cautious".
  - The dominoes were knocked over on the first night. Fans disagree whether Yuichi did it or "manipulated / pushed someone to do it."
  - Sources: https://www.reddit.com/r/TomodachiGame/comments/1kt0n98/im_looking_for_a_detailed_explanation_of_the/, https://www.reddit.com/r/TomodachiGame/comments/1e8f8zh/prison_game_question/, https://www.reddit.com/r/TomodachiGame/comments/1eodav5/question_about_the_prison_game_ending/
- The exact mechanics are UNVERIFIED. Readers in these threads also found the arc hard to follow.

**Why it works [Analysis].** This is the purest version of the brief:
- An explicit, slow, fully cooperative clear (the dominoes) that one person can wreck.
- A fast individual exit (the key) whose cost falls on everyone else.
- A democratic "protection" mechanism (the exile vote) that doubles as a weapon.

#### Adult Game 2a: All Bet (Jinsei Bakuchi Gēmu; manga ch. 48–65)
**Rules.** Sources: https://tomodachi-game.fandom.com/wiki/All_Bet and https://ja.wikipedia.org/wiki/トモダチゲーム
- Four teams on a cruise ship.
- Every player is "appraised" for a value. Teams may **sell teammates** for gambling funds; sold teammates cannot gamble; a team buys them back by repaying the price before the end.
- Players invent their own gambles.
- There is a boarding fee per player, with a ¥100M penalty if unpaid.
  - **[Conflict]** The fan wiki says ¥1 million; Japanese Wikipedia says ¥10 million (1000万円).
- Japanese Wikipedia lists Yuichi's appraisal as ¥0.
- Yuichi introduces a rule accepted by all teams: each gamble's bets and both parties' consent must be **written down** first; undocumented gambles are void; breaking an agreement costs ¥100 billion. Source: https://tomodachi-game.fandom.com/wiki/All_Bet

**His "special method".** **[Fan claim]** He had **sold** teammates sign gambling papers that become valid once two or more signatories confirm. Rivals who bought back their sold members, or teams caught by the contract wording, lost their savings.
- Fans dispute exactly why some teams were bound. One asks how "Two teams lost money in a bet they didn't know existed."
- Source: https://www.reddit.com/r/TomodachiGame/comments/1iyv6ut/question_about_yuichis_infamous_special_method/
- **[Analysis]** A favourite arc, but its loophole lives in contract fine print that readers struggled to reconstruct. That is a warning about clarity.

#### Adult Game 2b: Friend Murder Game (manga ch. 66–87)
**Rules.** Source: https://tomodachi-game.fandom.com/wiki/Friend_Murder_Game
- A 20 km² island.
- "Money Zombies" hunt players; anyone caught has all current and future money confiscated.
- The game ends when 5 players remain.
- Paint guns:
  - Yellow bullets (¥1M) freeze a zombie for 10 seconds.
  - Red bullets (¥100M) "kill" it.
  - Black bullets freeze a player for 1 minute.
- Players keep whatever money they have at the end.

#### Adult Game 3: The Friendless Game (Tomodachi Gēmu, written 友断ち "friend-severing"; manga ch. 88–127)
**Rules** (as heard by Shiho; each player was briefed alone). Source: https://tomodachi-game.fandom.com/wiki/The_Friendless_Game
- Live together in a snowy lodge for two weeks. Violence is banned.
- Administrators issue tasks individually by phone.
- At the end, everyone votes for anyone but themselves, and the winner gets ¥4.5 billion.
- You can **eliminate a player by reporting their password** (five hiragana or fewer) to admin. A wrong report brings "heavy punishment" on the reporter.

**Fan reading.** **[Fan claim]**
- A group task said to "**Tell** other players your password within 24 hours", which the fan argues is often misremembered as "exchange".
- Fan strategy theories exist. Source: https://www.reddit.com/r/TomodachiGame/comments/1444psc/friendless_game_yuuichis_strategy/
- Not verified.

**[Analysis]** Passwords are **information as ammunition**: telling someone your password is an act of trust that hands them a weapon. Private briefings mean nobody knows anyone else's rules.

### 1.4 The "traitor among friends" structure, across the series
- **Layer 1 (the applicant).** Tenji stole the trip money, applied for the game and wrote the cards. His motive is revenge on Shiho, whom he blames for his friends' betrayal in an earlier Tomodachi Game and for his father's death. Source: https://tomodachi-game.fandom.com/wiki/Episode_7
- **Layer 2 (liars about money).**
  - Several friends secretly halved their debt in Kokkuri and lied.
  - The revealed group total (¥10.8M) exposes this, and Tenji calls Shiho "quite the con artist" on the numbers.
  - Source: https://tomodachi-game.fandom.com/wiki/Episode_7
- **Layer 3 (the real traitor).**
  - Japanese Wikipedia calls Yutori "実は最初から友一たちを騙していた真の裏切り者" ("the real traitor who had been deceiving Yuichi's group from the start"). Source: https://ja.wikipedia.org/wiki/トモダチゲーム
  - English Wikipedia: she "is responsible for the murder of another participant's father to frame Sawaragi, executing this as part of her plan to force everyone into the Tomodachi Game." Source: https://en.wikipedia.org/wiki/Tomodachi_Game
- **Layer 4 (the protagonist's own sin).**
  - Wikipedia: "Despite later revelations that he originally conceived the Tomodachi Game as a child, he now seeks to destroy its administration."
  - Makoto "upon learning Yūichi's role in his father's financial corruption, he ultimately betrays him."
  - Source: https://en.wikipedia.org/wiki/Tomodachi_Game
  - The final chapters are titled "Yuichi's Sin", "The Real Traitor" and "Will You Guys Remain Friends?". Source: https://tomodachi-game.fandom.com/wiki/Tomodachi_Game_Story-Arcs
- **[Analysis]** The series keeps relocating the traitor:
  - the friend who applied,
  - then friends who lied about money,
  - then the meek friend,
  - then the hero himself.
  Each reveal recontextualises earlier games, which is why fans re-read (§1.6).

### 1.5 How Tomodachi Game turns friendship, debt and anonymity into suspicion [Analysis, with sources]
1. **The shared debt is someone's fault, and you agreed not to ask whose.** The opening vote not to investigate is itself a trust test, and Yuichi's doubt is framed as betrayal. (https://tomodachi-game.fandom.com/wiki/Episode_1)
2. **Private, unverifiable numbers.** You may say your debt but not show it, and showing it doubles it. Every claim is cheap talk. (https://tomodachi-game.fandom.com/wiki/Tomodachi_Game)
3. **Private side-deals inside a public game.** Kokkuri's hidden halving clauses in vanishing ink. (https://tomodachi-game.fandom.com/wiki/Episode_2)
4. **Anonymous attacks with a public scoreboard.** Sugoroku cards are unsigned; the audience vote is public. (https://tomodachi-game.fandom.com/wiki/Backbiting_Sugoroku)
5. **A single defector suffices.** In Kokkuri the minority wins; in Janken one off-card breaks the draw. (https://tomodachi-game.fandom.com/wiki/%22Kokkuri-San%22_Game, https://tomodachi-game.fandom.com/wiki/Friendship_Janken)
6. **Cost-shifting rules.** Debt flows to the largest debtor, the first finisher, the loser, or "everyone left behind" when someone escapes. Every rule tells you whom your defection hurts. (Kokkuri, Sugoroku, Janken, Prison pages above)
7. **A legal defection path.** Side-switching in Hide-and-Seek and escape keys in Prison. (https://tomodachi-game.fandom.com/wiki/Friendship_Hide-And-Seek, https://tomodachi-game.fandom.com/wiki/Friend%27s_Prison_Game)
8. **The organisers have incentives too.** The game must be watchable, so its structure must balance. Yuichi exploits this. (https://tomodachi-game.fandom.com/wiki/Episode_5)

### 1.6 What fans praise and criticise
**Praise**
- Complexity of the first game.
  - "the amount of game theory involved is kinda nuts ngl" (QuadraKev_)
  - "I did not expect the first game to have so many routes and what if's." (smhandstuff)
  - r/anime ep. 1 thread: https://www.reddit.com/r/anime/comments/twylkt/tomodachi_game_episode_1_discussion/
- Fair-play traps you can re-check. "the breakdown of how Yuuichi pulled it off was pretty great. I bet it holds up in rewatch and it's downright clever if you know what to look for." (dagreenman18, ep. 6 thread: https://www.reddit.com/r/anime/comments/umks6x/tomodachi_game_episode_6_discussion/)
  - In the ep. 5 thread, viewers note the show nudging them to "rewatch older episodes to seek out each trap" (thelawofL): https://www.reddit.com/r/anime/comments/uhi3ib/tomodachi_game_episode_5_discussion/
- Favourite games (manga readers).
  - Gambling (All Bet), Prison and Battle Royale are named most often.
  - "The ones i found best thought out and well executed were Gambling and Prison Game." (Adept-Procedure3898)
  - Source: https://www.reddit.com/r/TomodachiGame/comments/we90y4/which_game_is_your_favourite_up_till_the_latest/
  - A ranking post puts All Bet first and Backbiting Sugoroku second: https://www.reddit.com/r/TomodachiGame/comments/wlckgz/my_ranking_of_all_tomodachi_gamesmini_games/
- Hide-and-Seek. "the best game in the series in my opinion. Mainly because that was the only game that stayed in Yuuichi's prospective, and it shows him go through trial and error." https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/
- Critic praise (Anime Corner, Tamara Lazic, 19 May 2022): "We don't really suspect anything until the shoe drops and it's a part of the charm for sure." Yuichi "does not fit the usual mold", "a potential psychopath with a goal known only to him." https://animecorner.me/can-tomodachi-game-stop-being-a-mediocre-addition-to-the-high-stakes-games-anime-genre/

**Criticism**
- Explanation dumps. "do we really need a 5-10 minute explanation of his actions every 3 episodes?"; "it just ends up being an info dump without much meaning other than making (usually) Yuichi look cool"; "The constant "who is the traitor" game gets tiring." (Anime Corner, same URL)
- Anticlimax and petty secrets. Ep. 2 is "a bit anti-climatic", and "the secrets revealed thus far are your run of the mill who likes who drama." (Amari Allah, Wherever I Look, 13 Apr 2022): https://wherever-i-look.com/tv-shows/anime/tomodachi-game-season-1-episode-2-you-have-a-lot-to-say-to-me-dont-you-recap-review-with-spoilers
- Off-screen solutions and protagonist dominance.
  - "every time a side character needs character development, Yuuichi just disappears from the chapter and he comes back only for the chapter to tell the readers how he solos the game." (11ah4vq OP)
  - Commenters agree he wins too often: https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/
- Asspulls. "sometimes with MCs like yuuichi it feels the writer got trapped in a corner and so they pull a sorta asspull to victory" (DiscountJoJo, on All Bet): https://www.reddit.com/r/TomodachiGame/comments/wlckgz/my_ranking_of_all_tomodachi_gamesmini_games/
- Dumb opponents. "The players don't elaborate complex strategies and they get fooled very stupidly." (Use-Naive, comparing to *Liar Game*): https://www.reddit.com/r/TomodachiGame/comments/141kgtk/akiyama_liar_game_vs_tomodachi_game/
- Too-obvious tricks. The Rock-Paper-Fingers left-hand twist was "a bit *too* obvious" (MapoTofuMan): https://www.reddit.com/r/anime/comments/vhfg1f/tomodachi_game_episode_12_discussion_final/
- Rule confusion. Multiple threads ask for explanations of All Bet and Prison: https://www.reddit.com/r/TomodachiGame/comments/1iyv6ut/question_about_yuichis_infamous_special_method/, https://www.reddit.com/r/TomodachiGame/comments/1kt0n98/im_looking_for_a_detailed_explanation_of_the/
- Hide-and-Seek has "some inconsistencies when you think about how it was executed" (Adept-Procedure3898): https://www.reddit.com/r/TomodachiGame/comments/we90y4/which_game_is_your_favourite_up_till_the_latest/
- Late-series decline. One downvoted post says the games got "lamer and lamer" after the island arc and that "Liar Game, Kaiji etc all did everything a thousand times better". Others push back and call it better binge-read: https://www.reddit.com/r/TomodachiGame/comments/11co78t/this_manga_really_turned_to_shit_didnt_it/
- Mixed ending reception: https://www.reddit.com/r/TomodachiGame/comments/1gkoozi/finished_the_series_and_its_alright_i_guess/

---

## 2. KAIJI (Nobuyuki Fukumoto)

### 2.1 Restricted Rock-Paper-Scissors (Espoir arc; manga ch. 5+; anime ep. 1–9)
**Rules.** Sources: https://kaiji.fandom.com/wiki/Restricted_Rock_Paper_Scissors and https://kaiji.fandom.com/wiki/Episode_2:_Open_Fire.
- **Loan.** Each player borrows "war funds" of ¥1M–10M as a loan at 1.5% compound interest every ten minutes over a four-hour voyage. Holding funds the whole trip costs about 140%, so there is an incentive to finish early.
- **Cards and stars.** Each player gets 12 cards (4 Rock, 4 Paper, 4 Scissors) and 3 stars.
- **Matches.** A match stakes one star: the winner takes a star and a draw returns both. Used cards go into a slot.
- **To survive** you must use up **all** your cards and still hold **3 or more** stars. Cards cannot be destroyed or thrown away (instant disqualification).
- **Losers** are taken to a back room.
- **After the game** there is a short window for star sales. The price of freeing someone from the back room is three stars.
- Wikipedia states the tournament "has a 50% survival rate." https://en.wikipedia.org/wiki/Kaiji_(manga)

**The cooperative "draw" loophole and its betrayal.**
- Funai tells Kaiji "the only way to win is to have twelve consecutive draws", and that ending early saves interest. Source: https://kaiji.fandom.com/wiki/Episode_2:_Open_Fire.
- They agree to exhaust their cards without losing stars. "At the last minute, Funai backstabs Kaiji and scams him out of two stars." Source: https://kaiji.fandom.com/wiki/J%C5%8Dji_Funai

**The hidden-information insight (cornering a card type).**
- Kitami's strategy is to buy up all the Rock cards and hold them while other cards deplete, then prey on Scissors holders. Kaiji found the same plan and bought Rock; Kitami countered by buying Paper. Source: https://kaiji.fandom.com/wiki/Kitami
- From the anime episode summaries:
  - Kaiji aims to "monopolize the game by first acquiring 30 Rock cards".
  - He reads which card Kitami wants to discard, wins three stars, and buys out Kitami's 30 Paper cards.
  - Funai then proposes reshuffling all remaining cards, which would ruin the plan.
  - Kaiji accuses Funai of "cheating and manipulating the card distribution".
  - Source: https://en.wikipedia.org/wiki/Kaiji:_Ultimate_Survivor
- A blog review: "They decide to double-hoard rock *and* paper" and "Funai has basically engineered himself to have only rocks, and to deal scissors to those with one card." (Stephen, *Blackjack Rants*, 18 Nov 2017): http://blackjackrants.blogspot.com/2017/11/kaiji-ultimate-survivor-s01e06-07.html

**The fragile alliance ending.**
- Kaiji's team (Kaiji, Furuhata, Andō) ends with enough stars but an excess of cards. "Kaiji decides to sacrifice himself with the cards, knowing Furuhata and Andō can save him." Source: https://kaiji.fandom.com/wiki/Kaiji_It%C5%8D
- Andō "has a change of heart when he has the money … refuses to pay Kaiji's bail" and convinces Furuhata to go along. Source: https://kaiji.fandom.com/wiki/Mamoru_And%C5%8D
- Kaiji escapes by stealing another inmate's jewellery. Sources: https://kaiji.fandom.com/wiki/Mamoru_And%C5%8D, https://kaiji.fandom.com/wiki/Takeshi_Furuhata

**Why it works [Analysis].**
- Stars are **zero-sum within a match** and interest punishes waiting, so a clock and scarcity drive betrayal.
- The everyone-wins draw pact is real but needs mutual trust across 12 simultaneous reveals.
- The deep insight is that **the card pool is a finite market**: control supply and you control outcomes.
- The final betrayal happens **after** victory, when one ally holds everyone's assets.

### 2.2 E-Card (manga ch. 94+; anime ep. 15–20)
**Rules.** Source: https://kaiji.fandom.com/wiki/E-Card
- The Emperor side holds Emperor + 4 Citizens; the Slave side holds Slave + 4 Citizens.
- Emperor beats Citizen, Citizen beats Slave, and Slave beats Emperor.
- The Slave side pays five times as much because winning is harder.
- 12 rounds in blocks of 3, swapping sides each block.
- Kaiji bets millimetres of an ear-drill device, not money: 30 mm means injury, 45 mm means death. Source: https://kaiji.fandom.com/wiki/Ear_and_Eye_Drills

**Hidden insight.**
- The ear device secretly contains **sensors that report Kaiji's vitals** to a watch, so Tonegawa reads his physiological responses. Source: https://kaiji.fandom.com/wiki/Ear_and_Eye_Drills
- Kaiji realises Tonegawa is reading his play through "the instrument attached to his ear". He cuts off his ear and leaves it in the bathroom to send false readings, then wins with the Slave card. Source: https://en.wikipedia.org/wiki/Kaiji:_Ultimate_Survivor

**Why it works [Analysis].** The "pure psychology" game is actually a hidden-information leak. The fix costs the hero physically, which makes the loophole feel earned.

### 2.3 Human Derby / Brave Men Road (Steel Beam Crossing)
- **Human Derby.** Contestants cross narrowing beams at height. The first two finishers are paid, and pushing is encouraged. Contestants "realize they must push the one in front of them off the beam to win"; Kaiji refuses and is disqualified. Sources: https://kaiji.fandom.com/wiki/Brave_Men_Road (page title "Steel Frame Crossing") and https://en.wikipedia.org/wiki/Kaiji:_Ultimate_Survivor
- **Brave Men Road.** An electrified beam 22 storeys up. "Kaiji discovers the hidden exit and is the sole survivor. However, due to Kaiji begging for them to cut the electricity, his win is voided." Source: https://kaiji.fandom.com/wiki/Kaiji_It%C5%8D

### 2.4 The Rescue (Salvation) Game (*Kazuya-hen*): the clearest "test of friendship" game in Kaiji
**Rules.** Source: https://kaiji.fandom.com/wiki/Rescue_Game
- Three indebted friends (Mitsuyama, Chan and Mario) are strapped into seats in a staircase formation and cannot look behind.
- Each round the pot doubles. Helmet lights secretly mark one "savior" and two "hostages".
- The savior must unbuckle after 30 seconds but before 60 and press a button across the room, or the hostages' helmets crush their heads.
- Players must deduce their own role. The top seat can see the other two lights.
- **Halfway through, Kazuya reveals that if the savior fails to rescue, he gets double the entire pot.**

**Outcome.**
- "Mitsuyama fails to put his trust into his friends and bails out, taking all the money for himself and leaving Chan and Mario behind." Source: https://kaiji.fandom.com/wiki/Mitsuyama
- Kaiji pays to save Chan and Mario, and they later bet their lives for him in One Poker. Source: https://kaiji.fandom.com/wiki/Kaiji_It%C5%8D

**Why it works [Analysis].** Cooperation is the default until the organiser **adds a betrayal payout mid-game**. Combined with hidden roles (who is the savior?), one player can defect while seeming to act by mistake.

### 2.5 Reception (as quoted on Wikipedia)
Source: https://en.wikipedia.org/wiki/Kaiji_(manga)
- Michael Toole (ANN): "run through with entertaining lowlifes, odd situations, and intoxicating moments of suspense."
- Bradley Meek (THEM Anime Reviews): the games are "devilishly clever and reliant on player psychology as much as strategy."
- David Cabrera (Polygon): Fukumoto has "a gift for presenting the abstract terror of staking one's life on a coin flip."
- John Oppliger (AnimeNation), criticism: "extensive reliance on coincidence, deus ex machina, and authorial manipulation."

---

## 3. KAKEGURUI

### 3.1 Vote Rock-Paper-Scissors (ch. 1; anime ep. 1)
**Rules.** Source: https://kakegurui.fandom.com/wiki/Vote_Rock-Paper-Scissors
- Two players start with 120 chips each (¥10,000 per chip) and bet blind.
- The classmates who are not playing each draw Rock, Paper or Scissors on a card, and the cards go into a box.
- Each player draws 3 cards at random and plays one. Ties are played out.
- Hands are usually two of one move and one other; all three different is rare.

**The cheat.**
- Mary has most of the voters in her debt.
- A confederate (Ryota) stands behind the opponent and signals which symbol the voters should draw. Mary then knows the opponent's likely majority card and counters it.
- In the anime, 21 of 30 students are rigging it. Source: https://kakegurui.fandom.com/wiki/A_Woman_Named_Yumeko_Jabami_(Episode)

**Yumeko's insight.** Source: https://kakegurui.fandom.com/wiki/A_Woman_Named_Yumeko_Jabami_(Episode)
- She saw that Mary wasn't signalling. Everyone was looking "at the person behind her," Ryota.
- She read his signals with a hand mirror. She lost big rounds while learning the system, then went all in.
- How she got the winning Scissors on the last round: "it was simply a complete coincidence, it was simply luck."
- She prefers risk: "she hates situations in which she knows her own outcome in a game as it really isn't gambling."

**Why it works [Analysis].**
- A "fair" game whose randomness is supplied **by the crowd** is only as fair as the crowd's loyalties.
- Spotting the information channel (who looks at whom) is the solution.
- Note the risk the creators accept: the final win is partly luck, which purists may dislike.

### 3.2 The Greater Good Game (public-goods game; manga Election arc, where the wiki cites ch. 45 and 49; anime *Kakegurui ××* ep. 7–8)
**Rules.** Source: https://kakegurui.fandom.com/wiki/Greater_Good_Game
- 5 players and 5 rounds. To win you need at least 40 coins **and** the most coins.
- Each round, each player, alone in a room, splits 5 coins between a personal box (counted as is) and a tax box.
- The tax box is **doubled and split evenly** among all five (rounded up).
- Once per game, a majority of 3 may vote to remove a player, who loses and forfeits their coins.
- The page notes that if everyone keeps their coins, no one exceeds 40 and there is no winner. If everyone pays tax but one person withholds, that person risks being voted out if discovered.

**Arithmetic derived from the stated rules [Analysis].**
- If everyone pays all 5 coins: 25 doubled is 50, or 10 each per round, so 50 each after 5 rounds. Everyone clears 40.
- If one player withholds while the others pay: 20 doubled is 40, or 8 each. The withholder gets 13 that round and the others 8.
- So **free-riding wins, cooperation clears.**
- How a tie at the top is resolved is **not stated** in the source: UNVERIFIED.

**What happened.** Sources: https://kakegurui.fandom.com/wiki/The_Treacherous_Woman_(Episode), https://kakegurui.fandom.com/wiki/The_Winning_Woman_(Episode)
- Yumeko proposes everyone pays full tax. Only 20 coins arrive, so there is a traitor.
- She assigns secret per-player amounts, and the shortfall suggests **two colluding traitors**.
- Kaede and Yumeko announce they will pay nothing. Paradoxically the next round brings the maximum 25.
- Kaede deduces the traitors were Miroslava and Itsuki, who **colluded by leaving notes in the deposit room** (not forbidden by the rules). Miroslava is voted out.
- Itsuki wins with 45 coins.
- **[Conflict]** Side-bet details differ between the game page and the episode pages, so they are omitted.

**Why it works [Analysis].**
- This is the textbook "cooperative but fragile" loophole: everyone can qualify by trusting.
- Anonymity of contributions plus a single exile vote makes the group hunt traitors instead of maximising together.
- The real loophole is an **unforbidden communication channel** (notes).

---

## 4. SQUID GAME

### 4.1 The built-in exit (Clause 3) and the vote
- The consent form has three clauses:
  - Clause 1: a player is not allowed to stop playing.
  - Clause 2: a player who refuses to play will be eliminated.
  - Clause 3: games may be terminated if the majority agrees.
  - Source: https://squidgame.fandom.com/wiki/Squid_Games
- **Season 1 (33rd game).** Voting X returned players home with nothing. After the first game, **101 voted X and 100 voted O.** Source: https://squidgame.fandom.com/wiki/Voting
- **Season 2 (37th game).**
  - Players may vote after every game.
  - If the games end, the accumulated prize money is **split evenly among survivors**.
  - A tie forces a revote.
  - Voters wear O/X patches, producing factions.
  - Not voting by the count of three counts as abstention.
  - Sources: https://squidgame.fandom.com/wiki/Squid_Games, https://squidgame.fandom.com/wiki/Voting
- **[Analysis]** The "everyone survives" option is **printed in the rules from minute one**. Greed (the growing pot), debt and the minority who want to continue keep it shut. Season 2's split-the-pot change makes stopping rational and still fails, which is a powerful study of how fear and greed beat the obvious solution.

### 4.2 Marbles (game 4, S1)
- Players first choose a partner without knowing the game. Only then are they told they must take all 10 of their partner's marbles within 30 minutes, by any marble game, and the loser dies. Source: https://squidgame.fandom.com/wiki/Marbles
- Trivia on the same page: the game "was meant to demoralize the players, as they weren't told until *after* choosing their partners that they would be competing *against* each other."
- **Betrayal example.** Sang-woo has Ali hand over his marble bag on a pretext, swaps the marbles for pebbles, and turns in Ali's marbles. Ali realises "his plan was to betray him all along." Source: https://squidgame.fandom.com/wiki/Ali_Abdul
- **[Wiki interpretation, not canon]** The Marbles page speculates that Il-nam's talk of *gganbu* "allud[es] to the possibility that all players could survive if they shared their marbles". The stated rule (take all ten) does not obviously allow that, so treat it as UNVERIFIED.

### 4.3 Glass Stepping Stones (game 5, S1)
- Players pick numbered vests 01–16 **before** learning that the number is crossing order. Source: https://squidgame.fandom.com/wiki/Glass_Stepping_Stones
- Two parallel bridges of 18 panels, each tempered or normal glass, 16-minute limit. When time expires the panels explode.
- 3 of 16 survived. The page's "Methods to win" section says glass-making knowledge, such as player Do Jeong-soo's, makes the panels easier to tell apart.
- The page's own trivia says it "has been calculated in most instances seven or more people would win". It also speculates about loopholes (railings, panel ends, front players stalling), labelled unconfirmed.
- **[Analysis]** Order equals information: **every death buys information for those behind.** Allocating order before revealing its meaning is the cruelty.

### 4.4 Dalgona (game 3, S1): hidden information withheld
- Sang-woo guessed the next game was Dalgona and that the triangle was easiest. He "sees no reason to tell the others his guess … keeping the advantage solely for himself," and suggested the group split up. Source: https://squidgame.fandom.com/wiki/Cho_Sang-woo

---

## 5. ZERO ESCAPE: Virtue's Last Reward (Ambidex / "AB" Game)

### 5.1 Rules
Sources: https://zeroescape.fandom.com/wiki/Nonary_Game:_Ambidex_Edition, https://zeroescape.fandom.com/wiki/Bracelet_Points
- **Bracelet Points (BP).** Nine players each start with **3 BP**. At **9+ BP** a player can open the Number Nine Door. At **0 or less**, the bracelet kills them by lethal injection.
- **Ally or Betray.** After each escape-room round, a SOLO faces a PAIR (the pair shares **one** vote). Each side votes Ally or Betray:
  - Ally / Ally: both +2.
  - Betray / Ally: the betrayer +3, the betrayed −2.
  - Betray / Betray: no change.
- **Voting rules.**
  - At least one member of each side must vote; if **neither side votes, both die.**
  - A side that doesn't vote defaults to Ally if the other side voted.
- **Shuffle.** Colours and SOLO/PAIR assignments shuffle randomly after every AB Game, so you never know whom you'll face next.
- **Door 9.** "Once Door 9 is opened, it will remain opened for 9 seconds then close forever … trapping the remaining players in the facility forever."
- The game is framed by Dio's line: "This game isn't about compassion, and it's not about being clever. It's about one thing: how well you can manipulate people to your advantage. How unfair you can be." (quote at top of https://zeroescape.fandom.com/wiki/Nonary_Game:_Ambidex_Edition)

### 5.2 The cooperative solution and why it is fragile
- **Everyone allies.** 3 + 2 + 2 + 2 = 9, so everyone can escape after three rounds. In the "Phi END", once Dio's bombs are disarmed, "everyone decides to cooperate and pick ally during the next three rounds, allowing everyone to reach 9 BP" and they leave Dio tied to a sink. Source: https://zeroescape.fandom.com/wiki/Bracelet_Points
- **Group-total view** (from the wiki's Prisoner's Dilemma page): both allying is +6 for all players combined. Pair-ally with solo-betray is a net −1 (pair −2 each, solo +3). Mutual betrayal is 0, which is "better for the point total" than the solo betraying. Phi's summary: "The AB game is the same: You want to pick [ally], but you can't." Source: https://zeroescape.fandom.com/wiki/Prisoner%27s_Dilemma
- **Fan design analysis.** https://www.reddit.com/r/ZeroEscape/comments/cgnroh/why_the_ab_game_from_virtues_last_reward_was_very/
  - On betray/betray = 0: "putting it at exactly 0 points, makes it no longer a viable option to work towards, nor a situation you actively need to avoid" (OP).
  - On the starting 3 BP: "if your goal is to escape as fast as possible you **have** to betray two times" (RythmicChaos).
  - On the vote-or-die rule: "I always liked the "one party must vote or everyone dies" rule, as otherwise you could beat the game trivially just by keeping everyone in one room and making sure nobody voted." (fbjim)
  - On the shared pair vote: it adds manipulation, letting you "overwhelm your partner to betray" (flightofangels).
- **Fan criticism and replies.** https://www.reddit.com/r/ZeroEscape/comments/1enj825/why_is_everyone_in_vlr_just_an_asshole/
  - The OP's complaint: "The only advantage betraying gets you is MAYBE a chance of getting out in 2 rounds instead of 3."
  - Replies:
    - Players are "betraying for fear of the OTHER person being an asshole" (neeeeeeeeeeeev).
    - "Dio was included specifically to ensure that Betrayals would happen." (PCN24454)
    - "Trust is incredibly fragile in VLR" (SoldierDelta46).
  - **[Analysis]** If betrayal's payoff is small, you need an **openly hostile player or a time/door constraint** to make defection plausible. Otherwise readers say "just cooperate."

---

## 6. Cross-cutting design patterns (for a game with a hidden everyone-survives loophole)

**A. Friends must trust each other but have reasons to betray**
1. **One defector breaks it.** A rule that gives any single player a veto over the group's success:
   - Kokkuri: the minority answer wins (https://tomodachi-game.fandom.com/wiki/%22Kokkuri-San%22_Game).
   - Janken: one off-card breaks the draw (https://tomodachi-game.fandom.com/wiki/Friendship_Janken).
   - Greater Good: one free-rider (https://kakegurui.fandom.com/wiki/Greater_Good_Game).
   - Paranoia grows with group size.
2. **Private, asymmetric temptations.**
   - Kokkuri's bribe clauses printed on each questioner's own card, in vanishing ink (https://tomodachi-game.fandom.com/wiki/Episode_2).
   - Private rule briefings in the Friendless Game (https://tomodachi-game.fandom.com/wiki/The_Friendless_Game).
   - Hidden roles in the Rescue Game (https://kaiji.fandom.com/wiki/Rescue_Game).
3. **Cost-shifting payoffs**: your gain is someone else's named loss.
   - Prison escape adds ¥400M to each person left behind (https://tomodachi-game.fandom.com/wiki/Friend%27s_Prison_Game).
   - Hide-and-Seek defector pushes debt onto old teammates (https://tomodachi-game.fandom.com/wiki/Friendship_Hide-And-Seek).
   - AB betray: +3 for you, −2 for them (https://zeroescape.fandom.com/wiki/Bracelet_Points).
4. **Late or mid-game betrayal bonuses.**
   - The Rescue Game's double-pot reveal (https://kaiji.fandom.com/wiki/Rescue_Game).
   - The one-time Door 9 (https://zeroescape.fandom.com/wiki/Nonary_Game:_Ambidex_Edition).
   - Partners learning they are opponents only after pairing (https://squidgame.fandom.com/wiki/Marbles).

**B. The cooperative solution is real but fragile**
5. **Make the "everyone lives" path discoverable in the rule text** but costly to trust:
   - Squid Game's Clause 3 vote (https://squidgame.fandom.com/wiki/Voting).
   - The Espoir 12-draw pact (https://kaiji.fandom.com/wiki/Episode_2:_Open_Fire.).
   - All-ally in the AB Game (https://zeroescape.fandom.com/wiki/Bracelet_Points).
   - Full tax in Greater Good.
   - The dominoes in the Prison Game.
6. **Front-load the pain of cooperating.** Sugoroku's negative squares sit in the first half, so the honest "all blanks" route looks like a losing route until someone reasons the board must balance (https://tomodachi-game.fandom.com/wiki/Episode_5).
7. **Cooperation fails at the hand-off.** Kaiji wins and then trusts allies to buy him out; they sell him (https://kaiji.fandom.com/wiki/Mamoru_And%C5%8D). The weakest moment is when one person holds everyone's assets.
8. **Removing the saboteur unlocks cooperation**, and the removal mechanism is itself abusable:
   - Phi END ties up Dio (https://zeroescape.fandom.com/wiki/Bracelet_Points).
   - The Greater Good exile vote.
   - The Prison exile vote, which fans say Yuichi turned against people.

**C. Hidden traitors and hidden information create paranoia**
9. **Unverifiable claims.** Debts can be spoken but not shown (https://tomodachi-game.fandom.com/wiki/Tomodachi_Game). AB votes are private. Every reassurance is cheap talk.
10. **Anonymous attacks with public consequences.** Sugoroku cards (https://tomodachi-game.fandom.com/wiki/Backbiting_Sugoroku).
11. **Traps that make the traitor self-identify.** Design a move that only the guilty party has a reason to make or to avoid:
    - Yuichi's "I applied" card, cross-checked by the liar penalty.
    - Secret-only-I-told-you test cards.
    - Watching who volunteers.
    - (https://tomodachi-game.fandom.com/wiki/Episode_6)
12. **Information leaks hidden in logistics.**
    - Hider food runs (https://tomodachi-game.fandom.com/wiki/Episode_8).
    - Vital-sign sensors in the E-Card ear drill (https://kaiji.fandom.com/wiki/Ear_and_Eye_Drills).
    - Signals from the person behind you (https://kakegurui.fandom.com/wiki/A_Woman_Named_Yumeko_Jabami_(Episode)).
    - Crossing order (https://squidgame.fandom.com/wiki/Glass_Stepping_Stones).
13. **Rule-scope loopholes.**
    - Showing versus giving a plate (Ep. 6).
    - Violence banned against *opponents* only (Ep. 11).
    - "Right hand" only (Ep. 12).
    - Notes not forbidden (Greater Good).
    - Contract wording (All Bet).
    - Fans love these when the wording was visible from the start. They call it an "asspull" when it wasn't (https://www.reddit.com/r/TomodachiGame/comments/wlckgz/my_ranking_of_all_tomodachi_gamesmini_games/).
14. **The organiser's incentives are a clue.** "An unfair game isn't fun to watch" (https://tomodachi-game.fandom.com/wiki/Episode_5).

**D. Craft lessons from criticism**
15. Show the clues on-page before the reveal. Avoid long observer info-dumps (Anime Corner). Let the protagonist fail and adapt, as in Hide-and-Seek (the 11ah4vq thread).
16. Keep rule text short and complete enough that readers can reconstruct the solution. All Bet and Prison generated "please explain" threads.
17. Give opponents competent strategies (Kei and Juuzou in Hide-and-Seek; Kitami in Kaiji). "Fooled very stupidly" opponents deflate tension (https://www.reddit.com/r/TomodachiGame/comments/141kgtk/akiyama_liar_game_vs_tomodachi_game/).

---

## 7. Gaps and unverified items
- **Tomodachi Game, manga-only games** (Friend-Sin Trial, Friends Prison, All Bet, Friend Murder, Friendless): I found rule summaries, but no step-by-step solutions from an authoritative source. Solution descriptions above are **[Fan claim]**.
- **Friendless Game outcome** and full password mechanics: UNVERIFIED.
- **Kakegurui Greater Good tie-break**: not stated in the source.
- **Restricted RPS**: the exact number of participants, the remaining-card monitor, and the final Funai match mechanics are not fully covered by sources I opened. Only the points cited above are verified.
- **ANN "This Week in Anime"** on Tomodachi Game: blocked (403), so not used.
