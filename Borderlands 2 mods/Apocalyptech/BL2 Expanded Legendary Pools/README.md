BL2 Expanded Legendary Pools
============================

Adds all legendaries/uniques/pearls/seraph items (weapons,
grenade mods, class mods, shields, relics) into the global "legendary" loot
pools.  This was basically taken directly from BL2 Better Loot and
repackaged as standalone functionality, since folks may find it useful
without wanting to buff their loot more generally.

This isn't entirely dissimilar from FromDarkHell's `BL1Loot.txt`, though
that mod just adds a bunch of stuff to the legendary weapons pool (and
doesn't include things like COMs), whereas this one adds things to their
respective loot pools and allows for more configuration.

Usage/Installation
==================

This mod must be imported into BLCMM using `File -> Import single mod`.
Simply choose the file `BL2 Expanded Legendary Pools.blcm` and have at it!

### Configuration

There are several items which aren't enabled by default, and I've labeled
them as "undesirables."  You can enable them on an item-by-item basis in
the last category, if you like.  These are:

* Captain Blade's Midnight Star
* Contraband Sky Rocket
* Cracked Sash
* ERROR MESSAGE *(the Ahab version that Master Gee wields)*
* Vault Hunter's Relic

Differences Between This And BL2 Better Loot's Version
======================================================

This mod was taken pretty much directly from BL2 Better Loot, but has a
couple of differences to make it a more general-purpose solution:

* This version does not nerf the drop rates for E-Tech pistols (darts and
  spikers), when adding gemstones to the E-Tech pool.  All E-Tech weapon
  type pools should have an equal chance of dropping an E-Tech or a
  gemstone.

TODO
====

* Options to buff legendary drop rate
* Options to buff E-tech drop rate
* Option to add "reward" relic pool
* Probably need to add in alignment COMs?

Bugs
====

* The mission Medical Mystery: X-Com-municate is supposed to reward an
  E-Tech pistol, but because we add gemstones into the E-Tech pool (at least
  by default), you may end up with a gemstone weapon instead.

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

I generate this mod using a Python script named `generate-mod.py`.  It
makes use of `modprocessor.py` from the parent directory.  You'd need to copy
(or symlink, if you're on Mac or Linux) `modprocessor.py` into this directory
in order to run the script.

Licenses
========

The `generate-source.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause),
which should be permissive enough to do just about whatever with.

The mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

See [COPYING-code.txt](../COPYING-code.txt) and [COPYING-mods.txt](../COPYING-mods.txt)
for the full text.

Changelog
=========

**v1.0.0**, (unreleased):
 * Initial public release
