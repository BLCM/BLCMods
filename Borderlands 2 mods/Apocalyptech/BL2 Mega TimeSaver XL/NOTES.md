Some notes on some things which I may want to tweak again in the future.
Used to be a few more things in here but I've since figured 'em out.

Gate to Hero's Pass
-------------------

This actually *is* sped up a reasonable amount, though there's a six-second
delay between the three bars opening and the main doors opening that I haven't
figured out yet, and I'm sick of running through that battle repeatedly, so
I'm giving up for now.  :)  The main `SeqAct_Interp` objects which deal with
that are:

 * Main two doors: `Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqAct_Interp_2`
 * Three bars: `Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqAct_Interp_3`

I believe that there's these two Delay statements inbetween opening the bars
and opening the doors:

 * `Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqAct_Delay_4`
 * `Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqAct_Delay_7`

... and I'm pretty sure that at least one of those gets buffed properly by
the mod, but I'm not quite sure yet where the other delay comes in.  Anyway,
I'm done with it -- six seconds is good enough for me.
