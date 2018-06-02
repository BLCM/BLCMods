Stalkers Use Shields
====================

Stalkers already use shields in Borderlands, of course.  This mod will
equip them with "real" shields, of the sort your character finds and equips
throughout the game, though.  Optionally, and for a greater challenge, you
can opt to equip them with only Maylay shields.

**WARNING:** There seems to be some interaction between Stalkers and Maylay
shields where the Roid damage increase may be far in excess of what's
listed on the card.  A Stalker with a depleted Maylay shield is likely to
hit like a ton of bricks.  You've been warned!

This mod was basically taken straight out of my Cold Dead Hands mod.  If
you're already running Cold Dead Hands, the exact same functionality is
available in there, so there's no reason to run both.  The main difference
between the two is that the shield-using stalkers in Cold Dead Hands will
drop their shields, whereas the Stalkers in this mod will not.

Requirements
------------

This mod should be able to be used mostly on its own, but it does require
one specific category of UCP to be active:

* `Loot Pool & Drop Changes -> Skinpool Fixes (Don't uncheck this)`

This is required to free up the custom loot pools that we use to equip
stalkers with.  If for whatever reason you'd like to run this mod by itself
without UCP, make sure to at least enable/copy that folder over.

Usage/Installation
------------------

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Stalkers Use Shields.txt` and
have at it!

### Configuration

The three main categories contain some options to customize shield quality
in various ways, when loaded into FilterTool/BLCMM:

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
  chosen.  Note that there seems to be some strange interaction between
  Stalkers and Maylay shields which make them do far more damage than the
  buff listed on the shield card, so beware!  Stalkers with depleted Maylay
  shields are likely to be quite deadly.

Compatibility
-------------

This mod is compatible with UCP, and in fact requires that UCP's skinpool
changes be in place.

The mod can be used at the same time as my Cold Dead Hands mod, though
there's not much reason since it's already included inside Cold Dead Hands.
If you use this at the same time as CDH, Stalkers will *not* drop their
equipped shields.

Mod Construction / Implementation Details
-----------------------------------------

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in FilterTool/BLCMM as well, once it's
been imported.)*

This mod is actually generated using a simple little Python script named
`generate-source.py`.  The script makes use of `hotfix.py` from the parent
directory.  You'd need to copy (or symlink, if you're on Mac or Linux)
`hotfix.py` into this directory in order to run the script.

To generate the end result file, I actually run the small shell script
`create.sh` in this directory, which just does the following:

    ./generate-source.py && ../conv_to_mod.py -f "Stalkers Use Shields"

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

**v1.0.0** - Currently unreleased!
