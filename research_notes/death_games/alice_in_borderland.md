# Alice in Borderland: what makes its death games work

Research notes for *Dead Man's Algorithm*, compiled 2026-10-28.
Scope: Haro Aso's manga (main series, side stories, *RETRY* sequel) and the Netflix live action (seasons 1 to 3).

## How these notes were sourced (read first)

- **Fan wiki.** aliceinborderland.fandom.com. A direct page fetch returned HTTP 402, so every wiki page was read in full as raw wikitext through the wiki's own MediaWiki API (`api.php?action=parse&prop=wikitext`). Each claim below cites the normal page URL.
- **Reddit.** Threads were read through the official API with `tools/reddit_tool.py`. Scores and dates are as returned on 2026-10-28.
- **Web articles.** Read with WebFetch. A few sites (thereviewgeek, tvinsider, hollywoodreporter) refused access and are **not** used.
- **Labels.** Where a claim rests only on a fan's say-so, it is attributed to that fan. Anything I could not check against a source I opened is marked **UNVERIFIED**. My own inferences are marked **(my inference)**.
- **Fan wiki caveat.** The wiki is fan-written. Its "Strategy" and "Trivia" sections are editors' analysis, not canon. I flag these as "wiki analysis".

Wiki URL shorthand. All `W:` links resolve to `https://aliceinborderland.fandom.com/wiki/<Page>`.

---

## 0. The framework the games sit in

- **Card suit sets the game type.** Netflix's own explainer: "Diamonds mean it's a brain game", "clubs are all about teamwork", "hearts are games of psychological warfare against other players", "spades are physical challenges". The card number is the number of visa days won. When a visa runs out, "a laser from the sky zaps them from existence". Face Cards are "the most difficult games yet", and "The games can only be cleared once the host Citizen is dead."
  - Source: https://www.netflix.com/tudum/articles/alice-in-borderland-series-game-rules
- **The fan-wiki definition of Hearts games is almost exactly the design brief for *Dead Man's Algorithm*.**
  - It says: "Rules of many Hearts games also tend to mislead the players into believing that sacrificing other players is required to claim victory, but would otherwise be unnecessary if all participants could calmly deduce the true nature of each Hearts game."
  - It adds: "Many of the higher difficulty Hearts games forbid violence, so players can only progress forwards through manipulation and psychology."
  - Source: https://aliceinborderland.fandom.com/wiki/Hearts
- **Hearts venues bait violence.** The 7♥ table of tools "hint[s] at the need for violence". In the 10♥, the instruction to burn a murderer "immediately forces them to turn against each other".
  - Source: https://aliceinborderland.fandom.com/wiki/Hearts
- **Face Card games are run by Citizens.** Citizens are former players who now host the games. Each game reflects its host's personality (see King of Diamonds and Jack of Hearts below).
  - Source: https://aliceinborderland.fandom.com/wiki/Face_Cards
- **Background clock.** Visas expire. In the manga's Jack of Hearts, stalling inside one game kills players *outside* it, whose visas run out.
  - Source: https://aliceinborderland.fandom.com/wiki/Jack_of_Hearts

---

## 1. Game dossiers

Fans most often name **Jack of Hearts**, **King of Diamonds** and **King of Clubs** as the best games. In the "Favorite AIB game" thread (r/AliceInBorderland, score 197), the most-upvoted answer is "Jack Of Hearts All The Way! … this game was so tense!" (38 points). Another user wrote: "Even before Season 2 was released, it was common debate that either the Jack of Hearts or the King of Diamonds are the best Games." The Witch Hunt is praised for a "clever and simple solution".
- Source: https://www.reddit.com/r/AliceInBorderland/comments/1m6jx2n/favorite_aib_game_and_why/

A manga reader's post names "King of Clubs with Kyuma, King of Diamonds and Witch Hunt" as favourites and King of Spades as "pretty uninteresting".
- Source: https://www.reddit.com/r/AliceInBorderland/comments/v1hws3/so_i_just_finished_the_manga/

---

### 1.1 King of Diamonds: "Beauty Contest" (manga) / "Balance Scale" (Netflix S2E6)

