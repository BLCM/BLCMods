*All files and content provided here were written by me (55tumbl), unless stated otherwise.*

*- They are free for personal use. I do decline any responsability in case it blows up in your face somehow, or any other misuse.
You may use these mods in videos, or for streaming, as long as you give me proper credit. I would appreciate you letting me know about it.*

*- You may re-use small bits of code (e.g. formulas, behavior modifications, etc) for your own purposes as long as you give me proper credit, and let me know about it.
Ask me for permission first if you wish to use larger portions of this code, make a modified/improved version, include it in a mod pack, etc.*

*- Do not re-upload any of those files anywhere.*

# Overview

NT-AreaScaling makes all areas and side-missions progressively scale up according to your advancement in the main mission, in Normal mode and TVHM. Level restrictions on the DLCs are lifted, so they can be played anytime during NVHM/TVHM, and they will also scale up according to the progress in the main game story.

This means that you can for example go back and farm Knuckledragger for a Hornet at level 18. Or start Tiny Tina's DLC at level 8, do a couple missions before coming back to the main game, and return to finish the DLC at level 28. Or farm the snowman over and over and over and over. Unlike UVHM (or the "Level 1 UHVM" mod), the areas/missions will not always be exactly at your level (but close enough, as long as you keep up with the main story). However, NT-AreaScaling does not change anything else about the Normal and TVHM playthroughs and their balance.

*Disclaimer: testing this takes a lot of time... it seems to be working fine, but I haven't checked everything. So let me know if you notice something weird, or if there are undesirable side-effects, etc.*

# Compatibility

NT-AreaScaling should be compatible with any other mods, as long as these mods do not touch the area level definitions (I don't know of any mod that does, but I don't know everything).

NT-AreaScaling can be applied before loading any save game: it should automatically scale up the relevant areas. If you reload the save later on without NT-AreaScaling, the areas will go back within the acceptable limits in vanilla.

It is a relatively big file (2.4MB, more than half the UCP), so it may take a few seconds to load. The DLC sections may be disabled at will using BLCMM (in case you don't own some of the DLCs, or if you don't want to play them with the NT-AreaScaling modifications). NT-AreaScaling does absolutely nothing in UVHM, so there's not much point loading it when playing in UVHM.


# Detailed changes

## Normal mode

* Turning in one of the main story missions (not all of them, but most) will make all previous areas and non-accepted side missions scale up to your level, within certain limits (for example, after finishing Wildlife Preservation, all areas should scale up to 19-21).
* Some areas will scale up directly, **others may require a save/quit**.
* Missions that have already been accepted (and their rewards) will never scale up, but the areas in which they take place, and the enemies you fight, should scale up.
* Finishing the main story and killing the Warrior will make all areas scale up to level 30.
* The mission You. Will. Die. (Terramorphous) will be between level 30 and 35 (depending on your level when you finish the main story). Completing this mission should make all areas in the main game and headhunter DLCs scale up to 35.
* Some areas like Caustic Caverns or Lynchwood have a special behavior in the vanilla game, which is mostly conserved here. But they will also scale to 30/35 after killing the Warrior/Terra.

**DLCs**
* All DLCs will scale to your level (when you first travel to the area), at any level between 5 and 35.
* Progress in the main game story will scale up the already visited areas in the DLC. A save/quit generally seems to be required for the DLC areas.
* The DLC raid boss missions (as well as some arena fights like in Murderlin's Temple) will be between level 30 and 35.
* Completing the raid boss mission (Hyperius, Pyro Pete, Vorac, Dragons) will make all areas in the corresponding DLC scale up to level 35.

## TVHM

* Same thing, except that the Terramorphous mission is level 50, as in vanilla.
* Finishing the main story and killing the Warrior will make all areas scale up to level 50, as in vanilla.

**DLCs**
* All DLCs will scale to your level (when you first travel to the area), at any level between 30 and 50.
* Progress in the main game story will scale up the already visited areas in the DLC, same system as in Normal mode.
* The DLC raid bosses and some missions that were locked at level 50, can now be played at any level between 30 and 50. They  will also scale up: e.g. you can fight Pyro Pete at level 42, and then come back later to fight him again at level 48.

# Credits

This was all written by me.


# Change log

* [2018-09-23] v1.0.
