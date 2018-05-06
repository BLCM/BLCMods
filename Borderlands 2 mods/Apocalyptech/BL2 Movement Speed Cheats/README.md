BL2 Movement Speed Cheats
=========================

This mod increases movement speed of all BL2 characters (including while
crouched, and while in FFYL).  It also increases the jump height a bit, and
increases air control by quite a lot.  If you're looking to zip through
some levels like there's no tomorrow, this is for you.

Obviously this is quite cheaty.

There are actually three options to choose from, in a mututally-exclusive
folder inside the mod:

* Reasonable Improvements
* Extreme Improvements
* Stock Values

"Extreme Improvements" used to be the only setting for this mod, and was
useful while testing out some of my other mods, but is a bit much for
ordinary play (and ends up making movement in multiplayer a bit jerky
looking).  "Reasonable Improvements" is the new default, which makes
things a bit more reasonable, though it will still be an improvement
from stock.  "Stock Values" can be used to set the vanilla BL2 values
for movement speed.

Usage
=====

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `BL2 Movement Speed Cheats.txt` and have
at it!

Mod Construction / Implementation Details
=========================================

This mod is actually generated using a simple little Python script named
`generate.py`.  The script makes use of `hotfix.py` from the parent directory.
You'd need to copy (or symlink, if you're on Mac or Linux) `hotfix.py` into
this directory in order to run the script.

Licenses
========

The `generate.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause),
which should be permissive enough to do just about whatever with.

The mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.1.0**, May 6, 2018:
 * Added "Reasonable Improvments" and "Stock Values" options, and made
   "Reasonable Improvements" the default.

**v1.0.1**, April 25, 2018:
 * Changed mod to have a `.txt` extension

**v1.0.0**, April 2, 2018:
 * Initial public release
