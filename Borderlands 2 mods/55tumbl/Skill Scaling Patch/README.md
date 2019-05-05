*All files and content provided here were written by me (55tumbl), unless stated otherwise.*

*- They are free for personal use. I do decline any responsability in case it blows up in your face somehow, or any other misuse.
You may use these mods in videos, or for streaming, as long as you give me proper credit. I would appreciate you letting me know about it.*

*- You may re-use small bits of code (e.g. formulas, behavior modifications, etc) for your own purposes as long as you give me proper credit, and let me know about it.
Ask me for permission first if you wish to use larger portions of this code, make a modified/improved version, include it in a mod pack, etc.*

*- Do not re-upload any of those files anywhere.*

# Overview

The Skill Scaling Patch fixes a number of bugs or inconsistencies in character skills, mostly about the way they scale with level, and across playthroughs. It is not meant to change the balance of the game according to my personal preferences, but to make it work as intended (or at least more consistently), which does improve some aspects of the balance. The skills that are the most affected are Phaselock and Ruin (Maya), Light the Fuse (Krieg), Deathtrap and all its damage abilities (Gaige), the Sabre Turret and all its damage abilities (Axton).

Concerning Deathtrap and the Sabre Turret, the main problem addressed by this patch was actually not present on console. With the Skill Scaling Patch, their damage output should thus be identical (or close) to what it is on console. And that makes a huge difference on their end-game viability.

# Compatibility

The Skill Scaling Patch can be used as a standalone, for a vanilla experience with less bugs, and to meet Deathtrap and the Sabre Turret the way they were supposed to be (and actually are, on console). You can also try to combine it with other mods, using BLCMM. However, this may create incompatibilities if the other mods affect the skills modified by the Skill Scaling Patch, or even skills in general. I'd recommend importing the Skill Scaling Patch after other mods, and disabling any changes affecting the mentioned skills, in those other mods.
   
The Skill Scaling Patch (v1.0) is included in the Unofficial Community Patch, as of version 4.1. If you are using the UCP 4.1, you already have most of the Skill Scaling Patch. However, the fixes to Phaselock, Immolate, Steady as She Goes, Made of Sterner Stuff, Electrical Burn, and Deathtrap's Shock ranged attacks are not (yet) included in the UCP. If you want those, you can simply import the current version of the Skill Scaling Patch as a single mod after the UCP. I strongly recommend to disable the Electrical Burn fix, since this skill already receives a very strong (indirect) boost in the UCP.

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

**(optional) Phaselock**: activates Wreck/Elated/Chain Reaction after hitting immune target.  
* After hitting a non-phaselockable target, Phaselock remains artificially active for the base phaselock duration of 5 seconds (not affected by Suspension).
* During that time, Chain Reaction, Elated, and Wreck are active (if specced into) and give all their bonuses.
* Phaselock cooldown will only start after this phase is finished (even if not specced into Wreck/Elated/Chain Reaction)
* It does not change anything about the way Phaselock works with regular targets.
* When combined with Subsequence, a bug may sometimes happen that will keep Phaselock active for a few additional seconds.

**Immolate**: compensate for the double dip in damage penalty against higher level enemies in the OP levels (the special mechanics of this skill made it so that it was doing only about 20% damage versus a level 80 enemy, while other skills and weapons are doing 45% damage).   
* No effect up to level 72. Damage increase in the OP levels, up to +122% at OP8.

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

**(optional) Deathtrap**: Made his ranged shock attack (used against flying and non-phaselockable targets) benefit from all his melee damage bonuses, including roid damage from Sharing is Caring, and Make it Sparkle. This makes his damage output more consistent against different types of enemies. The animation was modified so that the damage is spread over 2 damage ticks instead of 7 (per shock beam), but the overall damage should be exactly the same in absence of any melee damage bonuses.

**Made of Sterner Stuff**: fixed a bug that gave Gaige too much damage reduction against Burn status effect.

**Electrical Burn**: compensate for the double dip in damage penalty against higher level enemies in the OP levels (the special mechanics of this skill made it so that it was doing only about 20% damage versus a level 80 enemy, while other skills and weapons are doing 45% damage).   
* No effect up to level 72. Damage increase in the OP levels, up to +122% at OP8.

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

## Salvador

**Steady as She Goes**: fix the effect of this skill on Hyperion weapons.
* The passive 80% recoil reduction (while gunzerking) becomes an accelerated reverse recoil for Hyperion weapons.
* The chance to improve accuracy on both guns now actually increases accuracy of Hyperion weapons instead of decreasing it.
* It still works the same for non-Hyperion weapons, except that the calculation of the amount of accuracy gained is somewhat changed, but in all cases it should be noticeable without being excessive.

# Credits

This was all written by me.

Thanks to Koby for making me want to do something about it, and inviting me to Shadow's Evil Hideout Discord channel. And thanks to all the folks there who answered my questions and helped me get started.


# Change log

* [2019-05-05] v2.6: Added the fix to Steady as She Goes, and worked around an issue that caused semi-infinite Phaselock when a subsequence bubble hits an immune target.
* [2019-04-08] v2.5: Added the fix to Made of Sterner Stuff, and included the changes making Phaselock active after hitting an immune target.
* [2018-08-09] v2.1: Added the modifications to Deathtrap's ranged shock attacks.
* [2018-07-31] v2.0: Added the Immolate & Electrical Burn fixes.
* [2018-07-18] v1.1: Fixed a small issue with the calculation of the Phalanx Shield Capacity. Switched to BLCMM-compatible format.
* [2018-06-24] v1.0.
