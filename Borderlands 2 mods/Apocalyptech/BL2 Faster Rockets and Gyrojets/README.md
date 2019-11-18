BL2 Faster Rockets and Gyrojets
===============================

After years of playing BL2, I've found that I basically never use
most Torgue weapons, outside of various named legendaries/uniques and
the occasional specific part combos, because the gyrojet speed was
just too much of a detriment for me.  So, I figured rather than
continue to never use these weapons, I should just speed 'em up and
have a wider pool of weapons available to me!

This mod improves the speed of all gyrojet-based projectiles by 3x,
which also affects other Torgue-barrel-provided projectiles on ARs,
like grenades on Jakobs and Dahl ARs.  Rocket speeds are also buffed
by 3x, since I nearly always take Vladof launchers over other brands.
Vladof launchers do get a buff, but only get a much-smaller 1.4x.
E-Tech launchers only get 2x.

Many Unique/Legendary/Seraph/etc Torgues also get a buff, though those
are generally more slight.  Here's the list of specific named gear
that's been given a bit of a boost:

* 12 Pounder
* Ahab
* Badaboom
* Boom Puppy
* Bunny
* Carnage
* Hive
* Landscaper
* Mongol
* Norfleet
* Nukem
* Pocket Rocket *(though the buff is identical to UCP's Pocket Rocket buff)*
* Pyrophobia
* Seeker
* Swordsplosion
* Tunguska
* Unicornsplosion

I am of course well aware that speeding up these projectiles is
getting rid of one of the main balances meant to counteract the
generally-increased damage output these weapons are capable of,
but I have never been one to shy away from OP gear.

Usage
=====

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `BL2 Faster Rockets and Gyrojets.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from the parent directory.  You'll need
to copy (or symlink, if you're on Mac or Linux) `modprocessor.py` into this
directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, November 17, 2019:
 * Initial public release
