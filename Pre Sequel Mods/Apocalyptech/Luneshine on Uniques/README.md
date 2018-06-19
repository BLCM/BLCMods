Luneshine on Uniques
====================

Several unique/legendary weapons in TPS don't have any Luneshine attachments
specified in the game data, so they will never spawn with Luneshine.  This mod
fixes those, and additionally sets it up so that they will ALWAYS have
Luneshine, so long as you're doing something which allows Luneshine.  In order
to actually get most of these to have Luneshine, you'll need to also be using
something like UCP's "`Make Luneshines Appear in the Wild`" option (found in its
"`2.1 Optionals`" folder), or my own "TPS Better Loot" mod.

**WARNING:** This mod will generate gear which the vanilla game doesn't think
is valid.  If you have some of this gear in your inventory and start the game
without having this mod enabled, the engine will remove those items from your
inventory.  If you see this, be sure to `Alt-F4` out of the game to prevent it
from saving over your savegame.

Specifically, this mod alters the parts pool for the following weapons:

* Berrigan
* Black Snake
* Boomacorn
* Boss Nova
* Boxxy Gunn
* Cyber Eagle
* Party Line
* Plunkett
* T4s-R
* Too Scoops
* The ZX-1

Usage
=====

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Luneshine on Uniques.txt` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in FilterTool/BLCMM as well, once it's
been imported.)*

This mod is actually generated using a simple little Python script named
`generate-mod.py`.  The script makes use of `hotfix.py` from Apocalyptech's
main BL2 mod directory.  You'd need to copy (or symlink, if you're on Mac
or Linux) `hotfix.py` into this directory in order to run the script.

Licenses
========

The `generate-source.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause),
which should be permissive enough to do just about whatever with.

The mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.1**, April 25, 2018:
 * Renamed mod file to have a `.txt` extension.

**v1.0.0**, March 30, 2018:
 * Initial public release
