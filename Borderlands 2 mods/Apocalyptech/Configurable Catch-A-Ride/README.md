Configurable Catch-A-Ride
=========================

This directory houses the code used to generate a "Configurable
Catch-A-Ride" mod, which is basically an extension of FromDarkHell's
CarReplacements/More Vehicles mod.

The mod itself lives in FromDarkHell's directory, so head over there
to get it!

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

This mod itself is ambivalently licensed - see FromDarkHell for redistribution
and modification terms.

Credits
=======

FromDarkHell's "More Vehicles" mod was the genesis for this, and provided
the actual methods to make this work.  I just slapped together some Python to
make a more thorough version easy to generate.

Changelog
=========

**v1.0.0**, May 30, 2018:
 * Initial public release
