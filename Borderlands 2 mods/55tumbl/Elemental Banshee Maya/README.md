*All files and content provided here were written by me (55tumbl), unless stated otherwise.*

*- They are free for personal use. I do decline any responsability in case it blows up in your face somehow, or any other misuse.
You may use these mods in videos, or for streaming, as long as you give me proper credit. I would appreciate you letting me know about it.*

*- You may re-use small bits of code (e.g. formulas, behavior modifications, etc) for your own purposes as long as you give me proper credit, and let me know about it.
Ask me for permission first if you wish to use larger portions of this code, make a modified/improved version, include it in a mod pack, etc.*

*- Do not re-upload any of those files anywhere.*

# Overview

Elemental Banshee Maya is a complete rework of Maya's skills, pushing her into different playstyles, with a focus on elemental effect damage and melee (including some ranged melee abilities).

Many of the important skills in her vanilla configuration are taken away (e.g. Wreck, Reaper, slag on Ruin, Ward for easy Beehawking), and replaced by completely new skills with some interesting synergies.
Her health and health regeneration skills are boosted to allow for a more aggressive and close quarter gameplay, incl. with depleted shields.
Most class mods have been adapted, and some new ones (Legendary Banshee,...) are introduced. I recommend starting a new playthrough to build her progressively.

This is kind of a beta version: it should be fully functional, but the balance is still not perfect and is subject to further changes, so check for updates.
Feedback on the matter would be appreciated. 

[Trailer Video](https://www.youtube.com/watch?v=x4PDKIh6TII)

# Compatibility

Elemental Banshee Maya should be compatible with any mod that doesn't affect Maya skills and class mods.
If you combine it with other mods (e.g. UCP), disable anything Maya-related in those mods, and add Elemental Banshee Maya at the end.

It is meant to be balanced for the vanilla version of the game, except for some internal tweaks. 
A priori, I wouldn't combine it with mods that affect the balance of the game (e.g. slag overhaul, UVHM overhaul etc), but that's up to you.

# Skills

## Phaselock

The damage that Phaselock inflicts on non-phaselockable targets is now based on Maya's melee damage, and benefits from all her melee damage bonuses (incl. roid shield, bladed weapon). 

## Motion

**Ward**: Increases Shield Recharge Rate and Shield Recharge Delay (makes the delay longer).

**Siren Song**: Sweet Release, with the addition of a stacking mechanism: one stack of Siren Song is gained each time a phaselocked enemy is killed.
Siren Song stacks last for 6 minutes, increase Max Health, and play a role in other skills in the Motion tree.

**Sustenance**: Passive health regeneration, faster when shields or magazine is empty.

**Quicken**: Increase Phaselock and Scorn cooldown rate, depending on the number of stacks of Siren Song.

**Fleet**: No changes.

**Converge**: Now also adds 1 second to Phaselock duration.

**Shriek**: Massive increase in Fire Rate and Gun Damage while an enemy is phaselocked, but also consumes the shields. Bonuses are lost when shields are empty.

**Kinetic Reflection**: The %damage that deflected bullets deal to enemies now depends on the number of Siren Song stacks and on the level of the player.
(e.g. at 5/5 with 5 stacks, deflected bullets deal 100% of their original damage at level 20, but 400% at OP8)

**Chain Reaction**: Passive skill, chance to ricochet depends on the number of Siren Song stacks.

**Subsequence**: 1 point capstone with 100% chance to seek a new enemy. Also increases phaselock duration by 3 seconds.

## Harmony

**Mind's Eye**: No changes.

**Accelerate**: No changes.

**Restoration**: Increased Max Health bonus.

**Pins and Needles**: Increases melee damage and elemental status damage, while an enemy is phaselocked.

**Elated**: Increased health regeneration, while an enemy is phaselocked.

**Res**: Now also adds 1 second to Phaselock duration.

**Out with a Bang**: When a phaselocked enemy is killed, it explodes and deals damage to nearby enemies. The damage is based on Maya's melee damage, and benefits from all her melee damage bonuses.

**Life Tap**: No changes.

**Reaper**: Stacks of Reaper are gained when an enemy is killed by an elemental status effect. Reaper stacks last 90 seconds and increase melee damage.

**Scorn**: The damage is now based on Maya's melee damage, and benefits from all her melee damage bonuses.

## Cataclysm

**Flicker**: Increased Elemental effect chance bonus.

**Petals**: Damage resistance vs. non-elemental, Fire and Corrosive attacks.

**Pestilence**: Adds Corrosive damage to melee attacks. The corrosive damage is based on the melee damage actually dealt (Immolate calculation). Skill is passive but with a smaller percent than Immolate.
I also tweaked the formulas so that it does not suffer twice from the damage penalty against higher level enemies in the OP levels.

**Backdraft**: Chance to set the target on Fire when hitting a crit with a bullet (probability is higher for weapons with small Fire Rate and small number of projectiles per shot).
And large radius Nova explosion when shields are depleted.

**Supernova**: Enemy that deals health damage to Maya has a chance to catch a Burn and a Corrode status effects. Deadly response to enemies inflicting DOTs on Maya.

**Cloud Kill**: Very small damage, but can give stronger Corrode status effects. Cloud lasts much longer (20 seconds) to make its placement more tactical. Also adds 1 second Phaselock duration.

**Death Wish**: Increases Elemental effect damage, depending on how low Maya's health is.

**Elemental Queen**: Kill Skill, increases all Fire and Corrosive damage.

**Ruin**: Slag replaced by Fire, and made to be a 5/5 skill (can be boosted up to 11/5 with class mods).

**Nephilim**: Constantly inflict Slag damage to nearby enemies. A simple, but risky, way to slag enemies.


# Credits

This was all written by me,    
except for the modified visual effects on Ruin (credits & thanks to Koby).

Thanks to the people who made this kind of modding possible and practical (Shadowevil, LightChaosMan, etc).    
Thanks to Apocalyptech for his BPD graph generator, this thing is so damn useful.

# Change log
[2018-08-09] v1.1: Fixed an error in the calculation of reflected bullet damage for Kinetic Reflection.    
[2018-08-05] v1.0.
