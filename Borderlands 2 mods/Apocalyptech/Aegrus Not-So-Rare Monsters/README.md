Aegrus Not-So-Rare Monsters
===========================

This is a real simple mod which just alters the spawn rates of the "rare"
creature types in Sir Hammerlock's Big Game Hunt.  This is really only
useful if you're looking to complete the
[I Like My Monsters Rare](http://borderlands.wikia.com/wiki/I_Like_My_Monsters_Rare)
mission without having to do any extra farming.

There are two options (presumably mutually-exclusive, but that doesn't
seem to work yet) when loaded into FilterTool:

1. Normalize spawn rates so that they're about as common as other
   creature types (slightly less for Drifters, since there's no
   other Drifter types).  This is the default.
2. Nearly-Guaranteed spawns for all rare types.  You'll still see
   the occasional normal creature (the first one spawned in any given
   den seems to often be regular), but in general nearly every
   creature you see will be of the rare type.  This isn't enabled by
   default.

TODO
====

* As mentioned above, I can't actually seem to get the mutually-exclusive
  thing to work properly when imported into FilterTool.  It just seems to
  ignore the flag.  I think maybe it's got something to do with the patches
  being hotfix rather than `set` style?  Who knows.  If you check both, note
  that it's the second (nearly-guaranteed spawns) which would take precedence.
