Stalkers Use Shields
====================

Stalkers already use shields in Borderlands, of course.  This mod will
equip them with "real" shields, of the sort your character finds and equips
throughout the game, though.  Optionally, and for a greater challenge, you
can opt to equip them with only Maylay shields.

This mod was basically taken straight out of my Cold Dead Hands mod.  If
you're already running Cold Dead Hands, the exact same functionality is
available in there, so there's no reason to run both.  The main difference
between the two is that the shield-using stalkers in Cold Dead Hands will
drop their shields, whereas the Stalkers in this mod will not.

Requirements
------------

As of v1.1, this mod should be able to be used on its own, and does not
require any UCP config to run.

Usage/Installation
------------------

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `Stalkers Use Shields.blcm` and have at it!

### Configuration

The three main categories contain some options to customize shield quality
in various ways, when loaded into BLCMM:

* **Legendary Pool Setup**: Stalkers have the ability to use legendary
  shields, and as with my Better Loot and Cold Dead Hands mods, this
  section can optionally add unique and seraph shields into the global
  "legendary" shield pool, so Stalkers can use them.  Note that this will
  affect shield drops for the rest of the game, too!  By default, uniques
  and seraphs are added in.

* **Stalker Shield Quality**: This is a mutually-exclusive category (so you can
  only choose one of the options), and defines how good the shields are.
  The default ("Excellent") is more or less at the Better Loot mod's
  "Lootsplosion" levels, so powerful shields on Stalkers will be quite common.

* **Shield Selection**: By default, Stalkers will just pull from the main
  shield pools, but you can optionally have them *only* use Maylay shields
  in here.  This is another mutually-exclusive category, so only one can be
  chosen.

Compatibility
-------------

This mod is compatible with UCP, and should in general be compatible with
anything which isn't also changing Stalker equipment.

The mod can be used at the same time as my Cold Dead Hands mod, though
there's not much reason since it's already included inside Cold Dead Hands.
If you use this at the same time as CDH, Stalkers will *not* drop their
equipped shields.

Mod Construction / Implementation Details
-----------------------------------------

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is actually generated using a Python script named `generate-mod.py`.
The script makes use of `modprocessor.py` from the parent directory.  You'd
need to copy (or symlink, if you're on Mac or Linux) `modprocessor.py` into
this directory in order to run the script.

Bugs
====

Known issues with the mod:

* As a side-effect of the way we have to make use of loot pools, skin drops
  from various enemies will be broken (it's that or break skin rewards for
  challenges/missions).  This mod breaks skin drops for skags and
  chubbies/tubbies.

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

**v1.1.1** - July 22, 2018
 * Included fix, thanks to 55tumbl, so that enemies using Roid/Maylay shields
   receive the intended melee damage boost, instead of the extremely powerful
   attacks that they were doing.

**v1.1.0** - July 18, 2018
 * Converted to BLCM format *(Requires BLCMM now, will not work with FilterTool)*
 * Update to use the same skinpools as BL2 Cold Dead Hands
 * Include skinpool reassignments, so no part of UCP is required
 * Cosmetic change: Condensed the rarity choice comments so that regular
   and badass enemy equip chances are printed on the same line.

**v1.0.0** - June 2, 2018
 * Initial Release
