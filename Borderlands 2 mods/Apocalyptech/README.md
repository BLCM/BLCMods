Apocalyptech's Borderlands 2 Mods
=================================

This is a collection of the mods that I've put together for BL2.  I've got
an area in the `Pre Sequel Mods` directory as well, so feel free to check
that out (though damned if I can get this README to link to it).

The mods found in the main BLCMods repo are intended to be the full, most
recently-released version.  I do most of my work on mods
[in my own BLCMods Fork](https://github.com/apocalyptech/BLCMods/), so you
can head over there to see if I have anything in the works, if you want.
Note that my larger mods (Better Loot and Cold Dead Hands) have their own
branches, so you can browse in `bl2betterloot`, `bl2colddeadhands`,
`tpsbetterloot`, or `tpscolddeadhands`, in addition to `master`, if you like.

* [Mod List](#mod-list)
  * [Aegrus Not-So-Rare Monsters](#aegrus-not-so-rare-monsters)
  * [BL2 Better Loot Mod](#bl2-better-loot-mod)
  * [BL2 Cold Dead Hands](#bl2-cold-dead-hands)
  * [BL2 Early Bloomer](#bl2-early-bloomer)
  * [BL2 Expanded Legendary Pools](#bl2-expanded-legendary-pools)
  * [BL2 Movement Speed Cheats](#bl2-movement-speed-cheats)
  * [BL2 No Wasted COMs](#bl2-no-wasted-coms)
  * [Configurable Catch-A-Ride](#configurable-catch-a-ride)
  * [Guaranteed Omnd-Omnd-Ohk](#guaranteed-omnd-omnd-ohk)
  * [Guaranteed Varkid Evolution](#guaranteed-varkid-evolution)
  * [More Loot Midget Containers](#more-loot-midget-containers)
  * [More Muscles](#more-muscles)
  * [Speedier Sandskiffs](#speedier-sandskiffs)
  * [Stalkers Use Shields](#stalkers-use-shields)
* [Utilities](#utilities)
  * [modprocessor.py](#modprocessorpy)
  * [conv_to_human.py](#conv_to_humanpy)
* [Licenses](#licenses)

Mod List
========

### Aegrus Not-So-Rare Monsters

This is a real simple mod which just alters the spawn rates of the "rare"
creature types in Sir Hammerlock's Big Game Hunt.  This is really only
useful if you're looking to complete the
[I Like My Monsters Rare](http://borderlands.wikia.com/wiki/I_Like_My_Monsters_Rare)
mission without having to do any extra farming.

### BL2 Better Loot Mod

This mod's general goal is to make loot drops in Borderlands 2 "better",
as in skewing very much towards the rarer loot.
Legendaries/Uniques/Pearls/Seraphs will drop far more frequently than they
do in vanilla B2, etc.

It's essentially a cheat mod, intended for those BL2 players like myself who
tend to play in Normal most of the time, dislike grinding, get bored easily by
the uninteresting and drab loot that typically gets dropped in-game, and who
often end up just resorting to Gibbed to be able to play around with some
better gear.  The README in the mod dir itself should provide a lot more info.

### BL2 Cold Dead Hands

This mod completely revamps the way in which weapons and shields are
acquired during the game.  Instead of dropping weapons/shields from a
random loot pool, enemies will now *always* drop the specific gun and
shield that they're using.  In the default configuration, enemy gear
quality is also improved considerably.

### BL2 Early Bloomer

Unlocks all weapons/items to be able to spawn right at the beginning of the game.
A more powerful version of the same functionality provided by UCP.  (This is
technically a subset of Better Loot; if you're already running Better Loot then
you already have this.)

### BL2 Expanded Legendary Pools

This mod adds all legendary items across DLCs into the global legendary loot
pools, and by default adds all uniques, seraphs, and pearlescents into the
legendary pools, too.  The mod will also by default add in gemstone weapons
into the E-Tech pool, and add the Dragon Keep "Alignment" Class Mods to the
global class mod drops.

### BL2 Movement Speed Cheats

This mod increases movement speed of all BL2 characters (including while
crouched, and while in FFYL).  It also increases the jump height a bit, and
increases air control by quite a lot.  If you're looking to zip through
some levels like there's no tomorrow, this is for you.

### BL2 No Wasted COMs

This mod changes the Class Mod drop pools such that the only COMs which drop
are for characters who are actually playing the game.  For a singleplayer
game, that means you'll only ever get COMs for your one character, for
instance.

### Configurable Catch-A-Ride

This mod is a souped-up version of FromDarkHell's "CarReplacements" mod,
which changed some of the Catch-A-Ride locations so that you can spawn
various types of vehicles throughout all the game's content.  That version
just had a few hardcoded replacements, though.  This one lets you fully
customize every single Catch-A-Ride slot in the game!

### Guaranteed Omnd-Omnd-Ohk

Gives all Badass Savages a 100% chance of evolving into Omnd-Omnd-Ohk, when
left in the presence of a Witch Doctor.  Mostly just useful if you want to
farm OOO without having to gamble on its spawn chances.

### Guaranteed Varkid Evolution

Gives all Varkids a 100% chance of evolution, regardless of player count or
playthrough.  Mostly just useful if you want to farm Vermivorous without
having to gamble on its spawn chances.

### More Loot Midget Containers

*Note:* This mod has been obsoleted by [mopioid](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/mopioid)'s
[Loot Midget World](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/mopioid/LootMidgetWorld.blcm) mod.

Alters a few levels (specifically: Arid Nexus Badlands, Hero's Pass, Opportunity,
Sawtooth Cauldron, and Tundra Express) so that as many containers as possible
can spawn loot midgets.  This doesn't meant that *all* containers can spawn
midgets, but there'll be more than there were.

### More Muscles

This simple mod improves the spawn rate for Muscles, a unique Bruiser who
appears in Thousand Cuts.  He will be fairly likely to appear during a full
playthrough of the level.

### Speedier Sandskiffs

Improves the speed (and afterburner capability) of Sandskiffs.

### Stalkers Use Shields

Stalkers already use shields, of course, but this mod equips them with "real"
shields, of the sort your characters equip.  Optionally, you can have them
only use Maylay shields, as well.

Utilities
=========

I like writing my mods using code, so that I can set constants which are used
throughout the mod file, or just simply take advantage of looping and keeping
data in useful data structures, etc.  BLCMM includes a Plugins architecture
which will eventually be public, which could provide that kind of thing right
from BLCMM, but for now I use Python to construct nearly all of my mods.

The utilities in here are what assists me in doing so.  These utilities are
written in Python, and probably require Python 3.  They're intended to just be
run from a commandline, which may pose some logistical problems for folks on
Windows/Mac who may not be used to doing that.  (Also, Python probably isn't
already installed by default on those platforms.) Folks running Linux, like
myself, should be able to just run 'em as per usual from a terminal.

modprocessor.py
---------------

This is my latest mod-construction library, which lets me build mods
programmatically the way I'm used to while exporting in a BLCMM-compatible
file format.  It uses a custom intermediate file format which is very
similar to FilterTool's format, which then gets converted to BLCMM.  That way I
can easily continue to use code-assisted templates for mod construction, which
is the way I still prefer to do things.  This is mostly intended to be used
by my generation code itself, but it can be invoked on the commandline to
convert my custom mod-building format into a BLCM-style mod file as well.

conv_to_human.py
----------------

This utility takes FT or BLCMM files and converts them to something extremely
close to the custom format which `modprocessor.py` uses, and converts any
single-line statements into multiline, if appropriate.  The file generated
may not be 100% compatible with `modprocessor.py` -- I only really use this
tool for manual verification and comparison, so it's not worth it to make it
100%.  This can also be used on `obj dump` output to make that nicer as well.

For instance, if you've got a file which contains the following:

    BalancedItems(0)=(ItmPoolDefinition=None,InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Vitality_Rare',Probability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),bDropOnDeath=True)

... this utility would convert it to something like:

    BalancedItems(
        0
    )=(
        ItmPoolDefinition=None,
        InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Vitality_Rare',
        Probability=(
            BaseValueConstant=1.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        ),
        bDropOnDeath=True
    )

If you don't specify any filenames, this util will read/write to STDIN/STDOUT.
You an also use `-` as either of the filenames, if you wanted to use
STDIN/STDOUT for one end but not the other.

The utility will ask you to overwrite the output file, if it's specified and
already exists.  You can use the `-f` or `--force` option to automatically
overwrite without confirmation.  You can also use `-h` or `--help` as you'd
hope, though there's no features not already mentioned here.

Licenses
========

All the code here is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause),
which should be permissive enough to do just about whatever with.

Mods under this folder are licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

See [COPYING-code.txt](COPYING-code.txt) and [COPYING-mods.txt](COPYING-mods.txt)
for the full text.
