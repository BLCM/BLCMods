BL2 Sorted Fast Travel
======================

This mod does two things:

1. Makes the Fast Travel menu sorted by default (you can still hit
   `q` to see it in the usual non-sorted way, of course)
2. Removes the prefix "The" from all Fast Travel locations which
   use it, so that they sort *properly*.

That's it!  Many thanks to Our Lord And Savior Gabe Newell for the
command to sort-by-default, which is what spurred me into finally
looking into the other part of this mod.

Usage
=====

This mod should be imported into BLCMM using `File -> Import single mod`.
Choose the file `Sorted Fast Travel.blcm` and have at it!

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
generation script.  It also actually relies on some game data which is not
yet bundled by default with FT/BLCMM Explorer (namely, data for the 
`FastTravelStationDefinition` class), so, er, sorry about that.  The script
also makes use of `modprocessor.py` from the parent directory, so copy (or
symlink) that as well.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.1**, July 28, 2019:
 * Renamed to include `BL2` in the title, to avoid any potential confusion
   with the TPS version.

**v1.0.0**, July 16, 2019:
 * Initial public release
