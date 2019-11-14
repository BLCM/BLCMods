TPS Mega TimeSaver XL
=====================

This mod speeds up nearly all the noticeably-slow interactive objects
that you use throughout TPS by 5x (in general), most notably:

 * Computers / Switches
 * Containers
 * Doors / Gates
 * Fast Travel Stations *(mostly just for after the Felicity Rampant fight)*
 * Grinder
 * Lifts / Elevators / Transporters
 * Oxygen Generators
 * Slot Machines
 * Vehicle Aimations

This mod obsoletes one of my previous mods: *TPS Container TimeSaver XL*.
The container section of this mod is identical to the old one, so it won't
actually *hurt* anything to have both installed, but you may as well delete
the old one anyway.

The mod is *primarily* focused on the things you directly interact with,
so there's a number of things which are generally **not** sped up, such
as: NPCs performing actions or moving around; sequences like a gate
opening to spawn a new enemy; dialogue; or anything relating to cutscenes.
(If you want faster cutscenes, just use FromDarkHell's Cutscene Remover to
skip them entirely.)

The vehicle speedup section here owes a lot to Gronp's
[Faster Vehicle Animations mod for BL2](https://www.nexusmods.com/borderlands2/mods/175).
Thanks for the pointers on that!

Some other notable things sped up by this mod (this is not an exhaustive
list):

 * Moonshot Bullet in the prologue
 * The Library transformation in Jack's office
 * The conveyor belt speed for the missions To The Moon and Lock and Load
 * The AI Download during Things That Go Boom
 * Rotating the methane pipes in Outlands Spur
 * Much of the Felicity construction sequence in Titan Robot Production Plant
 * The Bunch of Ice Holes mission has been sped up a bit
 * The paint barrel sequence during Rose Tinting

Things NOT Sped Up
------------------

There are a few mission-related things which could probably
be sped up a bit but didn't seem worth the effort:

 * Most of the doors in the opening sequence in Helios Station weren't
   touched, since they're basically all part of scripted dialogue
   segments.
 * If you side with Torgue in "Torgue-o! Torgue-o!", the destruction
   sequence intentionally takes a long time; I left that as-is.
 * The methane-dumping animations in Outland Spur weren't touched;
   they were already reasonably quick.
 * There's a lot of waiting for Felicity dialogue in Pity's Fall, but
   maybe that's a bit outside the remit of this mod?  I bet the
   door-openings could probably be triggered earlier.  In the end I
   don't care enough to start digging through kismets, though.
 * There's a bit of delay on opening the drawer of the slot machine
   in Wiping the Slate which I wasn't able to speed up.  Whatever.  Also
   didn't touch any of the rocket-launch stuff in that mission, since
   nothing waits on any of those animations.
 * Tony Slows' tour of spaceship wreck remnants has been left alone.
 * The rocket launch in Home Delivery has been left alone.
 * A few segments of Felicity's construction were either left alone or
   not buffed as much -- most notably the very last couple of sequences --
   though in general it should be much snappier than in vanilla.
 * Claptrap trying to get Jack's office door open has been left as-is.
 * Many of the animations from It Ain't Rocket Surgery were untouched.
   Most of them were already plenty fast.
 * The automated moving platforms and things in Veins of Helios were
   left untouched, since it'd be harder to time jumping onto them, etc.
 * Some elements of the mission To The Moon haven't been changed,
   though the conveyor has been sped up a fair amount.
 * The garbage bot in Veins of Helios during the mission "Quarantine:
   Infestation" has been left alone, since I couldn't figure out how to
   speed up unlocking the door, regardless of the animation speed.
 * The airlocks in Veins of Helios aren't sped up as much as I'd like,
   on account of not being able to find the between-door delay vars.
 * The mission Don't Get Cocky was left as-is
 * The timed fight during Eye to Eye (right outside Eye of Helios) was
   left alone; it could certainly be sped up, but it's a fun fight.
 * The two Captain Chef missions were left alone -- they could probably
   use some speeding up, but there are enough events happening in there
   that I didn't feel like sorting through it all.
 * The Eridian doors in Tycho's Ribs were left alone, partially because
   they're already pretty speedy, but also because I couldn't find the
   right vars to speed them up anyway.
 * Very little in Claptastic Voyage needed speeding up, in the end -- a
   lot of things which *could* be sped up had to wait on dialogue anyway,
   so wasn't really worth looking into.  I did want to speed up the Data
   Stream transporters a bit, but couldn't figure out the vars to change,
   so that's been untouched.

Usage
=====

This mod should be imported into BLCMM using `File -> Import single mod`.
Choose the file `TPS Mega TimeSaver XL.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`,
which makes use of some data classes from my [FT/BLCMM Explorer](https://github.com/apocalyptech/ft-explorer)
project.  You'll need to copy (or symlink, if you're on Linux or OSX) that
project's `resources` and `ftexplorer` dirs into this one, to run the
generation script.  The script also makes use of `modprocessor.py` from my
main BL2 mods directory, so copy (or symlink) that as well.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, November 14, 2019:
 * Initial public release
