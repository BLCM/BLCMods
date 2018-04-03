TPS No Wasted COMs
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
"joining the game."  If you start the game with a Gladiator at the main menu,
execute the mod, then switch to a Lawbringer, the mod will set the game
to drop both Gladiator and Lawbringer COMs.

Usage
=====

This mod must be run by adding it into FilterTool with `Developer tools` ->
`Add single mod`.  Choose the file `TPS No Wasted COMs` and have at it!

Mod Construction / Implementation Details
=========================================

This mod is actually generated using a simple little Python script named
`generate-source.py`, and a companion `create.sh`.  The script makes use of
`hotfix.py` from the parent directory.  You'd need to copy (or symlink, if
you're on Mac or Linux) `hotfix.py` into this directory in order to run the
script.  It also needs my `conv_to_mod.py` to be available in the parent
directory.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, April 3, 2018:
 * Initial public release
