No Broken Chests Near Denial Subroutine
=======================================

**NOTE:** This mod is now included as a basic part of TPS UCP 2.2, so if
you're using TPS UCP 2.2 or higher, there's no longer any reason to use
this mod directly!  (It won't hurt anything to have both enabled, though.)

The Denial Subroutine arena (in Cluster 99002 0V3RL00K) has six bandit
"coolers" which don't actually work -- they open and spawn their items, but the
items can't actually be picked up.  This mod changes them to be the round ammo
chests instead, so at least they work.

Usage
=====

This mod must be imported into BLCMM with `File -> Import single mod`.
Choose the file `No Broken Chests Near Denial Subroutine.blcm` and have at it!

TODO
====

I'd love to figure out a way to make the original bandit coolers work, rather
than going the nuclear route by just replacing them altogether.  The problem
is basically that the bandit cooler BPD seems to have an error in it somewhere
related to opening in a Vacuum.  There'd be a few possible avenues of fixing
this while keeping the bandit coolers in place: fixing the BPD in general,
setting the BPD to always act like it's not in vacuum, or setting the coolers
so that they don't think they're in vacuum in the first place.  I've tried
various methods of all three of those, all without success.  Given that this is
such a minor thing, I couldn't justify spending any more time on it, though, and
just went for the replacement route.

License
=======

This mod is licensed under
[Public Domain / CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Changelog
=========

**v1.0.0**, August 6, 2018:
 * Initial public release
