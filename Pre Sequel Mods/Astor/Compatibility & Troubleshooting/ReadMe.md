## Compatibility & Troubleshooting
  
### Compatibility:

Before being released, all my mods are tested with:

1. [TPS Patch 2.2](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Community%20Patch/Community%20Patch%202.2) by [Community Patch](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Community%20Patch) 
2. [TPS Better Loot Mod](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Apocalyptech/TPS%20Better%20Loot%20Mod) & [TPS Cold Dead Hands](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Apocalyptech/TPS%20Cold%20Dead%20Hands) by [Apocalyptech](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Apocalyptech)

### Troubleshooting:

If a option or a fix don't work as intended, it's not because the Mod is not well coded, but probably because this code is overwritten by another mod.

### What's go wrong?

It's simply because 2 commands work on the same parameter, and one is overwritten by the other.

Better to explain that with a example, isn't?

Let's take the 2 following Mods:

1. The *UCP Patch 2.2*, will make you game better, but... will change some description/upgrade into English.  
2. My *UCP French Patch*, which will correct that. 

You import my *UCP French Patch* but you still see some English description/upgrade on your screen. :cry:

Look on the example with picture below to understand why:

**Left picture:** My mod *UCP French Patch* is placed **BEFORE** the Mod *UCP Patch 2.2* and the French description/upgrade appear in *Dark Green*, that's mean, that another bunch of code overwrite this command (in this case the English description/upgrade from the Mod *UCP Patch 2.2*)... and yes, that's don't work... but you noticed the big red wrong logo, isn't?

**Right picture:** To fix this overwriting problem and get the code working as intended, my mod *UCP French Patch* must be moved **AFTER** *UCP Patch 2.2*. Once done, the French description/upgrade will appear in *Light Green*, meaning that the code will work correctly, and you will see all the previous English description/upgrade changed in French description/upgrade.

![Fix or option not working as intended](https://imgur.com/l1tHmBu.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")

### To summarize: 

1. **Correct:**
 - *White* = work (normal set command code)
 - *Blue* = work (hotfix)
 - *Light Green* = work (overwrite)
2. **Incorrect:**
 - *Dark Green* = don't work (is overwritten)... by moving the mod at the end of your patch, the problem will be solved in 90% of cases.  

### Note: 
I know that all these informations already are mentionned in the wiki page [Functional Changes from FilterTool to BLCMM](https://github.com/BLCM/BLCMods/wiki/Functional-Changes-from-FilterTool-to-BLCMM), so these additional explanations are just for those who don't get the memo :wink:

### Disclaimer

All files and content provided here were written by me (Astor), unless stated otherwise.

- They are free for personal use. You may use these mods in videos, or for streaming, as long as you give me proper credit. I would appreciate that you'll letting me know about it, and at least, provide a link to [Github.com/BLCM/BLCMods/Pre-Sequel Mods/Astor](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Astor).

- You may re-use small bits of code (e.g. formulas, behavior modifications, etc) for your own purposes, and let me know about it. 

- Ask me for permission first if you wish to use larger portions of this code, make a modified/improved version, include it in a mod pack, etc..., and don't forget to provide credit.

- Do not re-upload this mod or any of my mods anywhere without my explicit permission... ANYWHERE!

* * * * *
