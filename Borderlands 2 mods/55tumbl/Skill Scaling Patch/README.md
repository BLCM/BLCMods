*All files and content provided here were written by me (55tumbl), unless stated otherwise. They are free for personal use. You may use these mods in videos, or for streaming, as long as you give proper credit and let me know about it. You may re-use small bits of code (e.g. formulas, etc) for your own purposes as long as you give proper credit and let me know about it. Ask permission if you wish to use larger portions, make a modified/improved version, include it in a mod pack, etc. Do not re-upload any of those files anywhere.*

# Overview

The Skill Scaling Patch fixes a number of bugs or inconsistencies about the way skills scale with level, and across playthroughs. It is not meant to "fix" the balance of the game according to my personnal preferences, but merely to make it work as was (most probably) intended. It does clearly improve some aspects of the balance, though. The skills that are the most affected are Ruin (Maya), Light the Fuse (Krieg), Deathtrap and all its damage abilities (Gaige), the Sabre Turret and all its damage abilities (Axton).

Concerning Deathtrap and the Sabre Turret, the main problem addressed by this patch was actually not present on console. With the Skill Scaling Patch, their damage output should thus be identical (or close) to what it is on console. And that makes a huge difference on their end-game viability.

# Compatibility

The Skill Scaling Patch can be used as a standalone, for a vanilla experience with less bugs, and to meet Deathtrap and the Sabre Turret the way they were supposed to be (and actually are, on console).

The Skill Scaling Patch is included in the Unofficial Community Patch, as of version 4.1.

You can also try to merge it with other mods, using [BLCMM](https://www.youtube.com/watch?v=VkRgUqru3oU&t=27s). However, this may create serious incompatibilities if the other mods affect the skills modified by the Skill Scaling Patch, or even skills in general. I'd recommend adding the Skill Scaling Patch after other mods, and disabling any changes affecting the mentioned skills, in those other mods. 

# Detailed changes

You can find [here](http://blstats.com/skilldamage.php) all the damage values at different levels/playthroughs, on console and on PC/mac (with or without the Skill Scaling Patch).

## Maya

**Ruin (elemental explosions and DOTs)**: made to scale like other skills and removed the level 72 cap.    
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +590% at OP8.    
* This also affects the Burn and Corrode DOTs that can be caused by Blight Phoenix (but not the main Blight Phoenix damage). 
* This also affects the Corrode DOT that can be caused by Cloud Kill (but not the main Cloud Kill damage). Since the DOT is very small, this has practically no effect on the overall Cloud Kill damage (about +1.5% at OP8). 

**Phaselock (damage on non-phaselockable targets)**: made to scale like other skills.   
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +160% at OP8

**Scorn**: made to scale like other skills.   
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +160% at OP8

## Krieg

**Light the Fuse**: removed the level 72 cap.
* No effect on damage up to level 72. Damage increased by +183% at OP8.

**Krieg's innate melee damage bonus (without blade attachment)**: removed the level 72 cap.
* No effect on damage up to level 72. Base melee damage increased by +6.6% at OP8.

## Zer0
**Unf0rseen (electrocute DOT)**: made to scale like other skills and removed the level 72 cap.    
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +590% at OP8.
* This is minor, since it does not affect the main damage from Unf0rseen (if the target is electrocuted, the increased DOT would give about +5% overall Unf0rseen damage at OP8).

## Gaige
**Deathtrap**: Made its damage scale the way it was supposed to (and actually does, on console)
* This affects the base melee damage, and the damage from its skills (Explosive Clap, The Stare, etc)
* Damage decrease of -29% at level 5 (Normal), increase of +4% at level 30 (Normal), +110% at level 50 (TVHM), +156% at level 72 (UVHM), +173% at OP8.
* The multiplicative bonus on his roid damage from Sharing is Caring now depends on level: instead of a constant value of x1.4, it increases from about x1.5 at level 31 (Normal), to about x3.8 at OP8.
* Deathtrap now gets a bonus to his damage in co-op. The max bonus (4 players) should be about x1.9 in Normal, and about x1.3 in TVHM/UVHM.
* All of this should now be exactly the same as it is on console.

**Deathtrap**: Fixed a bug that made the interaction between Make it Sparkle and Sharing is Caring (with a roid shield) completely broken.

## Axton
**Sabre Turret**: Tried to make its damage scale the way it was supposed to (and actually does, on console). Unlike Deathtrap, I couldn't figure out a way to do it perfectly, so I got as close as I could. I'll update if I find a better solution.
* This affects the damage of the bullets, the Scorched Earth Rockets, Nuke, and the capacity of the Phalanx Shield.
* The damage is now as it should be (and the same as on console) at level 0 (Normal), and at OP8. But it evolves a bit differently in-between. Mostly: it gets about 30% too large at the end of Normal mode, and about 30% too small in the beginning of TVHM. 
* Bullets, Rockets & part of the Nuke damage: -38% damage at level 5 (Normal), +14% at level 30 (Normal), +56% at level 50 (TVHM), +119% at OP8.
* Other part of the Nuke damage: +43% at level 30 (Normal), +95% at level 50 (TVHM), +173% at OP8.
* Nuke Fire DOT: +43% at level 30 (Normal), +95% at level 50 (TVHM), +620% at OP8 (there was a level 72 cap on this one, also on console).
* Phalanx Shield capacity is made to scale better, to stay (very roughly) constant relative to the turret's health. This is not the case on console. -12% capacity at level 16 (Normal), +18% at level 30 (Normal), +61% at level 50 (TVHM), +125% at OP8.
* The Sabre Turret still does not get any bonus damage in multiplayer, as it does on console (like Deathtrap).

One issue with this fix is that the damage of the turret is in part calculated from the level of the game, rather than the level of the turret itself. For example, if you join the game of a lower/higher level player, your turret damage will adapt (to some extent), and be lower/higher than it should. I don't think this should be too problematic in practice.

# Credits

This was all written by me.

Thanks to Koby for making me want to do something about it, and inviting me to Shadow's Evil Hideout Discord channel. And thanks to all the folks there who answered my questions and helped me get started.


# Change log

* [2018-07-18] v1.1: Fixed a small issue with the calculation of the Phalanx Shield Capacity. Switched to BLCMM-compatible format.
* [2018-06-24] v1.0.
