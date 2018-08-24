Speedier Stingrays
==================

    Wait, I think that Moxxi's designs didn't get fully
    integrated...  Try it now.

This mod improves the speed of both varieties of Stingrays in Borderlands: The
Pre-Sequel.  Stingrays were already quite good, but this makes traversing the
icy wastes even speedier.  In addition to a general speed improvement, this
increases the afterburner charge and improves handling quite a bit.

Usage
=====

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `Speedier Stingrays.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from Apocalyptech's BL2 mod
directory.  You'd need to copy (or symlink, if you're on Mac or Linux)
`modprocessor.py` into this directory in order to run the script.

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

**v1.1.0**, July 27, 2018:
 * Converted to BLCM format *(BLCMM is now required; will not work with FilterTool)*

**v1.0.0**, June 14, 2018:
 * Initial public release
