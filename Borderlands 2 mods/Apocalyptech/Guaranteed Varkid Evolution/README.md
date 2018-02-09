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

The best way to use this mod is to add it into FilterTool with
`Developer tools` -> `Add single mod`.  Choose the file `Guaranteed Varkid
Evolution` and have at it!

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

This mod is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0) license](https://creativecommons.org/licenses/by/4.0/).
