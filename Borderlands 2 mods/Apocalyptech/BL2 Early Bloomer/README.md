BL2 Early Bloomer
=================

This mod is an improvement on the similar section from UCP 4.0 which unlocks
various equipment in the game.  In addition to the basic early-game weapon
unlocks that UCP provides, this additionally allows Relics, Class Mods, all
shield types, all grenade types, and probably just about everything to spawn
from the beginning.

There's no problem with having both this and UCP enabled -- it'll just mean
that a few statements get executed twice.

This mod was copied directly from a section of my Better Loot mod.  If you're
running Better Loot, you already have this mod active, so there's no reason to
import it again.

Usage
=====

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `BL2 Early Bloomer.txt` and have
at it!

Compatibility
=============

Note that the "`Exhaustive Weapon/Item Part Unlocks`" section overwrites part
data for many weapons/grenades/COMs/etc to allow all parts to spawn in the
early game.  This may interfere with any other mods which alter part data, so
it probably makes sense to have this mod as high up in the list as possible,
so other mods can override.

Mod Construction / Implementation Details
=========================================

This mod is generated using a simple little Python script named
`generate-mod.py`.  The script makes use of `hotfix.py` from the parent
directory.  You'd need to copy (or symlink, if you're on Mac or Linux)
`hotfix.py` into this directory in order to run the script.

Licenses
========

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause),
which should be permissive enough to do just about whatever with.

The mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

See [COPYING-code.txt](../COPYING-code.txt) and [COPYING-mods.txt](../COPYING-mods.txt)
for the full text.

Changelog
=========

**v1.0.0**, May 23, 2018:
 * Initial public release
