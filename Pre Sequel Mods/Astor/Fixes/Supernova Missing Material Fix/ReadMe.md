## *SuperNova* Missing Material Fix

The Missing Material bug (and its consequences), as explained on __[Borderlands Wiki - Supernova](https://borderlands.fandom.com/wiki/Supernova)__ page:

> Due to a coding bug, it is possible for the *Supernova* to spawn with four different materials rather than just the predefined one. Normally, a Legendary shield has a predefined material, either custom or the standard Epic rarity material. **The material difference affects the shield capacity, nova damage, and nova radius, even when all other parts are the same.**
>
>- **Common** (Same skin as *white rarity* Maliwan shields)
>- **Uncommon** (Same as *green rarity* Maliwan shields)
>- **Rare** (Same as *blue rarity* Maliwan shields)
>- **Epic** (Same as *purple rarity* Maliwan shields) 
>
> When the *Supernova* spawns with the Uncommon (Green) skin, its rarity colour will be Magenta, although it is still sorted in the inventory as if it were a Legendary shield. The Magenta rarity version does not actually have different properties than the other versions of the shield, apart from the usual Material Grade bonuses.

To explain the *Missing Material* bug in a simple way, when a Legendary or Unique shield spawn, it has his own predefined material... for example:

__*Sunshine*__ - Unique Maliwan Rare (Blue) Nova shield 
 
```ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_Nova_Sunshine'```

__*Deadly Bloom*__ - Unique Maliwan Epic (Purple) Nova shield
 
```ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_Nova_DeadlyBloom'```

__*Black Hole*__ - Legendary Maliwan Nova shield
 
```ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_Nova_Singularity'```

_*SuperNova*__ - Legendary Maliwan Nova shield... instead to have his own predefined material (like above), it has the following:

```MaterialParts=ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_NovaSpike_Maliwan'```

...which include four different materials: 

```ShieldPartDefinition'GD_Shields.Material.Material1_Common_NovaSpike_Maliwan'```
```ShieldPartDefinition'GD_Shields.Material.Material2_Uncommon_NovaSpike_Maliwan'```
```ShieldPartDefinition'GD_Shields.Material.Material3_Rare_NovaSpike_Maliwan'```
```ShieldPartDefinition'GD_Shields.Material.Material4_VeryRare_NovaSpike_Maliwan'```

... and that's the reason why the *SuperNova* can spawn with four random different materials affecting the shield capacity, Nova damage, and Nova radius.

Not clear? ... Well, perhaps it will be more easy to compare (and understand) how the *Random Material Grade Bonuses* differences affect the *SuperNova* capacity (Capacity), Nova damage (Special 01), and Nova radius (Special 02) in a table:

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) |
| -------------            | ------------- | -------------            |-------------             |
| Common (White)           | N/A           | N/A                      | N/A                      |
| Uncommon (Green)         | 4             | 6                        | 6                        |
| Rare (Blue)              | 8             | 12                       | 12                       |
| Epic (Purple)            | 12            | 18                       | 18                       |

### My solution to fix it:

Such a fix didn't seem to exist for TPS, though, so I took it upon myself to create one...

As the *predefined* or *custom* material is missing for the *SuperNova*, I make it spawn with the best Material available, in this case, the *Epic (Purple) Material*, to get the best shield capacity, Nova damage, and Nova radius as possible. 

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Epic (Purple)            | 12            | 18                       | 18                       |

Obviously, with the *Epic Material* selected, the *SuperNova* has the properties from a *Unique Epic (Purple) Shield* (in fact the *Material Grade Bonuses* are identical to the Maliwan Legendary *Flame of the Firehawk* in BL2), but NOT (real) Legendary shield properties.

### Legendary Skin Fix

As the *Supernova* use now a the *Epic (Purple) Material*, it will have a *Epic (Purple) Skin*, so even if it's better than a random Epic/Rare/Common/Uncommon skin, I give it a legit Legendary Maliwan Skin.

![SuperNova Missing Material Fix](https://imgur.com/2J1QGKs.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")

### Legendary Value fix:

As the Monetary value, is linked to the *Epic Material* used, I upgrade the Epic (purple) Monetary Value to Legendary Monetary Value.

### Optional Legendary Shield Properties Upgrade 

There is a toggle option to upgrade the *Material Grade Bonuses* from the *SuperNova* properties:

__No Upgrade:__ (shield properties similar to the Maliwan Legendary *Flame of the Firehawk* in BL2)

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Legendary                | 12            | 18                       | 18                       |


__Capacity Upgraded Only__


| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Legendary                | 16            | 18                       | 18                       |

__Capacity + Nova Damage Upgraded__

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Legendary                | 16            | 24                       | 18                       |

__Full Upgrade:__ (Capacity + Nova Damage + Nova Radius Upgraded)

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Legendary                | 16            | 24                       | 24                       |


On this way, instead to have the properties from a *Unique Epic (Purple) Shield*, the *SuperNova* can become a (real) *Legendary shield* and the solution applied must be safe for the *Sanity Check*.

__Note:__ No change done to the lootpool, as the *SuperNova* is already in the (correct) Legendary pool.

Enjoy!

### Changelog:
- v1.0.0, November 17, 2018
  - Initial public release
 
### Compatibility:

- 100% compatible with the latest version of [TPS Community Patch](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Community%20Patch)
- Should be compatible with most other mods, as long as they do not touch the *Legendary Nova Shield Properties* or *Nova Spike Properties*

### To do:

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