BL2 Invulnerable Escortees
==========================

There are a few missions in BL2 in which you must keep either an enemy or
an ally alive, or else fail the mission.  This mod makes those escortees
invulnerable (or at least effectively invulnerable), so you no longer
have to worry about inadvertantly failing the mission.  This is most
useful for the escort missions where your charge is hostile, because the
player can no longer accidentally kill them while taking care of the
other enemies in the area.

The full list of affected escortees is:

 * **Enrique**: Tina's pet in the Torgue DLC, during the mission
   "Walking the Dog"
 * **Flesh-Stick**: Tina's nemesis during the "You Are Cordially
   Invited" quest line in Tundra Express
 * **Hacked Overseer**: The hacked constructor from the mission
   "Statuesque" in Opportunity
 * **Mosstache**: Aubrey's instrument of vengeance in the Dragon
   Keep DLC mission "Tree Hugger"

One enemy only receives a 25x health buff (bringing it a bit past
"badass" level) rather than the usual buffs:

 * **Der Monstrositat**: The Borok Dietmar wants you to trap in the
   Hammerlock DLC mission "Still Just a Borok in a Cage."  UCP makes
   Der Monstrositat respawnable, and an alternate source for the
   Chopper, so full invulnerability seems unwarranted if you're
   using UCP.  The default is a 25x health boost (Badass Boroks
   are 16x).  You can optionally choose to make Der Monstrositat
   effectively invulnerable anyway, if you want.

Additionally, one more is disabled by default:

 * **Murderlin's Son**: The tower you must defend in the Dragon
   Keep DLC quest "The Magic of Childhood."  Making the tower
   invulnerable makes this quest pretty pointless: you can win
   by just sitting there doing literally nothing.  So, it's
   disabled by default, though you can choose to make the tower
   invulnerable anyway if you like.

Note that Maya's "Converge" skill has a fairly unique damage type
definition -- most likely a subtle bug in the game code, honestly --
and the damage from Converge cannot by default be blocked by any
enemy.  The increased health pools given to these escortees should
protect them from casual Converging, though.

Usage
=====

This mod should be imported into BLCMM using `File -> Import single mod`.
Choose the file `BL2 Invulnerable Escortees.blcm` and have at it!

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

**v1.1.0**, August 18, 2019:
 * Changed Der Monstrositat to only have a 25x health boost by default, since
   UCP makes it a respawnable monster.  The original 99999999x boost is
   still available as an option.

**v1.0.0**, August 14, 2019:
 * Initial public release
