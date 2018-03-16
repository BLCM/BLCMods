BL2 Better Loot Mod by Apocalyptech
===================================

This mod aims to make loot in Borderlands 2 "better" in general.  It's
essentially a cheat mod, intended for those BL2 players like myself who
tend to play in Normal most of the time, dislike grinding, get bored easily
by the uninteresting and drab loot that typically gets dropped in-game, and
who often end up just resorting to Gibbed to be able to play around with
some better gear.  The goal, personally, was to get the loot drops in-game
to a point where I never felt tempted to open up Gibbed.

This patch is set up to play nicely with FilterTool, and basically
everything in here can be toggled on or off inside FilterTool as you'd
hope, on an item-by-item basis.  Basically every bullet point in the
"Overview" section is its own "folder" once imported into FilterTool.

**NOTE:** One known incompatibility is with Shadowevil's "VaultHunter" mod.
Best not to use both of them at the same time.  See the "Compatibility"
section, below, for details.

Usage/Installation
------------------

The recommended way to use this mod is with FilterTool/UCP.  In FilterTool,
select `Developer Tools` -> `Add Single Mod` and then select one of these
two files:

* `BL2 Better Loot Mod (Lootsplosion) - UCP Compat` - Default drop weights
  which I'm personally happy with.  Many folks may find these a bit extreme.
  This version probably makes more sense in Normal mode than it does in UVHM.
* `BL2 Better Loot Mod (Reasonable Drops) - UCP Compat` - More reasonable
  drop weights.  This version may be more suitable for UVHM, where lots
  of Legendary drops might be excessive. *(Work in Progress - needs
  tweaking+testing, etc)*

Once the mod has been added, you'll have a new folder for this mod
underneath the `mods` folder at the bottom, and can turn parts on or off at
will.

If for whatever reason you don't want to use FilterTool, there are also
standalone versions at `BL2 Better Loot Mod (*) - Standalone`,
and an offline standalone version at `BL2 Better Loot Mod (*) - Standalone Offline`.
Simply copy the file into the game's `steamassets/binaries` directory with
an easy-to-type filename, and then run `exec <filename>` from the console
to load it on its own.  It works quite well by itself.

The only actual differences between the UCP and Standalone versions are
that the "Standalone" versions contain all of the original Gearbox hotfix
data, and set up the hotfix commands for execution by Borderlands, whereas
the "UCP Compat" version lets FilterTool/UCP take care of that for you.

All versions are fully FilterTool compatible.

Mod Overview
------------

*(Note that the "Reasonable Drops" variant of this mod won't be **quite**
as great as some of these statements imply, though the probabilities of
getting better gear should still be much better than in the vanilla game.)*

Specifically, this mod does the following:

* Adds all legendaries/uniques/pearls/seraph items (weapons, grenade mods,
  class mods, shields, relics) into the global "legendary" loot pools, so
  you'll start seeing those much more frequently.
* Loot will skew much more rare, in general.  You should expect to see
  those legendaries/uniques/pearls/seraphs far more frequently than in
  vanilla BL2.
* Adds the "Alignment" Class Mods from the Dragon Keep DLC into the global
  Class Mod drop pools (and makes those COMs always drop at at least blue
  rarity).
* Adds Gemstone-rarity weapons into the E-Tech weapon pools.
* Darts and Spikers drop far less frequently in the E-Tech pools.  *(I
  suspect this might annoy some folks; I could probably be convinced to
  undo that)*
* Normalizes weapon type drops a bit.  *(Decreases pistol drop chance,
  increases all other weapon types.)*
