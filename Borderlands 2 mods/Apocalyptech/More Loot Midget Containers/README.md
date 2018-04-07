More Loot Midget Containers
===========================

This mod converts various maps so that that levels which contain
loot-midget-spawning containers will always use the loot-midget-spawning
versions if possible.

Note that not *every* container is loot-midgetable.  For instance, in
Opportunity, the only loot-midget-spawning container is the shorter ammo
containers.

Number of containers changed on each map:

* **Arid Nexus - Badlands**: 53
* **Arid Nexus - Boneyard**: 52
* **The Dust**: 5
* **Frostburn Canyon**: 50
* **Hero's Pass**: 1
* **Opportunity**: 45
* **Sawtooth Cauldron**: 144
* **Thousand Cuts**: 66
* **Tundra Express**: 74
* **Wildlife Exploitation Preserve**: 105

Usage
=====

This mod must be added via FilterTool, with `Developer tools` ->
`Add single mod`.  Choose the file `More Loot Midget Containers` and have at it!

Mod Construction / Implementation Details
=========================================

This mod is actually generated using a Python script named `conv_to_traps.py`,
which makes use of some data classes from my [FT Explorer](https://github.com/apocalyptech/ft-explorer)
project.  There's a couple other scripts in here which were used to do the
initial finding of which maps contained which loot-midget containers, as well.

License
=======

The `generate-mod.py` script itself is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

This mod itself is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.1**, April 2, 2018:
 * Added in a bunch more containers which my generation code missed.  D'oh.

**v1.0.0**, April 2, 2018:
 * Initial public release
