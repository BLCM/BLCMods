## Compatibility & Troubleshooting
 
 
### Compatibility:
Before being released, all my mods are tested with:

1. [UCP Patch v4.1](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Community%20Patch%20Team/Patch.txt) by [Community Patch Team](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Community%20Patch%20Team) 
2. [Gear Overhaul 1.36](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Orudeon/Gear%20Overhaul%201.36.txt) by [Orudeon](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Orudeon)
3. [BL2 Better Loot Mod v1.3.1](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech/BL2%20Better%20Loot%20Mod) & [BL2 Cold Dead Hands v1.1.2](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech/BL2%20Cold%20Dead%20Hands ) by [Apocalyptech](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech)
4. [Better Quest v2.014](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Hemaxhu/Quest%20Rewards/Better%20Quests) by [Hemaxhu](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Hemaxhu)

### Troubleshooting:

If a option or a fix don't work as intended, it's not because the Mod is not well coded, but probably because this code is overwritten by another mod.

#### What's go wrong?

It's simply because 2 commands work on the same parameter, and one is overwritten by the other.

Better to explain that with a exemple, isn't?

Let's take 2 of my mods:

1.  The *Double Quest Rewards*, which give the choice between 2 *Kiss of Death* given by Moxxi for the mission *Hell Hath No Fury*.  
 
2. The option in *SMG Dahl Discord Solver - Moxxi Edition*, which give the choice betwen 2 *SMG Dahl Discord Solver - Moxxi Edition* given by Moxxi as reward for the mission *Hell Hath No Fury*. 

You activate the option to have the choice between 2 *SMG Dahl Discord Solver - Moxxi Edition* given by Moxxi as reward for the mission *Hell Hath No Fury*, but you still receive the choice from 2 *Kiss of Death* instead of the choice between 2 *SMG Dahl Discord Solver* as desired. :cry:

Ah! You noticed that *"given by Moxxi as reward for the mission Hell Hath No Fury"* was present in the 2 mods, so you get the idea.   :thought_balloon:

Look on the example with picture below to understand why:

Left picture: The mod *SMG Dahl Discord Solver - Moxxi Edition* is placed **BEFORE** the Mod *Double Quest Rewards*, and the option which give the choice betwen 2 *SMG Dahl Discord Solver - Moxxi Edition* appear in *Dark Green*, that's mean, that another bunch of code overwrite this command (in this case the choice from 2 *Kiss of Death* from the Mod *Double Quest Rewards*)... and yes, that's don't work... but you noticed the big red wrong logo, isn't?

Right picture: To fix this overwriting problem and get the code working as intended, the mod *SMG Dahl Discord Solver - Moxxi Edition* must be moved **AFTER** *Double Quest Rewards*. Once done, the reward will appear in *Light Green*, meaning that the code will work correctly, and you will have the choice betwen 2 *SMG Dahl Discord Solver - Moxxi Edition* for the mission *Hell Hath No Fury*.

![Fix or option not working as intended](https://i.imgur.com/a0eZEVB.png "Don't worry guys... even if my screen capture show French text, my mods are in English")
#### To summarize: 
1. **Correct:**
 *- White* = work (normal set command code)
 *- Blue* = work (hotfix)
 *- Light Green* = work (overwrite)
2. **Incorrect:**
 *Dark Green* = don't work (is overwritten)... by moving the mod at the end of your patch, the problem will be solved in 90% of cases.  

### Note: 
I know that all these informations already are mentionned in the wiki page [Functional Changes from FilterTool to BLCMM](https://github.com/BLCM/BLCMods/wiki/Functional-Changes-from-FilterTool-to-BLCMM), so these additional explanations are just for those who don't get the memo :wink:

### Disclaimer

All files and content provided here were written by me (Astor), unless stated otherwise.

- They are free for personal use. You may use these mods in videos, or for streaming, as long as you give me proper credit. I would appreciate that you'll letting me know about it, and at least, provide a link to [Github.com/BLCM/BLCMods/Borderlands 2 mods/Astor](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Astor) .

- You may re-use small bits of code (e.g. formulas, behavior modifications, etc) for your own purposes, and let me know about it. 

- Ask me for permission first if you wish to use larger portions of this code, make a modified/improved version, include it in a mod pack, etc..., and don't forget to provide credit.

- Do not re-upload this mod or any of my mods anywhere without my explicit permission... ANYWHERE!

* * * * *
