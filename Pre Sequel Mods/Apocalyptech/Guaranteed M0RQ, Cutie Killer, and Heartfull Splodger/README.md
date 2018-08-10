Guaranteed M0RQ, Cutie Killer, and Heartfull Splodger
=====================================================

**NOTE:** This mod is now included as a basic part of TPS UCP 2.2, so if
you're using TPS UCP 2.2 or higher, there's no longer any reason to use
this mod directly!  (It won't hurt anything to have both enabled, though.)

There are three chests hidden around in the Claptastic Voyage DLC which
provide, respectively, the M0RQ shield, and the unique glitch weapons
Cutie Killer and Heartfull Splodger.  These chests are intended to only
be available once per playthrough, but some bug in Borderlands can
sometimes cause the chests to spawn already open, which prevents the
player from receiving the loot during the current playthrough.  This
mod simply makes it so that those chests will always spawn in an
openable state, so the player can always get that loot.

Note that technically this goes a little too far in the other direction --
the chests will now be available every time you start up TPS, so you can
access them more than once per playthrough if you want.

Usage
=====

This mod must be imported into BLCMM with `File -> Import single mod`.
Choose the file `Guaranteed M0RQ, Cutie Killer, and Heartfull Splodger.blcm`
and have at it!

TODO / Technical Details
========================

The game tries to manage the openability of these chests via three "Player
Flags" internally in the game data:

* `GD_Ma_Population_Treasure.PlayerFlags.PF_Ma_HiddenStash_01`
* `GD_Ma_Population_Treasure.PlayerFlags.PF_Ma_HiddenStash_02`
* `GD_Ma_Population_Treasure.PlayerFlags.PF_Ma_HiddenStash_03`

What seems to happen in the vanilla game is that the checks for these flags
end up believing that the flags are set, when really they shouldn't be.  This
mod just bypasses that check entirely, to say "this chest should be closed,"
but the *real* solution should really be to fix the check itself, so that the
one-open-per-playthrough is still enforced.  The checks happen inside the
following behaviors:

* `GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_01:BehaviorProviderDefinition_0.OzBehavior_HasPlayerFlag_36`
* `GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_02:BehaviorProviderDefinition_0.OzBehavior_HasPlayerFlag_38`
* `GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_03:BehaviorProviderDefinition_0.OzBehavior_HasPlayerFlag_50`

One thing I noticed inside the flag data itself is that `02` and `03` share
the attribute value `HashValue=1657936231`, whereas `01` has `HashValue=1368252839`.
Should that be unique to each flag?  Could that be related somehow?

In the end, I'm not going to bother actually looking into it any further,
but if any intrepid modder ends up figuring it out, I certainly wouldn't
mind hearing about it.

License
=======

This mod is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, August 5, 2018:
 * Initial public release
