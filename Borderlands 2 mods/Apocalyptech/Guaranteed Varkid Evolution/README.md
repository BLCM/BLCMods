Guaranteed Varkid Evolution
===========================

This is a mod which sets the evolution probability of varkids to 100%
regardless of player count and playthrough.  This means that every varkid
will be sure to evolve to its next stage, so long as it remains in a
combat state.  This would be mostly useful if you're looking to farm
Vermivorous but don't want to gamble on the spawn each time.

Note that UCP 4.0 includes a section which improves the evolution chances
generally, without going as overboard as this mod does.

Usage
=====

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `Guaranteed Varkid Evolution.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from the parent directory.  You'll
need to copy (or symlink, if you're on Mac or Linux) `modprocessor.py`
into this directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.1.0**, April 25, 2018:
 * Converted to BLCM format *(BLCMM is now required; FilterTool is not supported)*
 * Added a byline to the mod header comments

**v1.0.2**, April 25, 2018:
 * Renamed the mod to have a `.txt` extension.

**v1.0.1**, April 25, 2018:
 * Tweaked comments in the mod file a bit, to look better inside FT/BLCMM.
 * Removed the `Transient.SparkServiceConfiguration_6` set statements at the
   bottom of the file, to enforce needing to run this via FT/BLCMM.

**v1.0.0**, February 26, 2018:
 * Initial public release
