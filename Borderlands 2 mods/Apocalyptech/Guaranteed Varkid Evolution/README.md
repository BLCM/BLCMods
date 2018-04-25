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

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Guaranteed Varkid Evolution.txt` and
have at it!

Mod Construction / Implementation Details
=========================================

This mod is actually generated using a simple little Python script named
`generate-mod.py`.  The script makes use of `hotfix.py` from the parent
directory.  You'd need to copy (or symlink, if you're on Mac or Linux)
`hotfix.py` into this directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.2**, April 25, 2018:
 * Renamed the mod to have a `.txt` extension.

**v1.0.1**, April 25, 2018:
 * Tweaked comments in the mod file a bit, to look better inside FT/BLCMM.
 * Removed the `Transient.SparkServiceConfiguration_6` set statements at the
   bottom of the file, to enforce needing to run this via FT/BLCMM.

**v1.0.0**, February 26, 2018:
 * Initial public release
