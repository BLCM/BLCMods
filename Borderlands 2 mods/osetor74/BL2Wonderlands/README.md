# BL2:Wonderlands
***Special thanks to playtesters: Vi, Rapoulas, Toto, Graimer***

### Scroll down a little bit for instructions on mod installation, as well as being able to convert Oselands to work with this mod

## Mod Info

A complete rework of Borderlands 2 characters' skill trees to add functionality to **multiclass** similar to Wonderlands.

In essence, there are 6 skill tree branches crafted specifically for this mod, each one representing a Borderlands 2 character. As if the unique aspects of that character were condensed into a single tree.

The character you are playing always comes with the tree dedicated to that character, and you can toggle your secondary class within the mod file using BLCMM. **By default this is set to no multiclass, so you need to use BLCMM**.

Much like Wonderlands, the order of your skill trees does not matter (i.e Siren/Commando and Commando/Siren). Both versions have the exact same potential within their trees. The thing that differs is the action skill you are able to use

![An example of what the skill trees look like](https://i.imgur.com/J874JxV.png)


Your green skill tree is the one determined by the character you are playing, and blue is your selected secondary class.

The purpose of the red tree is for small stat bonuses after level 50 as you level up through UVHM, regardless of which classes you picked. The exact mechanics of it are explained in-game


### DISCLAIMER

If you are going to play with this mod and start at level 1, you need to make the character and get to the first fast travel point *before* you turn the mod on. If you enter the character select screen with this mod turned on, your game will crash.

Also, the mod is incompatible with Co-Op (sadly). That also makes the game crash.




## How to install mod

*This section will assume that you haven't installed a BL2 mod before. Feel free to skip steps if you have it set up already*

**If you are completely new to modding**, please watch **[this video](https://www.youtube.com/watch?v=57WxvASCX70&t=1s)** done by Apple1417 to install the PythonSDK. This is required for both executing the mod in the game to apply its effects, and to make other mods work that BL2:Wonderlands requires to function.

*You may also click [this link](https://bl-sdk.github.io/) for a written guide on how to install the SDK. Also leads to the video guide listed above.*

**You then need to download the following PythonSDK mods if you have not already:**

> **[Command Extensions](https://bl-sdk.github.io/mods/CommandExtensions/)** - Required in the functionality of the entire mod

This mod **will not work** if you have not properly installed and enabled these 2 mods (mainly command extensions, but still)

*Credits to Apple1417 for Comamnd Extensions*


**Once you have all this setup, please right click [this link](https://raw.githubusercontent.com/BLCM/BLCMods/master/Borderlands%202%20mods/osetor74/Oselands/Oselands.blcm) and save the mod file as bl2wl.blcm**


# Oselands Conversion

This mod is built with compatibility with Oselands in mind (for the most part), and below are the instructions on how to make it work.

You can go to the Oselands mod page through this link

### Make sure you have "Structural Edits" turned on in BLCMM.  Tools > Settings
![structural edits](https://i.imgur.com/GY64MHN.png)

### ***Make a copy of Oselands to be sure***, open the file and import your bl2wl.blcm
![import mod](https://i.imgur.com/9377L5D.png)

### Delete the "Vault Hunters" category from the Oselands file
![delete VH category](https://i.imgur.com/EvXXb5Q.png)

### Move the imported file below Enemy Changes (click & drag)
![aaaaaaaaa](https://i.imgur.com/ylKyVtK.png)

### Move the "Global" and "Relic Rework" categories below the imported file
![bbbbbb?](https://i.imgur.com/w08Laj9.png)

### Ta-daaa! it should now look something like this. Don't worry about all the overriding, it's meant to do that
![ccccc!](https://i.imgur.com/RDMNnsJ.png)
