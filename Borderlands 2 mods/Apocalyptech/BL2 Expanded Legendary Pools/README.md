BL2 Expanded Legendary Pools
============================

This mod adds all legendary items across DLCs into the global legendary loot
pools, and by default adds all uniques, seraphs, and pearlescents into the
legendary pools, too.  This applies to weapons, grenade mods, class mods,
shields, and even relics.  The mod will also by default add in gemstone weapons
into the E-Tech pool, and add the Dragon Keep "Alignment" Class Mods to the
global class mod drops.  These additions, like most of the functionality in
this mod, can be disabled/configured easily.

To compensate for the increased number of items which are available in
the legendary/E-tech pools, this mod also doubles the chances of those
drops, by default.  An optional configuration section can be used to revert
those rates to the standard drop rates, or set them to drop three times as
often, instead.

This mod was basically taken straight out of BL2 Better Loot, though there
are a few functional differences.  This mod will **not** play nicely with
Better Loot, or my Cold Dead Hands mod, for that matter!  Those mods already
improve the loot drops in their own ways, and having this mod on top will
result in undefined behavior.

This mod isn't entirely dissimilar to FromDarkHell's `BL1Loot.txt`, though
that mod just adds a bunch of stuff to the legendary weapons pool (and
doesn't include things like COMs), whereas this one adds things to their
respective loot pools and allows for more configuration.

Usage/Installation
==================

This mod must be imported into BLCMM using `File -> Import single mod`.
Simply choose the file `BL2 Expanded Legendary Pools.blcm` and have at it!

### Configuration

* **Loot Pool Setup** - This is where the main bit of the mod happens.
  The one locked category adds all legendary items to the various legendary
  pools.  Then all the other options in here can be freely unchecked if you
  want.  For reference here, they are:
  * Add Dragon Keep "Alignment" Class Mods to Global Drop Pool
  * Add Gemstones to E-Tech Pool
  * Add Uniques to Legendary Pools
  * Add E-Tech Relics to Legendary Pools
  * Add Pearls to Legendary Pools (Weapons Only)
  * Add Seraphs to Legendary Pools
* **Add Undesirable Items to Pools (disabled by default)** - There are several
  items which aren't enabled by default, and I've labeled them as
  "undesirables."  You can enable them on an item-by-item basis in the last
  category, if you like.  These are:
  * Captain Blade's Midnight Star
  * Contraband Sky Rocket
  * Cracked Sash
  * ERROR MESSAGE *(the Ahab version that Master Gee wields)*
  * Vault Hunter's Relic
* **E-Tech Drop Rate Adjustment (defaults to 2x)** - Since we doubled the
  amount of weapons in the E-Tech pools, it seemed fair to double the drop
  rate.  This can optionally be reverted down to stock values, or increased
  further to 3x.
* **Legendary Drop Rate Adjustment (defaults to 2x)** - As with E-Techs, since
  we greatly increased the number of items in the Legendary pools, it seemed
  fair to double the drop rate.  This can optionally be reverted down to
  stock values, or increased further to 3x.

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

**v1.0.1**, August 24, 2018:
 * The Ogre is now properly considered a Legendary, not a Unique, and will
   be in the legendary pool regardless of whether you have Uniques added
   or not.

**v1.0.0**, July 22, 2018:
 * Initial public release
