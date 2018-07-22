TPS Early Bloomer
=================

This mod is an improvement on the similar section from UCP 2.1 which unlocks
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

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `TPS Early Bloomer.txt` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in FilterTool/BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from the parent directory.  You'd need
to copy (or symlink, if you're on Mac or Linux) `modprocessor.py` into this
directory in order to run the script.

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

**v1.1.0**, (unreleased):
 * Converted to BLCM format *(BLCMM is now required; FilterTool is not supported)*

**v1.0.0**, May 23, 2018:
 * Initial public release
