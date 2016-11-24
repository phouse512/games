---
layout: post
title: "Mew2King's Performance at Smash Summit 3"
date: 2016-11-19 18:00:00 -0600
categories: smash-summit m2k
permalink: /m2k-smash-summit-3/
---

I've watched a bit of smash, and I've always been a little curious about stats
are tracked for the game. [tafostats][tafo] is very helpful, but unfortunately
as far as I could tell, there isn't much more detail about specific in-game
statistics. Here is a little experiment that I'm trying with annotating games
to see what kind of interesting numbers could be found from SSBM tournaments.

This first post follows Mew2King's performance at Smash Summit 3 from this past
year. Because this first dataset is so small, this post *won't* try to draw any
concrete conclusions or trends from Jason's playing style. It's simply
a presentation of some numbers I found interesting from his games at the
tournament.

Before we dive in, a little about the stats that are tracked. It was all centered
around kills/deaths, and I tried to only record things that are not subjective.
For example, for each death I recorded stats like the attacker/defender's
percentage, what part of the stage did they die on (left, top, right), the move
used, and a couple others. I also recorded the timestamp for each death for
further analysis.

### Overview

Before we get into some of the smaller details, let's go through some of the
high level stats from the tournament. In total, M2K played in 5 rounds, for
a total of 20 matches. He went 3-2 overall, and went 10-10 in his sets.
Figure 1 below is a table that represents his individual character vs.
character set records, as well as the average game time for each matchup.

[figure 1][image here]

As you can see, M2K's best record is as Marth when playing against Fox, but
this is also when he 3-0'd Leffen in Winner's Quarterfinal. Unfortunately
here, most of the win-loss records are representative of specific rounds in the
tournament, versus single players. You can see the Marth-Peach matchup versus
Armada, the Fox-Jigglypuff from Losers' Finals with Hbox, and the 5-set match
with S2J (Sheik-Captain Falcon). In time as I catalogue and annotate more
tournaments, I hope to be able to show large collections of pro character
matchups.

The one interesting thing to note here is related to the average time per game.
For the most part, the quick games make sense. Marth-Fox and Marth-Falco are
both heavy damage hitters and can kill quickly. The sole long game with
Marth-Peach also makes sense. Surprisingly, the Fox-Jigglypuff matchup was the
third-fastest, coming in at 3:39.33. From what I've seen, Hbox's Jigglypuff
matches sometimes take quite a while, but I'm attributing this to M2K pulling
out Fox, a character he doesn't play as much.

[figure 2][basic kill analysis]

Figure 2 is a breakdown of all of M2K's kills throughout the tournament,
grouped by each character. Mew2King uses a variety of methods to kill his
opponents, but there is a clear gap between Marth's best attacks and the other
methods he uses. The only edgeguards[^1] with his Marth came from his off-stage
forward air combos. The highest average defender % came from up-throws into
oblivion, while the lowest non-SD kill came from the forward airs. As a note,
I am not tracking combos or anything related because of the subjectivity, these
are just the last-hits.

M2K's Sheik stuck to the basics and used aerials for 92.67% of his kills. His
Fox had even less variety against Jigglypuff and of the 8 kills, half of them
were up smashes.

### Specific Stats

Now that we've got some of the basic overview stats out of the way, let's look
into some more specific analysis of M2K's play.

#### Gimp Kills

One of the first things I wanted to check was the number of times that M2K was
gimped and the number of times he gimped others. The criteria for a gimp kill
here is not too specific, the player getting killed must have less than
50 percent damage at the time of death. In total, M2K's Marth got 3 gimps in
the tournament, 2 of them with his forward airs, and one with a forward tilt.
Surprisingly here, none of them came from down air punishes.

He got gimped 3 times as well, one of them coming from a shine spike and
another one from an early rest from Hbox. The lowest percentage M2K died at was
15 percent, when he got hit by a forward air from Jigglypuff near the bottom of
Final Destination.

#### Comebacks

Next, let's look at how Mew2King performs when he goes down by a stock or more.
This was a little bit tougher to analyze and breakdown, simply because the
stock count at any given time in a match is not a true indicator. Let's say
a match starts 4-4, and one player kills the other, but not before her
character takes 85% damage. If you look only at the stock count, it would look
like she has the lead but you miss out on all the work the second player did
to bring her percent up to 85%. There are also other intangibles such as momentum
that can't be tracked with the statistics I've gathered. 

For the purpose of this analysis, we'll look at occurrences when the stock
count goes to 4-3, 3-2, 2-1 and the other player has less than 50%. This
analysis also does not include the inverse, when Mew2King goes up by a stock
against his opponent.

In this tournament, there were 11 total situations where M2K went down
by 1 stock and his opponent had less than 50%. These 11 moments happened across
7 total sets, so in 2 sets, M2K went down 4-3, tied it, then went down 3-2,
and tied it one more time at 2-2 before going down 2-1. Of these 7 matches, his
win percentage is __28.57%__, which is not too surprising. For those two times that
he was able to pull off the win, the first time[^2] he went down by a stock was on the 4-4
even stock. If the first time he went down by a stock was at a count of __3-3 or
2-2__, Mew2King was *not* able to comeback and pull out the win.

In both of those sets where he went down by a stock multiple times, his win
percentage was 50%, so nothing indicative. As I collect more data, I'm curious
to find out whether or not that number will change.

### What's Next

If you've made it this far.

***

[^1]: here, edgeguards are defined as times when the opponent is close enough to grab the stage edge, but the attacking player keeps or rolls up off the edge to keep the opponent from grabbing the edge in reach. Edgeguarding in this post does not refer to attacking moves used on the edge to damage and push the opponent away.

[^2]: first time as in blah
