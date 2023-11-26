# [XP & Level Controller]
*V. 1.0*

Adds a system to the game that allows you to set a level threshold that makes nothing scale past that point.

*You will still be fighting, for example, a level 80 enemy, but they will have the base stats of a level 50 enemy.*
*By default this is set to follow the vanilla lvl 80op10 cap, so you need to manually open the mod file using BLCMM to change it to something lower.*


Also gives you options to increase XP gain across the whole game (set to 1.2x for enemies and 1.4x for quests by default), as well as an additional multipiler to XP gain once you are beyond the level threshold mentioned above (set to 3x by default).


### DISCLAIMER

This mod is incompatible with Co-Op. Your game will crash.




## How to install mod

*This section will assume that you haven't installed a BL2 mod before. Feel free to skip steps if you have it set up already*

**If you are completely new to modding**, please watch **[this video](https://www.youtube.com/watch?v=57WxvASCX70&t=1s)** done by Apple1417 to install the PythonSDK. This is required for both executing the mod in the game to apply its effects, and to make other mods work that the Level Controller requires to function.

*You may also click [this link](https://bl-sdk.github.io/) for a written guide on how to install the SDK. Also leads to the video guide listed above.*

**You then need to download the following PythonSDK mods if you have not already:**

> **[Command Extensions](https://bl-sdk.github.io/mods/CommandExtensions/)** - Required in creation of new objects that this mod relies on.

This mod **will not work** if you have not properly installed and enabled Command Extensions.

*Credits to Apple1417 for this mod*


**Once you have all this setup, please right click [this link](https://raw.githubusercontent.com/osetor74/BLCMods/master/Borderlands%202%20mods/osetor74/Oselands%20Standalones/XP%20%26%20Level%20Controller/XPController.blcm) and save the file as new within your Binaries folder to install the mod.**


## How to make the mod work

Assuming you have followed the steps in the last section, you then need to execute the mod while in the main menu of the game.

Open your console
*(tilde by default when installing the PythonSDK. If you do not have a key that naturally creates a tilde then you should also install the Hex Multitool to manually set the console key to somethting else)*

Then type in "exec XPController.blcm" (assuming you didn't rename the file)

After that, it should show you a notification that it is working.


---
