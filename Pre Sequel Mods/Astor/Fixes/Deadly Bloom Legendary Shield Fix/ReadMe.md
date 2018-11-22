## *Deadly Bloom* Legendary Fix

The *Deadly Bloom* Legendary bug, as explained on **[Borderlands Wiki - Deadly Bloom](https://borderlands.fandom.com/wiki/Deadly_Bloom)** page:

> Though it displays in inventory as a purple-rarity item, ***the Deadly Bloom is internally classified as a legendary, and is part of the general legendary loot pool***. Because of this the shield has a small chance to be found from any suitable loot source, including from chests and other containers as well as from defeated enemies. 
>

### My modest contribution to fix this bug:

Such a fix didn't seem to exist for TPS, though, so I took it upon myself to create one...

### Step 01: Legendary Rarity fix:

With a simple tweak, the *Deadly Bloom* has regained his *legit* Legendary rarity, instead of the Epic (purple) rarity.

### Step 02: Legendary Value fix:

With another simple tweak, the *Monetary Value* from the *Deadly Bloom* is adapted to his (recovered) Legendary rarity.

### Step 03: Legendary Skin Fix

To find a way to give a Legendary skin to the *Deadly Bloom* make me scratch my head more than once, because unlike the applied solution for the identical bug in BL2, in TPS, I cannot use the following command:

```
set GD_Shields.Material.Material5_Legendary_Nova_DeadlyBloom Material Item_Shields.Materials.Mati_ShieldTorgueLegendary
```

Why?... Well... I had imagined that, when developping TPS, 2K Australia had just repeated the same mistake that GearBox had made previously when developping BL2... No way! They make it worse because ```Item_Shields.Materials.Mati_ShieldTorgueLegendary``` didn't exist in TPS!!! :tired_face:

After some research, I was forced to notice that only 2 Unique Torgue Shields exist in TPS: *Asteroid Belt*, a Unique Rare (Blue) spike shield which launch a homing meteor and the *Deadly Bloom*... but no trace from any Legendary Torgue shield anywhere; so it make sense if ```Item_Shields.Materials.Mati_ShieldTorgueLegendary``` isn't present in TPS... even if that don't solve my problem! :thought_balloon:

Obviously, if I make any modification in the actual ```Item_Shields.Materials.Mati_ShieldTorgueEpic``` used, this will not only apply to the *Deadly Bloom* skin, but also to all the Epic (purple) *Explosive Spike Shields* and *Explosive Nova Shields* manufactured by Torgue. :unamused:

My solution to solve this problem "properly", was to borrow the ```Item_Shields.Materials.Mati_ShieldVladofLegendary``` from the Vladof Legendary Shields skin and use it for the *Deadly Bloom*. :relieved:

![Deadly Bloom Legendary Rarity, Value & Skin Fix](https://imgur.com/5q2qCWI.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")
__Note:__ The *Vertical Lines Pattern* are gone, but the *Deadly Bloom* look better with the Legendary shield skin borrowed to Vladof... at least in my eyes :smile: 

### Step 04: Optional Legendary Shield Properties Upgrade: 

There is a toggle option to upgrade the *Deadly Bloom* basic stats (Capacity/Nova Damage/Nova Radius) to create a real legendary variant for bigger explosive supernova destruction.

__No Upgrade:__ shield properties similar Epic (purple) values.

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Epic (Purple)            | 12            | 12                       | 12                       |

![Deadly Bloom without Legenday Properties Upgrade](https://imgur.com/sjPiAnr.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")

__Legendary Upgrade:__ (Capacity + Nova Damage + Nova Radius Upgraded)

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Legendary                | 16            | 18                       | 18                       |

![Deadly Bloom with Legenday Properties Upgrade](https://imgur.com/8PoEvdJ.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")

### Step 05: Legendary Shield Lootpool:

At least, no change needed to be done to the lootpool, as the *Deadly Bloom* is already in the (correct) Legendary pool.

__Note:__ The *Deadly Bloom* can be randomly obtained in the grinder by grinding three Legendary shields (like any other Legendary shield)

Enjoy!

### Changelog:

- v1.0.0, November 20, 2018
  - Initial public release
- v1.0.1, November 25, 2018
  - Add Optional Legendary Properties Upgrade
- v1.0.2, November 30, 2018
  - Add Optional TPS Rarity Color Fix (with toggle option)  
 
### Compatibility:

- 100% compatible with the latest version of [TPS Community Patch](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Community%20Patch)
- Should be compatible with most other mods, as long as they do not touch the *Legendary Nova Shield Properties* or *Legendary Nova Spike Properties*

### To do:

- [ ] Find a way to get back the *Vertical Lines Pattern* for the skin.
- [ ] Might be tweaked later... if a better solution is found?
  
### Note: 

Any critique would be appreciated as I am still beginner to make Mods... and by the way, please leave constructive criticism if you make a video. 
Enjoy!

### Disclaimer

All files and content provided here were written by me (Astor), unless stated otherwise.

- They are free for personal use. You may use these mods in videos, or for streaming, as long as you give me proper credit. I would appreciate that you'll letting me know about it, and at least, provide a link to [Github.com/BLCM/BLCMods/Pre-Sequel Mods/Astor](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Astor).

- You may re-use small bits of code (e.g. formulas, behavior modifications, etc) for your own purposes, and let me know about it. 

- Ask me for permission first if you wish to use larger portions of this code, make a modified/improved version, include it in a mod pack, etc..., and don't forget to provide credit.

- Do not re-upload this mod or any of my mods anywhere without my explicit permission... ANYWHERE!

* * * * *



