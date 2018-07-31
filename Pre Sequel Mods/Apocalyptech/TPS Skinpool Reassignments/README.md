TPS Skinpool Reassignments
==========================

This mod serves the same purpose as BL2 UCP's "`Loot Pool & Drop Changes ->
Skinpool Fixes (Don't uncheck this)`" section, but for TPS.  Specifically, it
frees up 624 skin/head pools for use by TPS mods.  This is possible because the
default skin/head pool structure uses an effectively unnecessary intermediate
pool inbetween the pool that's actually used for drops and the skins/heads
themselves.

See https://github.com/BLCM/BLCMods/wiki/TPS-Custom-Skin-and-Head-Pool-Registry
for a registry of TPS Skin Pools, if you'd like to use one of these pools in
a TPS mod.

Usage
=====

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `TPS Skinpool Reassignments.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from Apocalyptech's BL2 mod
directory.  You'll need to copy (or symlink, if you're on Mac or Linux)
`modprocessor.py` into this directory in order to run the script.  It also makes
use of some data libraries from my own
[FT/BLCMM Explorer](https://github.com/apocalyptech/ft-explorer) project.
That project's `resources` and `ftexplorer` directories will need to be
copied (or symlinked) in here as well.

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

**v1.1.0**, July 28, 2018:
 * Converted to BLCM format *(BLCMM is now required; FilterTool will not work)*

**v1.0.0**, June 9, 2018:
 * Initial public release
