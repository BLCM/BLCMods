BL2 Early Bloomer
=================

This mod is an improvement on the similar section from UCP 4.0 which unlocks
various equipment in the game.  In addition to the basic early-game weapon
unlocks that UCP provides, this additionally allows Relics, Class Mods, all
shield types, all grenade types, and probably just about everything to spawn
from the beginning.

There's no problem with having both this and UCP enabled -- it'll just mean
that a few statements get executed twice.

This mod was originally copied directly from a section of my Better Loot mod.
If you're running Better Loot, you already have this mod active, so there's
no reason to import it again.

Usage
=====

This mod must be imported into BLCMM with `File -> Import single mod`.
Choose the file `BL2 Early Bloomer.blcm` and have at it!

Compatibility
=============

v1.0.0 of this mod could potentially get in the way of various grenade/COM
mods due to editing the whole parts list structures directly.  The current
version (v1.1.0 and up) should play much more nicely with custom objects,
and should theoretically not cause any problems.  (This is actually what
the TPS version of this mod already does.)

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's been
imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocesor.py` from the parent directory.  You'd need
to copy (or symlink, if you're on Mac or Linux) `modprocessor.py` into this
directory in order to run the script.  Likewise, `generate-mod.py` makes
use of some data introspection abilities available in my FT/BLCMM Explorer
project.  You'll need to copy (or, again, symlink) FT Explorer's `ftexplorer`
and `resources` dirs into this directory to generate the mod.

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

**v1.1.0**, July 11, 2018:
 * Converted to BLCMM format (no longer compatible with FilterTool)
 * Updated part unlock mechanism to play more nicely with custom objects.
   Should no longer conflict with custom grenade/COM mods, for instance.

**v1.0.0**, May 23, 2018:
 * Initial public release
