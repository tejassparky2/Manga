# Death games: craft, audience and game-theory notes

Research notes for **Dead Man's Algorithm**: students forced into survival games, where every game hides a hard-to-find loophole that would let everyone survive, and greed, fear or betrayal breaks it.

- **Compiled:** 2026-10-28.
- **Sources:** Reddit was read through the official API (`tools/reddit_tool.py`). Web pages were opened with WebFetch.
- **Verification:** Every claim has the URL of a source that was actually opened.
  - **Reddit quotes** are copied exactly from the API output. A score like `[103]` is that comment's upvote count when it was fetched.
  - **Web quotes** are as the fetch tool returned them from the page.
  - **UNVERIFIED** marks anything not confirmed in an opened source.
  - **DESIGN IDEA** marks my own suggestions for the author. These are synthesis, not sourced facts.
- **Caveat:** Reddit comments are individual opinions, not surveys. Recurring patterns across many threads count for more than any single quote.

**Pages that would not open (not used):**
- TV Tropes (HTTP 403)
- the-artifice.com (403)
- Alice in Borderland fandom wiki (402)
- Liar Game and Kaiji fandom wikis (403)
- thereviewgeek.com (403)
- trillmag.com (403)
- TED transcript for J.J. Abrams' "Mystery Box" (the page had no transcript text)

**Excluded:** r/danganronpa thread 13sel4v ("these games are BAD") is a satire or shitpost. Its "complaints" are jokes, so it is not cited.

---

## 1. What readers say makes a death game or mind game clever, and what makes it cheap

### 1.1 Top complaints (things to avoid)

