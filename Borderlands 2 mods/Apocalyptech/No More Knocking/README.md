No More Knocking
================

Prevents NPCs from banging/knocking on walls, mostly in Sanctuary, but
it also does so in every other map where that behavior is found in the
game, namely the Badass Crater Bar, and possibly Flamerock Refuge.
(I'm not sure if the Perch in Flamerock Refuge which has knocking is
actually accessible by any NPCs -- I suspect not.)

By default, the behavior that's put in instead is mixed up a bit, so
the various locations around town where NPCs would be banging on the
wall is a bit different from place to place, but you can instead choose
a single behavior to use across the board, from the following list:

 * Arms Crossed
 * Hands on Hips
 * Kick Ground
 * Look at Ground
 * Look Intently

Enjoy your more relaxing Sanctuary experience!

Usage
=====

This mod should be imported into BLCMM using `File -> Import single mod`.
Choose the file `No More Knocking.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from the parent directory.  You'll need
to copy (or symlink, if you're on Mac or Linux) `modprocessor.py` into this
directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.1**, July 19, 2019:
 * Removed some maps because the knocking behavior was part of mission/storyline
   definitions:
   * Holy Spirits
   * Southern Shelf

**v1.0.0**, July 19, 2019:
 * Initial public release
