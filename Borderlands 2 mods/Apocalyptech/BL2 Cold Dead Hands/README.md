BL2 Cold Dead Hands
===================

**NOTE:** This mod is a work in progress, and has not yet been officially
released.  Use at your own risk, at the moment!

This mod completely revamps the way in which weapons and shields are
acquired during the game.  Instead of dropping weapons/shields from a
random loot pool, enemies will now *always* drop the specific gun and
shield that they're using, and their gear quality has been improved
considerably.  You'll be up against enemies using purples, gemstones, and
even legendaries.  Badass enemies will, in general, have better gear than
their ordinary counterparts, though even ordinary enemies have a chance to
spawn with the highest-tier gear.

The intention is that these enhanced enemy drops will be just about the
*only* way to acquire weapons and shields in the game.  At the moment, gear
can still be found in vending machines, and in some containers.  Weapons
and shields can no longer be found in treasure chests, though.

This mod is a spiritual cousin of my own Better Loot mod, and you can
expect to enjoy a much better quality of gear throughout your playthrough.
Functionally it feels very similar, thanks to the increased volume of loot
which gets dropped.

Grenade Mods, Class Mods, and Relics will still be acquired as per usual -
via world drops, chests, and the like.

Requirements
------------

This mod should be able to be used mostly on its own, but it does require
that certain parts of UCP are active.  If for whatever reason you'd like to
run this mod by itself without UCP, make sure to at least enable/copy these
bits, all inside the `Loot Pool & Drop Changes` folder:

* `Skinpool Fixes (Don't uncheck this)`: this is
  required to free up the custom loot pools that we use to equip enemies with.
* `Specific Loot Changes`: Without the items in this category enabled, the
  relevant enemies won't spawn with the proper items:
  * `Add Deliverance to Bad Maw`
  * `Add RokSalt to Flinter`
  * `Add Kitten and Baby Maker to Motor Momma`
  * `Add Torgue Legendaries and Torgue Tokens to Piston`
  * `Add Pitchfork to Prospector Zeke`
  * `Add Roaster to Smash-Head`

Usage/Installation
------------------

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Guaranteed Varkid Evolution.txt` and
have at it!

Mod Details
-----------

As stated above, enemies who use guns and shields will always drop that gun
and shield, and should never drop anything else.  Creatures like Stalkers
and Skeletons, and devices like turrets, will NOT drop a shield, even if
they spawn with one.  Shielded loaders will drop shields, though.

Bosses with unique weapon drops who don't actually use weapons (ie: most
"creature" enemies like Knuckedragger, machines like BNK3R, melee-only
bosses) will nevertheless have a guaranteed drop of one item from their
drop pool, even though other melee-only enemies wouldn't.

If a weapon/shield-using boss has multiple unique drops of a weapon or
shield, they will spawn with one of those items chosen randomly, and that
will be the item that they'll drop.  So you should be able to tell right
from the start of the battle which gun you'll receive.

### Exceptions

* Doc Mercy has to be using an E-Tech blaster for Medical Mystery to make
  sense, so I've chosen to keep that rather than having him use an Infinity
  on you.  So Doc Mercy will drop an Infinity even though he's not actually
  using one.  If someone has a clever way to make a loot pool change in
  response to a mission being active or not, I'd love to hear it!

### Implications

* Giving better gear to enemies obviously makes them tougher, though the
  abundance of good gear for yourself seems to do a reasonable job of
  keeping things pretty level, at least in Normal mode.  You'll still be in
  for some tougher times in tighter areas, though, if enemies start
  spawning with Rocket Launchers or Grenadiers, etc.
* It's not obvious in the vanilla game, but all Loaders spawn with a
  shield, it's just that ordinarily their shield can *only* be charged up
  by Shield Surveyors, and their shields start out at zero strength.  With
  this mod, all their shields have turned into real shields, which start
  regenerating immediately, which will probably make Loader-heavy areas
  much more difficult than ordinarily.

Compatibility
-------------

This will obviously conflict with other mods with similar aims.
theNocturni's "Enemy Enhancer" is one obvious conflict.  The mod should be
compatible with UCP, and in fact requires that UCP's skinpool changes be in
place.

This mod overwrites/disables much of the functionality in my own "Better
Loot" mod, though theoretically nothing should break if you have both (so
long as this mod appears later in your patch file).

Mod Construction / Implementation Details
-----------------------------------------

This mod is actually generated using a simple little Python script named
`generate-source.py`.  The script makes use of `hotfix.py` from the parent
directory.  You'd need to copy (or symlink, if you're on Mac or Linux)
`hotfix.py` into this directory in order to run the script.

To generate the end result file, I actually run the small shell script
`create.sh` in this directory, which just does the following:

    ./generate-source.py && ../conv_to_mod.py -f "BL2 Cold Dead Hands"

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
