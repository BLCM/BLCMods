Speedier Moon Buggies
=====================

This mod improves the speed of both varieties of Moon Buggies in Borderlands: The
Pre-Sequel, mostly with an eye to ensuring that the few early-game jumps are 
a bit easier to hit when using the buggy.   The jump back from Concordia to the
main Serenity's Waste area, for instance, is usually easily missed if you don't
happen to aim for the right part of the bridge.  With this mod, I've been able
to get that one at 100% regardless of which part of the bridge I'm aiming at.

In doing so, of course, the Moon Buggy has become overall quite speedier, and
is even capable of making the leap over to Outlands Canyon.  I've tried to keep
the speed somewhat reasonable, since Moon Buggies were already a bit liable to
accidentally drive off cliffs or the edge of the map if you're not careful,
though of course some of that is unavoidable when making them even faster.
Buckle your seat belts!

Usage
=====

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Speedier Moon Buggies.txt` and
have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in FilterTool/BLCMM as well, once it's
been imported.)*

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

Credits
=======

Thanks to soze's BL2 "Faster Runner" mod, which simplified the attribute hunt
for this mod considerably.

Bugs
====

Unlike my "Speedier Sandskiffs" and "Speedier Stingrays" mods, this one features
no alliteration in its name.  I considered "Breakneck Moon Buggies" and "Brisk
Moon Buggies" but didn't really like the sound of either, in the end.  Alas!

Changelog
=========

**v1.0.0**, June 24, 2018:
 * Initial public release
