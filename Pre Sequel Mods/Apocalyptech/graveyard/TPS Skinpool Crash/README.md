TPS Skinpool Crash
------------------

This is a very bizarre situation where some combination of sets/hotfixes on skinpools might end up causing
a crash-to-desktop of TPS.  This is presumably related to DLC skinpools, which apparently might not be
entirely resilient to being hotfixed in some circumstances.

To reproduce the crash:
1. This case only actually works when using Doppelganger skinpools.  Even Baroness skinpools work fine
   in this case.  So choose the "Doppelganger" section (or try the other ones to verify that it does
   NOT crash)
2. Load a savegame with your char at the Fast Travel in Triton Flats
3. Zip over to the Crisis Scar entrance (the main one, where SC4V-TP hangs out)
4. Game crashes halfway through loading Crisis Scar

I think that also happens when going to Sanctuary, or probably to other maps leading out of Triton Flats.
Weirdly, if you load a game alrady *at* the Crisis Scar entrance, the crash will NOT happen.  It WILL
happen if you start at Crisis Scar, head over to the Fast Travel, and then go back again, though.  Go
figure.

As I say: it's weird.  There's four statements in each character's section -- the first one, which
clears out an entry in a skinpool, is a bit superfluous and can be removed without changing the
crash behavior.  Without it, though, the BalancedItems stanza would be in a weird state, so I left it in.

For the remaining three statements, if you remove *any* one of them, the crash does not occur.  This
is especially weird for the middle one, the `set` on a pool totally not referenced by either of the
surrounding pools, but doing so seems to be necessary to trigger the crash.

If anyone can figure out a reason why this might happen other than "DLC Skinpools might not be trustable"
I'd love to hear about it.
