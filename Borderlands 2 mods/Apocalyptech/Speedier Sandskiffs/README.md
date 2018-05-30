Speedier Sandskiffs
===================

This mod improves the speed of all three varieties of Sandskiffs in
Borderlands 2.  Sandskiffs were already quite good, but this makes
traversing the wastes of the sands a bit speedier.  In addition to
a general speed improvement, this doubles the afterburner capacity
and considerably shortens its recharge time.

FromDarkHell's "More Vehicles" mod (`CarReplacements.txt`) can be used
to spawn the Sandskiff in any map with a vehicle station, if you're
interested in making more use of this fine, fine vehicle.

Note that while I set various afterburner variables in this file, I
don't think they actually do much of anything.  I'd love for someone
to figure out how exactly to tweak afterburner speeds on this thing,
because it seems relatively anemic, actually.

Usage
=====

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Speedier Sandskiffs.txt` and
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

Thanks to soze's "Faster Runner" mod, which simplified the attribute hunt
for this mod considerably.

Changelog
=========

**v1.0.0**, May 30, 2018:
 * Initial public release
