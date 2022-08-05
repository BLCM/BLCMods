BL2 Happy Horizontal People Transporter©®
=========================================

This mod converts the Mongol to be the **Happy Horizontal People
Transporter©®**, a device which enables your enemies (and friends!)
to travel around Pandora in style, with the best vantage points on
the planet!  Despite the name, the **Happy Horizontal People Transporter©®**
is pleased to transport your foes vertically as well as horizontally,
returning them eventually back to the Pandoran surface with the knowledge
of a job well done, all thanks to the patented *Integrated Transport
Solutions™* module!

Perhaps once they've seen firsthand the fragility and beauty of the
world they call home, your enemies will return to the ground with a
friendlier, fresh perspective and a skip in their step!  Or they
might just be crankier and want to kill you even more.

The **Happy Horizontal People Transporter©®** does *no* damage to enemies
directly, and does not consume ammo like ordinary rocket launchers.
Feel free to provide *Integrated Transport Solutions™* to the denizens
of Pandora, free of charge!

By default, the **Happy Horizontal People Transporter©®** will only
affect your foes on Pandora, but it can be configured to provide you and
your co-op partners with a fast and easy way to navigate the Pandoran
landcape.  Note that due to fluctuations in the local digistruct firmament,
this configuration option will cause singularity grenades to affect you and
your teammates as well, so be careful out there!

The *Integrated Transport Solutions™* module is configured by default to
provide a nice quick jaunt across the landscape for 7.5 seconds, but can
optionally be configured to last up to 30 seconds, or as short as 2.5.
*You* are in control of your destiny, and the destiny of your foes, with
*Integrated Transport Solutions™!*

The **Happy Horizontal People Transporter©®** is redeemable easily with
the following Gibbed code:

    `BL2(hwAAAACJ2gBCJ4M/ChEIVKIYQ2GKogDFGgoIFBwo/v+fovj/34ri)`

It can also be found wherever a Mongol might have otherwise been found.

Usage/Installation
==================

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `BL2 Happy Horizontal People Transporter.blcm` and have at it!

If you're using this mod along with my `BL2 Faster Rockets and Gyrojets`
mod, make sure that HHPT is loaded *after* the Faster Rockets mod, so that
the HHPT's projectile speed is set properly.

More Technical Notes
====================

Okay, enough of that pseudo-in-game narration above; here's a few more
things to know about the gun:

- Since this doesn't act like a regular gun, I've partlocked it all to
  hell, but it shouldn't sanity-check any Mongols already in your inventory.
- It *does* use a nonstandard body, though, so the HHPT itself may get
  sanity checked if you start your game without this mod installed.  (Just
  disable sanity checks using Hex Multitool, it's nicer that way.)
- If you want a *proper* HHPT, on account of the partlocking, use the
  Gibbed code, or convince one to world drop.  Accessories which alter
  projectile speed or the like could potentially get in the way of the
  transport effectiveness.  I've not actually tested it out on anything
  other than the locked accessory.
- The HHPT uses the same method that World Burn does, to prevent accessory
  prefixes from showing up in the weapon name, and uses a DLC5-specific
  object to do so.  AFAIK this gun should work fine without DLC5 installed,
  though - the worst-case scenario should be that you'll wind up with an
  accessory prefix mucking up your otherwise pristine weapon title.
- Some "bigger" enemies (like some Adult Bullymongs) aren't really affected
  by this.  Presumably I could increase the effectiveness, but that'd be
  buffing singularity grenades too, so I don't really care to.
- There's basically no difference between a level 1 HHPT and a level 90
  HHPT, so don't go looking for anything more effective at higher levels.
  The Gibbed code just gives you a level 1 weapon.
- Unfortunately, singularities don't affect flying enemies.  No tossing
  Rakk around, alas!

TODO
====

- It would be nice if the singularities would affect NPCs as well, but
  I haven't found a way to do that yet.
- The skin is pretty lame, but I don't really care enough to spruce it up,
  myself.
- I would love to figure out a way to spawn a working singularity without
  having to spawn a whole Singularity Grenade projectile.  I can get the
  explosion effect itself, of course, but actually having it apply to any
  enemies seems to require binding variables inside a BPD, which nobody's
  come close to figuring out yet.

License
=======

This mod is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

See [COPYING-mods.txt](../COPYING-mods.txt) for the full text.

Changelog
=========

**v1.0.2** - November 18, 2019
 * Explicitly lock the main projectile to its intended speed, in case the user has
   a mod enabled which alters it (such as my Faster Rockets and Gyrojets mod).  That
   way there'll at least be an overwrite alert in BLCMM.

**v1.0.1** - July 29, 2019
 * Changed name to include `BL2`, so there's no confusion between this and
   the TPS version.
 * Fixed the displayed verison number inside the mod, too.

**v1.0.0** - July 26, 2019
 * Initial Release