**C1. The win comes from a plan hidden off-page, then explained afterwards ("I planned all of this").**
- Tomodachi Game critique, r/manga, 2022 ([source](https://www.reddit.com/r/manga/comments/vpnpi9/tomodachi_game_is_one_of_the_worst_manga_i_have/)). The OP describes the per-arc formula: "we cut to a character revealing something to another character that doesn't get revealed till like 20 chapters lately... yuichi reveals that he planned all of this to happen". They call it "the writer pulling sikes in the audience and thinking it's good writing."
- r/TomodachiGame, 2023 ([source](https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/)).
  - The OP complains of "Yuuichi's ass pull hedge bet plan(which is just in my humble opinion lazy writing...) he did offscreen".
  - The OP adds that "every time a side character needs character development, Yuuichi just disappears from the chapter and he comes back only for the chapter to tell the readers how he solos the game(which breaks the 'show don't tell' rule".
  - The same OP's favourite game is Hide and Seek, "the only game that stayed in Yuuichi's prospective, and it shows him go through trial and error."
  - A commenter [15]: "The first three games were the best when he did everything under our noses and we still had no idea what this bitch was up to."
- r/writing twist guide, score 1589 ([source](https://www.reddit.com/r/writing/comments/de7120/dos_and_donts_of_a_good_twist/)).
  - The guide's rule: "It should not heavily rely on information the reader had no access to. If the twist requires flashbacks to scenes that the reader never saw before ... Your reader will feel cheated."
  - A commenter [39] on BBC Sherlock: "it is solved without the audience seeing any of the evidence or how anything is solved. Sherlock essentially just reads the script".

**C2. Rules that appear only when they kill someone, or that are relayed off-screen.**
- Alice in Borderland S3 critique, 2025 ([source](https://www.reddit.com/r/AliceInBorderland/comments/1nr83tb/season_three_felt_like_a_huge_middle_finger_to/)).
  - "HOW WERE PLAYERS SUPPOSED TO KNOW THAT THE CAN EXPLODES IF IT GETS THROWN TOO HARD? It just feels stupid; it just ends up being the plot device to kill off the less significant characters."
  - On Bingo: "why are balls falling when people hit a button? Was that ever explained as a rule?"
  - A commenter: "how does it make sense that you need to yeet the canister, but it explodes on impact? and they withheld that rule".
- Squid Game marbles debate ([source](https://www.reddit.com/r/squidgame/comments/qajzl0/why_i_think_the_marble_game_was_100_survivable/)). A commenter [104] undercuts the "loophole" theory because "Sang woo relays a previously unknown rule 'no violence' which indicates that the players are given rules off screen." Off-screen rules make readers distrust every loophole.

**C3. Games decided by luck, or by an arbitrary trap.**
- Same AiB S3 post: "The train game is just plain unfair... asides from hyperfixation levels of knowledge of the train, the game is impossible. NOT TO MENTION, Arisu and the others just so happened to win the train game without any explanation."
- r/AliceInBorderland, 2026 ([source](https://www.reddit.com/r/AliceInBorderland/comments/1qkesjf/manga_felt_way_more_thriling_than_the_live_action/)): "1st game in the LA has 25% percent of everyone surviving(IT IS A FRICKING CLUB GAME AND YOU ARE TELLING ME THAT YOU HAVE TO RELY ON LUCK NOT TEAMWORK)". Note: Clubs games are supposed to be teamwork games, so a luck-based Clubs game breaks the show's own genre contract.
- r/squidgame, 2025 ([source](https://www.reddit.com/r/squidgame/comments/1p5vrfd/i_really_hate_how_the_glass_bridge_blows_up/)). The title says the glass bridge explosion is "Completely random and unfair... totally against the spirit of the games." A commenter [3]: "It resulted in the most bullshit death ever."
  - Counterpoint [35]: the unfairness is thematic: "throughout the series they say that the integrity of the game is sacred, but time and again, you see that it's def not true."
  - Lesson: if unfairness is the point, the story must say so on purpose.

**C4. Plot armour and no real stakes.**
- Tomodachi thread above, comment [19]: "Bro there is just no consequences in tomodachi game... never for a moment do you feel like 'oh shit he might die' (like in Usogui)."
- r/TomodachiGame [24]: "I'm tired of him winning all the time too, I wish he would lose at least one game so we can see how vulnerable he really is."
- r/writing, score 1911 ([source](https://www.reddit.com/r/writing/comments/8s0vfa/been_seeing_a_lot_of_this_deathforthesakeofdeath/)), comment [191]: "After the third time in a row of the characters escaping a dangerous situation without a scratch, I no longer feel any suspense in the story because I know they'll always come out fine."

**C5. "Fake smart": everyone else holds the idiot ball, or the character is called a genius instead of shown being one.**
- r/anime, "fake smart characters" ([source](https://www.reddit.com/r/anime/comments/z6gubd/what_are_some_fake_smart_characters_you_have/)).
  - [51]: "the Sherlock holms effect. They magically know what ever piece of information they need to know... and often they make massive leaps of logic and seemingly by sheer luck are always correct".
  - The same commenter on a positive example: "The writers actually show her line of reasoning an how she unravels the mysteries of the series one step at a time. Its amazing how much difference actually showing a character figuring things out makes."
  - [14]: "When they keep having characters call another one smart, it usually makes them look dumber, not smarter."
  - [32], on Classroom of the Elite: "made the dialog and game rules far too dense on purpose so nobody would care to try and understand everything that's going on and wouldn't realize that the characters are rather dumb."
  - [31] notes COTE's island-arc win should have triggered the arc's own injury-penalty rule. Readers check the winning move against every rule.
- Death Note, "Near cheated" theory, score 427 ([source](https://www.reddit.com/r/deathnote/comments/1kd5lvu/why_i_firmly_believe_matsudas_theory_that_near/)).
  - "If the theory is false, then both Near and Light are idiots... The literal most obvious thing to do with a Death Note before using it in an elaborate plot like that is to make a quick test killing."
  - Also: "Gevanni to perfectly craft a forgery... in a single night, which is simply physically impossible."
  - Lesson: if the climax depends on a smart opponent skipping the obvious check, readers revolt.
- Usogui ([source](https://www.reddit.com/r/Usogui/comments/1ujkitm/did_fraudcent_lalo_really_watch_baku_tap_the/)).
  - The title asks whether a top opponent "really watch[ed] Baku tap the table rhythmically 25 TIMES and decide he was just frustrated?!"
  - Defenders list in-world reasons: oxygen deprivation, a second layer of deception. Lesson: give opponents an in-world reason for missing the trick, and show it.
- Liar Game ending ([source](https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/)), comment [6]: "Akiyama's final gambit was fatally flawed. The endless stalemate only works if Yokoya decides not to interfere... Yokoya decides to support the stalemate instead, which felt out-of-character."
- Death Note ([source](https://www.reddit.com/r/deathnote/comments/16xxt81/this_anime_lost_me_because_it_suddenly_decided_to/)), comment [8]: "it borders on PIS [plot-induced stupidity] for him to allow his main suspect to get in touching range of what is essentially his main weapon."

**C6. A dominant strategy nobody notices, which breaks the game.**
- AiB S3 critique: "The Zombie Hunt game had a serious flaw. Why not just turn everyone into a zombie? There are no drawbacks."
- Another commenter: "i honestly thought i missed something".
- A defender [6] argues players are biased against "being called a Zombie". If a game has a degenerate solution, a character must raise it and the story must close it on the page.

**C7. Pseudo-intellectual, wrong or over-dense game theory.**
- r/manga, 2015 ([source](https://www.reddit.com/r/manga/comments/362a4k/you_really_want_to_tell_me_liar_game_is_good/)).
  - [3]: "it's definitely not as smart as it'd like you to think it is. It's pseudo-intellectual at best and at times, downright wrong in its use of game theory principles."
  - [1]: "at a certain point the huge explanation of how they succeeded once again just felt old to me and overdone".
- r/manga, 2022 ([source](https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/)), [19], a fan: "My only complaint was that, it was too big brainy for me at times. Too often he explains the the solution and I'm like... 'Yeah, sure... I totally get that' (spoiler: I totally did not get that)."
- Same thread, [6]: during hiatuses "remembering all the rules and whose goal was what... became very jumbled in memory". Serialised readers forget rules, so re-state them.

**C8. A repetitive win formula.**
- Tomodachi OP's formula: "new game, yuuichi gets pressured, seems like everything is lost... yuichi reveals that he planned all of this... acts like a psycho for like three minutes while all the other characters think 'wow he is scary'" ([source](https://www.reddit.com/r/manga/comments/vpnpi9/tomodachi_game_is_one_of_the_worst_manga_i_have/)).
- r/TomodachiGame [9]: "Shit got repetitive after the 3rd/4th game. We all know who's going to win" ([source](https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/)).

**C9. The protagonist knows what only the author knows.**
- r/rational ([source](https://www.reddit.com/r/rational/comments/4pfpt0/d_an_example_of_a_story_with_lots_of_exposition/)).
  - Thread title: "Characters should solve problems through the intelligent application of *their*, not *your*, knowledge and resources."
  - [2]: "Authorial knowledge should not be used to augment a character's reasoning, nor should a lack of authorial knowledge get in the way of a character's reasoning."
  - Another commenter: "The author knew how he was going to do it, so the murderer ended up planning for that particular scenario, which would have been impossible to reliably predict beforehand."

**C10. Ambiguous wording. Readers will audit every rule, number and timer.**
- AiB King of Diamonds, 0.8 x average ([source](https://www.reddit.com/r/AliceInBorderland/comments/1mth6tx/power_of_66_67_and_0_in_the_king_of_diamonds_game/)). A fan builds an exact-hit trick (pick 66 vs an opponent's 100, since 0.8 x 83 = 66.4). A commenter rebuts: "That only works if you assume numbers are rounded... I don't remember them saying they were rounding". Rounding, ties and "exact" must be defined.
- Squid Game "everyone could survive" theory ([source](https://www.reddit.com/r/squidgame/comments/q254pg/theory_every_game_is_winnable_with_all_players/)).
  - [32]: "The timer is 15 minutes (900 seconds), which means with 456 people there has to be someone crossing the bridge every 2 seconds... No chance that happens."
  - [16] disputes it as 16 minutes. Readers do the arithmetic.
- Marbles loophole debate ([source](https://www.reddit.com/r/squidgame/comments/qajzl0/why_i_think_the_marble_game_was_100_survivable/)).
  - [104]: "If you trade marbles, he now has 10 new marbles that you haven't gotten, so you haven't gotten all his marbles."
  - [56] asks what happens at the exact moment of the last marble.
  - [35]: "They weren't going to spend 10 minutes doing lawyer speak to cover every possible loophole."
  - A loophole that rests on vague wording splits the audience. One that rests on precise wording convinces it.

**C11. The organiser can change the game, which voids every loophole.**
- Squid Game marbles thread [52]: "We saw in the glass game that when a player was able to beat the game without a loophole they changed the game in order to ensure people died. Having seen this I am certain they wouldn't allow an actual loophole".
- Squid Game "all survive" theory: the OP notes that when a glass worker began telling the panes apart, "they dim the lights to remove the advantage".
- DESIGN IDEA: make the organiser bound by its own rules, with a visible, enforced commitment, or the loophole has no value.

**C12. Final games that remove the mind games, and rushed endings.**
- Liar Game ending reread ([source](https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/)).
  - "Having players just pushing buttons without any real opening for the mind games and manipulation that we'd come to expect... was a bummer".
  - "Nao being completely sidelined after having been the central focus of the story's message is a bit infuriating."
  - "To only have 5 pages that need to cover the entire post-game is still jarring."
- r/manga ([source](https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/)): "the *final* twist was in some ways *super* anticlimactic".

**C13. Disposable extras killed only for tension.**
- See section 4b, and the AiB S2 essay ([source](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/)): "The show simply treated the Beach members who weren't a part of our main cast as disposable 'extras' to be killed off for dramatic tension."

### 1.2 What readers praise

**P1. The solution follows from the rules on the page, and the suspense moves from "who" to "how".**
- Tomodachi thread ([source](https://www.reddit.com/r/manga/comments/vpnpi9/tomodachi_game_is_one_of_the_worst_manga_i_have/)).
  - [103]: "we know Yuuichi is gonna win, but how?... I never know what he's actually going to do, even though it makes sense with the rules of the game we're given."
  - [6]: "The suspense shifts from 'who's gonna win' to 'how's gonna win'."
- r/manga ([source](https://www.reddit.com/r/manga/comments/qqv3c1/i_saw_that_tomodachi_game_is_a_psychological_mind/)), [2], 2026: "in my opinion the games in AIB aren't really great unlike TG where there's a clear logical explanation of how they were beaten by the mc".
- r/writing ([source](https://www.reddit.com/r/writing/comments/1dg9mtl/does_it_ruin_the_story_if_the_readers_can_predict/)): "The reader knows main character will move from point a to point b. But you as the writer, provides the HOW."

**P2. Real calculation, not just "psychology".**
- r/manga Liar Game fan [19] ([source](https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/)): "I particularly liked how the Genius Mc isn't just relying on psychological trickery, but he also uses actual math in some cases (like calculating card placements based on a perfect shuffle)."
- AiB S2 essay ([source](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/)) misses manga moments the show cut: "the economist explaining the concept of Nash Equilibrium, the loan shark demonstrating the principle of reciprocity, and the mathematician showing the downfalls of purely rational thought in the K♢".

**P3. Layered, multi-party schemes, with two geniuses using the same high-level plan.**
- r/liargame ([source](https://www.reddit.com/r/liargame/comments/1n770i8/contraband_game_is_the_best_display_of/)).
  - On Musical Chairs: "Having not two but three teams strategyzing against each other with such layered mind games is unbelievable."
  - On the same game: "at the end of the game ir turns out the solution is just an insatisfactory cheat". The payoff still has to be fair.
  - On Contraband: "Akiyama and Yokoya both trying to successfully outplan each other using the same high-level plan, poor Akagi getting his mind played with by both... and the battle of principles taking place between Nao and Yokoya".
- r/manga ([source](https://www.reddit.com/r/manga/comments/3fjr41/liar_game_is_a_truly_horrific_manga/)): "musical chair is the best game of all game in liar game for me" [34].

**P4. Wit combined with trust: the moral spine of the genre.**
- r/manga [21] ([source](https://www.reddit.com/r/manga/comments/qqv3c1/i_saw_that_tomodachi_game_is_a_psychological_mind/)): "In most mind game stories like Kaiji and Liar Game, the protagonists win via superior wit, but also trust, friendship, and teamwork. Tomodachi Game also achieves victory via superior wit, but also backstabbing, blackmail, and fraud."
- Den of Geek on Liar Game ([source](https://denofgeek.beehiiv.com/p/the-anime-that-made-squid-game-possible), Daniel Kurland / Michael Ahr, 13 May 2026).
  - Liar Game "prioritizes psychological challenges over feats of physical strength."
  - "Deception, greed, and manipulation become the players' most valuable tools".
  - It "builds genuine emotional stakes and moving relationships instead of relying on death games alone."

**P5. Opponents and game-masters who are people with philosophies, and whose virtues can be exploited.**
- AiB S2 essay ([source](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/)): "the manga went out of its way to establish the fact that the main four Citizens... are not malicious/sadistic entities... we got to understand their reasons for designing their games the way they did."
- AiB Beauty Contest ([source](https://www.reddit.com/r/AliceInBorderland/comments/1ivbqxw/how_was_chishiya_supposed_to_win_in_beauty_contest/)), [33]: "once he figured out kuzuryu's weakness of equality in fair outcomes, and he used that against him. Kuzuryu could've easily ended Chishiya at any moment but couldn't bring himself to do it."

**P6. Real lethality.** Usogui is the benchmark cited for "oh shit he might die" ([source](https://www.reddit.com/r/manga/comments/vpnpi9/tomodachi_game_is_one_of_the_worst_manga_i_have/)).

**P7. Characters who earn information instead of "pulling insights out of their bum", and solutions that feel "unexpectedly obvious".**
- r/thepromisedneverland ([source](https://www.reddit.com/r/thepromisedneverland/comments/96w0tt/spoilerless_what_do_you_think_made_neverland_such/)).
  - [19]: characters "don't pull insights out of their bum and have to find innovative ways of obtaining new information".
  - [3]: "That sense of 'it's so obvious why didn't I think of that!?' feeling really pulled me in... the foreshadowing in TPN is something that also push me to reread the series over and over again."
  - [6]: "being smart isn't exaggerated into a superpower. Everyone solves problems in smart ways... It's like Death Note but everyone's Light."

**P8. Simple rules so the reader's attention goes to the people.**
- Squid Game director Hwang Dong-hyuk, Korea JoongAng Daily, 29 Sep 2021 ([source](https://www.koreajoongangdaily.com/entertainment/squid-game-director-talks-scripts-society-and-season-2/11690926)).
  - "The games are so simple that their rules can be explained and universally understood within 30 seconds."
  - "So it is easier for audiences to concentrate on the psychology of the characters".
- Korea Times, 30 Sep 2021 ([source](https://www.koreatimes.co.kr/amp/entertainment/shows-dramas/20210930/interview-director-shares-backstory-of-global-hit-squid-game)): "...which gives more room for them to follow the emotions of the characters who are playing the games".
- UNVERIFIED (secondary, could not open): an often-quoted Hwang line, "I wanted to go the other way — go simple — and make people wonder why the characters would put their lives at stake". It appeared only in search snippets of a Trill Mag page that returned 403.

**P9. Audiences hunt for the cooperative loophole themselves.** This is strong evidence for the author's premise.
- r/squidgame, score 159 ([source](https://www.reddit.com/r/squidgame/comments/q254pg/theory_every_game_is_winnable_with_all_players/)). Theory: "Every game is winnable with all players surviving". The OP cites the old man's "do you still trust people" and the host's "everyone has an equal chance" as hints.
- r/squidgame, score 1154 ([source](https://www.reddit.com/r/squidgame/comments/qajzl0/why_i_think_the_marble_game_was_100_survivable/)).
  - The OP: "the true reason for this game wasn't to watch contestants playing marbles, but to watch whether they pick self-preservation".
  - [436]: "it's a commentary on their conditioned beliefs and attitudes about life, believing it to be a zero sum game, when it just doesn't have to be."
- A real-world mirror from the reality show *Squid Game: The Challenge* ([source](https://www.reddit.com/r/squidgame/comments/186smuv/my_problem_with_squid_game_the_challenge/)), score 347.
  - Contestants agreed a glass-bridge pact where everyone jumps once. One contestant refused when her turn came ("I'm not gonna risk my shot"), then demanded others honour the pact for her. The top comments are fury at the hypocrisy, e.g. [12]: "Ashley didnt want to follow with the teamwork plan... and then she wanted people to follow through with the teamwork plan to save her."
  - This is exactly the "loophole broken by fear" beat, and it enraged real viewers.

**P10. The genre's appeal (what readers come for).**
- r/rational ([source](https://www.reddit.com/r/rational/comments/1ov3flv/what_are_the_best_deconstructions_of_the_death/)), [11]: "the appeal... is seeing characters pushed to and past their breaking point, and what it reveals about them. Who you are in the dark... That plus the relentless pressure to survive, forcing people to think carefully and play a smart game to keep going."
- Same thread, [16]: "Death games are a metaphors for the relations of workers to capital and the state. It's a zero sum game where the law is to kill or be killed".
- Same thread, [11]: "a lot of death game stories end with the death game blowing up in the face of whoever set it up".
- Term note, r/anime ([source](https://www.reddit.com/r/anime/comments/4un4uw/spoilers_kiznaiver_death_note_and_the_death_game/)): a commenter says the genre is registered in Japanese as "sabaibu-kei" (survival story) and names Battle Royale as the progenitor. UNVERIFIED beyond that comment.

---

## 2. How fair-play puzzles are built

### 2.1 The classic fair-play contract (detective fiction)

- **Fair play and the "Challenge to the Reader".**
  - Wikipedia's Ellery Queen article ([source](https://en.wikipedia.org/wiki/Ellery_Queen)) defines "fair play" mysteries as "a subgenre of the whodunit mystery in which the reader obtains the clues along with the detective".
  - Queen's "Challenge to the Reader" was "a single page near the end of the book" where the narrative paused and declared "they had now seen all the clues needed to solve the mystery, and only one solution was possible."
  - Julian Symons: "The rare distinction of the books is that this claim is accurate."
  - DESIGN IDEA: a manga version is a "Rules are complete. Can you find the way everyone lives?" page before the reveal chapter.
- **Ronald Knox's Decalogue** ([source](https://en.wikipedia.org/wiki/Golden_Age_of_Detective_Fiction)). The rules most relevant here:
  - (1) "The criminal must be mentioned in the early part of the story…"
  - (4) "…nor any appliance which will need a long scientific explanation at the end."
  - (6) "No accident must ever help the detective, nor must he ever have an unaccountable intuition which proves to be right."
  - (8) "The detective is bound to declare any clues which he may discover."
  - (9) The Watson's "intelligence must be slightly, but very slightly, below that of the average reader."
  - (10) Doubles "must not appear unless we have been duly prepared for them."
  - Knox's definition of the form: a mystery "whose elements are clearly presented to the reader at an early stage in the proceedings."
  - Note: rule 5 is an ethnic slur of its era. Ignore it.
- **The "Fair Play Insight" (Yudkowsky, "Level 2 Intelligent Characters")** ([source](http://yudkowsky.tumblr.com/writing/level2intelligent)).
  - "the solution the character proposes must be one that, in principle, the reader could have thought of."
  - "all the pieces of the puzzle must be present and active in the reader's mind".
  - Advice from the same page: plant the needed facts early and repeat them so the reader can follow the solution at the climax without pausing. Don't have other characters declare someone brilliant. Show the costs and failures of clever plans.
- **Sanderson's First Law, applied to game rules** ([source](https://www.brandonsanderson.com/blogs/blog/sandersons-first-law)).
  - "An author's ability to solve conflict with magic is DIRECTLY PROPORTIONAL to how well the reader understands said magic."
  - "Resist the urge to use magic to solve problems unless you've already explained and shown that aspect of how the magic works."
  - Replace "magic" with "the game's rules".

### 2.2 Planting clues

- r/writing, "Mystery writers: what are your rules?" ([source](https://www.reddit.com/r/writing/comments/1ued8b1/mystery_writers_what_are_your_rules/)).
  - [53]: "Writing mystery is basically starting with a complete picture then breaking it up and scattering the pieces."
  - [22]: "My rule is that I must be signposting the real story enough that if you read it a second time, you have to be thinking 'god, it's so obvious, how did I not see it?'"
  - [45] and [39]: heavy-handed foreshadowing toward a wrong answer, with the real answer as "a third thing that completely works with all the signposting".
  - [9]: "Every reveal has to be hinted at. If your victim was poisoned by an exotic plant found only in... Papua New Guinea, you have to mention that your killer spent some time in remote parts of the Southern Hemisphere".
  - [9] (another commenter): "I put the truth (vital clues) in the mouth of unlikeable and/or idiotic characters".
  - [13]: "Start at the end & work backwards."
- r/writing, foreshadowing without giving it away ([source](https://www.reddit.com/r/writing/comments/1kx2pe4/how_do_i_use_foreshadowing_and_red_herrings_to/)).
  - "Have pieces of foreshadowing that serve both the reader's expected story and the actual one."
  - "have your characters place no importance on it whatsoever. If it doesn't stand out, readers won't use it to form theories."
  - "Straight foreshadowing of a twist that ties into character emotions/motivations tends to get overlooked... they didn't because they were buried in emotionally impactful scenes."
  - Another commenter: "if you aren't putting enough information in the story that some readers will guess it, it is going to just feel like a cheap trick".
- **Work backwards with a dependency map.**
  - Ron Gilbert, *Grumpy Gamer*, 10 Aug 2014 ([source](https://grumpygamer.com/puzzle_dependency_charts/)): "I always work backwards when designing an adventure game." Start from the goal, ask what it requires, and chain the dependencies.
  - DESIGN IDEA: build each loophole as a chart. The goal is "all survive". Below it go the facts the reader must know, and below those, the chapter and panel where each fact is planted.
  - A commenter in the mystery-rules thread above also recommends these charts.
- **Write the twist as earned.** Same r/writing twist guide ([source](https://www.reddit.com/r/writing/comments/de7120/dos_and_donts_of_a_good_twist/)).
  - A good twist "should be possible to predict it using story clues... this is different from predicting it by knowing storytelling conventions".
  - It "should recontextualize previous scenes".
  - It "should not fill in plot holes".
  - [84]: "A twist should surprise the reader on the first run through, then be obvious on the second."
  - [29]: "1) Wow, I did not see that coming, and 2) but it makes perfect sense."

### 2.3 Reveal structure: show the wrong answers first

- **Many wrong solutions from the same clues.**
  - Wikipedia ([source](https://en.wikipedia.org/wiki/The_Poisoned_Chocolates_Case)): in *The Poisoned Chocolates Case* (Anthony Berkeley), six club members each present a different solution to the same murder.
  - Martin Edwards (2017) praised it for showing that "many equally wrong deductions can be made from a single fact."
  - Barzun and Taylor felt the extra twists "reduce tension". Don't overdo it.
- **Danganronpa trials prove the evidence is NOT the answer.**
  - r/danganronpa on trial 1-4 ([source](https://www.reddit.com/r/danganronpa/comments/14ahkod/what_is_the_best_trial_and_why/)): "your ultimate task is to piece together how that evidence is NOT the answer, while the ones that the evidence supposedly incriminates are convinced that they actually did it and are confessing".
  - The same thread praises trial 2-5 for a luck-based resolution that is acceptable because the luck "has been established and that he's been using to his advantage since chapter 1". A wild card is fair if it is planted early.
- **Level-k ladder as a staircase of wrong answers.** In AiB's beauty contest, a fan explains the king's first pick ([source](https://www.reddit.com/r/AliceInBorderland/comments/1ivbqxw/how_was_chishiya_supposed_to_win_in_beauty_contest/)). He "assumed about half the group would be thinking 2 steps ahead and the other half 3 steps ahead (either popping in 32 or 25)... he popped in 23 and got it spot on." Each naive level is a visible wrong answer.
- **Recap device.**
  - Danganronpa ends each trial with a "Closing Argument", a comic of the crime in order: "This section involves creating a manga with the correct order of events" (TheGamer, [source](https://www.thegamer.com/danganronpa-trigger-happy-havoc-chapter-one-trial-walkthrough/)).
  - DESIGN IDEA: end each game with a one- or two-page silent "replay" of the loophole, panel by panel.

### 2.4 Making the solution clear to non-math readers

- Rules a reader can absorb in about 30 seconds (Hwang, JoongAng Daily, [source](https://www.koreajoongangdaily.com/entertainment/squid-game-director-talks-scripts-society-and-season-2/11690926)). Put the complexity in the people, not the rulebook.
- Avoid the "Yeah, sure... I totally get that" effect ([source](https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/)).
- Avoid rules made "far too dense on purpose" ([source](https://www.reddit.com/r/anime/comments/z6gubd/what_are_some_fake_smart_characters_you_have/)).
- Keep explanations short. r/rational ([source](https://www.reddit.com/r/rational/comments/2m65pm/writing_level_2_intelligent_characters/)):
  - "Put a lot of your thought, by the real-world clock, into very little of their thought, by the in-story clock."
  - "Make your explanation of the character's thoughts as short as possible."
- Let an expert character explain one concept in plain words. The AiB manga used an economist for Nash equilibrium and a mathematician on the limits of pure rationality ([source](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/)).
- Make the genius fast, not encyclopaedic. r/writing, score 780 ([source](https://www.reddit.com/r/writing/comments/djfuac/how_to_write_a_character_smarter_than_you/)):
  - [686]: "any time a character quickly comes up with a solution that you took longer to construct, they are already exhibiting more intelligence on the page."
  - [41]: "brainstorm 3-5 different ways... pick the best one, then brainstorm 3-5 ways... to improve upon that decision".
  - [161]: "It's basically a magic trick: everything in the background is meticulously planned... you only let the reader see the key setpieces".
- Re-state the rules at arc and chapter openings, because serialised readers forget them ([source](https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/)).

### 2.5 Suspense vs surprise (where to put the reader's knowledge)

- Hitchcock, in Truffaut's *Hitchcock* (1967), quoted by Futility Closet ([source](https://www.futilitycloset.com/2023/12/20/hitchcocks-bomb-theory/)): "There is a distinct difference between 'suspense' and 'surprise,' and yet many pictures continually confuse the two."
- David Bordwell ([source](https://www.davidbordwell.net/blog/2013/11/29/hitchcock-lessing-and-the-bomb-under-the-table/)) quotes: "In the first case we have given the public fifteen seconds of surprise at the moment of the explosion. In the second case we have provided them with fifteen minutes of suspense."
  - Suspense needs the audience to know more than the characters, while the outcome stays uncertain.
  - Hitchcock allowed exceptions where "the unexpected ending is itself the highlight of the story."
- DESIGN IDEA: for the loophole, let the reader see (or almost see) that a cooperative way out exists before the characters agree on it. The suspense then comes from watching trust erode, a "bomb under the table" made of human fear. Keep the full mechanism (the "how") as the surprise.

### 2.6 Fair-play checklist for each game

1. Every rule that can kill is shown on the page before the game starts. No off-screen or retroactive rules (C2).
2. Rules are explainable in about 30 seconds (P8). Complexity comes from interaction between players, not from a long rulebook.
3. Define the edge cases: ties, rounding, "exact", simultaneity, what counts as "taking" or "having", the timer and the head-count arithmetic (C10).
4. The organiser is visibly bound by its rules. If it can change them, the loophole is worthless (C11).
5. Before release, try every degenerate or dominant strategy (C6). Close each one on the page, or make it the loophole.
6. Every fact the solution needs is planted at least once, ideally twice: once neutrally and once in an emotional scene (2.2). Knox 8: the protagonist hides no clue from the reader.
7. No luck saves the hero unless that luck was established long before (C3; Danganronpa 2-5).
8. Opponents are not idiots. If they miss something, give an on-page reason (C5).
9. The protagonist uses only knowledge they could have (C9). Show their trial and error at least partly (P1).
10. Show two or three wrong answers (the naive greedy play, the clever-but-wrong play) before the right one (2.3).
11. The explanation is short, visual and checkable, ending with a silent replay (2.3, 2.4).
12. Some sharp readers should be able to solve it, and most should say "it was there all along" (2.2, 1dg9mtl).
13. Do the maths yourself. Readers will (C10).

---

## 3. Game-theory and logic structures death games can borrow

Definitions and results below come from the linked pages. The "Loophole idea" lines are **DESIGN IDEAS** (my synthesis) and are not sourced claims.

### 3.1 Keynesian beauty contest / "Guess p x the average"

- **Definition.** A contest whose judges "are rewarded for selecting the most popular choices among all judges" ([Wikipedia](https://en.wikipedia.org/wiki/Keynesian_beauty_contest)). Keynes: "We have reached the third degree where we devote our intelligences to anticipating what average opinion expects..."
- **Numeric version** ([Wikipedia](https://en.wikipedia.org/wiki/Guess_2/3_of_the_average)). Players pick 0–100, and the winner is closest to 2/3 of the average.
- **Equilibrium.** The unique pure Nash equilibrium is 0, reached by iterated elimination of dominated strategies.
- **Counter-intuitive result: the "rational" answer usually loses.**
  - Nagel (1995): average first guess about 36.
  - Politiken (2005): 19,196 entrants, average 33.
  - Most people reason 0–3 levels deep, and reaching 0 takes about 21 levels.
  - Choosing 0 is only right if everyone is rational and that is common knowledge.
- **Genre use.** AiB's King of Diamonds uses 0.8 x the average ([source](https://www.reddit.com/r/AliceInBorderland/comments/1ivbqxw/how_was_chishiya_supposed_to_win_in_beauty_contest/)).
- **Loophole idea.**
  - With 0.8 x average and a rule that an exact hit is safe, the everyone-survives answer is for everyone to write 0. The target is then 0, and everyone hits it exactly.
  - Nobody profits by deviating: a lone deviator with x makes the target 0.8x/n, so the zero-pickers are closer than the deviator. The pact is self-enforcing.
  - Fear breaks it, not greed: "what if the others don't trust 0?" Distrust drags people to level-1 and level-2 numbers, and those numbers are what kill.
  - Fair-play clue to plant: someone explains "you're not guessing a number, you're guessing other people".

### 3.2 Prisoner's dilemma, one-shot and iterated

- **Definition** ([SEP](https://plato.stanford.edu/entries/prisoner-dilemma/), revised 24 Oct 2025): "whatever the other does, each is better off confessing than remaining silent", yet "the outcome obtained when both confess is worse for each than the outcome they would have obtained had both remained silent."
- **Iterated version: fixed length.** By backward induction, unconditional defection is the only subgame-perfect equilibrium of a fixed-length iterated PD. Real people behave differently "except near the end".
- **Iterated version: unknown or infinite length.**
  - With a "shadow of the future", cooperation can be an equilibrium.
  - "Since there is no last round, it is obvious that backward induction does not apply to the infinite IPD."
  - In Axelrod's tournaments Tit for Tat won. It is "nice", "retaliatory", "forgiving" and "clear".
  - With noise, imperfect TFT "will set off a long chain of moves in which the players take turns defecting". Generous TFT (forgiving about 25% of defections) does better.
- **Loophole idea.**
  - The rules hide the number of rounds, so cooperation is rational. The loophole is noticing that nobody knows when it ends.
  - The betrayal engine: one student learns, or believes they learn, which round is last, and defects. Or a single accidental "defection" (a misread signal) starts a TFT revenge spiral.
  - The fix is a generous player who forgives once, which costs them.

### 3.3 Stag hunt (assurance game): the purest form of "fear breaks the loophole"

- **Definition** ([Wikipedia](https://en.wikipedia.org/wiki/Stag_hunt)). From Rousseau: players "would be better off cooperating to achieve a more ambitious goal". Other names: assurance game, trust dilemma.
- **Equilibria.** It has two pure equilibria. One is payoff-dominant (hunt the stag together, e.g. 10/10). The other is risk-dominant (hunt hares alone, e.g. 5/5).
- **Difference from the PD.** Unlike the PD, mutual cooperation is itself stable. Nobody gains by betraying alone. The problem is coordination and trust.
- **Loophole idea.**
  - Design a game whose "everyone lives" outcome is a stable equilibrium, so no one profits from betrayal, yet the sucker's payoff for cooperating alone is death.
  - Students who never trust each other choose the safe-but-lethal-for-some hare.
  - The tragedy is that no villain is needed, only fear.

### 3.4 Volunteer's dilemma

- **Definition** ([Wikipedia](https://en.wikipedia.org/wiki/Volunteer%27s_dilemma)). Each player can "make a small sacrifice that benefits everybody". If nobody does, "the worst possible outcome is obtained for all participants."
- **Strategy.** There is no dominant strategy. With two players it has the character of Chicken.
- **Counter-intuitive result.** "an increase in N players will decrease the likelihood that at least one person volunteers."
- **Kitty Genovese caveat.** Wikipedia notes the famous 1964 bystander story was later found "to have been unfounded". Don't use it as fact.
- **Loophole idea.**
  - The rules let the volunteer's cost be split. Wikipedia mentions a cost-sharing variant (Weesie and Franzen 1998).
  - The loophole is that ten people paying one-tenth survives where one person paying the whole cost dies.
  - Larger classes make it worse, which is a good dark irony for a whole-class game.

### 3.5 Chicken (hawk–dove) and credible commitment

- **Definition and equilibria** ([Wikipedia](https://en.wikipedia.org/wiki/Chicken_(game))). The pure equilibria are "the two situations wherein one player swerves while the other does not". The symmetric equilibrium is mixed.
- **Commitment.** "reducing one's own options can be a good strategy". Example: visibly disabling your steering wheel.
- **Bertrand Russell.** He compared Chicken to nuclear brinkmanship: "it will come to be felt that loss of face is more dreadful than nuclear annihilation."
- **Loophole idea.**
  - A student wins, or saves everyone, by publicly destroying their own option to defect (handcuffs, a burned card, a sealed choice).
  - The betrayal is the fake commitment: a burned card that wasn't the real one.

### 3.6 Dollar auction, all-pay auction and war of attrition

- **Dollar auction** ([Wikipedia](https://en.wikipedia.org/wiki/Dollar_auction)). Martin Shubik, *Journal of Conflict Resolution*, 1971. The highest bidder gets the dollar, but "the second-highest bidder also pays".
  - Bidding escalates past $1 because each loser faces "paying for nothing or bidding 5 cents more".
  - The winner gets the dollar for 5 cents "only if no one else joins the bidding."
- **Real classroom figures** (IESE Insight, Hafenbrädl and Woike, 1 Dec 2018, [source](https://www.iese.edu/insight/articles/not-lose-head-bidding-war/)).
  - For a $20 bill, "end payments of $40 to $50 are not uncommon". One executive class "even reached $2,000."
  - Setting an exit limit in advance did not help once escalation began.
  - UNVERIFIED: an often-repeated "$204" Bazerman figure appeared only in a forum post.
- **All-pay auction** ([Wikipedia](https://en.wikipedia.org/wiki/All-pay_auction)). "every bidder must pay regardless of whether they win the prize". In experiments, "the seller's revenue frequently exceeds that of the value of the prize." The war of attrition is a form of it.
- **Loophole idea.**
  - The all-survive solution is that exactly one person bids the minimum and nobody else bids.
  - The rules let them collude, but each extra bidder turns a free prize into a death spiral.
  - Greed (one more bid) or fear (of being the one who paid and lost) breaks it.
  - Make the currency something lethal (minutes of air, blood, points that cost lives).

### 3.7 Pirate game (proposal-and-vote under backward induction)

- **Rules** ([Wikipedia](https://en.wikipedia.org/wiki/Pirate_game); popularised by Ian Stewart, *Scientific American*, May 1999).
  - Five ranked pirates split 100 coins. The most senior proposes, and all vote, with the proposer casting the tie-break.
  - If the vote fails, the proposer is thrown overboard.
  - Their priorities, in order: survive, then maximise coins, then prefer others die.
  - Promises outside the proposal are not binding.
- **Counter-intuitive result.** A 98, B 0, C 1, D 0, E 1. The leader buys the cheapest votes with single coins.
  - With 100 coins and more than 200 pirates, only specific pirates survive: #201, #202, #204, #208, #216, #232... (200 plus a power of 2). Runs of others die.
  - Note: Wikipedia flags this article as relying on a single source.
- **Loophole idea.**
  - The cruelty comes entirely from two assumptions: promises are not binding, and voters prefer others die.
  - Hide a rule that makes one kind of promise binding (a signed contract the organiser enforces). The coalition of zeros can then guarantee an equal split.
  - The betrayal is the senior who realises they don't need the contract.

### 3.8 Minority game / El Farol bar problem

- **El Farol** ([Wikipedia](https://en.wikipedia.org/wiki/El_Farol_Bar_problem); W. Brian Arthur, 1994).
  - People enjoy the bar if fewer than 60% go, and are worse off if more than 60% go. Decisions are simultaneous.
  - Any deterministic, symmetric strategy "is guaranteed to fail no matter what it is", because if everyone predicts empty, everyone goes.
  - A mixed strategy works better, and asymmetric pure-strategy equilibria exist.
- **Minority game** (Challet and Zhang, 1997, [arXiv adap-org/9708006](https://arxiv.org/abs/adap-org/9708006)): "N players have to choose one of the two sides independently and those on the minority side win."
- **Genre use.** Liar Game's first round is "Minority Rule", where the smallest voting group wins ([Wikipedia](https://en.wikipedia.org/wiki/Liar_Game)). Den of Geek notes it later became the premise of *Tasuketsu* ([source](https://denofgeek.beehiiv.com/p/the-anime-that-made-squid-game-possible)).
- **Loophole idea.**
  - Symmetric reasoning always fails, so the way out is asymmetry: a pre-agreed assignment (by seat number or birthday parity) that guarantees a safe minority. Then rotate it across rounds so everyone survives on aggregate.
  - The betrayal: whoever controls the assignment list controls who dies.

### 3.9 Ultimatum game

- **Rules** ([Wikipedia](https://en.wikipedia.org/wiki/Ultimatum_game); first experiments by Güth, Schmittberger and Schwarze, 1982). A proposer offers a split, and the responder accepts or both get nothing.
- **Counter-intuitive result.**
  - The subgame-perfect prediction is a minimal offer that is accepted.
  - In experiments, "offers of less than 30% are often rejected". Typical first offers are about 40% (Oosterbeek et al., 2004).
- **Loophole idea.** Spite is a weapon. A cornered student who credibly will reject (and die, taking the proposer with them) forces fairness. Combine with 3.5 commitment.

### 3.10 Hat puzzles: silence as information, and parity

- **Four prisoners** ([Wikipedia](https://en.wikipedia.org/wiki/Prisoners_and_hats_puzzle)). C's silence tells B that A and B differ, so "if C says nothing the hats on A and B must be different."
- **Ten in a line.**
  - The back prisoner announces the parity of red hats they see. They have a 50% chance, and all nine others are guaranteed.
  - "the nine other prisoners will know their own hat color after the prisoner behind them responds."
- **Loophole idea.**
  - A plan saves everyone except one person, who must volunteer for a coin flip (combine with 3.4).
  - One lie anywhere in the chain kills everyone downstream. That makes it the perfect betrayal trap: a single student's panic mis-call cascades.

### 3.11 Common knowledge (muddy children)

- **Puzzle** ([Wikipedia](https://en.wikipedia.org/wiki/Induction_puzzles)). With X muddy children, "they will step forward together on turn X". Each round of nobody stepping forward is information.
- **Counter-intuitive result.** A public announcement of something everyone already knew still changes the outcome, because it becomes common knowledge.
- **Loophole idea.** The organiser's "useless" public announcement is the key clue. The loophole is that inaction is a signal. Fair play requires that the announcement is shown verbatim.

### 3.12 The 100 prisoners problem: the best "hidden strategy that saves everyone"

- **Rules** ([Wikipedia](https://en.wikipedia.org/wiki/100_prisoners_problem); Gál and Miltersen, 2003).
  - 100 prisoners each open 50 of 100 drawers to find their own number.
  - All live only if every prisoner succeeds, and there is no communication once the first enters.
- **Counter-intuitive result.**
  - Random search succeeds with probability (1/2)^100.
  - The cycle-following strategy: open the drawer with your own number, then follow the numbers. It succeeds about 31% of the time (1 − ln 2 ≈ 30.7% in the limit).
  - If one prisoner may first inspect all the drawers and swap two contents, "all prisoners will survive."
- **Loophole idea.**
  - Students are told it's hopeless. The hidden strategy turns certain death into roughly one-in-three, and the swap insider turns it into certainty.
  - The betrayal: the one person allowed to enter first (or bribed to) holds everyone's life, and can sell it.
  - Fair-play clue: a numbered-locker or "follow the chain" motif planted chapters earlier.

### 3.13 Traveler's dilemma

- **Rules** ([Wikipedia](https://en.wikipedia.org/wiki/Traveler%27s_dilemma); Kaushik Basu, 1994). Two players claim $2–$100. The lower claim is paid to both, with a bonus to the lower claimant and a penalty to the higher.
- **Counter-intuitive result.**
  - Undercutting logic drives the equilibrium to $2.
  - In practice "most participants select a value higher than the Nash equilibrium and closer to $100", and they earn more.
  - The equilibrium predicts behaviour better when the bonus or penalty is large.
- **Loophole idea.** Make the undercut bonus small, so mutual high claims are the "everyone lives" zone. Then raise the bonus mid-game: the organiser's temptation lever.

### 3.14 Centipede game

- **Rules** ([Wikipedia](https://en.wikipedia.org/wiki/Centipede_game); Rosenthal, 1981). Two piles double with each pass, and either player can take at any time.
- **Counter-intuitive result.** The unique subgame-perfect equilibrium is to take immediately. Real subjects "regularly show partial cooperation" before defecting.
- **Loophole idea.** "Pass" builds a pot big enough to buy everyone out. Each pass is an act of trust, and greed ends it one step too early.

### 3.15 Truel (three-way duel)

- **Result** ([Wikipedia](https://en.wikipedia.org/wiki/Truel); Kilgour and Brams, *Mathematics Magazine*, 1997). "deliberate missing may be the best strategy for a duelist with lower accuracy than both opponents."
- **Loophole idea.** The weakest player survives by refusing to act, which is a great "the weak one was the smartest" reveal. Plant the accuracy facts early.

### 3.16 Public goods game (and punishment)

- **Rules** ([Wikipedia](https://en.wikipedia.org/wiki/Public_goods_game)). Secret contributions to a pot that is multiplied and shared equally.
- **Equilibrium.** Each token returns less than a token to its giver but more than a token to the group. Free-riding (contributing 0) is the equilibrium, while full contribution is the social optimum.
- **Experiments.** People "do tend to add something"; in one setting average initial contribution was "around 50%"; contributions decline over repeated rounds.
- **Punishment.** Costly punishment of non-contributors usually raises cooperation.
- **Loophole idea.** The pot is shared oxygen, food or time. Allowing punishment saves the group, but turns students into each other's executioners, which is the darker cost.

### 3.17 Focal points (Schelling points)

- **Definition** ([Wikipedia](https://en.wikipedia.org/wiki/Focal_point_(game_theory)); Thomas Schelling, *The Strategy of Conflict*, 1960). "a solution that people tend to choose by default in the absence of communication".
- **Examples.** Grand Central at noon. Heads over tails. On splitting $100, "36 out of 40 chose $50."
- **Loophole idea.** Students separated without communication must pick the same answer. The loophole is a focal point unique to their class (a shared memory, a teacher's catchphrase), planted in flashbacks. It turns backstory into a survival key and an emotional payoff.

### 3.18 Unexpected hanging paradox

- **Setup** ([Wikipedia](https://en.wikipedia.org/wiki/Unexpected_hanging_paradox)). The prisoner "proves" a surprise hanging is impossible by backward induction, and is then hanged on Wednesday, "an utter surprise to him".
- **Loophole idea.** The organiser's promise of a "surprise" elimination. A clever student's airtight proof that it can't happen is the trap. Useful as a wrong-answer beat (2.3).

### 3.19 Genre precedent: game shows

- Korea's *The Genius* has 13 contestants, Main and Death Matches, and garnet currency ([Wikipedia](https://en.wikipedia.org/wiki/The_Genius_(TV_series))).
- It was accused of copying *Kaiji* ("1.2.3 Game") and *Liar Game* ("Zombie Game"). The producer said the show was a "reference, but not copied."
- Useful as evidence that the Liar Game / Kaiji template transfers to real players.

---

## 4. Story craft: mystery, character drama and mind-play around the games

### 4a. How the well-regarded series weave mystery and drama around the games

**Squid Game: a mastermind hidden in plain sight, misdirected by the most emotional episode.**
- Fans list the planted clues ([source](https://www.reddit.com/r/squidgame/comments/pvp8cm/spoiler_foreshadowing/); [source](https://www.reddit.com/r/squidgame/comments/r9ih6u/almost_predicted_the_twist_until/)):
  - "We never saw him get killed - why was he the only person we didn't see die?! EVERY ONE ELSE GOT A GRUESOME MURDER".
  - "the policeman is looking through the files... it starts from player 002".
  - His "pleading being the catalyst for the staff to step in" during the riot.
  - "the old man slightly moved after red light was said but didn't get shot".
  - Asked about the brilliant Sang-woo, he replied "oh so he must be a really good person right?"
- The misdirection was the marbles episode.
  - [47] in the second thread: "I was convinced that he was just meant to be a face for all the lonely old people... that twist was a genuine slap in the face after I bawled during the marble episode".
  - [24]: "I thought 'there's no way he's committed enough to endure this kind of public humiliation just for an act'".
  - Lesson: hide the mastermind inside the reader's pity.
- Trade-off. Some viewers guessed early and felt it "ruined the pay off" ([pvp8cm](https://www.reddit.com/r/squidgame/comments/pvp8cm/spoiler_foreshadowing/)).
  - One ([16]): "Too many hints - they must have expected the audience to realize soon."
  - Another ([2]): "This show is a real hindsight is 20/20 though."
  - Calibrate the number of clues.
- Thematic hints to cooperation. "gganbu", and "do you still trust people", cited in the all-survive theory ([source](https://www.reddit.com/r/squidgame/comments/q254pg/theory_every_game_is_winnable_with_all_players/)).
  - The final bet over the drunk man reframes the whole game as a test of human nature. A commenter [211]: "the simplest way to have won would have been to simply get on the elevator and walk over and BE the one who helps".

**Tomodachi Game: the traitor inside the friend group.**
- Fans dig up foreshadowing: a knowing reaction from another character, an implausible kidnapping that only makes sense if the victim staged it ([source](https://www.reddit.com/r/TomodachiGame/comments/1at6bp3/minor_foreshadowing_about_the_traitor_reveal/)).
- They also note the risk:
  - "alot of people say that the Kokorogi reveal was just too sudden and had no buildup".
  - One reader's tell: "out of all the characters she was painted as 'the most innocent.' just screamed she'd probably be at least be revealed as a bitch in sheep's clothing".
- Lesson: the "most innocent" ally is now a cliché that genre readers suspect first. Use it as a red herring, or give the real traitor a better cover.

**Danganronpa: evidence that misleads, confessions made out of love, murders that carry the theme.**
- Trial 1-4: the accused "are convinced that they actually did it and are confessing", and the player must disprove even a friend's false confession ([source](https://www.reddit.com/r/danganronpa/comments/14ahkod/what_is_the_best_trial_and_why/)).
- V3: each murder explores a different "fiction" (entertainment, religion, virtual worlds) that converges on the final reveal ([source](https://www.reddit.com/r/danganronpa/comments/1vzggqr/v3s_true_themes_and_how_the_murders_tied_together/)).
- V3's meta ending ("the V not standing for version was such a mindfuck") is divisive. Fans still argue its meaning ([source](https://www.reddit.com/r/danganronpa/comments/1u0scmo/i_just_beat_danganronpa_v3_and_it_left_me/)).
- Hiding a protagonist's own actions in dialogue (trial 3-1) is praised as "mindblowing" ([source](https://www.reddit.com/r/danganronpa/comments/14ahkod/what_is_the_best_trial_and_why/)).

**Death Note: planted false rules, and deliberate ambiguity.**
- Light has a fake 13-day rule written into the notebook, so L "has no way of proving that some of the rules are fakes" ([source](https://www.reddit.com/r/deathnote/comments/16xxt81/this_anime_lost_me_because_it_suddenly_decided_to/)).
- DESIGN IDEA: an organiser or a player can plant false rules, but the reader must be able to suspect it (fair play: the rule's provenance is shown).
- On Near's win, the thread's OP reports that author Ohba said he "wants the reader to decide for themselves". UNVERIFIED primary source ([source](https://www.reddit.com/r/deathnote/comments/1kd5lvu/why_i_firmly_believe_matsudas_theory_that_near/)).

**Alice in Borderland (manga): game-masters and bit players as full humans.**
- Citizens get philosophies and reasons for their game designs. Minor players get expertise and arcs. Dead friends return as apparitions at Arisu's low points ([source](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/)).
- The same essay faults the adaptation for an opponent acting against his own stated philosophy. The manga K♠ "would never try to beat/stab a player to death because it puts them through too much suffering - which is *exactly* what he'd designed his game to spare them from".
- Lesson: an opponent's game design should express their philosophy, and their behaviour must stay consistent with it.

**Liar Game: emotional reveals about other players, and character-driven games.**
- "I literally cried just like Nao when she found what happened to Fukunaga". Human Auction is praised because "It's such a great exploration of character for all of the mains" ([source](https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/)).

**Kaiji: betrayal with arithmetic behind it, and dread from unknown penalties.**
- Restricted Rock-Paper-Scissors. A reader summarises Ando's pitch to turn Furuhata against Kaiji: "if they save Kaiji they'll still be stuck with mountains of debt" ([source](https://www.reddit.com/r/kaiji/comments/1vq493i/why_were_contestants_so_desperate_to_buy_stars_in/)).
- On the penalty: "No one told any of the contestants the results of a loss... By the work of player's mind, you can pretty much come up with every other possible resolution what could await you".
- DESIGN IDEA: an undisclosed penalty is fair dread (the rules state that the penalty is unknown). An undisclosed rule is not.

**The Promised Neverland: chapter-one bombshell, planning, and allies who push back.**
- r/thepromisedneverland ([source](https://www.reddit.com/r/thepromisedneverland/comments/96w0tt/spoilerless_what_do_you_think_made_neverland_such/)):
  - "Gripping 1st chapter. It had three major reveals at the end. A story planned out in advance."
  - "revealed enough about the world to get us thinking but not so much as to give everything away."
- First arc called "a masterpiece", with a wish the authors had "took their time after goldy pond and thought the story out instead of sticking to the weekly schedule" ([source](https://www.reddit.com/r/thepromisedneverland/comments/1s72syo/manga_the_jailbreak_arc_is_still_one_of_the_best/)).
- Critique ([source](https://www.reddit.com/r/thepromisedneverland/comments/1uablkr/manga_my_critique_of_the_tpn_manga/)).
  - "Everyone becomes a yes man/woman to Emma. The fun part of TPN in it's earlier days was the other orphans while having the same goal as Emma doesn't always do what she wants". Allies who disagree keep tension alive.
  - A villain surviving "feels like an asspull because there was no foreshadowing". A reply argues it was foreshadowed: lineage, flashbacks, a flinch. Fans adjudicate on evidence.
- Kaiu Shirai, VIZ interview, published 21 Jul 2021 ([source](https://www.viz.com/blog/posts/the-promised-neverland-writer-interview)): "We wanted a create a big difference between the 'gentleness' that the title may imply" and the story. He also says "I didn't want to push my ideas onto the reader either."
- DESIGN IDEA: "Dead Man's Algorithm" can likewise set up a contrast, a clean-sounding term hiding a brutal meaning.

### 4b. What makes a death or betrayal land, and what makes it cheap

**Lands:**
- The character was loved before they died, and the death changes the living. r/writing ([source](https://www.reddit.com/r/writing/comments/17gf0ae/how_do_you_make_a_sudden_character_death/)):
  - [32]: "How does the death affect those who still live? Answer that, and the death will be meaningful."
  - [14]: "you need to come up with something this character does beforehand that makes us really like that character".
  - [3]: "There should be a plot-relevant reason for them to die (so not mere shock value)".
  - [3] (another commenter): "introduce the reader to a strong desire the doomed character has. When they die, you emphasize that they had unfulfilled dreams".
  - [6]: a death can also matter mechanically. The group loses a skill or option they needed.
- Set up the death, and it still hits. The most-discussed Squid Game S3 death, score 4350 ([source](https://www.reddit.com/r/squidgame/comments/1lqe0u3/this_had_to_be_most_shocking_death_of_the_series/)).
  - It was foreshadowed by her own earlier line "about not knowing what to do with her son wasn't alive".
  - Readers: "149 and 007's demise was expected but still hit so hard"; "the only death that had me gasp".
  - A forced choice between loved ones ("her having to kill 007") was "devastating".
- The betrayal's *why* matters more than the *what*. r/writing ([source](https://www.reddit.com/r/writing/comments/1dg9mtl/does_it_ruin_the_story_if_the_readers_can_predict/)), on The Matrix: "a character betrays the other heroes which isn't a very remarkable twist all on its own. But his reasons for doing so were interesting".
  - Same thread: "if *everyone* predicts it" is the problem, and "The plot twist should never be the point itself. It needs to lead somewhere."
- Betrayal by fear plus hypocrisy provokes visceral anger in real audiences. See *Squid Game: The Challenge* in P9 ([source](https://www.reddit.com/r/squidgame/comments/186smuv/my_problem_with_squid_game_the_challenge/)).
- Deaths of the genre-savvy kind ("killing" a character's strongest trait rather than their body): "Game of Thrones did really well was 'killing' the strongest parts of a character. Think Jaime's sword hand" ([source](https://www.reddit.com/r/writing/comments/8s0vfa/been_seeing_a_lot_of_this_deathforthesakeofdeath/)).

**Cheap:**
- Death for its own sake, or deaths so constant that nobody is worth caring about. Same thread: "TWD taught me to not care about any characters because they'll be killed off. Unlike GOT which taught me to care about characters because we might lose them at any second."
- Disposable extras ([source](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/)).
  - "There was nothing to make the audience to feel for their sudden deaths".
  - Stock extras "a timid/cowardly/helpless player, a macho/athletic player, and a dumb/naive player".
- A sudden change of heart without groundwork, AiB S3 ([source](https://www.reddit.com/r/AliceInBorderland/comments/1nr83tb/season_three_felt_like_a_huge_middle_finger_to/)): "There's no reason to that just from seeing Arisu saving Usagi, to completely change his heart. It's too sudden, too late."
- A personality that flips to suit the scene. Tomodachi ([source](https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/)): "has a nasty habit of switching between an 'innocent basic soy boy' to 'psychopathic nut job'".
- A dead character who returns without foreshadowing reads as an "asspull" (TPN critique above). Fake deaths need planted doubt; Squid Game's unseen body is the model.

### 4c. Slow-burn mystery: planting the conspiracy without revealing it

- **"Golden goose" vs "mystery box"** ([source](https://www.reddit.com/r/writing/comments/18d62v7/the_difference_between_a_golden_goose_and_a/)).
  - The OP contrasts David Lynch's "golden goose" with the Lost-style "mystery box". Lynch: a central mystery that keeps laying smaller mysteries which "progress the main plot and characters". Mystery box: titillation, "each answer must create two questions".
  - The OP quotes Lynch: "I want things to feel solved up to a point, but there's got to be a certain percentage left over".
  - The OP quotes Abrams: "mystery is the catalyst for imagination". UNVERIFIED in primary: the TED transcript did not load.
  - Commenters warn the mystery box "works like a financial pyramid, but with plot... the longer you do it, the less able will you be to finish your story in a way that satisfies the viewer".
  - Commenters split being "vague" (author doesn't know) from being "ambiguous" (author knows and withholds deliberately).
  - DESIGN IDEA: know the full answer to the conspiracy (who runs the games and why "Algorithm") before chapter 1. Each game should answer one small question while making the big question sharper, not just adding new questions.
- **Twist hygiene.** A good twist "should explain a mystery or mysteries that have been prevalent throughout the book", and must not make previous scenes "no longer make sense" ([source](https://www.reddit.com/r/writing/comments/de7120/dos_and_donts_of_a_good_twist/)). From the same thread:
  - [49]: "have the characters think about it to a realistic degree. If a character doesn't acknowledge how strange it was... the reader will assume you just gave them plot armour."
  - Make mysteries visible *as* mysteries, so readers don't file them as plot holes.
- **Dramatic irony and suspense.** Hitchcock and Bordwell (2.5). Let the reader hold a fact the characters lack: a planted false rule, an ally's secret.
- **Protagonist or ally secrets.** r/writing ([source](https://www.reddit.com/r/writing/comments/18ve4r5/how_do_you_write_protagonists_who_have_something/)):
  - Vague narration: "It reminded him of what happened in the church fire. He shook his head to push the thoughts away."
  - "Let the reader realise themselves that the character could've acted differently at some critical time but didn't." (lies of omission)
  - Others around the narrator "act suspiciously" because they know.
  - The Murder of Roger Ackroyd as the extreme case.
  - Knox rule 9 sets the limit: the Watson must not conceal thoughts.
- **Cliffhangers.** r/writing ([source](https://www.reddit.com/r/writing/comments/1u8cmkm/self_contained_chapters_vs_cliffhanger_chapters/)).
  - "Occasional cliffhangers may be more effective than consistent cliffhangers."
  - The "Yes, but / No, and" method: "Did you solve the problem or conflict? End the chapter with either yes, but there's a complication or no, and there's an escalation."
  - Early chapters need harder hooks. Middle chapters can use backstory once readers are invested.
- **Let some readers guess.**
  - "The best twists will manage to surprise most readers. Chances are, if you want a twist to surprise *all* readers, they're going to be surprised because it came out of nowhere" ([source](https://www.reddit.com/r/writing/comments/1dg9mtl/does_it_ruin_the_story_if_the_readers_can_predict/)).
  - Online communities crack twists fast. In the foreshadowing thread, a commenter notes Reddit "figured out R+L=J immediately" ([source](https://www.reddit.com/r/writing/comments/1kx2pe4/how_do_i_use_foreshadowing_and_red_herrings_to/)).
- **Keep the theme visible.**
  - Liar Game's ending is re-appraised years later; the reader is "extremely grateful for the themes carrying through strong from beginning to end" ([source](https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/)).
  - That reader prefers a meaningful ending to a "the cycle repeats" horror ending, which "would have left no impact, because we wouldn't have actually gotten anywhere".

### 4d. Story-craft checklist (synthesis)

1. Hide the mastermind or traitor inside the reader's sympathy (Squid Game), and plant three or four concrete, checkable clues: unseen body, missing record, an odd exemption.
2. Calibrate so a minority of readers can guess (4c).
3. Every game should raise the larger mystery by answering one small question. Know the final answer now (golden goose).
4. Each opponent or game-master has a philosophy that their game expresses, and they act consistently with it (AiB).
5. Allies should disagree and act on their own (TPN's early arc). "Yes-men" kill tension.
6. Before a death: a want, a bond, and a line that foreshadows it. After: show what it costs the living, emotionally and in options.
7. Betrayals need a legible motive, ideally arithmetic plus fear (Kaiji) or a hypocrisy readers can feel (*The Challenge*). Make the *why* the payoff, not just the *who*.
8. Flashbacks should recontextualise a choice the reader already saw. Don't let a flashback introduce the solution (C1).
9. A false rule or false death is allowed only with fair suspicion planted (Death Note, Squid Game).
10. Use occasional hard cliffhangers, and "yes, but / no, and" endings elsewhere.

---

## 5. Source index (all opened during this research)

**Reddit (official API)**
- r/manga: [vpnpi9](https://www.reddit.com/r/manga/comments/vpnpi9/tomodachi_game_is_one_of_the_worst_manga_i_have/), [362a4k](https://www.reddit.com/r/manga/comments/362a4k/you_really_want_to_tell_me_liar_game_is_good/), [3fjr41](https://www.reddit.com/r/manga/comments/3fjr41/liar_game_is_a_truly_horrific_manga/), [wh5dht](https://www.reddit.com/r/manga/comments/wh5dht/whats_your_opinion_about_liar_game/), [34tnb0](https://www.reddit.com/r/manga/comments/34tnb0/is_liar_game_that_good/), [qqv3c1](https://www.reddit.com/r/manga/comments/qqv3c1/i_saw_that_tomodachi_game_is_a_psychological_mind/)
- r/anime: [z6gubd](https://www.reddit.com/r/anime/comments/z6gubd/what_are_some_fake_smart_characters_you_have/), [4un4uw](https://www.reddit.com/r/anime/comments/4un4uw/spoilers_kiznaiver_death_note_and_the_death_game/)
- r/AliceInBorderland: [1nr83tb](https://www.reddit.com/r/AliceInBorderland/comments/1nr83tb/season_three_felt_like_a_huge_middle_finger_to/), [1ivbqxw](https://www.reddit.com/r/AliceInBorderland/comments/1ivbqxw/how_was_chishiya_supposed_to_win_in_beauty_contest/), [1mth6tx](https://www.reddit.com/r/AliceInBorderland/comments/1mth6tx/power_of_66_67_and_0_in_the_king_of_diamonds_game/), [zys8ut](https://www.reddit.com/r/AliceInBorderland/comments/zys8ut/as_a_longtime_fan_of_the_manga_here_is_my_biggest/), [1qkesjf](https://www.reddit.com/r/AliceInBorderland/comments/1qkesjf/manga_felt_way_more_thriling_than_the_live_action/)
- r/squidgame: [q254pg](https://www.reddit.com/r/squidgame/comments/q254pg/theory_every_game_is_winnable_with_all_players/), [qajzl0](https://www.reddit.com/r/squidgame/comments/qajzl0/why_i_think_the_marble_game_was_100_survivable/), [1p5vrfd](https://www.reddit.com/r/squidgame/comments/1p5vrfd/i_really_hate_how_the_glass_bridge_blows_up/), [186smuv](https://www.reddit.com/r/squidgame/comments/186smuv/my_problem_with_squid_game_the_challenge/), [1lqe0u3](https://www.reddit.com/r/squidgame/comments/1lqe0u3/this_had_to_be_most_shocking_death_of_the_series/), [pvp8cm](https://www.reddit.com/r/squidgame/comments/pvp8cm/spoiler_foreshadowing/), [r9ih6u](https://www.reddit.com/r/squidgame/comments/r9ih6u/almost_predicted_the_twist_until/)
- r/liargame: [1n770i8](https://www.reddit.com/r/liargame/comments/1n770i8/contraband_game_is_the_best_display_of/), [1tkyon1](https://www.reddit.com/r/liargame/comments/1tkyon1/reevaluating_the_ending_10_years_later/), [1v4empy](https://www.reddit.com/r/liargame/comments/1v4empy/just_confused_on_akiyamas_logic/) (a reader alleges a plot hole mid-arc and others rebut it, showing readers audit logic live)
- r/TomodachiGame: [11ah4vq](https://www.reddit.com/r/TomodachiGame/comments/11ah4vq/the_one_thing_i_dislike_about_yuuichis/), [1at6bp3](https://www.reddit.com/r/TomodachiGame/comments/1at6bp3/minor_foreshadowing_about_the_traitor_reveal/)
- r/Usogui: [1ujkitm](https://www.reddit.com/r/Usogui/comments/1ujkitm/did_fraudcent_lalo_really_watch_baku_tap_the/)
- r/kaiji: [1vq493i](https://www.reddit.com/r/kaiji/comments/1vq493i/why_were_contestants_so_desperate_to_buy_stars_in/)
- r/deathnote: [16xxt81](https://www.reddit.com/r/deathnote/comments/16xxt81/this_anime_lost_me_because_it_suddenly_decided_to/), [1kd5lvu](https://www.reddit.com/r/deathnote/comments/1kd5lvu/why_i_firmly_believe_matsudas_theory_that_near/)
- r/danganronpa: [14ahkod](https://www.reddit.com/r/danganronpa/comments/14ahkod/what_is_the_best_trial_and_why/), [1vzggqr](https://www.reddit.com/r/danganronpa/comments/1vzggqr/v3s_true_themes_and_how_the_murders_tied_together/), [1u0scmo](https://www.reddit.com/r/danganronpa/comments/1u0scmo/i_just_beat_danganronpa_v3_and_it_left_me/)
- r/thepromisedneverland: [96w0tt](https://www.reddit.com/r/thepromisedneverland/comments/96w0tt/spoilerless_what_do_you_think_made_neverland_such/), [1s72syo](https://www.reddit.com/r/thepromisedneverland/comments/1s72syo/manga_the_jailbreak_arc_is_still_one_of_the_best/), [1uablkr](https://www.reddit.com/r/thepromisedneverland/comments/1uablkr/manga_my_critique_of_the_tpn_manga/)
- r/writing: [de7120](https://www.reddit.com/r/writing/comments/de7120/dos_and_donts_of_a_good_twist/), [djfuac](https://www.reddit.com/r/writing/comments/djfuac/how_to_write_a_character_smarter_than_you/), [1ued8b1](https://www.reddit.com/r/writing/comments/1ued8b1/mystery_writers_what_are_your_rules/), [1kx2pe4](https://www.reddit.com/r/writing/comments/1kx2pe4/how_do_i_use_foreshadowing_and_red_herrings_to/), [17gf0ae](https://www.reddit.com/r/writing/comments/17gf0ae/how_do_you_make_a_sudden_character_death/), [8s0vfa](https://www.reddit.com/r/writing/comments/8s0vfa/been_seeing_a_lot_of_this_deathforthesakeofdeath/), [1dg9mtl](https://www.reddit.com/r/writing/comments/1dg9mtl/does_it_ruin_the_story_if_the_readers_can_predict/), [18d62v7](https://www.reddit.com/r/writing/comments/18d62v7/the_difference_between_a_golden_goose_and_a/), [1u8cmkm](https://www.reddit.com/r/writing/comments/1u8cmkm/self_contained_chapters_vs_cliffhanger_chapters/), [18ve4r5](https://www.reddit.com/r/writing/comments/18ve4r5/how_do_you_write_protagonists_who_have_something/)
- r/rational: [4pfpt0](https://www.reddit.com/r/rational/comments/4pfpt0/d_an_example_of_a_story_with_lots_of_exposition/), [2m65pm](https://www.reddit.com/r/rational/comments/2m65pm/writing_level_2_intelligent_characters/), [1ov3flv](https://www.reddit.com/r/rational/comments/1ov3flv/what_are_the_best_deconstructions_of_the_death/)

**Web: craft and genre**
- Yudkowsky, Level 2 Intelligent Characters: http://yudkowsky.tumblr.com/writing/level2intelligent
- Sanderson's First Law: https://www.brandonsanderson.com/blogs/blog/sandersons-first-law
- Golden Age of Detective Fiction (Knox's Decalogue): https://en.wikipedia.org/wiki/Golden_Age_of_Detective_Fiction
- Ellery Queen (Challenge to the Reader): https://en.wikipedia.org/wiki/Ellery_Queen
- The Poisoned Chocolates Case: https://en.wikipedia.org/wiki/The_Poisoned_Chocolates_Case
- Ron Gilbert, Puzzle Dependency Charts: https://grumpygamer.com/puzzle_dependency_charts/
- Futility Closet, Hitchcock's bomb theory: https://www.futilitycloset.com/2023/12/20/hitchcocks-bomb-theory/
- David Bordwell, Hitchcock, Lessing and the bomb under the table: https://www.davidbordwell.net/blog/2013/11/29/hitchcock-lessing-and-the-bomb-under-the-table/
- Korea JoongAng Daily (Hwang Dong-hyuk), 29 Sep 2021: https://www.koreajoongangdaily.com/entertainment/squid-game-director-talks-scripts-society-and-season-2/11690926
- Korea Times (Hwang Dong-hyuk), 30 Sep 2021: https://www.koreatimes.co.kr/amp/entertainment/shows-dramas/20210930/interview-director-shares-backstory-of-global-hit-squid-game
- Den of Geek newsletter (Liar Game): https://denofgeek.beehiiv.com/p/the-anime-that-made-squid-game-possible
- Liar Game: https://en.wikipedia.org/wiki/Liar_Game
- The Genius (TV series): https://en.wikipedia.org/wiki/The_Genius_(TV_series)
- VIZ, Kaiu Shirai interview: https://www.viz.com/blog/posts/the-promised-neverland-writer-interview
- TheGamer, Danganronpa trial 1 walkthrough (Closing Argument): https://www.thegamer.com/danganronpa-trigger-happy-havoc-chapter-one-trial-walkthrough/
- IESE Insight, bidding wars: https://www.iese.edu/insight/articles/not-lose-head-bidding-war/

**Web: game theory**
- Keynesian beauty contest: https://en.wikipedia.org/wiki/Keynesian_beauty_contest
- Guess 2/3 of the average: https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
- Prisoner's dilemma (SEP): https://plato.stanford.edu/entries/prisoner-dilemma/
- Stag hunt: https://en.wikipedia.org/wiki/Stag_hunt
- Volunteer's dilemma: https://en.wikipedia.org/wiki/Volunteer%27s_dilemma
- Chicken: https://en.wikipedia.org/wiki/Chicken_(game)
- Dollar auction: https://en.wikipedia.org/wiki/Dollar_auction
- All-pay auction: https://en.wikipedia.org/wiki/All-pay_auction
- Pirate game: https://en.wikipedia.org/wiki/Pirate_game
- El Farol Bar problem: https://en.wikipedia.org/wiki/El_Farol_Bar_problem
- Minority game (arXiv): https://arxiv.org/abs/adap-org/9708006
- Ultimatum game: https://en.wikipedia.org/wiki/Ultimatum_game
- Prisoners and hats puzzle: https://en.wikipedia.org/wiki/Prisoners_and_hats_puzzle
- Induction puzzles: https://en.wikipedia.org/wiki/Induction_puzzles
- 100 prisoners problem: https://en.wikipedia.org/wiki/100_prisoners_problem
- Traveler's dilemma: https://en.wikipedia.org/wiki/Traveler%27s_dilemma
- Centipede game: https://en.wikipedia.org/wiki/Centipede_game
- Truel: https://en.wikipedia.org/wiki/Truel
- Public goods game: https://en.wikipedia.org/wiki/Public_goods_game
- Focal point: https://en.wikipedia.org/wiki/Focal_point_(game_theory)
- Unexpected hanging paradox: https://en.wikipedia.org/wiki/Unexpected_hanging_paradox
