# Overview

The Skill Scaling Patch fixes a number of bugs (or inconsistencies) about the way skills scale with level, and across playthroughs. It is not meant to "fix" the balance of the game according to my personnal preferences, but only to make it work as was probably intended. It does improve some aspects of the balance, though. The skills that are the most affected are Ruin (Maya), Light the Fuse (Krieg), Deathtrap and all its damage abilities (Gaige), the Sabre Turret and all its damage abilities (Axton).

# Compatibility

The Skill Scaling Patch can be used as a standalone, for a vanilla experience with less bugs, and to meet Deathtrap and the Sabre Turret the way they were (I believe) supposed to be. For that, use the SkillScalingPatch_standalone.txt file, which includes the latest Gearbox hotfixes.

The Skill Scaling Patch can also be merged onto the UCP. For that, use the SkillScalingPatch_UCP.txt, which contains additional statements that should resolve incompatibility issues.

Adding other mods that affect those skills, or even skills in general, may create some issues. 

# Detailed changes

## Maya

**Ruin (elemental explosions and DOTs)**: made to scale like other skills and removed the level 72 cap.    
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +590% at OP8.    
* This also affects the Corrode DOT (but not the main damage) from Cloud Kill. Since the DOT is very small, this has practically no effect on the overall Cloud Kill damage (about +1.5% at OP8). 

**Phaselock (damage on non-phaselockable targets)**: made to scale like other skills.   
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +160% at OP8

**Scorn**: made to scale like other skills.   
* Damage increase of +60% at level 30, +100% at level 50, +144% at 72, +160% at OP8

## Krieg

**Light the Fuse**: removed the level 72 cap.
* No effect on damage up to level 72. Damage increased by +183% at OP8.

**Krieg's innate melee damage bonus (without blade attachment)**: removed the level 72 cap.
* No effect on damage up to level 72. Base melee damage increased by +6.6% at OP8.
