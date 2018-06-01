BL2 Cold Dead Hands
===================

This mod completely revamps the way in which weapons and shields are
acquired during the game.  Instead of dropping weapons/shields from a
random loot pool, enemies will now *always* drop the specific gun and
shield that they're using.  In the default configuration, enemy gear
quality is also improved considerably.

The intention is that these enhanced enemy drops will be just about the
*only* way to acquire weapons and shields in the game.  Quest rewards will
be unchanged, so weapons and shields can still be acquired that way.  At
the moment, weapons and shields can still be found in vending machines,
but should mostly be not available otherwise.

In the default configuration, this mod is a spiritual cousin of my own
Better Loot mod.  You'll be up against enemies using purples, gemstones,
and even legendaries.  Gear quality can be customized easily in
FilterTool/BLCMM, so you can still play using something close to the stock
Borderlands gear quality.  Regardless of gear quality configuration, Badass
enemies will have better gear than their ordinary counterparts.

Grenade Mods, Class Mods, and Relics will still be acquired as per usual -
via world drops, chests, and the like.

Requirements
------------

This mod should be able to be used mostly on its own, but it does require
one specific category of UCP to be active:

* `Loot Pool & Drop Changes -> Skinpool Fixes (Don't uncheck this)`

This is required to free up the custom loot pools that we use to equip enemies
with.  If for whatever reason you'd like to run this mod by itself without UCP,
make sure to at least enable/copy that folder over.

Usage/Installation
------------------

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `BL2 Cold Dead Hands.txt` and
have at it!

Mod Details
-----------

As stated above, enemies who use guns and shields will always drop that gun
and shield.  Creatures like Stalkers and Skeletons, and devices like turrets,
will NOT drop a shield, even if they spawn with one.  Shielded loaders will
drop shields, though.

Bosses with unique weapon drops who don't actually use weapons (ie: most
"creature" enemies like Knuckedragger, machines like BNK3R, melee-only
bosses) will nevertheless have a guaranteed drop of one item from their
drop pool, even though other melee-only enemies wouldn't.  Raid bosses, and
other large "lootsplosion" events may end up generating some guns/shields
as well.

If a weapon/shield-using boss has multiple unique drops of a weapon or
shield, they will spawn with one of those items chosen randomly, and that
will be the item that they'll drop.  So you should be able to tell right
from the start of the battle which gun you'll receive.

### Exceptions

* Some chests are likely to spawn weapons+shields still, or at least I'm not
  specifically removing those loot drops from the containers.  This list is
  unlikely to be exhaustive, and I haven't really tested many of these to find
  out:
  * Roland's Chest in Sanctuary will probably contain actual gear.
  * Dice Chests (from the Tiny Tina DLC) - weapons will be sparse enough during
    that DLC as it is.
  * Chests which were hardcoded to give specific gear should still provide that
    gear:
    * Shotgun chest at the end of Windshear Waste
    * Slag Gun chest in the Wattle Gobbler Headhunter Pack

* Doc Mercy has to be using an E-Tech blaster for Medical Mystery to make
  sense, so I've chosen to keep that rather than having him use an Infinity
  on you.  So Doc Mercy will drop an Infinity even though he's not actually
  using one.  If someone has a clever way to make a loot pool change in
  response to a mission being active or not, I'd love to hear it!

* Mad Mike will retain at least a 50% chance of spawning with a random
  rocket launcher, even on "guaranteed" unique loot configurations.

* Master Gee is the only raid boss who actually uses a recognizable weapon --
  a strange version of the Ahab.  He rarely ever actually fires it, though,
  and his animations don't really support other weapons anyway, so I'm
  leaving him alone.  He'll continue to use the special Ahab, and drop
  however he'd otherwise drop.  (See other mods like Better Loot to improve
  his (and other Raid boss) drops.)

* UCP adds a Manly Man shield drop to H3RL-E.  Even though H3RL-E uses
  a shield normally, the Manly Man would only nerf the fight, which I'm
  not keen to do.  So H3RL-E may drop the Manly Man without actually having
  it equipped.

* The Tributes (from the Wattle Gobbler Headhunter Pack) will have a 2/3rds
  chance of dropping the unique items that UCP adds to their drop pools
  compared to other enemies, since there are so many of them in one location.
  So even on "guaranteed" drops you may not get their unique items.

### Other Pool Tweaks

