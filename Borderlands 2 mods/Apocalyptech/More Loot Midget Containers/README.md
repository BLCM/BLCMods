More Loot Midget Containers
===========================

**NOTE:** This mod is considered deprecated.  [mopioid](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/mopioid)
has created a better version of this which adds Loot Midgets to literally
every container in the game, using some clever map merging, and thus
makes this one fairly obsolete.  [Get mopioid's "Loot Midget World" mod here.](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/mopioid/LootMidgetWorld.blcm)

Original README
---------------

This mod converts various maps so that that levels which contain
loot-midget-spawning containers will always use the loot-midget-spawning
versions if possible.

Note that not *every* container is loot-midgetable.  For instance, in
Opportunity, the only loot-midget-spawning container is the shorter ammo
containers.

Number of containers changed on each map:

* **Arid Nexus - Badlands**: 53
* **Arid Nexus - Boneyard**: 52
* **The Dust**: 5
* **Frostburn Canyon**: 50
* **Hero's Pass**: 1
* **Opportunity**: 45
* **Sawtooth Cauldron**: 144
* **Thousand Cuts**: 66
* **Tundra Express**: 74
* **Wildlife Exploitation Preserve**: 105

Usage
=====

This mod must be imported in BLCMM, using `File -> Import single mod`.
Choose the file `More Loot Midget Containers.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`,
which makes use of some data classes from my [FT Explorer](https://github.com/apocalyptech/ft-explorer)
project.  You'll need to copy (or symlink, if you're on Linux or OSX) that
project's `resources` and `ftexplorer` dirs into this one, to run the
generation script.  The script also makes use of `modprocessor.py` from the
parent directory, so copy (or symlink) that as well.  There's also a couple
other scripts in here which were used to do the initial finding of which
maps contained which loot-midget containers, as well.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.1.0**, July 27, 2018:
 * Converted to BLCM format *(BLCMM is now required; FilterTool is no longer supported)*
 * Added a byline to the mod header comments
 * Added a note about mopioid's Loot Midget World, and how that's the preferred
   mod to use now.

**v1.0.2**, April 25, 2018:
 * Renamed mod file to have a `.txt` extension.

**v1.0.1**, April 2, 2018:
 * Added in a bunch more containers which my generation code missed.  D'oh.

**v1.0.0**, April 2, 2018:
 * Initial public release
