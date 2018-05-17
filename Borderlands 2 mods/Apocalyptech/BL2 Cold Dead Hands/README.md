BL2 Cold Dead Hands
===================

**NOTE:** This mod is a work in progress, and has not yet been officially
released.  Use at your own risk, at the moment!

This mod completely revamps the way in which weapons and shields are
acquired during the game.  Enemies will now always drop the specific gun
and shield that they're using, when killed, and this is now the *only* way
to acquire weapons and shields in the game.  Additionally, the gear quality
which enemies use has been greatly improved, so this mod will make your
game harder.  You'll be up against enemies using purples, gemstones, and
even legendaries.  Badass enemies will, in general, have better gear than
their ordinary counterparts, though even ordinary enemies have a chance to
spawn with the highest-tier gear.

Creatures like Stalkers and Skeletons, and devices like turrets, will NOT
drop a shield, even if they spawn with one.  Shielded loaders will drop
shields, though.

Bosses with unique weapon drops who don't actually use weapons (ie: most
"creature" enemies like Knuckedragger, machines like BNK3R, melee-only
bosses) will nevertheless have a guaranteed drop of one item from their
drop pool, even though other melee-only enemies wouldn't.

Grenade Mods, Class Mods, and Relics will still be acquired as per usual -
via world drops, chests, and the like.

Usage/Installation
------------------

This mod must be imported into FilterTool/BLCMM with `Developer tools` ->
`Add single mod`.  Choose the file `Guaranteed Varkid Evolution.txt` and
have at it!

This mod requires that the UCP option "Skinpool Fixes (Don't uncheck this)" is
enabled!  If you want to run this without UCP, make sure to at least copy that
category over.

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
