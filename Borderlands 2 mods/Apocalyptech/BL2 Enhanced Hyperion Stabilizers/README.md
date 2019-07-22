BL2 Enhanced Hyperion Stabilizers
=================================

This mod vastly improves the starting accuracy of all Hyperion weapons,
and greatly decreases the time it takes for them to reach peak accuracy.
This is most notable with pistols, SMGs, and sniper rifles, though
shotguns received a small buff as well.  Sniper rifles in particular
have basically no initial sway to the targetting, so Hyperion snipers
aren't totally useless anymore.  The Bitch, which already had its own
buffs to accuracy, basically starts off as accurate as it can be.

This mod obviously makes Hyperion weaponry rather OP -- it should really
be paired with a mod to decrease damage or otherwise make up for the
lack of a downside for Hyperion weapons, but I've never been one for
worrying about using OP weapons.

There are two options to choose between, in the `Choose Improvement Level`
folder.  The default option will apply the maximum improvement to all
rarities of gear, so white weapons are improved just as much as purples
are.  The other option, `Lower Rarities Receive Less Improvement` will
reserve the best improvement for purple/e-techs/legendary/pearl/seraph
weapons.  Whites will still receive a small boost with this option, but
it won't be nearly as good as the higher-tiered weapons.

Usage
=====

This mod must be imported into BLCMM using `File -> Import single mod`.
Choose the file `BL2 Enhanced Hyperion Stabilizers.blcm` and have at it!

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`.  The
script makes use of `modprocessor.py` from the parent directory.  You'll need
to copy (or symlink, if you're on Mac or Linux) `modprocessor.py` into this
directory in order to run the script.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, July 21, 2019:
 * Initial public release
