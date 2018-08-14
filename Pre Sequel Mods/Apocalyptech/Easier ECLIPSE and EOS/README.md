Easier ECLIPSE and EOS
======================

This mod makes the ECLIPSE and EOS boss fights at the end of the Claptastic
Voyage DLC easier in a variety of ways.  The default settings in the mod
aim to have the bosses remain quite dangerous -- the goal isn't really to
make them *super* easy (except on the "Total Chump" option).  That said,
I'm not great at balancing, so it's possible I've gone too far in some areas,
or not far enough in others.  Let me know if anything needs tweaking!

The mod has one section per boss, so you can configure their difficulty
independently.  There are five options for each boss:

* Easier (the default)
* Even Easier
* Total Chump
* Stock Difficulty
* Mega Badass Difficulty (This is a buff, not a nerf!  In case you
  were feeling masochistic.)

You can use the "stock" option to have one of the bosses remain unchanged, if
you'd only wanted to nerf one of the two.  The "Easier" default is the one
which intends to have the bosses still be quite dangerous.

Note that this mod doesn't address all aspects of the boss fights -- EOS
will still be out of range of beam lasers, and the stomp damage from
ECLIPSE is probably mostly unchanged, for instance.  The overall strategy
during the fights will not change much either.  EOS's Eye of Helios attack
will remain quite devastating, for instance, so stay out of the way.

It's perhaps worth noting that this has only really been tested in Normal
mode, and hasn't really received a lot of playtesting in general.

Usage
=====

This mod must be imported into BLCMM, via `File -> Import single mod`.
Choose the file `Easier ECLIPSE and EOS.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from Apocalyptech's main BL2 mod
directory.  You'll need to copy (or symlink, if you're on Mac or Linux)
`modprocessor.py` into this directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, August 14, 2018:
 * Initial public release
