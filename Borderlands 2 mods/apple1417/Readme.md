### Anemone Fast Travels
Super quick fix to let you fast travel to the two new one-way stations.
I will try to expand this with a few related QoL fixes.

### Bigger Is Not Always Better
Allows you to switch the direction of the arrows when comparing items.
Looking for a low damage gun, high fuse grenade, or low booster chance shield? Now you can make the arrows point in the right direction.
Most options will make smaller better for that stat. The options where smaller is already better are  all labelled, and they will make bigger better instead.
Note that not all stats display properly when this is done, so only the ones that work are included.

Incudes an option to change grenade status effect chance, which is only displayed when also using Grenade Status Chance Shower.

`BiggerIsNotAlwaysBetter_Broken.blcm`, contains all the stats that display incorrectly when the direction is changed. These may eventually be fixed and combined into the main file

### Grenade Status Chance Displayer
Shows the status effect chance on grenades.    
Note that just like weapons, the exact chance varies based on the health type (flesh/shield/armour) you use it on, so it won't always be completely accurate.

[Also see the TPS Version](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/apple1417/GrenadeStatusChanceDisplayer.blcm)

### Higher Level Scaling Remover
Removes various forms of scaling that happen when there is a large level difference between you and your enemy.

[Also see the TPS Version](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/apple1417/HigherLevelScalingRemover.blcm)

### Item Level Uncapper
DEPRECATED - Use the [Python Mod](https://github.com/apple1417/bl-sdk-mods/tree/master/ItemLevelUncapper) instead


~~This mod is useless by itself, it should be used alongside the hexedit to increase the player level cap.    
Fixes the level cap of most items so that they continue spawning past level 100.    
Note that items past level 127 will overflow upon save-quit, and that Gibbed's Save Editor won't let you create items past 127, so past that point you'll have to pick up everything you use within the same session.    
Also note that there may still be various other issues with an increased level cap, this only fixes that most items stopped spawning.~~

~~[Also see the TPS Version](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/apple1417/ItemLevelUncapper.blcm)~~

### No Haderax Despawn
Prevents Haderax from despawning when you die

### Text Fixes
Fixes various inconsistencies in text across the game.    
This includes terminology changes like the Hoplite *decreasing* movement speed while the Fabled Tortoise *reduces* it, as well as small spelling and capitalization changes, such as Kreig's Slayer *of* Terramorphous vs everyone else's Slayer *Of* Terramorphous.    
In case of conflicts let any other mods overwrite this one.
