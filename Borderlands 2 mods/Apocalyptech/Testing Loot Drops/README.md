Testing Loot Drops
==================

This isn't really a mod, per se, so much as a little thing I use while
testing drops, to get a feel for how a pool's item/weapon distribution
feels, or for ensuring that a pool contains all the items that I expect
it to.  Originally this was basically just an optional part of BL2
Better Loot (though disabled by default).  It never really belonged
there, though, so here it is.

It'll always cause all (well, okay, most) enemies to have a 100% drop rate,
using the configured quantity (defaults to five).  So each enemy'll always
drop five items.  Optionally, you can restrict each of those to a specific
pool, or to a specific item.

The mod itself is not actually stored in git.  To use, you'll have to
be Python-conversant enough to alter `generate-mod.py` to suit, and
run it to generate the mod you want, then import into BLCMM.

The relevant bits in the Python script are:

    ###
    ### Control variables
    ###

    # Set `loot_drop_quantity` to the number of items each enemy will drop.
    loot_drop_quantity = 5

    # Force Pool_GunsAndGear to always drop the specified pool, if `force_gunsandgear_drop`
    # is True.  Useful for testing out how individual pools are behaving.
    force_gunsandgear_drop = True
    force_gunsandgear_drop_type = 'GD_Itempools.ClassModPools.Pool_ClassMod_All'

    # Force Pool_GunsAndGear to always drop the specified item, if
    # `force_gunsandgear_specific` is True.  Useful for seeing what exactly an
    # item is.  `force_gunsandgear_specific` will override `force_gunsandgear_drop`,
    # if both are set to True.
    force_gunsandgear_specific = False
    force_gunsandgear_specific_type = 'WeaponBalanceDefinition'
    #force_gunsandgear_specific_type = 'InventoryBalanceDefinition'
    force_gunsandgear_specific_name = 'GD_Orchid_BossWeapons.RPG.Ahab.Orchid_Boss_Ahab_Balance_NODROP'

Should be self-explanatory enough.  If it's not, this isn't the mod for you.

Licenses
========

The `generate-mod.py` script is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause),
which should be permissive enough to do just about whatever with.

The mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

See [COPYING-code.txt](../COPYING-code.txt) and [COPYING-mods.txt](../COPYING-mods.txt)
for the full text.

Changelog
=========

pfffffffff
