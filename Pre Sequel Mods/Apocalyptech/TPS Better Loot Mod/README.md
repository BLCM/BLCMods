TPS Better Loot Mod by Apocalyptech
===================================

This mod aims to make loot in The Pre-Sequel "better" in general.  It's
essentially a cheat mod, intended for those TPS players like myself who
tend to play in Normal most of the time, dislike grinding, get bored easily
by the uninteresting and drab loot that typically gets dropped in-game, and
who often end up just resorting to Gibbed to be able to play around with
some better gear.  The goal, personally, was to get the loot drops in-game
to a point where I never felt tempted to open up Gibbed.

This patch is set up to play nicely with FilterTool, and basically
everything in here can be toggled on or off inside FilterTool as you'd
hope, on an item-by-item basis.  Basically every bullet point in the
"Overview" section is its own "folder" once imported into FilterTool.

Usage/Installation
------------------

The recommended way to use this mod is with FilterTool/UCP.  In FilterTool,
select `Developer Tools` -> `Add Single Mod` and then select one of these
two files:

* `TPS Better Loot Mod (Lootsplosion) - UCP Compat` - Default drop weights
  which I'm personally happy with.  Many folks may find these a bit extreme.
  This version probably makes more sense in Normal mode than it does in UVHM.
* *("Reasonable Drops" version will be forthcoming in a bit)*

Once the mod has been added, you'll have a new folder for this mod
underneath the `mods` folder at the bottom, and can turn parts on or off at
will.

If for whatever reason you don't want to use FilterTool, there is also
a standalone version at `TPS Better Loot Mod (*) - Standalone Offline`.
Simply copy the file into the game's `steamassets/binaries` directory with
an easy-to-type filename, and then run `exec <filename>` from the console
to load it on its own.  It works quite well by itself.

The only actual differences between the UCP and Standalone versions are
that the "Standalone" versions contain all of the original Gearbox hotfix
data, and set up the hotfix commands for execution by Borderlands, whereas
the "UCP Compat" version lets FilterTool/UCP take care of that for you.
The "Offline" in the filename just means that it's using offline-style
hotfixes, which work better in TPS regardless of whether you're online or
offline.

All versions are fully FilterTool compatible.

Mod Overview
------------

* Adds all legendaries + uniques (weapons, grenade mods, class mods,
  shields, oz kits) into the global "legendary" loot pools, so
  you'll start seeing those much more frequently.
* Loot will skew much more rare, in general.  You should expect to see
  those legendaries/uniques far more frequently than in vanilla TPS.
* Glitch weapons spawn in the main game
* Luneshine weapons will drop in all world drop pools (this is identical
  to some functionality in UCP)
* Legendary/Unique weapons which allow Luneshine are guaranteed to spawn
  with Luneshine.  (Some legendaries/uniques don't have Luneshine set as
  possible accessories, so they will continue to not have Luneshine.  ie:
  Marek's Mouth, Cry Baby, Longnail, Heartfull Splodger, Cutie Killer, and
  a handful of others.)
* Makes Moonstones drop 2x more often
* Normalizes weapon type drops a bit.  *(Decreases pistol drop chance,
  increases all other weapon types.)*
* Lootable Container Changes:
  * "Regular" treasure chests will always provide at least blue-rarity gear,
    and have a decent chance of including stuff from the legendary pools.
  * "Epic" treasure chests have an extremely high probability of dropping
    from the legendary pools.
  * Moonstone chests are guaranteed to contain legendary loot.
  * When lockers spawn gear, they will always be blue-rarity.  *(Previously
    lockers had a chance to spawn even legendaries, so some could potentially
    see this as a drawback)*
  * Safes have been improved: Eridium configurations are far more likely, cash
    quantities have been improved.  Gear drop chances have been dropped
    somewhat, but gear from safes will always be legendary.
  * Fixes some "shield" loot configurations which had an error and would
    never spawn, previously.
