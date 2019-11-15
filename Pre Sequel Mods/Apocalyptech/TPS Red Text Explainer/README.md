TPS Red Text Explainer
======================

Inspired by Ezeith's BL2 mod "Red text explainer"

All weapons, grenades, and shields with red text will include text describing
the extra effects.  A lot of shields already have all their effects listed on the
card, so those will show up as "All effects listed."

Class Mods and Oz Kits have been left alone, since all those list their effects
right on the card.

Effect descriptions were largely taken from the Fandom wiki, so take them with a
grain of salt, and let me know if anything's wrong!

Usage
=====

This mod should be imported into BLCMM using `File -> Import single mod`.
Choose the file `TPS Red Text Explainer.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`,
which makes use of some data classes from my [FT/BLCMM Explorer](https://github.com/apocalyptech/ft-explorer)
project.  You'll need to copy (or symlink, if you're on Linux or OSX) that
project's `resources` and `ftexplorer` dirs into this one, to run the
generation script.  The script also makes use of `modprocessor.py` from my
main BL2 mods directory, so copy (or symlink) that as well.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, November 15, 2019:
 * Initial public release