Sources:
- W: [King_of_Diamonds](https://aliceinborderland.fandom.com/wiki/King_of_Diamonds)
- W: [King_of_Diamonds_(Netflix)](https://aliceinborderland.fandom.com/wiki/King_of_Diamonds_%28Netflix%29)
- W: [Keiichi_Kuzuryu](https://aliceinborderland.fandom.com/wiki/Keiichi_Kuzuryu)
- W: [Keiichi_Kuzuryu_(Netflix)](https://aliceinborderland.fandom.com/wiki/Keiichi_Kuzuryu_%28Netflix%29)
- W: [Hinako_Daimon](https://aliceinborderland.fandom.com/wiki/Hinako_Daimon)

**Set-up.**
- Four players plus the King (Kuzuryu, a former international lawyer) sit shackled at a round table in a Supreme Court.
- Each has a tablet showing 0 to 100.
- Rounds last 1 minute in the manga. The first round, and every round after a new rule is added, get 5 minutes. Netflix uses 3 minutes per round.

**Rules as stated (manga wiki).**
- Contestants choose a number between 0 and 100.
- The average of all chosen numbers is multiplied by 0.8.
- The closest number wins the round. Every other player loses a point.
- At -10 points, the scale above the player's head overflows and pours **aqua regia** on them ("an acid strong enough to dissolve gold"). Netflix uses sulfuric acid.
- "A new rule is introduced for every player eliminated":
  1. "If two or more players choose the same number, the number they choose becomes invalid, meaning they lose a point even if the number is closest…"
  2. "Choosing the exact correct number will cause other players to lose two points instead of one."
  3. "If one player chooses 0, the other player can win by choosing 100."

**The core insight.**
- It is a Keynesian beauty contest. Asuma explains that "one mustn't base their predictions on what they believe to be the best, but what they believe the market believes to be the best".
- Chishiya: "Be it chess or poker, any game of wits involves reading the opponent. But what we are reading isn't mentality, it's **rationality**."
- Because 0.8 × 100 = 80, then 0.8 × 80 = 64, and so on, rational play spirals toward 0. The rounds in the manga table track it: winning numbers of 29, 14, 5 and 1 in rounds 1 to 4.
- Daimon works it out after losing round 1: "If everyone picks 40 like her, the average is 32…" (Daimon page).
- The way to break the spiral is to pick "random" high numbers (Daimon and Chishiya pick 100) and drag the average up. Rational play is predictable, so irrational play becomes a weapon (wiki "Strategy").

**Escalation by added rules.**
- Rule 1 and Rule 2 arrive together after Asuma and Yashige die in the same round.
- The wiki reads Rule 1 as "included to prevent the existence of a stable Nash equilibrium" (wiki analysis).
- In round 11, all three survivors pick 1 (manga) or 0 (Netflix). Nobody wins.
- In round 12, Chishiya hits the exact number, 23, and the double penalty kills Daimon. Chishiya explains he predicted that she "wanted to distance herself" from 0 and 1 by picking somewhere in 2 to 100 (Daimon page).
- Rule 3 turns 0, 1 and 100 into rock-paper-scissors: "0 defeats 1, 1 defeats 100, and 100 defeats 0" (wiki).
- The wiki notes the "rules are kind" framing: 5 minutes to adjust after each new rule. In the manga, Daimon mutters that the rules are "kind" (Daimon page).

**How it was actually won: a moral trap, not maths.**
- The duel ends at Chishiya -9, Kuzuryu -7 going into round 13 (Netflix). Chishiya **announces or shows that he will pick 100**.
- Under Rule 3, Kuzuryu can now kill him by choosing anything except 0. Choosing 0 hands Chishiya the round. Chishiya has put his own life in the opponent's hands. In the manga, Kuzuryu reflects that the only way Chishiya wins is if "me choosing 0 … Is he telling me… to make the call?"
- Kuzuryu cannot decide who deserves to live. That inability is his whole backstory: a lawyer who watched the poor lose to corporations, now a Citizen so the "system" decides for him.
- He picks 0 three times, rounds 13 to 15, and dies.
- Manga last words: "If that's the case… then I finally was able to decide how to live my life thanks to you." In the manga, the wiki describes his thumbs pressing 1 and 0 at the same moment. The round table records 0.
- Netflix last words: "I'm finally free. I made my own choice based on my own ideals. It's all thanks to you."
- In the manga, Kuzuryu also says he chose 0 to keep the game "impartial". Chishiya points out he "could have killed him if he truly wished to avoid making decisions" (Kuzuryu page).

**Designer reflected in the game** (wiki trivia, analysis).
- The courtroom setting reflects "Kuzuryu's values of justice".
- Aqua regia "likely symbolizes Kuzuryu's opposition to corruption and greed".
- "this one is likely the most impartial and generous" Face Card game.
- Chishiya in the manga reads the 1-in-5 survival rate as "fair". If players outnumber Citizens four to one, the odds balance (Daimon page).

**Hidden information.** Every choice is simultaneous and secret. The only evidence is the history of other players' numbers. The final duel turns this around: Chishiya *reveals* his choice, making information the trap.

**Fan reception.**
- Praise. "the evolution from a game of logic and probability, to a brutal and deep reflection of the meaning of life is shockingly brilliant" (u/basgoonie). Source: https://www.reddit.com/r/AliceInBorderland/comments/1m6jx2n/favorite_aib_game_and_why/
- Criticism, the luck complaint. "This game requires luck… Chishiya is a genius but he isn't a mind reader" (OP, score 22).
- Rebuttals from the same thread:
  - "It's not so much of a numbers game but more so how well you can read your opponents… once he figured out kuzuryu's weakness of equality … he used that against him" (u/taylordeff, 34).
  - "half maths and half a game of chess" (u/FW_layerAUS-anyms).
  - Source: https://www.reddit.com/r/AliceInBorderland/comments/1ivbqxw/how_was_chishiya_supposed_to_win_in_beauty_contest/
- Adaptation complaint. In the manga Kuzuryu presses "1 and 0 at the same time". Netflix has him "just giving up", which makes "the lesson fall a little short". Source: https://www.reddit.com/r/AliceInBorderlandLive/comments/zwamfb/my_very_long_review_of_aib_season_2_as_a_manga/
- Looper: "sadistic, complex, and nearly impossible to escape alive". It notes that rules added after each death make it harder. Source: https://www.looper.com/1357825/every-game-alice-in-borderland-ranked-reckless

---

### 1.2 Jack of Hearts: "Solitary Confinement" (manga ch. 45 to 49; Netflix S2E3 and E4)

Sources:
- W: [Jack_of_Hearts](https://aliceinborderland.fandom.com/wiki/Jack_of_Hearts)
- W: [Jack_of_Hearts_(Netflix)](https://aliceinborderland.fandom.com/wiki/Jack_of_Hearts_%28Netflix%29)
- W: [Enji_Matsushita](https://aliceinborderland.fandom.com/wiki/Enji_Matsushita)
- W: [Enji_Matsushita_(Netflix)](https://aliceinborderland.fandom.com/wiki/Enji_Matsushita_%28Netflix%29)
- W: [Shuntaro_Chishiya_(Netflix)](https://aliceinborderland.fandom.com/wiki/Shuntaro_Chishiya_%28Netflix%29)

**Set-up.**
- A penitentiary, 19 players plus the Jack hidden among them.
- Explosive collars. One-hour rounds, no round limit.
- About half a year of food.

**Rules as stated (manga wiki).**
- "Players need to guess the card suit symbol that appears on the back of their collar at the end of each round."
- No reflective surfaces. The mark is on the back of the collar, "making it impossible for anyone to see their own symbol".
- Players move and talk freely. In the final five minutes, everyone enters a cell and announces their symbol.
- Prohibited: more than one person inside a locked cell; obstructing someone from entering a cell; preventing someone from announcing their mark, "including killing them".
- GAME CLEAR for all remaining players once the Jack dies.
- GAME OVER for using a reflective surface, a wrong or missing answer, killing with weapons or violence, and "for the last remaining player alongside the Jack of Hearts".
- Netflix adds: "When a round is over, the symbol will reset and change for the next round." It also adds: "Visa days are not removed from the players' visas for the duration of the game."

**The environment enforces the hidden information.** "All knives in the kitchen are ceramic, the faucets dispense tomato juice instead of water, and there are no mirrors." The large building "naturally encourages players to have discreet conversations" (manga wiki).

**Core insight: the game cannot end without a lie.**
- Netflix Chishiya: the game "will not end unless the Jack gives a wrong answer and dies, and it is not possible to clear the game without lying to the Jack."
- Honesty keeps everyone alive but keeps the game going forever. To clear it, someone must betray, and betraying the wrong person kills an innocent.
- Manga Yaba: "the game rules have hinted at finding a reliable partner from the very beginning."
- The wiki's strategy analysis: lone players die first, then big groups, because "Once one person in the group is killed, trust collapses". Pairs last longest.

**The "everyone survives" equilibrium and why it breaks (manga).**
- Mitsurugi forms a faction to stall until the food runs out. "Even if the Jack of Hearts is within this group, they could survive peacefully for several months."
- The flaw: stalling kills everyone *outside* the game, whose visas expire within a month.
- Yaba breaks the faction by "deceiving Kariya and pushing him into Mitsurugi's cell, knowing that only one person is allowed in a cell at a time". The safety rule becomes the murder weapon. Both die in Round 9.
- A fan theory (u/FloridAsh) praises the same idea: "all people have to do is NOT betray each other and they can all live together". The rebuttal: rounds are hourly, so "no full night of sleep". The wiki's Netflix trivia also flags sleep deprivation.
  - Source: https://www.reddit.com/r/AliceInBorderland/comments/zt4qxx/okay_but_can_we_talk_about_how_the_jack_of_hearts/

**How betrayal is generated.**
- Urumi manipulates the main group "into lying to those who show even the slightest suspicious tendencies".
- In the manga, Banda tricks Seto into the conflict that kills Kiriu. In Netflix, Banda advises Seto to lie to the bully Kiriu.
- The Jack (Matsushita, a hypnotherapist) plays weak:
  - He lets Banda "dominate" him, a "countertransference" technique.
  - He hypnotises Kotoko into distrusting her partner Yaba.
  - He feeds Kotoko and Banda wrong suits in the endgame.
- Matsushita quote: "most of them are essentially extras… the ones to survive until the final act… are the actors with overwhelming self-confidence and charisma!"

**How it is solved.**
- **Manga.**
  - Yaba and Banda secretly bonded in Round 8 and stay loyal to each other.
  - Banda deliberately tells Matsushita the truth in Round 10. Matsushita realises "Banda should have lied to him in the previous round if he already suspected him."
  - The reveal line: "I never thought you would betray me. Did you have a change of heart out of fear? Or maybe… you are the Jack of Hearts?"
  - They lock the Jack in a cell. The rules forbid only stopping him from *speaking*. Banda reasons he "does not need his eyes or limbs as long as he can speak" and tortures him.
  - Matsushita chooses a wrong answer to end the pain.
- **Netflix.**
  - Chishiya deduces it: Matsushita paired with a known murderer, and a self-important manipulator suggests "a special position".
  - The proof is a **snack-wrapper code**. Matsushita and Kotoko picked a biscuit brand with four wrapper colours, one per suit, so they could signal each other's true symbols.
  - In the last round, Chishiya stays in his cell and listens for Matsushita's victory laugh.

**The designer cheats (manga).** Matsushita has a prosthetic eye linked to his collar that shows his own suit. The wiki notes the rule bans *players* bringing reflective materials, so as a Citizen he is technically allowed.

**Fan reception.**
- Top thread: "Chishiya and The Jack Of Hearts game kinda carried this season" (score 958). Looper: "one of the trickiest games in the entire series".
  - Sources: https://www.reddit.com/r/AliceInBorderland/comments/zttedc/chishiya_and_the_jack_of_hearts_game_kinda/ and https://www.looper.com/1357825/every-game-alice-in-borderland-ranked-reckless
- **Criticism, the hidden reveal.** "if you (as a viewer) had [no] opportunity to catch the hidden messages that were sent… the reveal feels kinda forced, since it wants to mindf*ck you by revealing information which wasn't available before" (u/Beliar7, on zttedc).
- **Criticism, Chishiya's luck.** In the final round Chishiya's own logic is "it is either Diamonds or Spades? … At the end I'll have to trust my intuition." That is effectively a coin flip (Netflix Chishiya page). A fan: "I still search, 'How Chishiya deduced his symbol?' and every time it shows, 'Calculation and luck'…" (u/Friendly_Honey7772, on 1m6jx2n).
- **Criticism, designer cheating.** "for the Jack of Hearts game, it is quite literally impossible, unless they take/break Enji's fake eye… feels like cheating."
  - Source: https://www.reddit.com/r/AliceInBorderland/comments/1458yuw/how_did_enji_get_away_with_it_vague_bc_spoilers/
  - Also: https://www.reddit.com/r/AliceInBorderland/comments/1ok04fx/jack_of_heart_and_cheating/ ("It's disappointing, but why not.")
- **Adaptation complaint.** Netflix cut the hypnosis planning: "they never even explained why both were in kahoots" (u/Smooth-Ride-7181, on zt4qxx).
- **Manga praised for interiority.** "I LOVE that we travelled into Matsushitas mind" (u/Automatic-Divide8894, on 1m6jx2n).

---

### 1.3 Nine of Hearts: "Earth Invasion" (*RETRY* ch. 1 to 13)

This is the closest existing template for the *Dead Man's Algorithm* premise.

Sources:
- W: [Nine_of_Hearts](https://aliceinborderland.fandom.com/wiki/Nine_of_Hearts)
- W: [Chapter_1_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_1_%28RETRY%29)
- W: [Chapter_6_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_6_%28RETRY%29)
- W: [Chapter_9_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_9_%28RETRY%29)
- W: [Chapter_10_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_10_%28RETRY%29)
- W: [Chapter_11_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_11_%28RETRY%29)
- W: [Chapter_12_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_12_%28RETRY%29)
- W: [Chapter_13_(RETRY)](https://aliceinborderland.fandom.com/wiki/Chapter_13_%28RETRY%29)

**Set-up.**
- Six people struck by the same falling billboard: Arisu, a father and daughter, a doctor and his colleague, and a loner.
- A theme park with six country-themed halls. Ten minutes per round, six rounds.
- On entry they see a **dismembered corpse**.

**Rules as stated.**
- Each phone shows six LIFE cards, one DEATH card, and "six images of other participants excluding their own".
- A LIFE card can only be given to, or received from, another player. You need one to enter a shelter pod. Each player can give only one LIFE per round.
- A DEATH card nullifies the recipient's LIFE card.
- GAME CLEAR for players who use up all their cards and survive every invasion.
- The recipient sees which card arrived but not who sent it.
- The announcement: "This is a game designed for those who wants their loved one to live and who will guarantee their survival. In the face of the alien invasion, please protect those you cherish."

**Why it feels like a zero-sum betrayal game.**
- Hall 1 has a readable sign: "one person per shelter".
- After Hall 1, "there are only five safe pods left, and yet six players are still alive" (ch. 1).
- Everyone holds one DEATH card that *must* be used up to clear, and anonymity hides who sent one.

**The hidden loophole.**
- The corpse is a **replica that still counts as a participant**. Cards can only be given to those not killed by an invasion, so "the dead body at the start of the game can still receive cards". It can absorb every DEATH card. Its phone is still active and can give LIFE cards (ch. 9 to 10).
- By count, six players each see five others, so the sixth icon on every phone must be the corpse. The rules show the "fake player" on every screen from the start **(my inference)**.
- Pod capacity rises from one to three. The sign was only readable in Hall 1. The pods "look small but they are not cramped inside" (W: Nine_of_Hearts; ch. 10). By Hall 6 the sign reads "Capacity: 3 people" (ch. 12).
- Arisu's trigger is the daughter's story about playing musical chairs at a daycare (ch. 10).

**How greed breaks it.**
- Kitou, a doctor, finds the corpse's phone *before the game*.
- He uses it **selfishly**. He runs a LIFE circle between his partner Onoue, himself and the corpse, then claims he has no LIFE left and abandons her (ch. 9).
- He then uses his edge to send Arisu a DEATH card: "agree to lose your life or doom everyone to die" (ch. 10).
- His justification is triage. As a disaster doctor he gave a burned child a black tag, and he says he will "repay" by saving hundreds later (ch. 11).
- Earlier, a wounded father begs the others to dump their DEATH cards on him to spare each other. Arisu sees the flaw: anyone who keeps their DEATH card wins at the end (ch. 6).
- Resolution:
  - Arisu sends his DEATH card to the corpse and a LIFE card to Kitou, who intends to kill him.
  - Kitou breaks down and follows the plan.
  - Three of six survive. Onoue, the father Yuzuru and the loner Taiga are dead (ch. 11 to 13).
- In Hall 6, the daughter Himari tells Kitou that the three of them "would not be standing in the final room had he not found the extra phone" (ch. 13).

**Fan reception.** On r/manga: "this Heart of 9 game is one of my favourite games from this series." Another: "Almost all other Psychological games had a way for almost everyone to survive, just like this one."
- Source: https://www.reddit.com/r/manga/comments/lauw0j/disc_alice_in_borderland_retry_chapter_13_end/

---

### 1.4 Ten of Hearts: "Witch Hunt" (manga ch. 20 to 28; Netflix S1E6 to E8)

Sources:
- W: [Ten_of_Hearts](https://aliceinborderland.fandom.com/wiki/Ten_of_Hearts)
- W: [Ten_of_Hearts_(Netflix)](https://aliceinborderland.fandom.com/wiki/Ten_of_Hearts_%28Netflix%29)
- W: [Chapter_28](https://aliceinborderland.fandom.com/wiki/Chapter_28)

**Rules, in full.**
- "The evil Witch who took Momoka's life is hiding among the players. The 'Witch' role is not limited to women."
- Clear: find the Witch and burn them in the Fire of Judgement. GAME OVER if the Witch is not burned within 120 minutes.
- The game starts with Momoka's stabbed body in the hotel lobby.

**Hidden insight.** "Momoka is the Witch herself… who volunteered to die and put the knife through her own heart. All the players have to do to clear the game is to throw Momoka's body in the fire" (Netflix wiki).
- The wording is literally true: her body *is* among the players, and she *did* take her own life.
- **Planted evidence.** "the fingerprints on the knife show a reversed grip, which means Momoka held it with her own hands" (Chapter 28).

**Why it fails anyway.**
- Mira (Queen of Hearts) learns that the Beach's leader Hatter is dead. She raises the game from **5♥ to 10♥** "convinced that there would be no survivors". Aguni, wracked with guilt, becomes "the perfect defender for the Witch" (Chapter 28).
- Last Boss suggests the purge and Aguni supports it. Militants shoot people and burn the bodies (Netflix wiki).
- The wiki notes the solution is unchanged after the upgrade, so it "can be considered easier than both Seven and Nine of Hearts" (wiki analysis).

**The dealer's motive is the moral core.**
- Momoka: "For the sake of surviving, you do nothing but wish for others' deaths… Can something like that truly be called a person who is alive?"
- She "hoped people would not selfishly kill one another" (Chapter 28; Kuzuryu page flashback).
- Her friend Asahi's arc: rage at the massacre, then trust in Arisu. Asahi confesses and is lasered for revealing she is a Dealer (Netflix wiki).

**Reception.**
- Slashfilm: "the true agony of the witch hunt game lies in knowing that all of those deaths could have been avoided" if players had "paused and approach[ed] the problem rationally".
  - Source: https://slashfilm.com/631185/alice-in-borderland-season-1-ending-explained-the-games-have-just-begun
- Looper ranks it the most reckless S1 game and calls the massacre "entirely avoidable". Source: https://www.looper.com/1357825/every-game-alice-in-borderland-ranked-reckless
- Fans: "Such a clever and simple solution, really embodied the hearts game" (u/ThatCrowny, on 1m6jx2n).
- Counterpoint: a viewer objects that Arisu assumes "the games are winnable without any deaths" right after the 7♥ showed Hearts games "will include inevitable deaths".
  - Source: https://www.reddit.com/r/AliceInBorderland/comments/1gwgoir/idiotic_characters_and_lack_of_logic/

---

### 1.5 Seven of Hearts: "Hide and Seek" (manga; Netflix S1E3). The "is there a solution?" game

Sources:
- W: [Seven_of_Hearts](https://aliceinborderland.fandom.com/wiki/Seven_of_Hearts)
- W: [Seven_of_Hearts_(Netflix)](https://aliceinborderland.fandom.com/wiki/Seven_of_Hearts_%28Netflix%29)

**Rules (manga wiki).**
- Four players, 10 minutes (Netflix: 15), an indoor botanical garden.
- Headset with an eye-tracking eyepiece and microphone, wired to an explosive collar.
- "One player is randomly designated as the wolf… three players become sheep."
- "If the wolf makes eye contact with a sheep… the sheep becomes the new wolf."
- A 3-second cooldown before the previous wolf can become wolf again.
- At time zero, every sheep collar explodes and the wolf survives.
- "a large array of gardening tools and weapons, any of which may be used."
- Microphones broadcast everything said to everyone.

**Designed against friendship.** Mira (Queen of Hearts) designed it "specifically intended to be played by Arisu and his friends after she observes how close the four of them are" (manga wiki). In Netflix, per the wiki's paraphrase, Mira claims she designed it for Arisu's group "because the group was too close" (W: [Queen_of_Hearts_(Netflix)](https://aliceinborderland.fandom.com/wiki/Queen_of_Hearts_%28Netflix%29)).

**Outcome.** The friends Karube and Chota choose to die so that Arisu lives. Shibuki grabs the wolf role and runs (Netflix wiki strategy notes).

**Is there a no-death solution? Canon is deliberately silent.**
- The wiki says "Arisu theorizes that there is a solution in every Hearts game that involves no deaths. However, this theory is unconfirmed… The solution was never found by any character in the manga, and Haro Aso declined to provide a conclusive explanation." I did not find the chapter where Arisu states this.
- **Verified primary source.** I opened the screenshot of Haro Aso's reply (@asoharoo, 12/27/20): "Thank you for reading Alice! ♡7 is… I'll let you wonder."
  - Screenshot: https://i.imgur.com/JJ17lZM.jpg
  - Thread: https://www.reddit.com/r/AliceInBorderland/comments/klm14h/i_asked_aso_haro_creator_of_alice_in_borderland/ (score 334)
  - A later fan claims "the author… claimed there is one". That is **false** per the screenshot (https://www.reddit.com/r/AliceInBorderlandLive/comments/1m6oiq5/do_all_games_have_a_solution/).
- **Fan theories** (wiki and Reddit; none confirmed):
  1. **Cut the wolf's collar.** The wolf's collar won't explode, so sheep cut it, pass the role, and repeat. This cites the tools and the sheep being drawn *behind* the wolf. Supported by u/AceContinuum (67 points) on 1m6oiq5 and by u/Aggravating_Date_346 on https://www.reddit.com/r/AliceInBorderland/comments/keqpyo/was_there_any_real_solution_to_the_7_of_hearts/
  2. **Mirror trick for mutual eye contact.** The wiki doubts it. A commenter notes the 3-second cooldown "was to prevent this" (on klm14h).
  3. **"Just goggles, not collar."** A reply quoting the manga gives: "please equip this choker and enter the arena. If you do not, your participation rights will be revoked" (u/spaghetticourier, 47 points, https://www.reddit.com/r/AliceInBorderland/comments/q4skeo/7_of_hearts_solution/).
  4. **Wording in the official English Viz volume 2.** A Reddit user quotes it as "**Put on the collars before entering the arena**", "Whoever is in the wolf role completes the game", and "This Seven of Hearts guarantees **at least** one player's survival. A generous game, a fair game." They argue that "at least" implies more can live. **UNVERIFIED**: I did not see the volume. Source: https://www.reddit.com/r/AliceInBorderland/comments/w8kbkp/the_official_english_translation_of_seven_of/
- **Counter-argument** (wiki trivia and Netflix wiki). Mira, who taunts Arisu in the Queen of Hearts game to break him, "would have definitely told Arisu about a potential solution… Since… she did not mention any way to survive… it might mean that there was no intended solution."
- **Fans split on the value of ambiguity.** Some like that it is unsolvable ("shows 'The Borderland's' unfair nature", u/Ajaxorix777 on klm14h). Others think a solution would make the deaths "pointlessly avoidable" (u/Salty-Appointment-64 on q4skeo).
- **Emotional impact is unmatched.** "Seven of Hearts. I may never recover" (u/MoriTod on 1m6jx2n). Looper: the friends are "even more heroic for giving Arisu a second chance".

---

### 1.6 Queen of Hearts: "Croquet" (manga ch. 58 to 62; Netflix S2E7 and E8)

Sources:
- W: [Queen_of_Hearts](https://aliceinborderland.fandom.com/wiki/Queen_of_Hearts)
- W: [Queen_of_Hearts_(Netflix)](https://aliceinborderland.fandom.com/wiki/Queen_of_Hearts_%28Netflix%29)

**Rules.** "Players have to finish the game." There are no rules beyond standard croquet. "It is GAME CLEAR if the players finish three sets." "It is GAME OVER if the players decide to stop mid-game." Weapons are allowed.

**Hidden trap.** "if she provokes the players into killing her, the game does not clear or end, rendering it unclearable. The remaining players would then have no choice but to wait for their visas to expire. This is why weapons are permitted" (manga wiki trivia).
- The game is easy to win and easy to lose: just keep playing and don't listen.
- The wiki's strategy note: "finish the game without taking breaks, drinking the tea, or engaging in further conversation."

**Weapon used.**
- **Manga.** Tea laced with a hallucinogen, plus Mira's stories that "the Borderland is an illusion".
- **Netflix.** Mira slows the game while Usagi bleeds. She tells three joke "truths" and confesses to designing the 7♥ to bait a shotgun shot. Then she claims Arisu is a psychiatric patient. Usagi slits her own wrist to pull him back.

**Reception.**
- An OP defending it concedes "the common opinion is that the QOHs game was a little underwhelming". They argue it played with "OUR emotions" too.
- Critics: "QOH after KOS felt like a downer… anticlimactic" (u/khayrirrw).
- Source: https://www.reddit.com/r/AliceInBorderland/comments/1000ix3/why_the_queen_of_hearts_game_was_actually_really/
- **Adaptation plot hole.** "the Netflix version … makes a point of showing that Arisu does not drink the hallucinogenic tea, which raises the question of why he starts hallucinating" (Netflix wiki trivia). Echoed: "they skip Arisu drinking the tea which is the entire reason Mira can manipulate him" (u/-Bloodletter- on zt4qxx).
- Looper: Mira's strategy is "getting into the minds of her competitors and attacking their very will to keep on playing".

---

### 1.7 Four of Clubs: "Runaway" (manga side story) / "Distance" (Netflix S1E4)

Sources:
- W: [Four_of_Clubs](https://aliceinborderland.fandom.com/wiki/Four_of_Clubs)
- W: [Four_of_Clubs_(Netflix)](https://aliceinborderland.fandom.com/wiki/Four_of_Clubs_%28Netflix%29)
- W: [Keiichi_Kuzuryu](https://aliceinborderland.fandom.com/wiki/Keiichi_Kuzuryu)

**Rules.**
- "The players have to overcome all the trials and reach the GOAL" within the time limit, in a 10 km tunnel.
- Trials: a cheetah at 10 minutes, crocodiles and water at 20, a snowstorm at 30, an explosion at 50.
- Netflix: "Phones provide a counter showing the distance from the GOAL."

**Hidden solution.**
- "The bus is the GOAL. It has the word 'GOAL' spray painted on it."
- A dictionary in the glove box translates "runaway" as "a victory that is easily obtained".
- The bus is durable and has a heater, so it survives every trial.
- "only those who do not ignore an injured player are able to clear it."
- Netflix: "Distance: 0" on the counter means you are already there.
- Wiki trivia: "the only game in the series in which the solution is hidden in its title."

**Meta-clue.** "The fact that the game is not a Spades type but a low-number Clubs, despite the seemingly difficult trials, foreshadows that the solution is simple." Netflix wiki: running "is more likely to be a game of Spades".

**Kindness test.**
- The "injured player" was **Kuzuryu in disguise**. He wanted "to know whether someone willing to help him exists".
- One player stays with him and both survive.
- This moment returns to decide the King of Diamonds game (Kuzuryu page).

**Criticism.** A viewer found it too obvious: "the moment I saw the 'distance = 0' on one of their phones I assumed 'oh, theyre already at the goal'". The characters missing it for 30 minutes was "irritat[ing]".
- Source: https://www.reddit.com/r/AliceInBorderland/comments/1gwgoir/idiotic_characters_and_lack_of_logic/

---

### 1.8 Four of Hearts: "Survey" (manga side story)

Source: W: [Four_of_Hearts](https://aliceinborderland.fandom.com/wiki/Four_of_Hearts)

**Rules (stated).**
- Five players, each in a window-cleaning lift starting at floor 10.
- A survey question shows majority and minority answers. Players press "majority was right" or "minority was right".
- Reaching floor 20 clears the game. Reaching floor 0 is GAME OVER.

**Rules hidden until discovered in play.**
- A correct majority answer moves up 1 floor.
- A correct minority answer moves up 2 floors.
- A wrong majority answer moves down 1 floor plus an electric shock.
- A wrong minority answer is instant GAME OVER.
- "Tricking another player into picking the wrong answer grants bonus five floors up."

**Escalation.** Questions become absurd. From question 10 the survey data disappears and questions are about the building itself: "a guessing game with exact 50/50 odds".

**Hidden insight.** "the waiting room… has a selection of pamphlets containing all the answers to the 10th question and onward." If everyone answers majority when unsure and carries a pamphlet, "all players will be able to clear the game without any guessing."

**Outcome.** Dodo tricks Arisu and another player (the gallery caption says "Dodo fools Arisu and another player into picking an incorrect choice"). Three die. Dodo then gives Arisu the flyer and both clear (W: [Ryohei_Arisu](https://aliceinborderland.fandom.com/wiki/Ryohei_Arisu)).
- **Lesson.** A hidden *reward for betrayal* (+5 floors) that players only discover by being betrayed.

---

### 1.9 Three of Clubs: "Good Fortune, Bad Fortune" (manga) / "Sacred Fortunes" (Netflix S3)

Sources:
- W: [Three_of_Clubs](https://aliceinborderland.fandom.com/wiki/Three_of_Clubs)
- W: [Sacred_Fortunes_(Netflix)](https://aliceinborderland.fandom.com/wiki/Sacred_Fortunes_%28Netflix%29)

**Rules.**
- Each player draws a fortune slip with a numeric question.
- "For every point by which a player's answer differs from the correct answer, one flaming arrow is fired."
- Clear when everyone has drawn.

**Hidden insight.**
- Each slip carries a tiny corner note: "Fear the West", "Fear the East", "Fear the North".
- The "Excellent Luck" slip says "Lucky direction: South".
- The notes match where the arrows come from. "South of the festival grounds, there is a well that leads to a concealed room connected to the sewage system."
- The real clear is to escape, not to answer. In the Netflix version the safe direction is northwest, the one direction never mentioned.

**Fan view.** S3's Sacred Fortunes "was great". Arisu "was a bit slow picking up the North, South, East, West clue". Source: https://www.reddit.com/r/AliceInBorderlandLive/comments/1nqv7io/reasons_why_season_3_is_horrible_and_extremely/

---

### 1.10 Four of Diamonds: "Light Bulb" (Netflix S1E5)

Source: W: [Four_of_Diamonds_(Netflix)](https://aliceinborderland.fandom.com/wiki/Four_of_Diamonds_%28Netflix%29)

**Rules.**
- Three switches. One turns on a bulb in the next room.
- "With the door is closed, players may flip any switch. While the door is open, players may only flip the switch once."
- Rising water drowns, then electrocutes, the room.

**Insight.** "the Four of Diamonds game rules actually provide all the necessary leads to solving the game with a 100% chance of success." The trick is the classic heat test:
- With the door closed, flip A and wait, then turn it off.
- Open the door and touch the bulb. Warm means it was A.
- Flip B and watch whether the bulb lights.

**Lesson.** The loophole is a *permission* buried in the rule text: "may flip any switch" while the door is closed.

---

### 1.11 King of Clubs: "Osmosis" (manga ch. 33 to 41; Netflix S2E1 to E3). Hidden information in a team game

Sources:
- W: [King_of_Clubs](https://aliceinborderland.fandom.com/wiki/King_of_Clubs)
- W: [King_of_Clubs_(Netflix)](https://aliceinborderland.fandom.com/wiki/King_of_Clubs_%28Netflix%29)

**Rules, condensed.**
- Each five-person team splits 10,000 points freely, minimum 100 each.
- Touching an opponent starts a battle. The higher score wins 500 points from the loser.
- Groups that hold hands battle with combined totals, and "a player can only discover the total sum of points from that group".
- After a battle, a player is inactive until they touch their own base.
- Touching your own base gives infinite points. Touching the enemy base gives 10,000.
- A player at 0 points is shot.

**Why it works.** The split of points is secret, so every battle is a bet on hidden information.
- A "Provoker" deliberately loses a fight to learn totals.
- Kyuma's team evens out at 2,000 points each and accepts "the certain death of one person" so the other three become "invincible forces with over 10,000 points".
- The endgame: Arisu uses a door to cut off Tatta's arm so his wristband can be carried into a battle.

**Reception.** A favourite of several fans ("Osmosis!!"). Wiki trivia: "arguably one of the most complex games". A viewer argues the King's team could have spammed the base and the player team could have used Tatta as a "battering ram". Those are exploits the characters miss (OP of thread 1gwgoir: https://www.reddit.com/r/AliceInBorderland/comments/1gwgoir/idiotic_characters_and_lack_of_logic/).

---

### 1.12 Shorter entries, useful as contrast

- **Two of Hearts** (manga ch. 10). Four train cars, one full of poison gas, three five-minute air canisters. A vase of flowers is wilted in the poisoned car. The poison is in the 4th car.
  - Wiki trivia: the test is "whether the player is willing to risk their life once under favourable odds, when the guarantee of safety is within reach".
  - Source: W: [Two_of_Hearts](https://aliceinborderland.fandom.com/wiki/Two_of_Hearts)
  - The Netflix S3 remake, "Runaway Train", has eight cars, four of them poisoned, five canisters and a canary instead of flowers. The wiki computes a "1 in 14, or approximately 7.14%" chance by guessing alone. Fans called it "horrible (likely PURE LUCK?)… no way to solve" (1nqv7io).
  - Source: W: [Runaway_Train_(Netflix)](https://aliceinborderland.fandom.com/wiki/Runaway_Train_%28Netflix%29)
- **Six of Diamonds, "Blackjack"** (manga side story). Last player with chips survives. Getting caught cheating means being shot. "During the game, all players cheat at least once." Chishiya combines card counting with a deck-flip "turnover".
  - Source: W: [Six_of_Diamonds](https://aliceinborderland.fandom.com/wiki/Six_of_Diamonds)
- **Jack of Diamonds, "Mahjong."** The Citizen adds Kansai house rules "thinking they could help him win, but they end up sealing his fate". The host's own added rule backfires.
  - Source: W: [Jack_of_Diamonds](https://aliceinborderland.fandom.com/wiki/Jack_of_Diamonds)
- **King of Hearts, "Silent"** (Netflix only, shown in a montage). Players flee an unseen roaring beast through a maze. Viewers assume the beast doesn't exist.
  - Heavily criticised: "Wtf was that physical running through a maze game? Where is my master of trickery and treason?" (u/Karolmo, 92 points, zttedc). Also: "As a hearts game, why are people running… away from a animal, with an extremely physical portrayal?" (zwamfb).
  - Source: W: [King_of_Hearts_(Netflix)](https://aliceinborderland.fandom.com/wiki/King_of_Hearts_%28Netflix%29)
- **Zombie Hunt** (Netflix S3). Card duels in which the Zombie card infects the loser, Shotgun cards kill zombies, and Vaccines cure. The side with the most members wins.
  - Solution: "turn all the participants into zombies". The "monster" side is the safe side.
  - Fans: "The plot hole of where they could all become zombies and live since the very start is major, however I justify this since people would not want to risk speaking up… because they feared getting shotgunned" (1nqv7io). Fear of speaking up is what keeps the loophole hidden.
  - Source: W: [Zombie_Hunt_(Netflix)](https://aliceinborderland.fandom.com/wiki/Zombie_Hunt_%28Netflix%29)
- **Old Maid** (Netflix S3E1, played in the real world). The objective is reversed: you must *keep* the Joker. Leaving your seat or running out of cards means electrocution.
  - Source: W: [Old_Maid_(Netflix)](https://aliceinborderland.fandom.com/wiki/Old_Maid_%28Netflix%29)
- **Future Sugoroku** (Netflix S3 finale). Dice decide how many people can pass each door. Players have point budgets, and the walls show "images of their future".
  - Fans: "100% the worst game… dragged on" (1nqv7io). The wiki notes contradictory clear announcements.
  - Source: W: [Future_Sugoroku_(Netflix)](https://aliceinborderland.fandom.com/wiki/Future_Sugoroku_%28Netflix%29)

---

## 2. What fans praise and what they criticise (cross-cutting)

**Praised.**
- Games whose solution is "clever and simple" yet missed because of panic: Witch Hunt, Runaway (1m6jx2n; Slashfilm).
- Games where the maths turns into a moral question: King of Diamonds (1m6jx2n).
- Long, tense trust games with a hidden antagonist: Jack of Hearts (zttedc, zt4qxx).
- The emotional weight of friends forced against each other: 7♥ (1m6jx2n).

**Criticised.**
1. **Clears in the last second, every time.** "Almost every game is finished in the very last second" (r/netflix, score 1130). Source: https://www.reddit.com/r/netflix/comments/px0vf9/alice_in_borderland_was_extremely_disappointing/ Also: "They ALWAYS struggle till the last second" (1gwgoir).
2. **Reveals built on information the audience never saw.** The JoH cookie code (Beliar7, zttedc).
3. **The hero survives on intuition or luck.** Chishiya's final suit guess (Netflix Chishiya page; 1m6jx2n).
4. **The game master cheats.** Matsushita's prosthetic eye (1458yuw, 1ok04fx).
5. **Suit and theme mismatch.** A Hearts game that is just a physical chase (King of Hearts Netflix; zttedc, zwamfb).
6. **Pure luck with no deducible path.** Runaway Train (1nqv7io).
7. **Obvious loopholes the characters miss make them look stupid.** Distance; King of Clubs exploits (1gwgoir).
8. **An inconsistent "every Hearts game has a no-death solution" premise** while one Hearts game appears to have none (1gwgoir; 7♥ debate).
9. **Adaptation cuts that remove the causal clue.** QoH tea; JoH hypnosis set-up (zt4qxx; Netflix QoH wiki).

---

## 3. Design patterns to borrow

1. **Write the clear condition so it is literally true but invites a violent reading.**
   - "The Witch who took Momoka's life is hiding among the players": she took her own life, and her body is among them.
   - "Reach the GOAL": the goal is where you start.
   - "A game designed for those who wants their loved one to live" (Nine of Hearts).
   - "Players have to finish the game" (Queen of Hearts): don't quit, don't kill.
2. **Put the loophole in a permission, a definition, or an omission, never in a hidden rule.**
   - "With the door closed, players may flip any switch" (4♦).
   - LIFE and DEATH can go to anyone "who has not died from an alien invasion", which includes a corpse that was never killed by an invasion (9♥).
   - The JoH violence ban only stops a player being prevented from *speaking*, so torture is legal.
   - The reflective-items ban covers only *players*, so the Citizen's eye is legal.
3. **Plant one ignorable physical object per game, shown on-panel early.** A dictionary in the glove box. Pamphlets in the waiting room. A corpse and its phone. Corner notes on fortune slips. Wilted flowers. A reversed knife grip. Tools on a table. Fans punish reveals that rely on unseen information (JoH cookies).
4. **Use the category label as a meta-clue.** A low Clubs card with brutal physical trials means running is wrong (4♣). A Hearts game whose rules seem to demand a murder means the murder is the trap (Hearts wiki). In *Dead Man's Algorithm*, the game's "type" or title can serve the same role.
5. **Make honesty a stable but unsustainable equilibrium, so time forces betrayal.**
   - JoH: total honesty keeps everyone alive forever, but the game cannot end without a lie.
   - External pressure (visas outside, food, hourly rounds, sleep) makes stalling a slow death.
   - Your hidden "everyone survives" solution should *exist* but need a costly first act of trust.
6. **Hide each player's most vital fact from themselves.** JoH: you cannot see your own suit, and Netflix re-rolls it every round. Your life depends on someone else's word, every hour. Paranoia comes from the structure, not from the villain. The designer even removes mirrors, metal knives and water.
7. **Escalate with rules triggered by deaths, each one killing the current safe strategy.** In King of Diamonds, rules added on each elimination destroy the equilibrium the survivors had found: duplicates are voided, an exact hit doubles damage, and 100 beats 0. The deaths themselves rewrite the game. Offer "kind" adjustment time to make the cruelty feel fair.
8. **Add a hidden reward for betrayal that players discover by being betrayed.** 4♥: +5 floors for tricking someone. 9♥: Kitou's private use of the extra phone. A loophole found by one player can be hoarded rather than shared. That fits your theme of greed breaking the escape route.
9. **Turn safety rules into murder weapons.** The JoH "one person per locked cell" rule protects players, and Yaba uses it to kill two. Write protective rules that a cold player can weaponise.
10. **End a duel by handing your life to the opponent.** Chishiya reveals 100, so Kuzuryu must actively choose to kill him or let him live. It converts maths into character and is the most praised moment of the King of Diamonds game.
11. **Let the game master's philosophy shape the game and its weak point.**
    - Kuzuryu's equality obsession makes the game "fair" and becomes his flaw.
    - Mira designs 7♥ to break a tight friend group.
    - Matsushita's contempt for "extras" blinds him to Yaba and Banda's alliance.
    - Komayama's own house rules beat him.
12. **Use ambiguity sparingly.** One unsolved game (7♥) creates years of debate and grief. But if your premise promises a loophole in *every* game, as yours does, every game must pay it off, or readers will call it inconsistent (1gwgoir). Haro Aso's "I'll let you wonder" works because AiB never promised a loophole in every game.
13. **Avoid the fan-flagged failures.**
    - Clears in the last second every time.
    - Luck-only games (Runaway Train).
    - A genius protagonist surviving on a coin flip.
    - The villain cheating with tech the reader can't detect.
    - A loophole so visible that the cast looks dumb (Distance).

---

## 4. Unverified or caveated items

- The official Viz English wording for 7♥ ("at least one player's survival… A generous game, a fair game") rests only on a Reddit user's quote (w8kbkp). **UNVERIFIED.**
- The wiki says "Arisu theorizes that there is a solution in every Hearts game that involves no deaths". I could not locate the chapter. It is plausibly tied to the Witch Hunt reveal (1gwgoir paraphrases Arisu saying "maybe there was a way to clear this game without any player dying"). **UNVERIFIED** as a direct quote.
- The rule "GAME OVER for the last remaining player alongside the Jack of Hearts" is quoted as the wiki gives it. Its exact meaning in the manga text is unclear to me.
- Netflix King of Hearts rules are not given on screen. The wiki gives only inferred clear and fail conditions.
- The wiki's King of Diamonds manga table records Kuzuryu's last pick as 0. The same wiki's story text describes him pressing 1 and 0 with two thumbs. I did not check the panels.
- Wiki "Strategy" and "Trivia" sections, such as the Nash-equilibrium reading and the "most generous" Face Card game, are editors' analysis.

## 5. Source list

**Fan wiki** (read via MediaWiki API; canonical URLs):
- https://aliceinborderland.fandom.com/wiki/King_of_Diamonds
- https://aliceinborderland.fandom.com/wiki/King_of_Diamonds_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Keiichi_Kuzuryu
- https://aliceinborderland.fandom.com/wiki/Keiichi_Kuzuryu_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Hinako_Daimon
- https://aliceinborderland.fandom.com/wiki/Jack_of_Hearts
- https://aliceinborderland.fandom.com/wiki/Jack_of_Hearts_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Enji_Matsushita
- https://aliceinborderland.fandom.com/wiki/Enji_Matsushita_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Shuntaro_Chishiya_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Queen_of_Hearts
- https://aliceinborderland.fandom.com/wiki/Queen_of_Hearts_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Ten_of_Hearts
- https://aliceinborderland.fandom.com/wiki/Ten_of_Hearts_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Chapter_28
- https://aliceinborderland.fandom.com/wiki/Seven_of_Hearts
- https://aliceinborderland.fandom.com/wiki/Seven_of_Hearts_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Nine_of_Hearts
- Chapters 1, 6, 9 to 13 (RETRY), at https://aliceinborderland.fandom.com/wiki/Chapter_N_%28RETRY%29
- https://aliceinborderland.fandom.com/wiki/Four_of_Hearts
- https://aliceinborderland.fandom.com/wiki/Two_of_Hearts
- https://aliceinborderland.fandom.com/wiki/Hearts
- https://aliceinborderland.fandom.com/wiki/Face_Cards
- https://aliceinborderland.fandom.com/wiki/Four_of_Clubs
- https://aliceinborderland.fandom.com/wiki/Four_of_Clubs_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Three_of_Clubs
- https://aliceinborderland.fandom.com/wiki/Sacred_Fortunes_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Four_of_Diamonds_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/King_of_Clubs
- https://aliceinborderland.fandom.com/wiki/King_of_Clubs_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Six_of_Diamonds
- https://aliceinborderland.fandom.com/wiki/Jack_of_Diamonds
- https://aliceinborderland.fandom.com/wiki/King_of_Hearts_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Zombie_Hunt_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Runaway_Train_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Old_Maid_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Future_Sugoroku_%28Netflix%29
- https://aliceinborderland.fandom.com/wiki/Ryohei_Arisu

**Official and press:**
- https://www.netflix.com/tudum/articles/alice-in-borderland-series-game-rules
- https://slashfilm.com/631185/alice-in-borderland-season-1-ending-explained-the-games-have-just-begun
- https://www.looper.com/1357825/every-game-alice-in-borderland-ranked-reckless
- Haro Aso tweet screenshot: https://i.imgur.com/JJ17lZM.jpg

**Reddit:**
- https://www.reddit.com/r/AliceInBorderland/comments/1m6jx2n/favorite_aib_game_and_why/
- https://www.reddit.com/r/AliceInBorderland/comments/zttedc/chishiya_and_the_jack_of_hearts_game_kinda/
- https://www.reddit.com/r/AliceInBorderland/comments/zt4qxx/okay_but_can_we_talk_about_how_the_jack_of_hearts/
- https://www.reddit.com/r/AliceInBorderland/comments/1458yuw/how_did_enji_get_away_with_it_vague_bc_spoilers/
- https://www.reddit.com/r/AliceInBorderland/comments/1ok04fx/jack_of_heart_and_cheating/
- https://www.reddit.com/r/AliceInBorderland/comments/klm14h/i_asked_aso_haro_creator_of_alice_in_borderland/
- https://www.reddit.com/r/AliceInBorderland/comments/q4skeo/7_of_hearts_solution/
- https://www.reddit.com/r/AliceInBorderland/comments/keqpyo/was_there_any_real_solution_to_the_7_of_hearts/
- https://www.reddit.com/r/AliceInBorderland/comments/w8kbkp/the_official_english_translation_of_seven_of/
- https://www.reddit.com/r/AliceInBorderlandLive/comments/1m6oiq5/do_all_games_have_a_solution/
- https://www.reddit.com/r/AliceInBorderland/comments/1000ix3/why_the_queen_of_hearts_game_was_actually_really/
- https://www.reddit.com/r/AliceInBorderland/comments/1ivbqxw/how_was_chishiya_supposed_to_win_in_beauty_contest/
- https://www.reddit.com/r/AliceInBorderland/comments/1gwgoir/idiotic_characters_and_lack_of_logic/
- https://www.reddit.com/r/AliceInBorderland/comments/v1hws3/so_i_just_finished_the_manga/
- https://www.reddit.com/r/AliceInBorderlandLive/comments/zwamfb/my_very_long_review_of_aib_season_2_as_a_manga/
- https://www.reddit.com/r/AliceInBorderlandLive/comments/1nqv7io/reasons_why_season_3_is_horrible_and_extremely/
- https://www.reddit.com/r/manga/comments/lauw0j/disc_alice_in_borderland_retry_chapter_13_end/
- https://www.reddit.com/r/netflix/comments/px0vf9/alice_in_borderland_was_extremely_disappointing/
