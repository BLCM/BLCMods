TPS Expanded Legendary Pools
============================

This mod adds all legendary items across DLCs into the global legendary loot
pools, and by default adds all uniques and glitch uniques into the
legendary pools, too.  This applies to weapons, grenade mods, class mods,
shields, and oz kits.  These additions can be disabled/configured easily.

To compensate for the increased number of items which are available in
the legendary pools, this mod also doubles the chances of those
drops, by default.  An optional configuration section can be used to revert
those rates to the standard drop rates, or set them to drop three times as
often, instead.

This mod was basically taken straight out of TPS Better Loot, though there
are a few functional differences.  This mod will **not** play nicely with
Better Loot, or my Cold Dead Hands mod, for that matter!  Those mods already
improve the loot drops in their own ways, and having this mod on top will
result in undefined behavior.

Usage/Installation
==================

This mod must be imported into BLCMM using `File -> Import single mod`.
Simply choose the file `TPS Expanded Legendary Pools.blcm` and have at it!

### Configuration

* **Loot Pool Setup** - This is where the main bit of the mod happens.
  The one locked category adds all legendary items to the various legendary
  pools.  Then all the other options in here can be freely unchecked if you
  want.  For reference here, they are:
  * Remove Unique "Shift" Weapons from Global Rare Pools - in the default
    TPS loot configuration, four unique weapons were added to the global
    rare (blue) drop pools.  Since this mod adds them to the legendary
    pool instead, leaving this checked will remove them from the rare/blue
    pool.
  * Add Uniques to Legendary Pools
  * Add Unique Glitch Weapons to Legendary Pools
* **Add Undesirable Items to Pools (disabled by default)** - There are several
  items which aren't enabled by default, and I've labeled them as
  "undesirables."  You can enable them on an item-by-item basis in the last
  category, if you like.  These are:
  * Contraband Sky Rocket
  * Cracked Sash
  * Monster Trap
  * Probe
  * Springs' Oz Kit
* **Legendary Drop Rate Adjustment (defaults to 2x)** - Since we greatly
  increased the number of items in the Legendary pools, it seemed fair to
  double the drop rate.  This can optionally be reverted down to stock values,
  or increased further to 3x.

TODO
====

* This isn't actually necessarily a TODO, but I wonder if it makes sense to have
  an option in here to allow glitch weapons to spawn in the main game areas, like
  the BL2 version of this mod does with Gemstones. At the moment I've continued
  to be inclined to say no, since Glitch weapons aren't hard to come by in
  Claptastic Voyage, compared to gemstones from BL2, which were practically
  nonexistant.  It feels like adding glitches to the main game would be more the
  remit of something like Better Loot, which already does just that.  I could
  probably be convinced to add it as an option to this mod, though...

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

**v1.0.0**, July 27, 2018:
 * Initial public release
