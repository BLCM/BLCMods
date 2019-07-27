BL2 Expanded Legendary Pools
============================

This mod adds all legendary items across DLCs into the global legendary loot
pools, and by default adds all uniques, seraphs, pearlescents, and
effervescents into the legendary pools, too.  This applies to weapons, grenade
mods, class mods, shields, and even relics.  The mod will also by default add
in gemstone weapons into the purple drop pool, and add the Dragon Keep "Alignment"
Class Mods to the global class mod drops.  These additions, like most of the
functionality in this mod, can be disabled/configured easily.

To compensate for the increased number of items which are available in
the legendary/purple pools, this mod also increases the chances of those
drops, by default.  An optional configuration section can be used to revert
those rates to the standard drop rates, or set them to drop even more
frequently, instead.

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
  * Add Gemstones to Purple Pool
  * Add Uniques to Legendary Pools
  * Add E-Tech Relics to Legendary Pools
  * Add Pearls to Legendary Pools (Weapons Only)
  * Add Seraphs to Legendary Pools
  * Add Effervescents to Legendary Pools
* **Add Undesirable Items to Pools (disabled by default)** - There are several
  items which aren't enabled by default, and I've labeled them as
  "undesirables."  You can enable them on an item-by-item basis in the last
  category, if you like.  These are:
  * Captain Blade's Midnight Star
  * Contraband Sky Rocket
  * Cracked Sash
  * ERROR MESSAGE *(the Ahab version that Master Gee wields)*
  * Fire Drill
  * Vault Hunter's Relic
  * Winter Is Over Relic
* **Purple Drop Rate Adjustment (defaults to 1.3x)** - Since we added gemstones
  to the purple pool, it seemed fair to increase its drop rate.  The default
  increase is 1.3x, which should exactly normalize the drop percentage so you
  get the same number of purples as before (not counting the gemstone additions).
  This can optionally be increased further up to 1.6x, or reverted down to stock
  values.
* **Legendary Drop Rate Adjustment (defaults to 2x)** - As with purples, since
  we greatly increased the number of items in the Legendary pools, it seemed
  fair to double the drop rate.  This can optionally be reverted down to
  stock values, or increased further to 3x.

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

**v1.1.1**, July 27, 2019:
 * Fixed the Fire Drill so that it doesn't disappear from your inventory
   between runs, if you've chosen to include the Fire Drill in your drops.

**v1.1.0**, July 15, 2019:
 * Moved Gemstone weapons from the E-Tech pools to the Purple pools
   * Medical Mystery will now always correctly reward an E-Tech
   * Fixed a few gemstone types which weren't actually dropping properly
   * Removed E-Tech pool buff, replaced with Purple pool buff
   * E-Tech Pistol drop rate is no longer affected by this mod

**v1.0.2**, July 11, 2019:
 * Added in all DLC5 (Commander Lilith & the Fight for Sanctuary) items

**v1.0.1**, August 24, 2018:
 * The Ogre is now properly considered a Legendary, not a Unique, and will
   be in the legendary pool regardless of whether you have Uniques added
   or not.

**v1.0.0**, July 22, 2018:
 * Initial public release
