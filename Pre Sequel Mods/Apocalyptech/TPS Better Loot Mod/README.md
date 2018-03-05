TPS Better Loot Mod by Apocalyptech
===================================

Work in progress!

**WARNING:** This mod contains some statements which can generate gear
which the vanilla game doesn't think is valid.  If you have some of
this gear in your inventory and start the game without having this
mod enabled, the engine will remove those items from your inventory.
If you see this, be sure to `Alt-F4` out of the game to prevent it
from saving over your savegame.  The sections which could generate
these kinds of gear are contained entirely within the `Volatile Changes`
folder.

Mod Overview
------------

* Adds all legendaries + uniques (weapons, grenade mods, class mods,
  shields, oz kits) into the global "legendary" loot pools, so
  you'll start seeing those much more frequently.
* Loot will skew much more rare, in general.  You should expect to see
  those legendaries/uniques far more frequently than in vanilla TPS.
* Glitch weapons spawn in the main game
* Makes Moonstones drop 2x more often
* Luneshine weapons will drop in all world drop pools (this is identical
  to some functionality in UCP)
* Legendary/Unique weapons are guaranteed to have Luneshine, unless
  they have specific custom accessories in that slot (ie: Marek's Mouth,
  Cry Baby, Longnail, Heartfull Splodger, and Cutie Killer)

Compatibility
-------------

This'll be interesting - The TPS UCP touches a lot of the same stuff
that we'll be touching here.  Will figure it out as I go...

Loot Purposefully Excluded from Pools
-------------------------------------

There's some gear which I felt shouldn't be in the pools at all.  I am
quite willing to hear counterarguments; my mind could probably be pretty
easily persuaded otherwise if someone feels strongly about it.

* Springs' Oz Kit
* Cracked Sash (Shield)
* Contraband Sky Rocket grenade *can* spawn, but has a much decreased
  chance compared to all the other legendaries.

TODO
----

* Check legendary drop pools
* Legendary COM pool seems to be almost entirely Celestial.  Occasionally
  Chronicler, and no Eridian Vanquishers.  Figure that out.

Credits
-------

* A set of statements to allow Luneshine spawns in the world drops was
  taken from UCP.

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

**v1.0.0**, (tbd):
 * Initial public release