* Lootable Container Changes:
  * "Regular" treasure chests will always provide at least blue-rarity gear,
    and has a decent chance of including stuff from the legendary pools.
  * "Epic" treasure chests have an extremely high probability of dropping
    from the legendary pools.
  * Mordecai's Stash (from the mission The Good, The Bad, and the Mordecai) has
    been changed to only drop sniper rifles, and vastly improves the gear
    quality.
  * Roland's Chest in Sanctuary has been changed to only have loot pools with
    weapons, and is guaranteed to have at least a couple legendaries.
  * Dice Chests (from the Tiny Tina DLC) will have a small chance of containing
    legendary loot on a "very high" roll.
  * Captain Scarlett DLC and Big Game Hunt DLC endgame chests were converted
    to Epic chests.
  * Non-Mimic chests from Dragon Keep DLC will partially pull from the Epic
    chest pool as well.
  * When lockers spawn gear, they will always be blue-rarity.  *(Previously
    lockers had a chance to spawn even legendaries, so some could potentially
    see this as a drawback)*
  * Safes have been improved: Eridium configurations are far more likely, cash
    quantities have been improved.  Gear drop chances have been dropped
    somewhat, but gear from safes will always be legendary.
  * Fixes some "shield" loot configurations which had an error and would never
    spawn, previously.
* Makes Eridium drop 2.5x more often
* Makes Torgue Tokens more numerous when dropped
* Boss drop pools are generally improved, and bosses are guaranteed to drop as
  many items from their unique drop pool as are in that pool.
  * Bosses with just a single unique drop will therefore be guaranteed to drop
    that item.
  * If a boss has more than one in their drop pool, you may get duplicates
    of one rather than one of each.
* Raid Bosses will drop better loot, and will drop as many unique items as are
  in their pool.
* Seraph Crystals will drop from Seraph Guardians even in Normal mode, and the
  amount of Seraph Crystals have been increased.
* Fixes/Changes to some enemies' drop pools:
  * Badasses are guaranteed to drop some loot
  * Chubby drop pool has been improved
  * Some "Badass" enemies weren't actually pulling from the badass drop pool,
    which has been fixed:
    * Badass Bedrock Bullymongs
    * Badass Boroks
    * Badass Knights
    * Badass Fire Archers
    * Undead Badass Psychos
    * Badass Yeti
  * A few more standard enemies have also been set to drop from the badass pool:
    * Shirtlesss Men
    * Gluttonous Thresher *(actually drops from the "super" badass pool)*
    * Sinkhole
    * Rakkman
    * Mick Zaford
    * Papa/Jimbo Hodunk
    * Jack's Body Double
    * Deputy Winger
    * Mortar
    * Bonehead 2.0
    * Roscoe
    * Bulstross
    * Arguk the Butcher
    * Skeleton Giants *(as if the Dragon Keep DLC needed more loot)*
    * Individual Handsome Sorcerer stage bosses
    * Bridget Hodunk and Colin Zaford *(from the Wedding Day Massacre Headhunter Pack)*
    * Giant Craboid
  * Then a few other tweaks to certain enemies:
    * Laney's Dwarf companions will drop crystals, and have a good chance of dropping
      a gemstone weapon between 'em.
    * The Warrior's non-unique drops have been improved slightly *(though they were
      already pretty good with our other buffs)*.
    * Witch Doctors (both in Big Game Hunt and Son of Crawmerax) will drop an Eridium
      stick, and have a pretty good chance of dropping a Relic as well.
    * Elite Savages are guaranteed to drop loot (though just from the standard pool)
    * In the vanilla game, the Tributes from the Wattle Gobbler Headhunter Pack are
      mostly set to drop from the badadss loot pool, but three weren't set to drop any
      loot at all.  This mod fixes the three to match all the others.
    * The Loot Leprechaun (from Wedding Day Massacre) will drop from the Epic Chest
      pool, rather than the regular treasure chest pool.
    * The BLNG Loader (from Wedding Day Massacre) will drop from the badass pool and
      also drop a whole bunch of money.  I've always been mystified why it didn't
      drop a ton of money from the start.
* Improved gifts received in The Talon of God (from Sanctuary residents) to
  be purples and gemstones.
* Remove early-game loot restrictions.  This is actually a superset of the
  similar feature already present in UCP 4.0.  This version enables spawning
  of basically everything from the beginning, including all grenade types,
  relics, class mods, rocket launchers, etc.  Both this and the UCP 4.0
  "Remove Loot restriction in the beginning areas" mods can be active at the
  same time with no ill effects -- it'll just mean that the relevant commands
  get executed twice.  Note that if you *don't* have either this or UCP
  enabled on your game, the early game will end up dropping *no* gear, due
  to our rarity changes.

