Easier ECLIPSE and EOS
======================

The ECLIPSE and EOS boss fights, at the end of the Claptastic Voyage DLC,
are an unexpected and for some users unpleasant jump in difficulty.
Outside of raid bosses, neither TPS nor Claptastic Voyage contains battles
which are nearly so difficult.  This mod is aimed at users who don't feel
like fighting their way through both ECLIPSE and EOS at their full
strength.

The mod has one section per boss, so you can configure their difficulty
independently.  There are four options for each boss:

* Easier (the default)
* Even Easier
* Total Chump
* Stock Difficulty

You can use the last option to have one of the bosses remain unchanged, if
you'd only wanted to nerf one of the two.

Note that this mod doesn't address all aspects of the boss fights -- EOS
will still be out of range of beam lasers, and the stomp damage from
ECLIPSE is probably mostly unchanged, for instance.  I'm also not
especially good at balancing in general, so if you feel that anything in
here goes too far, or not far enough (for the given selection), definitely
let me know and I can tweak the values in here.

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

**v1.0.0**, Unreleased:
 * Initial public release
