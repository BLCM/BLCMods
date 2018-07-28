BL2 No Wasted COMs
==================

This mod changes the Class Mod drop pools such that the only COMs which drop
are for characters who are actually playing the game.  For a singleplayer
game, that means you'll only ever get COMs for your one character, for
instance.

Once a character has joined the game, the pools will not automatically
"shrink" when that character leaves.  In order to remove a player's COMs
from the drop pools, you'll have to exit all the way to the main menu and
re-execute the patch.  If anyone has any clever ideas about how to do this
more gracefully, I'm all ears!

Also, note that whatever character you have on the main menu counts as
"joining the game."  If you start the game with a Siren at the main menu,
execute the mod, then switch to a Mechromancer, the mod will set the game
to drop both Siren and Mechromancer COMs.

Usage
=====

This mod must be added to BLCMM using `File -> Import single mod`.
Choose the file `BL2 No Wasted COMs.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.
The script makes use of `modprocessor.py` from the parent directory.
You'll need to copy (or symlink, if you're on Mac or Linux) `modprocessor.py`
into this directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.1.0**, July 27, 2018:
 * Converted to BLCM format *(BLCMM is now required; FilterTool is not supported)*
 * Added a byline to the mod header comments

**v1.0.1**, April 25, 2018:
 * Changed mod to have a `.txt` extension

**v1.0.0**, April 3, 2018:
 * Initial public release