There's also a couple options which are disabled by default which I used primarily
to test out the drop pools while tweaking probabilities, but I left in in case
anyone feels like *really* going overboard with loot.  One will cause enemies to
always drop loot when killed, and the other will cause any regular enemy loot drop
to drop five items instead of just one.

An alternative to the guaranteed-loot-drop setting is an improved loot drop, which
will double the drop rate of standard enemies.  Like the guaranteed-drop version,
this is disabled by default.

Compatibility
-------------

### UCP ###

This mod is mostly compatible with UCP 4.0, with three known exceptions:

* "`Better Enemy Drops -> Regular Enemy Drop Improvements -> BLNG Loader`" in this
  mod will override UCP's "`Loot Pool & Drop Changes -> Specific Loot Changes ->
  Add Sledge's Shotgun to BLNG Loader`"
* "`Better Enemy Drops -> Raid Boss Drop Improvements -> Hyperius`" in this mod
  will override UCP's "`Loot Pool & Drop Changes -> Specific Loot Changes -> Add
  Black Hole and remove the Kiss of Death from Hyperius`"
* "`Better Enemy Drops -> Raid Boss Drop Improvements -> Hyperius -> Clean Up
  Seraph Pool`" in this mod will override the loot pool changes in UCP's
  "`Loot Pool & Drop Changes -> Specific Loot Changes -> Increase Hyperius' Seraph
  drop chance and add all DLC 1 Seraphs`".  Unselecting just "`Clean Up Seraph
  Pool`" in this mod but leaving the rest of our Hyperius section intact
  will still give a 100% drop rate for Seraphs on Hyperius.
* "`Better Enemy Drops -> Better Miscellaneous Boss Drops -> Knuckledragger
  Improvements`" in this mod will override the Knuckledragger portion of UCP's
  "`Loot Pool & Drop Changes -> Specific Loot Changes -> Make Knuckle Dragger /
  Boll be able to world drop`".  Our version is more powerful (drops from the
  badass pool, rather than standard).

### Shadowevil's "VaultHunter" mod

**NOTE:** This mod and Shadowevil's "VaultHunter" mod, which creates a
Legendary-level Vault Hunter's Relic, don't play very well together,
especially with Raid boss drops.  The combination has been known to
sometimes crash Borderlands after defeating the Ancient Dragons, in fact,
and legendary drops will be *far* more frequent than is useful.

I'm pretty sure that this mod makes the vanilla game's "Vault Hunter's
Relic" completely useless, but if you're using this mod, you certainly
won't miss it.

### Hemaxhu's "More Chubbies" mod

Hemaxhu's "More Chubbies" mod isn't *incompatible* with this one, but you
will almost certainly find it to be quite excessive if Chubbies are spawning
more frequently.  The best thing to do if using More Chubbies is probably to
disable this mod's Chubby buffs, at least partially.  There are two toggles
you can use in this mod:

* `Better Enemy Drops > Better Badass Pool Definitions > Chubby Enemies`
* `Better Enemy Drops > Boss Drop Improved Quantities > Chubby Enemies`

### SirUmnei's "COM Overhaul Pack" (and possibly other mods which touch COMs)

The COM Overhaul Pack, in conjunction with this mod, will end up creating
items which will get deleted by Borderlands after you save/quit.  You should
be able to avoid this by turning off this mod's `Loot Pool Tweaks -> Better
Class Mod Rarity Drops -> Force Alignment COMs Blue And Higher`.

### Other Mods

Obviously this mod will conflict with other mods which play with the same
variables.  I know that Hemaxhu's "Better White Chests" would conflict with
this, for instance, and possibly other mods in Hemaxhu's "Chest Mods"
folder.  FromDarkHell's collection in the "Loot Drops" folder likewise will
probably conflict.

This mod duplicates some of the statements in Koby's "Level 1 UVHM", to let
all item/weapon parts spawn starting at level 1 (though I'd autogenerated
the ones here, rather than copying from Koby) - the two should coexist without
problems, though, since the worst case scenario is just that the same command
gets executed twice.

Loot Purposefully Excluded from Pools
-------------------------------------

There's some gear which I felt shouldn't be in the pools at all.  I am
quite willing to hear counterarguments; my mind could probably be pretty
easily persuaded otherwise if someone feels strongly about it.

* Cracked Sash (Shield)
* GOTY/Preorder/Whatever starting game loot:
  * "Gearbox" themed guns (AR/SMG/Sniper)
  * Contraband Sky Rocket
  * Vault Hunter's Relic
* Captain Blade's Midnight Star
* Blue-rarity Magic Missile *(purple rarity will still spawn -- they're
  technically different items)*
* "ERROR MESSAGE" Ahab (the one used by Master Gee).  Regular Ahabs will
  still spawn, though.

There's also a few drop pools / containers / etc which I've purposefully
left alone:

* Bandit Coolers
* Money Boxes
* Laundry Machines / Toilets / Cardboard Boxes
* Dumpsters
* Loot Midgets

Some other stuff not done:

* Scaylion drops are rather anemic compared to everything else in the
  Hammerlock DLC, but the Hammerlock DLC is kind of ludicrous with loot
  anyway, so I'm leaving them the way they are.
* Badass Giant Burning Broomsticks will continue to drop from the standard
  enemy pool rather than the badass pool.  There's dozens of those things
  all at once and it'd be ridiculous.
* In general I've not touched skin/head drop rates at all.  There's a few
  Hammerlock DLC creatures which have a rare skin drop which I ended up
  making guaranteed just because I was already in there looking for
  uniques/legendaries, but that's about it.
* From the Wedding Day Massacre Headhunter Pack: Ed, Stella, and Innuendobot
  don't actually drop anything -- I felt that was probably approprate and
  left them alone.

Other Recommended Mods
----------------------

There's a few things which I'd considered adding to this mod, but were already
well-covered in other mods, so instead I'll just mention them here.

* EmpireScum's "ButtStallion" will make Butt Stallion's drops in Flamerock Refuge
  much better (can choose between blue-or-higher, or all-gemstone).
* JimRaven's "#MakeVendorsGreatAgain2017" improves vendor stocks across the game.
* Hemaxhu's "Better Quests" will improve quest rewards for the missions which
  don't already have good rewards.

TODO
----

* I haven't done much testing in TVHM/UVHM, though it should be fine in
  those modes.
* Can we increase boss drop counts depending on player count?
* Untested components from Torgue DLC *(I'm afraid that's my least favorite
  DLC, to the point of not really liking it much, so I suspect that these
  may go untouched)*:
  * Pyro Pete's initial non-raid drops
  * Piston drops (just Slow Hand, I figure the mini-lootsplosion after is
    good enough to not bother tweaking his actual drop any more)
  * Torgue Biker Gang drops are a little weird - there's an extra drop which
    happens outside of their weighted drop pool, but I can't seem to figure
    out where that is.
  * I think Biker Badasses, etc, have pretty anemic drops at the moment.
  * In order to retain UCP compatibility, we had to alter how we guarantee
    Piston's Slow Hand drop.  This remains untested.
* Looks like our recent changes to the weighted pools have ended up letting
  bandit coolers and other more "regular" containers like that get good
  loot...  I think I actually preferred those being kind of crappy; look
  into that.

Other Notes
-----------

It's perhaps worth mentioning that while this mod does a great job in most
of the game (IMO), in Normal mode at least, the amount of loot can get
pretty absurd when you're in any area which can generate a lot of Badasses
or the like.  The Hammerlock and Tiny Tina DLCs, in particular, were already
very generous with loot, and this mod steers them into ridiculousness.  The
last few stages of Murderlin's Magic Slaughter end up dropping enough loot
to cause some noticeble FPS hits on my system in fact:

![Pictured: A Bit Much.](excess.png)

Digistruct Peak is a little ridiculous as well, on account of all the bosses
and Badasses.

Mod Construction / Implementation Details
-----------------------------------------

I actually generate this mod using a simple little Python script named
`generate-source.py`, which enables me to do things like set the rarity
drop levels from a single location at the top of the file, and have it
apply to a number of different objects throughout the game.  That script
outputs to a human-readable multiline text file which can't actually be
read directly by FilterTool/Borderlands -- it must be processed by my
`conv_to_mod.py` script which you'll find in the parent directory.

The generation script makes use of `hotfix.py` from the parent directory.
You'd need to copy (or symlink, if you're on Mac or Linux) `hotfix.py`
into this directory in order to run the script.

To generate the end result file, I actually run the small shell script
`create.sh` in this directory, which effectively just does the following:

    ./generate-source.py && \
        ../conv_to_mod.py -f "BL2 Better Loot Mod by Apocalyptech - UCP Compat" && \
        ../conv_to_mod.py -f "BL2 Better Loot Mod by Apocalyptech - Standalone" && \
        ../conv_to_mod.py -f "BL2 Better Loot Mod by Apocalyptech - Standalone Offline"

*(It's actually slightly more complicated now that I'm exporting multiple
profiles of the same mod (Lootsplosion vs. Reasonable), but that's basically
what it does.)*

Credits
-------

I've taken various ideas and snippets from a few other mods:

* Lifting early-game loot restrictions came directly from UCP, though I since
  expanded that section quite a bit.
* Setting guaranteed drops for the vast majority of bosses in-game, via
  two nicely-concise statements, came from JimRaven's "FarmFest"
* Orudeon's "Gemstone Loot Pools" clued me in that the main Gemstone pool in
  the Tiny Tina DLC is heavily weighted towards Pistols.
* FromDarkHell's "BL1Loot" provided a great index of gear for my own similar
  addition of uniques/pearls/seraphs into the legendary pool (though I went
  about it slightly differently)

I'd also like to thank the fine folks in Shadow's Evil Hideout #borderlands-modding
Discord channel for putting up with all my noobish questions.

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

**v1.2.0**, (tbd):
 * Fixed an issue where *Plan B* and *Bright Lights, Flying City* wouldn't reward
   Weapon Slot SDUs on Playthrough 1.
 * Buffed "weighted" pools used by some enemies for drops, to be in line with the rest
   of the mod's drop weights (Marauders being the most obvious example).
 * Changes in the "Reasonable Drops" variant:
   * Nerfed chances of bosses dropping unique gear
   * Nerfed relic drops a bit
 * Set Grenades and Rocket Ammo to be available in the early game, both from vendors
   and world drops
 * Buffed Knuckledragger's drops: will drop from the badass pool, and his custom
   pistol drops will use our improved weights rather than the vanilla game weights.
 * Buffed the early-game shotgun chest (on leaving Windshear Waste) to use our
   custom weights rather than the vanilla game weights.
 * Enforced our blue-rarity lockers a little more thoroughly -- previously it was
   just SMGs/Pistols forced to blue, and other item types (shields, grenades) pulled
   from our main pools.
 * Refactor a lot of probability variables *(shouldn't actually have an effect on the
   mod, though it was a pretty big internal change)*

**v1.1.1**, March 7, 2018 (commit `ac9af0507b5b28f51e00f15e047cb019b1fc93e9`):
 * Fixed unlocking early-game elements for Maliwan Aquamarine Snipers on Windows

**v1.1.0**, March 1, 2018 (commit `4985d37cefc4d4cd339cf73f507c91eaca4c4bb8`):
 * Added "Reasonable Drops" Variant, suffixed original with "Lootsplosion"
 * Added some more folder structure inside many of the Raid Boss improvements,
   so they can be toggled at a more granular level.
 * Fixed an error which was causing Dexiduous's drops to be way too huge, even
   for this mod.
 * Nerfed Witch Doctor Relic drop chance a bit (from 60% -> 40%)
 * Added an optional folder which doubles the standard enemy drop rate (disabled
   by default)
 * Converted some hotfixes which didn't actually need to be hotfixes, to regular
   `set` commands
 * Fixed the "Shields" loot configuration on Digistruct Peak Dahl chests

**v1.0.0**, February 26, 2018 (commit `45e70cdc7982ac22715955e5ffb9e3f5963601c7`):
 * Initial public release
