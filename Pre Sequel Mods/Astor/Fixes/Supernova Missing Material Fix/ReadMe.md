## *SuperNova* Missing Material Fix

__Note:__ This fix is the stand-alone version from the one include in my Mod: *Black Hole & SuperNova On Steroids* (available in *Gears Improvement*)

Used independantly, the fix will resolve the *Missing/Random Material* bug (and the Properties consequences) from the *SuperNova* and restore (as close as possible) the Properties with the best Material available previously, which was the Epic (purple) Material.

![SuperNova Missing Material Fix](https://imgur.com/oyaBnu1.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")

If you're using *Black Hole & SuperNova On Steroids*, there's no longer any reason to use this fix... but it won't hurt anything to have both enabled, though!

* * * * *

## What is the *SuperNova* Missing Material Bug?

The Missing Material bug (and its consequences), as explained on __[Borderlands Wiki - Supernova](https://borderlands.fandom.com/wiki/Supernova)__ page:

> Due to a coding bug, it is possible for the *Supernova* to spawn with four different materials rather than just the predefined one. Normally, a Legendary shield has a predefined material, either custom or the standard Epic rarity material. __The material difference affects the shield capacity, nova damage, and nova radius, even when all other parts are the same.__
>
>- __Common__ (Same skin as *white rarity* Maliwan shields)
>- __Uncommon__ (Same as *green rarity* Maliwan shields)
>- __Rare__ (Same as *blue rarity* Maliwan shields)
>- __Epic__ (Same as *purple rarity* Maliwan shields) 
>
> When the *Supernova* spawns with the Uncommon (Green) skin, its rarity colour will be Magenta, although it is still sorted in the inventory as if it were a Legendary shield. The Magenta rarity version does not actually have different properties than the other versions of the shield, apart from the usual Material Grade bonuses.

To explain the *Missing Material* bug in a simple way, when a Legendary or Unique shield spawn, it has his own predefined material... for example:

__*Sunshine*__ - Unique Maliwan Rare (Blue) Nova shield 
 
```ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_Nova_Sunshine'```

__*Deadly Bloom*__ - Unique Maliwan Epic (Purple) Nova shield
 
```ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_Nova_DeadlyBloom'```

__*Black Hole*__ - Legendary Maliwan Nova shield
 
```ItemPartListDefinition'GD_Shields.Material.PartsList_Materials_Nova_Singularity'```

__*SuperNova*__ - Legendary Maliwan Nova shield... instead to have his own predefined material (like above), it has the following:

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

### My modest contribution to fix this (naughty) bug:

If I modify any properties from the actual Material (Common/Uncommon/Rare/Epic) wich actually spawn randomly with the *SuperNova*, this will modify all the Common/Uncommon/Rare/Epic Maliwan Spike Shield and the Common/Uncommon/Rare/Epic Maliwan Nova Shield... so the only way to solve this *Missing Material* bug properly, it's to borrow a *Unique (predefined) Material* to another Legendary shield.

### Step 1: Missing Material Fix

To keep the thing simple, as the *SuperNova* is a Legendary Maliwan shield, I will borrow the Missing Material from the *Black Hole* which is another Legendary Maliwan shield, and make the *SuperNova* always spawn with this *Unique (predefined) Material*.

So yes, now, the *Black Hole* and the *SuperNova* share the same Unique Material, which mean that any modification made to this Unique Material will apply on both shields... and obviously the *Black Hole* Unique Material already modifies the *SuperNova* Properties.

### Step 2: Unique Properties Fix

Yep! Ironically, I solve one problem by creating another one, but now as the *SuperNova* has Unique Properties, it can be solved easily.

Since the *SuperNova* share the ```GD_Shields.Material.PartsList_Materials_Nova_Singularity``` from the *Black Hole*, the *Material Grade Bonuses* from the *Black Hole* applies the *SuperNova*, and of course, they are different... very different:

| -Material Grade Bonuses- | Capacity      | Special 01 (Nova Damage) | Special 02 (Nova Radius) | 
| -------------            | ------------- | -------------            |-------------             |
| Black Hole               | 16            | 30                       | 0                        |
| SuperNova (Epic)         | 12            | 18                       | 18                       |

To resorb these differences caused by the new shared *Black Hole's Unique Material*, I manuallly edit the properties from the *SuperNova* to get them back as close as possible to the best Material available previously, which was the Epic (purple) Material... and here's the result from this tweak:

| SuperNova lvl 50    | Vanilla Epic (purple) Material | With Shared Black Hole Material    |  
| -------------       | -------------                  | -------------       |                              
| Capacity:           | 10242                          | 10310               |  
| Recharge Rate:      | 1750                           | 1751                |  
| Recharge Delay:     | 4,06                           | 4,01                |  
| Nova Damage:        | 20285                          | 21007               |  
| Nova Radius:        | 2056                           | 2052                | 

### Step 3: Legendary Skin Fix

As the *Supernova* use now a the Black Hole's *Unique (predefined) Material*, it will have a Legendary Maliwan skin instead of a random Epic/Rare/Common/Uncommon skin.

__Know Issue:__ It's purely cosmetic, but the the *Black Hole* of *SuperNova* share the same skin.

### Step 4: Legendary Value fix:

As the Monetary value is linked to the Black Hole's *Unique (predefined) Material* used, the random Epic/Rare/Common/Uncommon Monetary Value is upgraded to Legendary Monetary Value.

### Step 4: Legendary Shield Lootpool:

At least, no change needed to be done to the lootpool, as the *SuperNova* is already in the (correct) Legendary pool.

__Note:__ The *SuperNova* can be randomly obtained in the grinder by grinding three Legendary shields (like any other Legendary shield)

![SuperNova Missing Material Fix](https://imgur.com/oyaBnu1.jpg "Don't worry guys... even if my screen capture show French text, my mods are in English")
Et voila... Missing/Random Material Fix done!

Enjoy!

### Changelog:
- v1.0.0, November 17, 2018
  - Initial public release 

### Compatibility:

- 100% compatible with the latest version of [TPS Community Patch](https://github.com/BLCM/BLCMods/tree/master/Pre%20Sequel%20Mods/Community%20Patch)
- Should be compatible with most other mods, as long as they do not touch to the *Black Hole Properties*
- __Know Issue:__ It's purely cosmetic, but the the *Black Hole* of *SuperNova* share the same skin.

:warning: This fix is already includes my *Black Hole & SuperNova On Steroids* Mod, so if you're already using it, there's no longer any reason to use this fix... but it won't hurt anything to have both enabled, though... in this case, this *Supernova Missing Material Fix* must be placed __BEFORE__ the *Black Hole & SuperNova On Steroids*.


### To do:

- [ ] Create a new skin to make the difference faster between the *Black Hole* of *SuperNova*.
  
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