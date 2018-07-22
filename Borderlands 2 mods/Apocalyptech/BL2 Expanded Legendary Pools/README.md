BL2 Expanded Legendary Pools
============================

Adds all legendaries/uniques/pearls/seraph items (weapons,
grenade mods, class mods, shields, relics) into the global "legendary" loot
pools.

This isn't entirely dissimilar from FromDarkHell's `BL1Loot.txt`, though
that mod just adds a bunch of stuff to the legendary weapons pool (and
doesn't include things like COMs), whereas this one adds things to their
respective loot pools and allows for more configuration.

Usage/Installation
==================

This mod must be imported into BLCMM using `File -> Import single mod`.
Simply choose the file `BL2 Expanded Legendary Pools.blcm` and have at it!

Loot Purposefully Excluded from Pools
=====================================

There's some gear which I felt shouldn't be in the pools at all.  I am
quite willing to hear counterarguments; my mind could probably be pretty
easily persuaded otherwise if someone feels strongly about it.

* Cracked Sash (Shield)
* GOTY/Preorder/Whatever starting game loot:
  * "Gearbox" themed guns (AR/SMG/Sniper)
  * Contraband Sky Rocket
  * Vault Hunter's Relic
* Captain Blade's Midnight Star
* Blue-rarity Magic Missile *(purple rarity will still spawn -- they're
  technically different items)*
* "ERROR MESSAGE" Ahab (the one used by Master Gee).  Regular Ahabs will
  still spawn, though.

TODO
====

* Options to buff legendary drop rate
* Options to buff E-tech drop rate
* Option to add in "undesirable" loot (above) rather than omitting outright
* Option to add "reward" relic pool

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