* Big Sleep is usually the one to drop the 12 Pounder, but that drop/equip
  has been moved to Sandman.

* Torgue DLC gangs use equip pools which are restricted by manufacturer.
  Rather than consume more loot pools just to support gang badasses also
  being manufacturer-restricted, badass gang members in the Torgue DLC will
  just use the standard badass equip pool that all other badasses use.

* Torgue DLC gang members can equip/use launchers now.

### Configuration

There are three main categories which you can use to customize the gear
quality, when loaded into FilterTool/BLCMM:

* **Loot Pool Improvements**: This section adds gemstones into the global E-Tech
  pool, and improves the global legendary pool by adding all uniques,
  pearls, and seraphs.  These options can all be toggled individually.

* **Enemy Gear Quality**: This is a mutually-exclusive category (so you can
  only choose one of the options), and defines how good the enemy gear is.
  The default ("Excellent Gear") is more or less at the Better Loot mod's
  "Lootsplosion" levels, so high-level gear will be extremely common.
  Remember that guns and shields aren't easily acquireable outside of enemy
  equipment, so choosing the "Stock" preset here may hamper your own gear
  loadout.  Epic treasure chests will no longer help out, etc.

* **Boss Unique Weapon Frequency**: This is another mutually-exclusive
  category, so you can only choose one option.  It will let you choose how
  often bosses will equip/drop their unique loot.  The default is
  "guaranteed," which is what the Better Loot mod does in "Lootsplosion,"
  but you can scale that back all the way to the stock values.

### Implications

* Remember that with this mod active, mods which provide buffs to weapons
  will help your opponents as well as yourself.  You may not want to have
  any super-OP gear in your active mod list, unless you're looking for a
  real challenge.  This is sometimes offset by the enemy AI not really
  knowing how to use better gear efficiently, though for very powerful
  weapons, that's not much help.

* It's not obvious in the vanilla game, but nearly all Loaders spawn with a
  shield. Ordinarily their shield can *only* be charged up by Shield
  Surveyors, and their shields start out at zero strength.  With this mod,
  all their shields have turned into real shields, which start regenerating
  immediately, which will probably make Loader-heavy areas much more
  difficult.

* Weapon and Shields ordinarily found in treasure chests have been replaced
  with the main ammo/money/eridium pool, rather than removed outright,
  because otherwise the probabilities of getting grenade mods, COMs, and
  relics would be greatly buffed.  So you'll have to get used to epic chests
  opening up to find a handful of dollars and some pistol ammo.

* Keep in mind that areas which are creature-heavy (such as Caustic Caverns)
  or full of non-gear-using enemies (such as most of the Dragon Keep DLC) will
  be pretty weak in the loot front, since weapons and shields will generally
  not be found in those areas.

Compatibility
-------------

This mod is compatible with UCP, and in fact requires that UCP's skinpool
changes be in place.

This will obviously conflict with other mods with similar aims.
theNocturni's "Enemy Enhancer" is one obvious conflict, though the
non-loot-pool parts of Enemy Enhancer would still be active (such as
faster enemy animations, etc).

This mod overwrites/disables much of the functionality in my own "Better
Loot" mod, but it's designed to work fine with both enabled (so long as
this mod appears later in your patch file).  The "Better Loot" improvements
to Class Mods, Grenades, Relics, etc, should help out against the increased
enemy difficulty here, in fact.

My own "Early Bloomer" mod will unlock all gear from the beginning of the
game, so enable that if you want early-game bandits to have the best gear
possible.  Note that Better Loot already includes Early Bloomer, so if
you're running Better Loot, you wouldn't have to bother.

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

    ./generate-source.py && ../conv_to_mod.py -f "BL2 Cold Dead Hands"

Ideas
=====

Just some ideas to keep track of, not sure if I'll implement these here, or
in another mod, or as an optional category in THIS mod, etc...  Anyway,
things to think about:

* Restrict weapon manufacturer by level?  (Only Jakobs in Lynchwood, etc?)
* Might be nifty to restrict weapon manufacturer by enemy type, though that
  would require eating up more skinpools (the by-level idea could reuse all
  of ours w/ hotfixes)
* Option to allow Stalkers to have shields?  (Maybe just Roid shields?)
* Fix orientation of items spawning in chests?  I think we can do this
  without messing up "regular" item spawns because it's just the weapon mounts
  that we'd change.  Not sure about shield mounts...

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