* Boss drop pools are generally improved, and bosses are guaranteed to drop as
  many items from their unique drop pool as are in that pool. *(needs testing)*
  * Bosses with just a single unique drop will therefore be guaranteed to drop
    that item.
  * If a boss has more than one in their drop pool, you may get duplicates
    of one rather than one of each.
* Fixes/Changes to some enemies' drop poools:
  * Badass loot drops have been improved
  * Chubby drop pool has been improved.  *(Though the only chubbies in the
    game are Stalkers, so it's sort of hardly worth it.)*
  * Many enemies from the Claptastic Voyage DLC have a unique legendary drop
    associated with them, with a default drop rate of 0.1%.  This mod ups that
    probability to 1.5%.
* Remove early-game loot restrictions.  This is actually a superset of the
  similar feature already present in UCP 2.1.  This version enables spawning
  of basically everything from the beginning, including all grenade types,
  oz kits, class mods, rocket launchers, etc.  Both this and the UCP 2.1
  "Make good stuff drop earlier" mods can be active at the same time with
  no ill effects.  Note that if you *don't* have either this or UCP
  enabled on your game, the early game will end up dropping *no* gear, due
  to our rarity changes.

**NOTE:** I believe that due to our Legendary loot pool changes, Unique
gear will end up as possible Grinder results when trying to grind for
legendaries.

Compatibility
-------------

### UCP ###

This mod is mostly compatible with UCP 2.1, even though UCP touches a lot of
the same objects that this mod does.  Exceptions:

* This mod's `Better Enemy Drops -> Better Chubby Drops` overrides UCP's
  `Patch 2.1 -> Chubby SpawnRate and Loot -> Addition Of Holodome Com/
  Holodome gear 60% Random leg 30% to Chubbies`.  Our version is a bit
  more lootful.
* This mod's `Better Containers -> Better Moonstone Chests` completely
  overrides UCP's `Patch 2.1 -> MoonStone chests. Launchers 10% Longguns 5% ,
  Pistols GM,CoM,Shields 3%`.  Our version guarantees all legendaries.

Some instances where we touch the same objects but there's no real
compatibility issues:

* UCP improves the legendary pools as part of its Grinder changes -- this
  mod goes further and adds uniques to those pools as well.  The statements
  in this mod are supersets of the UCP statements, and shouldn't pose problems
  (except potentially for the Grinder giving you uniques in addition to
  legendaries).  Specifically, the following UCP 2.1 folders will get
  overridden by this mod:
  * `Patch 1.0` -> `Grinder & world drop changes` -> `Add DLC legendaries to grinder`
  * `Patch 1.0` -> `Grinder & world drop changes` -> `Add Rerouter & MORQ to grinder and world drops`
  * `Patch 1.0` -> `Grinder & world drop changes` -> `Add meganade to grinder and world drop`
  * `Patch 1.0` -> `Grinder & world drop changes` -> `Fix purple spike shields and remove purple from legendary pool`
* As mentioned above, our `Remove Level-Based Loot Restrictions` folder is a
  superset of UCP's `Make good stuff drop earlier` folder.  There are no problems
  with having both enabled, though -- they play nicely together.
* UCP's `Patch 2.0` -> `Loot changes 2.0` -> `Make Rosie available in First Playthrough.
  Make the Head available in all playthroughs` interacts a bit oddly with our changes
  there -- you'll end up getting two head drops, and will get the Rosie as a mission
  reward rather than a drop.  Not a big deal, so I'm not going to do a compat hotfix
  for that.
* This mod's `Loot Pool Tweaks -> Luneshine Drops -> Enable Luneshine in World drops`
  is a duplicate of UCP's `Patch 2.1 -> 2.1 Optionals -> Make Luneshines Appear in
  the Wild`.  There's no problem with having both enabled.

### Other Mods

Obviously this mod will conflict with other mods which play with the same
variables, though I'm not aware of any in specific at the moment.

Loot Purposefully Excluded from Pools
-------------------------------------

There's some gear which I felt shouldn't be in the pools at all.  I am
quite willing to hear counterarguments; my mind could probably be pretty
easily persuaded otherwise if someone feels strongly about it.

* Springs' Oz Kit
* Cracked Sash (Shield)
* Contraband Sky Rocket grenade *can* spawn, but has a much decreased
  chance compared to all the other legendaries.

There's also a few drop pools / containers / etc which I've purposefully
left alone:

* Cash Boxes
* Ammo Chests
* Cardboard Boxes
* Dumpsters
* etc...

Some other stuff not done:

* This mod won't touch the Grinder.  No point, really, given the rest of
  the mod, and there are plenty of other mods out there which already
  do that.

Other Recommended Mods
----------------------

* My own "Luneshine on Uniques" mod will add Luneshine attachments to ten
  uniques/legendaries which don't otherwise support them.  Weapons generated by
  that mod will get deleted by TPS if its started up without the mod active,
  though, which is why I didn't include it here.
* Kazy's "88.89% Less Luneshine" is great for decreasing the visual effect of
  Luneshine, which I appreciate since there's so much more Luneshine in general
  when using this mod -- weapons all look too similar with the vanilla Luneshine
  effect.
* The UCP 2.1 option `Customs -> makevendorsGreaterAgain` will improve vendor
  stocks.

TODO
----

* Check legendary drop pools
  * Legendary COMs especially - UCP does some different stuff than we do.  Specifically,
    their section `Add legendary coms to world drops and grinder` alters some character-
    specific legendary pools.  Check it out, to see if that's maybe altering the drop
    probabilities in ways we don't expect.
* Check boss unique drops
* Maybe decrease Moonstone chest cost in exchange for not doing guaranteed
  legendaries on it?  Mull it over.
* Check Lootbug drops
* I suspect that most everything that drops from the `UltimateBadassEnemyGunsAndGear`
  pool does so multiple times; we may want to nerf that a bit, or see about
  limiting the number of spawns for the more extreme enemies.
* Relatedly, I seem to recall that badasses might be more common in TPS in general,
  may need to nerf that drop pool a bit, too.
* Swagman drop pool - we're altering `GD_Itempools.Runnables.Pool_ScavWastelandWalker`
  but UCP alters `GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget`...
* Check on usage of `GD_Itempools.DropWeights.DropODDS_BossUniqueRares` in "regular"
  enemies, 'cause it seems to be used more frequently in TPS.  Probably will have to
  nerf some things.
  * UCP makes further use of this.  See `Loot changes 2.0` for various examples;
    check for those and maybe put in some compat hotfixes.

Mod Construction / Implementation Details
-----------------------------------------

I actually generate this mod using a simple little Python script named
`generate-source.py`, which enables me to do things like set the rarity
drop levels from a single location at the top of the file, and have it
apply to a number of different objects throughout the game.  That script
outputs to a human-readable multiline text file which can't actually be
read directly by FilterTool/Borderlands -- it must be processed by my
`conv_to_mod.py` script which you'll find in my BL2 mod directory.

The generation script makes use of `hotfix.py` from my BL2 mod directory.
You'd need to copy (or symlink, if you're on Mac or Linux) `hotfix.py`
into this directory in order to run the script.

To generate the end result file, I actually run the small shell script
`create.sh` in this directory, which effectively just does the following:

    ./generate-source.py && \
        ../conv_to_mod.py -f "TPS Better Loot Mod (Lootsplosion) - UCP Compat" && \
        ../conv_to_mod.py -f "TPS Better Loot Mod (Lootsplosion) - Standalone Offline"

*(It's actually slightly more complicated now that I'm exporting multiple
profiles of the same mod (Lootsplosion vs. Reasonable), but that's basically
what it does.)*

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
