# ============= [ Oselands ] =============

Version 1.2.6 changelog


 >**This is an extensive changelog with (most) changes within the mod.**
 > **I won't go in-depth with every single number change, but it serves**
 > **as an explanation on what to expect**


Use CTRL+F to find a section easier.

---

  #### > Other mods included in Oselands

  #### > Global Changes
	> Stop scaling past 72
	> Lower scaling
	> UVHM Rebalance
	> Element changes
	> Player scaling changes
	> Slower enemy bullets
	> Vendor changes
	> Miscellaneous
	> Player Skill Point Limiter


  #### > Relic Rework
	> Random stats
	> Uniques


  #### > Weapon Changes
	> Weapon types/Manufacturers
	> Weapon Parts
	> Effects of the changes (developer notes)
	> Gun Additions / other changes
	> Shield changes
		>E-Tech Shields

  #### > Drop Changes
	> Rarity odds
	> Raid Boss Legendary Drops
	> Dedicated legendary drop changes
	> Torgue Vendor Conversion to Legendary Vendors
	> Knuckledragger
	> Golden Chest
	> Tubbies
	> Witch Doctors
	> Omnd-Omnd-Ohk
	> Uranus / Cassius
	> Jimmy Jenkins / Loot Goon Goliaths / Muscles
	> Haderax Chests
	> Mimics

  #### > Enemy Changes
	> Base Enemy Stats
 	> Raid Bosses
	> Southpaw Steam & Power
	> Saturn, Uranus, Constructors

  #### > Vault Hunters
	> Overview
	> Base melee changes
	> Individual character changes (Search for the character's name)

  #### > Unique Items
	> Unique Rarity
	> *Completely new Legendary items*


---


## Other Mods Included

	- Most of these mods are QoL mods that i believe make the game more fun/comfortable to play
	- Credits of those that made the mods can be found in the mod file if you open it with BLCMM


	- A large portion of the Unofficial Community Patch
		- Mostly the QoL and bug fix side of the patch, as well as most of the dedicated drop pool changes

	- Loot Midget World
		- Makes Loot Midgets spawn in almost every part of the game, instead of a couple specific ones
		  Has been tweaked a little bit for Oselands

	- No More Orders
		- Removes the need to have Doctor's Orders active to make loot midgets spawn in the Wildlife Exploitation Preserve

	- Better Fast Travel
		- Opens all the one-way Fast Travel stations to work like all the other ones

	- More Chests on Pandora
		- Pretty self explanatory

	- Less Dumb Visuals
		- Reduces and tweaks a lot of particle effects and UI elements to make them clutter the screen less while playing

	- UHD Elemental Sniper Fix (TURNED OFF BY DEFAULT, ENABLE WITH BLCMM)
		- fixes various problems with the UHD patch breaking skins




## Global Changes

	> Stop scaling past 72

		- Added a system where nothing scales their stats past (by default) level 72. If you open the mod file with BLCMM,
		  you can choose betwee level 60, level 72, level 80 and reverting it back to vanilla OP10.

		- an OP7 gun or shield will have the exact same stats as an op0 variant, same with enemy base health and damage.
		  This means that you do not have to refarm items in OP levels at all. The items you get at the set threshold
		  will carry you through every level.



	> Lower Scaling

		- The level scaling multiplier was lowered from 13% per level to 9% per level, which creates much lower numbers
		  Across the game. This shouldn't take away from the experience, instead it should make it so guns last longer
		  while leveling.



	> UVHM Rebalance

		- Enemy health was drastically reduced in UVHM, and slag is way less necessary.
		  The health of enemies in UVHM scales naturally the higher level you are, starting at 50 and capping at 60.
			This should make the entry to UVHM a bit smoother (or 'easier')
		-XP gain is increased after level 60 by 50%
		
		- Passive enemy health regen in UVHM was also removed and they passively take an additional 25% DoT damage.
	
		  (Do note that with the 'nerf' to slag, life steal or any other healing mechanic that relies on
		   a % of damage dealt is just weaker)



	> Element changes

		Elemental damage now follows the following modifiers:

		- Non-Elemental(NE)/Explosive vs all	-> 1x
  		- Fire/Corrosive vs correct health type	-> 1.1x
		- Fire/corrosive vs wrong health type 	-> 0.7x
		- Shock vs shield 			-> 1.2x
		- Shock vs non-shield			-> 0.9x
		- Slag vs all health types		-> 0.95x


		- The duration of all fire/corrosive/shock status effects is now 5 seconds (instead of 5/8/2),
		  and removed shock DoT's inability to stack multiple times on the same enemy
			- This should make it so they are all much more consistent between each other

		- There is no longer any change in elemental damage when moving between playthroughs, and enemy health has
		  been adjusted for elemental damage being so much lower now



	> Player scaling changes

		- Player health (and shield capacity of all shields) is increased by 20%

		- Player skill DoT damage was 'fixed' and is now more heavily used as well.


	> Slower enemy bullets

		- All enemy bullets' speed has been reduced to give you a slighty higher chance of being able to dodge them.
		- This affects rocket enemies the most, making them way more manageable.

		- Multiple options that you can choose from with BLCMM that change how much you want the bullets to be slowed by
			- Options for completely normal speed to -300% speed. Set to -200% by default.


	> Vendor changes

		- Rarities of items in gun and health vendors now become better depending on the level of the area; higher level = better
		- Multiple options that you can choose from with BLCMM that change the cost of ammo and health from vendors
			- Ranges from vanilla values to completely free; set to 25% of original cost by default

		- Purple items in vending machines have a 20% chance to be replaced by a blue/purple unique of the same weapon type



	> Miscellaneous

		- Backpack SDUs now provide +4 to backpack size instead of +3
		- Enemies give 20% more xp, quests give 40% more xp
		- Respec costs no money
		- Legendary rarity color was changed to be a bit darker
		- Vehicles now have 20% more health to compensate for the NE/Explosive/Slag changes
		- You move twice as fast in FFYL compared to vanilla
		
		
		
	> Player Skill Point Limiter
	
		- You now gain your first skill point at level 2 instead of 5

		- You now stop gaining skill points after level 69. This grants you a total of 68 skill points, which is equal
		  to how much you would have had with the old level 72 cap.

			*the reduction in total amount of skill points in theory means more decision making in your build,
			 leading to more possible build diversity. In reality this is still a high amount of skill points,
			 but at the very least it's not limiting.




## Relic Rework

	> Random stats

		- Every non-unique relic in oselands now spawns with an additional randomised "Secondary Stat".
		  This can be anything from fire rate to reload speed to movement speed to elemental resistances to max health to- you get it.
			(the secondary stat can't be the same as the main stat of the relic, so max health on a vitality relic, for example)

		  This makes relics much more interesting and exciting to find, and more impactful from the very start.
		  The goal is that uniques(/ancients) would offer a new opportunity rather than just be better
		  (this is a common theme with me)



	> Uniques

		(A small amount of movement speed = usually 15%)


		Vault Hunter's Relic
			-Now has 15% movement speed instead of the increased blue item chance.
			 This is supposed to just be a nice boost to make the very early game a bit more comfortable,
			 while not being powerful enough so you can throw it away when you find literally anything else


		Afterburner
			-Now comes with 25% movement speed (UCP)

		
		Moxxi's Endowment
			-Spawns with an additional secondary stat alongside its xp buff


		Deputy's Badge
			-Increases mag size for shotguns by a flat +2 after other bonuses, plus some shotgun reload speed


		Sheriff's Badge
			-Legendary Rarity
			-A large global fire rate buff (around the same values as vanilla, but not locked to pistols), and additional
			 swap speed


		Otto Idol
			-Retains its health recovery aspect and the curse.
			 However, it is much more powerful (40-50% hp gained on kill at the highest levels) at the cost of a part of your
			 max health


		Ranger Emblem (Replacing the Winter is Over relic)
			-Legendary Rarity
			-Has both a reload speed and mag size secondary stat

		
		Loaded Dice (Replacing Lucrative Opportunity)
			-Increases the chance for a world drop legendary by a little bit


		Blood of Terramorphous
			-Only drops in UVHM
			-Grants immunity to fire DoT, akin to a shield. Plus its normal health regen.

		
		Blood of the Ancients
			-Unchanged, with exception of lowered numbers to match the changes to vitality relics


		Skin of the Ancients
			-Highest damage reduction boost in the game
			- +20% increased effectiveness of shield damage abilities


		Bone of the Ancients
			-Same as vanilla, but with lowered numbers. However, it is still the only relic in the mod with both
			 elemental damage and cooldown rate, which can be useful.


		Heart of the Ancients (specifically the AR version)
			-FFYL duration and life (vanilla), plus increased critical damage.


		Wings of the Ancients (New)
			- 38-45% movement speed, with a secondary stat


		Shadow of the Seraphs
			-All of your shots with any gun gain +1 projectiles, at the cost of damage, fire rate and accuracy


		Might of the Seraphs
			-A huge amount of melee override cooldown rate, and a small amount of movement speed


		Blood of the Seraphs
			-Increased max health as well as some life steal


		Soul of the Seraphs (Replacing Breath of the Seraphs)
			-Increased cooldown rate and a small amount of movement speed
			-Reduces your shield's recharge delay by a flat 1 second, after other buffs

		
		Death Toll (Replacing Mouthwash)
			-Legendary Rarity
			-Increased kill skill duration, movement speed and fire rate
			-No longer has an interaction with the Toothpick


		Shaped Glass (Replacing Hard Carry)
			-Pearlescent Rarity
			-A massive gun damage boost, but halves your health
			-No Longer has an interaction with Easy Mode (Which was reworked)
			
		
		Red Hellion (Replacing Heart of the Ancients - Pistol)
			-Legendary Rarity
			-Slightly increased reload speed
			-Applies 75% of your movement speed bonuses to your gun's fire rate (with a maximum of +100% movement speed)
			
			
		Medusa's Eye (Replacing Heart of the Ancients - Shotgun)
			-Legendary Rarity
			-Slagged enemies are rooted in place instead of slowed
			-Enemies are Blighted, getting their health drained equal to 100% of your maximum health per second


		Backup Magazine (Replacing Heart of the Ancients - SMG)
			-Legendary Rarity
			-Gain a small amount of ammo regen, akin to Salvador's Hoarder class mod
			-Slightly increased mag size
			
			
		Deathless (Replacing Heart of the Ancients - Sniper)
			-Legendary Rarity
			-Massive boost to shield capacity and recharge rate
			-Health is drained while you are above 10% HP


		=== Completely New Relics ===

		Eternal Youth  (Legendary)
			-Reduces your max shield to 10
			-While shield is full, you gain health regeneration equal to your equipped shield's recharge rate
			-Halves life steal effects

			-7.5% chance from Cursed Pirates


		Temporal Teardrop  (Legendary)
			-Small cooldown rate buff
			-While your action skill is active, it continues to cool down at 50% of its regular rate.

			-World Drop only


   		Pearl of Power  (Seraph)
			-Always rolls one of the 6 characters, and grants skill point bonuses to skills of that character.

			-Rolls a primary skill (+3) and a secondary skill (+2).
			 If both rolls give the same skill, it instead gives +4

   			- Skills are chosen from a predetermined list of 6 skills per character:

			Axton: Sentry, Crisis Management, Expertise, Steady, Resourceful, Quick Charge
			Maya: Reaper, Elated, Fleet, Inertia, Blight Phoenix, Discharge
			Salvador: Money Shot, Locked and Loaded, 5 Shots or 6, Yippe-Ki-Yay,
				  I'm The Juggernaut, Just Got Real
			Zer0: Weakness Expl0it, Fast Hands, Tw0 Fang, Fearless, Ambush, Unf0reseen
			Gaige: The Better Half, Unstoppable Force, Strength of 5 Gorillas, Evil Enchantress,
			       Blood-Soaked Shields, Radical
			Krieg: Blood-Filled Guns, Boiling Blood, Feed the Meat, Strip the Flesh, Burn Baby Burn
			       Fire Fiend


			-Guaranteed drop whenever you kill *any* raid in UVHM.


## Weapon Changes


	> Weapon Types/Manufacturers

		- Weapons now list their final crit damage on the item card instead of a % bonus compared to the base 2.0x multiplier

		- I won't list every change like damage or fire rate differences, those can be found in-game. Just try different guns and
		  see how they feel.

			- Rarity changes
				- Mag size and accuracy buffs from rarities has been removed

				- In vanilla, the damage buffs from item rarities stacked with those from parts, which made +damage%
				  parts less effective. This has been changed so that it boosts *base* damage, which means it will be
				  multiplicative with those from weapon parts

				- The rarity damage increase has been changed from 24/48/72% to 15/30/45% for green/blue/purple
					(Guns are more consistently good, damage parts are a tiny bit more effective, and player power in
					general is a bit higher)


			- All base mag sizes for guns have generally been increased to compensate both for the previous change, as well as
			  the changes to matching grip bonuses (listed further down in the weapon parts section).


			- The assault rifle critical damage penalty was removed.


			- All bandit assault rifles, pistols and SMGs have 15% Double shot chance.
			- Removed the aspect from blue+ bandit ARs where they would get a damage and reload penalty in exchange for higher
			  mag


			- Dahl pistols now have a base burst count of 3 while aiming, instead of 2
			- Dahl ARs now have a much shorter delay between bursts
			- Dahl snipers are now semi auto at all times, rather than having a burst while aiming


			- Hyperion guns have 10% increased base critical damage (2.2x instead of 2x)


			- Jakobs guns have 25% increased base critical damage (2.5x instead of 2x)


			- Jakobs and Torgue guns' damage were overall nerfed to compensate for the NE and Explosive damage changes
			  listed under Global Changes > Element Changes


			- Jakobs pistols have a chance to spawn with a Borderlands 1 Revolver style body, lowering their fire rate massively,
			  while increasing base damage, and base critical damage from 2.5x to 3x


			- Jakobs snipers are now always bolt-action, rather than semi auto for blue and purple+


			- Sniper rifle critical damage is calculated differently now, focusing more on base crit rather than increased crit
				- 3x base critical damage, 3.3x for Hyperion(+10%), 3.75x for Jakobs(+25%).

			- Gemstone skins now increase something related to the manufacturer's special effects, intead of being a critical
			  damage bonus for everything. Bandit gets increased double shot chance, Dahl gets increased burst count, etc.


	> Weapon Parts

		- Weapon parts and their manufacturers still keep their identity for the most part. Jakobs are still high damage, low fire
		  rate, tediore is low mag, quick reload, etc.

			- General

				- All vanilla matching bonuses were removed
					- Includes matching grip, matching barrel (a very small amount of damage), and special ones like
					  increased burst for dahl guns on dahl barrels and SMG/Sniper stocks

				- All parts (besides Vladof) now have some kind of small change to either DoT chance or DoT damage.
					- This is to create some small variety with the listed numbers on guns. Maliwan is still the king
					  of DoT.

				- Some stocks have gained small stat buffs to hopefully allow for more diversity. These are supposed to be
				  treated as small bonuses, rather than a main focus. A nice extra.

				- Bandit and Torgue barrels and grips provide +25% Melee Damage.


			- Bandit
				- Barrels now have a mag size buff
				- Stocks now have a small mag size buff
				- Highest DoT chance after Maliwan


			- Dahl
				- Now have a small increase to damage rather than a damage penalty
				- Small increase to both DoT chance and DoT damage


			- Hyperion
				- Now provide critical damage at the cost of damage, and a small amount of bullet speed.
				- Highest DoT damage after maliwan


			- Jakobs
				- Increases damage at the cost of fire rate and mag size (instead of fire rate and reload speed)
				- Has a small DoT chance penalty


			- Maliwan
				- Grip only boosts DoT chance, and barrel only boosts DoT damage. Both are the highest of each category.
				- Now have a very small reload speed buff at the cost of a very small damage nerf

				-Stocks add 1 second to fire/corrosive/shock DoT duration while holding the gun


			- Tediore
				- Grips no longer have a damage penalty
				- Barrels have a sizeable reload speed buff
				- Stocks have a small reload speed buff
				- Has a small DoT damage buff


			- Torgue
				- Grips have a damage buff at the cost of reload speed and accuracy
				- Barrels have a small amount of increased mag size (Does not apply to ARs, since they use unique torgue
				  barrels)
				- Stocks have a small damage buff
				- Has a small DoT damage penalty


			- Vladof
				- Barrels nerfed overall, as they were way ahead of everything else
				- Stocks have a small fire rate buff
				- Has no changes to DoT chance or damage



		- Accessories were more or less normalized across every weapon category (with some exceptions, particularly shotguns and
		  launchers).

			- Accessory_None can't spawn on Blue rarity Unique guns anymore (as well as the Longbow and the Infinity)

			- Bayonets now function similarly to shotguns' "General Boost" accessory, and the original shotgun accessory
			  was replaced with something else. They still retain the +0.5x Melee Damage boost.
			  Bayonets now also passively increase your movement speed by 15% while holding them.

			- Bullet Speed and Accuracy accessories were generally combined into one, and they all have additional fire rate
			  at the cost of a small amount of reload speed (i.e Flying for dahl SMGs or swift for vladof ARs)

			- Stability prefixes now have additional critical damage

			- Assault Rifle Accuracy accessory has been replaced with a double accessory, mimicing the pistol double accessory
				-Includes new prefixes

			- Rocket Launcher Accuracy accessory has been replaced with a ""BFG"" accessory, acting as a stronger variant of the
			  Damage accessory, but doubling the ammo per shot.
				-Includes new prefixes

			- The shotgun vertical grip accessory was heavily nerfed, now providing a +35% increase to pellet count rather than
			  +2, and with a fire rate penalty.

				-(for some guns this can be a buff, mainly high pellet shotguns like a ravager)

				- the accessory, alongside any other part that just wouldn't work on a particular gun (like crit on a
				  splatgun) has been removed from the part lists of that gun

			- SMGs accuracy accessory was replaced with a mag size accessory
				-Includes new prefixes




	> Effects of the changes  (developer notes)

		- The purpose of these changes have been to try to make the guns you find and pick up much more appealing, and  finding a
		  "good gun" is much easier. There will naturally be something better, but the gap in power should be smaller. This also
		  means that you, the player, is just naturally better regardless of what you pick





	> Gun additions / other changes

		- Jakobs and Torgue shotguns now have unique E-Tech barrels, creating the Tracer and Carnage (works like the pearlescent
		  shotgun, with some tweaks, and said pearlescent shotgun was entirely reworked)

		- E-Tech Dart pistols now have high fire rates, and don't consume 2 ammo per shot
		- Torgue pistols now have a unique E-Tech barrel, creating the Carbuncle

		- Snipers' E-Tech barrels are now divided into Splitters and Railguns, Vladof & Dahl / Maliwan & Hyperion respectively.
			-Mimics the laser types from The Pre-Sequel with the same names



	> Shield changes

		- Non-Unique Amp shields were completely reworked
			-No longer have a traditional Recharge Rate, instead recharges to full instantly when the Recharge Delay is over
			-Capacity has been generally lowered to compensate due to this.
			-The damage has been looked over to hpefully make them more appealing to use

			*- These changes were made to hopefully make amp shields a bit more unique compared to everything else,
			   and give you an opportunity to use the amp damage more
			
		- Absorb shields' base absorb chance was increased by 10%

		- Non-Unique Roid shields now provide increased max health. these values are identical to adaptive shields.

		- Non-Unique nova shields now activate when you take damage, regardless of how much shield you have (5 second cooldown)
		  They also gain additional damage equal to 30% of your current max shield capacity

		- Non-Unique Spike shields' damage was tripled

			
		- Shield parts have been completely rebalanced, TL;DR:

			- The shield parts generally keep their identity compared to vanilla, with exceptions

			- Special penalties have been removed, and maliwan's increased special has been slightly lowered.
			  However, it still has the highest +Special

			- Dahl parts now serve as a general-use part, giving a nice boost to the main 3 stats while not affecting special
			  in any way

			- Vladof parts now give a passive 10% movement speed each

			- Maliwan capacitors were reworked to not share stats with other maliwan parts,
			  so the main focus of those parts are the elemental immunities.




			> [E-Tech Shields]

				- This mod introduces new shields under the E-Tech rarity.
				  The whole gimmick with all of these is that, much like Rough Rider, they have 0 shield capacity but grant
				  other bonuses instead, either to compensate for that lack of shield, or just giving the risk of
				  sacrificing survivability to gain something else instead

				  Each E-Tech shield type has a 5% chance of dropping from a particular badass enemy type in the game, listed
				  below:

				- Berserker shield (Bandit) - Badass Psychos
					-Dealing or taking damage causes you enter a rage, gaining movement speed and life steal while your
					health drains very quickly.

				- Titan Heart Shield (Hyperion) - Badass Loaders
					-Grants increased max health, and adds 10% of your maximum health value as amp damage to all your
					 shots

				- Shatter Tank Shield (Pangolin) - Spiderant Kings/Queens (/their renamed versions in higher difficulties)
					-Reduces max health on top of the 0 capacity, but grants flat health regen

     				- Chromatic Hydra Shield (Anshin) - Elemental Badass Skags
					-High adaptive shield effect value
     					-*Overrides* elemental damage multipliers when dealing damage against enemies with its own
	  				 multiplier, negating the downsides of the elemental damage types but also the upsides in
					 exchange for a good general multiplier.



## Drop Changes

	> Rarity odds

		- TL;DR  white less common, purple and legendary more common

		- VeryCommon weight lowered from 200 to 100
		- Common weight lowered from 100 to 60
			
			- Both of the above get reduced down to half of their values between levels 30 and 80

		- Legendary weight increased from 0.01 to 0.0667. This gets increased by 20% for each OP level,
		  up to a tripled value (~0.2)

		- VeryRare weight increased from 0.1 to 0.25


		- Legendary weight is doubled in the following areas:
			Digistruct Peak
			the 3 Circles of Slaughter
			Leviathan's Lair
			Torgue's Arena (the big one in his DLC)


	> Dedicated legendary drop changes

		- Most UCP dedicated pool changes have been ported over to Oselands

		- Head and skin drops have been removed from dedicated legendary pools entirely

		- Any dedicated pool with more than 1 item in the pool has had its chance multiplied by the amount of items in the pool,
		  meaning that any individual item in the pool generally has a 10% chance of dropping, rather than having
		  10% split between all of them

		- Legendary shield pools not world dropping properly has been fixed
		- The 6 "new" legendary relics added in the mod are now part of the world drop pool


	> Torgue Vendor Conversion to Legendary Vendors

		- Torgue Vendors have been changed to now include a massive selection of legendaries every time you load the map it is in.
		  These legendaries are not locked to just torgue items, as they now basically serve the function of a legendary vendor.
			
		- Torgue Tokens now drop everywhere in the game as random drops from enemies, so you end up accumulating them over time.
			Torgue DLC activities still award you with tokens as well, so there is still a reason to farm them specifically.
			
		- Different vendors in the DLC are given different item pools, so it is easier to get the item you want out of them.
			The item types are spread as follows:
			
			Arena 		- shotgun, launcher
			Moxxi's Bar 	- SMG, pistol
			Beatdown 	- AR, sniper
			Pyro Pete's Bar - COM, relic
			Forge 		- grenade, shield
			Southern Raceway- random
			Badass Crater 	- random
			
			(the vendors for the latter 2 are in an awkward spot compared to the rest, so they aren't really worth it to farm)


	> Raid Boss Legendary Drops

		- Legendary world drop weight is multiplied by 3 in Terramorphous's Peak and the Winged Storm (dragons of destruction map)

		- Hyperius, Master Gee, Pyro Pete and Voracidous now all have 4 individual pools with 6.67% drop chance each every kill which
		  drop a random world drop item from the legendary pool of guns, shields, grenades and class mods respectively.
			This chance increases by 20% for each OP level, up to a tripled value

		- Voracidous now has a 25% chance to drop a random Gen2 Legendary Class Mod

		- Dexiduous now drops 5 guaranteed legendaries every time you kill it, and an additional 5 chances of ~13% each that scale
		  with OP levels


	> Knuckledragger

		- Now drops a random white rarity pistol instead of always dropping a jakobs pistol

		- The chest after knuckledragger now gives a random white rarity shotgun, in addition to a random white rarity AR, SMG or
		  sniper



	> Golden Chest

		- Made it cost 20 Eridium, instead of golden keys

		- Now throws out 3 items in front of it, instead of spawning items within the chest itself
			- This also had the side effect of bypassing the need of watching the entire chest opening/closing animation to
			  re-open it

		- Now also gives you gemstone guns, legendaries, and blue-rarity class mods (since they are actually good).



	> Tubbies

		- Gen1 Pearlescent guns have been removed from the Tubby pearlescent pool, and the base chances have been increased
		- The tubby pearlescent pool now also scales with Overpowered levels again:

			OP Level
			0   1   2   3   4   5   6   7   8   9     10
			10, 11, 12, 13, 14, 15, 18, 21, 25, 27.5, 30

		- This makes it so it's way less unforgiving. Also means that OP levels are more appealing, especially higher ones,
		  and makes 9 and 10 a smaller optional bonus.


		- Tubbies now have a 20% chance to drop an additional world drop legendary, similar to loot midgets' 15%


	> Witch Doctors

		- Now have a ~3.3% chance to drop a world drop legendary. This is doubled for badasses
		- Scales with OP levels, up to a tripled chance

	> Omnd-Omnd-Ohk

		- Now has a 3% chance to spawn instead of 1% (tweaked UCP)
		- Twister is now a guaranteed drop


	> Uranus / Cassius

		- The overall chance to drop legendaries was heavily reduced, though it still exists in a small capacity to keep an essence
		  of vanilla


	> Jimmy Jenkins / Loot Goon Goliaths / Muscles

		- All 3 of these enemies now have gotten additional legendary drop chances seperate from world drop chances,
		  on top of UCP making jimmy jenkins function like a normal loot midget


	> Haderax Chests

		- The chances for legendaries have been toned down to match the other raid bosses in the mod
		- The previously digi peak set items now have a 10% chance of spawning in their respective chests
			- Now basically acting as dedicated drops, and 'honors' their pearlescent rarity a little better

		- Now provide a somewhat even spread of the different types of items


	> Mimics

		- Now have a ~5% chance of dropping a world drop legendary. Scales with OP levels, up to a tripled chance
		- 66% chance of dropping a random Dragon Keep class mod



## Enemy Changes

	> Base Enemy Stats

		- Both base enemy health and damage have been adjusted so that they start off at a higher value than vanilla, while having
		  a slower and/or more consistent scaling per level. This is to make early game slightly more difficult (to make it less
		  boring), while not messing with very late game difficulty *too* much.
  
 
 	> Raid Bosses

		> All raid boss health (except dexi) has been reduced. Some of them by *very* substantial amounts.
			- Partially due to the nerfs to the Bee shield. But also to hopefully make it way more flexible to use different
			  kinds of items.

			- Voracidous's shield is lowered, but only in UVHM. I have not figured out how to lower it in the other 2
			  difficulties yet.

			(While not a raid boss, these changes also applies to Badassasaurus Rex because fuck that enemy lmao)

		> Master Gee

			- Now has a 98% resistance in his initial phase instead of a complete immunity
			- Absorbing an acid puddle reduces resistance by 20%, applies to both Gee and yourself

			- These changes should make it so you have way more flexibility in how you approach the fight by giving
			   you the ability to deal damage as well, while keeping the gameplay of trying to lure him to the acid puddles


		> Proof of a Hero

			- All raid bosses now have a 1% chance of dropping a new "Proof of a Hero" relic.
			  It only exists as a trophy, as it lists which raid boss you got it from in its description.


	> Southpaw Steam & Power

		- The following enemy types can now spawn anywhere in Southpaw
			shielded nomads
			shock nomads
			heavy nomads

		- Badass psychos and nomads are more common

		- Changed some enemies to be considered armored instead of flesh:
			Standard and Badass psychos
			Standard and shielded nomads (excluding badass)
			Assassin Oney
			Assassin Reeth

		- Increased the health of the following enemies:
			Standard psychos
			Standard nomads



	> Saturn, Uranus, Constructors

		- Can now be afflicted with status effects
 


## Vault Hunters

	> Overview
		- Overall, characters are just better in every single way, both damage and survivability. With some exceptions.
		- An overarching goal has been to give more opportunities to give said damage and survivability, spreading the sources for
		  each around

		- Every character has a 'passive bonus' for each of the 3 branches in their skill trees;
			Every time a skill reaches 5 points, you gain some buff that is shared across every skill in that branch
			This effect stacks for each skill you get to 5 points

			Works if class mods boost skills to 5/5 or higher

			Certain skills with a specific pre-requisite need to do that pre-requisite to get the passive effect as well.
				This includes every kill skill as well as things like Battlefront and Wreck.
				However, there also isn't any specific pattern to it.


	> Axton

	- Passive Bonuses:
		+4% Cooldown Rate
		+4% Mag Size
		3% Less Damage Taken

	- Turret

		- Base damage and health increased by ~20%


	- Guerrilla

		- Laser Sight
			Now grants +5% accuracy to you, and +10% accuracy to the turret
			Now grants a small amount of ammo regeneration for 3 seconds when you critically hit

		- Able
			0.5% max health regenerated per second instead of 0.4%

		- Longbow turret moved to tier 3, where Scorched Earth would be

		- Crisis Management
			+5% *all damage* (applies to both you and your turret) and +7% damage reduction while shields are down

		- New Skill: Special Munitions
			- +10% turret fire rate per point

	- Gunpowder

		- Metal Storm
			Fire Rate per point reduced to 8%
			Recoil Reduction per point reduced to 10%
			Visually looks like a passive skill on the tree, but functionally works the same

		- Scorched Earth
			Moved to tier 3, where longbow turret would be
			No longer has a damage penalty to the turret

		-Battlefront
			Now also boosts the turrets' *gun damage* by 6% per point

		- Duty Calls
			Now a kill skill that boosts reload speed and crit damage by 4% per point

		- Ranger
			boosts each stat by 3% instead of 1%

		- New Skill: Overclocked
			Maximum of 3 points
			Increases the damage of your currently equipped shield's abilities by 6.6% per pont (20% max)
				This also applies to added damage such as amp and roid damage

		- New alternate capstone: Stormweaver
			You gain a passive +15% fire rate, and an additional 5% per point you have in Metal Storm
			
			(this does not make you unable to spec into Nuke)

		- Nuke
			+30% cooldown rate
			Now benefits from your grenade damage and explosive damage bonuses

	- Survival

		- Resourceful and Last Ditch Effort swapped places

		- Resourceful
			+6% cooldown rate instead of 5%
			Now also grants +4% mag size per point

		- Last Ditch Effort
			+4% *all damage* (applies to both you and your turret) and accuracy while below 50% health or in
			FFYL, and +15% increased FFYL duration per point



	> Maya

	- Passive Bonuses:
		+8% Shield Recharge Rate
		+0.6% of max HP regenerated per second
		+10% Status Chance


	- Motion

		- Chain reaction is now in Tier 4

		- Sub-sequence
			Now a single point skill, and grants an additonal +1 second to phaselock duration

		- New Skill: Haste
			Tier 5 kill skill that boosts fire rate, reload speed and movement speed


	- Harmony

		- Restoration is now in tier 1 (although since co-op doesn't work, the skill is basically useless)
			No longer has max health per point

		- Mind's Eye
			now boosts accuracy instead of melee damage

		- Sustenance moved to tier 2
			Now also has +4% max health per point

		- Quicken moved to tier 2
			Now 5% cooldown rate per point instead of 6%

		- Elated
			Lowered to 0.8% regen per point

		- Res
			Now is a 3-point skill and gives 20% FFYL duration per point

		- Wreck Moved to tier 4
			Now gives 7% gun damage and fire rate

		- Scorn moved to tier 4
			Cooldown lowered to 12 seconds

		- New capstone: Angel of Death
			Provides kill skill duration and swap speed


	- Cataclysm

		- Flicker
			+5% DoT damage instead of DoT chance

		- Immolate
			Reworked to give +3% elemental damage (excluding explosive)

		- New skill: Dying Flame
			3-point skill in tier 2 that just has the vanilla Immolate effect, with doubled effect per point (60% at 3/3 instead
			of 50% at 5/5)

		- Helios
			Renamed to Smite and now deals shock damage

		- New skill: Salvation
			+4% DoT resistance per point

		- Cloud Kill  rework
			-Now activates on kill instead of on-hit, with no cooldown.
			-Massively increased radius
			-Damage is now actually considered DoT damage instead of really fast ticks of impact damage
				this means that Flicker will buff it

		- Backdraft, renamed to Discharge
			-Nova changed to shock damage

			-Fire damage on melee replaced with a chance to apply a shock DoT when you shoot someone
				This does not care about which element your gun is, or what the status chance of that gun is.
				This is entirely its own thing and can give you another source of damage.

		- Ruin
			Shock explosion replaced with a corrosive one



	> Salvador

	- Passive Bonuses:
		+5% Reload Speed
		+5% Ammo Carrying Capacity
		+6% Max HP

	- Gunzerk

		- Base duration and cooldown is now 15 seconds for both
		- Halved damage resistance


	- Gun Lust

		- Lay Waste moved to tier 1
			Now provides 3% fire rate per point passively
				effect is doubled on kill for 7 seconds (scales with kill skill duration)
			Removed crit damage

		- Quick Draw
			Removed crit damage, increased swap speed to 8% per point

		- All I Need is One reworked: Silver Bullet
			Now increases crit damage and bullet speed by 4% per point

		- Money Shot
			Raised maximum damage bonus magazine requirement to 16
			The values on the card now correctly show the proper values

		- Locked and Loaded moved to tier 4
			Now increases crit damage by 6% per point after reloading

		- Keep it Piping Hot
			Values increased to 8% per point

		- No Kill Like Overkill
			Halved the possible damage gained from the skill


	- Rampage

		- Filled to the Brim
			Removed ammo carrying capacity (converted into the passive skill tree buff)

		- All in the Reflexes
			Melee damage increased to 6% per point

		- Last Longer
			Duration gained reduced to 1 second per point

		- I'm Ready Already
			Increased to 6% cooldown rate per point

		- Get Some reworked: Conveyor of Death
			Hitting enemies gives you a 4% increase to fire rate and cooldown rate per point for 2 seconds


	- Brawn

		- Hard to Kill
			Health reduced to 3% per point, HP regen increased to 0.4% per point (from 0.1%)

		- I'm the Juggernaut
			Damage reduction increased to 6% per point

		- Ain't Got Time to Bleed
			HP regen increased to up to 1% of your hp per point (still based on how much hp you have)

		- Just Got Real
			Now increases all damage and mag size passively by 3% per point

		- Sexual Tyrannosaurus
			HP regen increased to 0.7% per point

		- New Skill: Provoke
			Maximum of 3 points
			Taking damage grants you a stack that lasts for 5 seconds which improves shield recharge delay by
			2% at rank 1 and +4% for each level after that.
			The stacks gain an additional 0.8% shield recharge delay for each point you have spent in the Incite
			skill, not changing with additional points spent in Provoke.
			No maximum cap on stacks, and no internal cooldown on getting stacks.



	> Zer0

	- Passive Bonuses:
		+5% Crit Damage
		+4% Shield Capacity
		+5% Melee Damage


	- Sniping

		- Headshot Reworked: True Sight
			Now increases crit damage and accuracy (combining headshot and precision)

		- 0ptics reworked: Weakness Expl0it
			Now grants 2% cooldown rate per point for a short duration when you crit an enemy

		- Precision reworked: Headhunter
			Now boosts sniper gun damage by 4% and sniper reload speed by 3% per point

		- Killer
			Crit damage reduced to 5% per point, reload speed reduced to 7% per point

		- 0ne Sh0t 0ne Kill reworked: High Caliber
			Now increases gun damage by 9% per point, but reduces fire rate by 4% per point

		- Kill C0nfirmed reworked: 0ptics
			Each stack now also increases fire rate and aim steadiness
			
		- New Skill: Arsenal:
			Increases your grenade, rocket and bullet damage by 2% per point
			Also gives you a multiplicative 2% bonus to your melee damage per point

		- At 0ne with the Gun
			Max skill point amount reduced from 5 to 4 (i am aware how cursed this is)
			now grants +3% mag size per point, an additional flat bonus after other calculations
			
				This bonus is +1 when you spec into the skill, and increases to +2 when you max the skill.
				(Reduced effect for rocket launchers; bonus only goes up to +1 after you've maxed the skill)
				
		- Critical Ascensi0n
			Removed Critical Damage bonus from stacks
			Gun Damage bonuses from stacks are now multiplicative with other gun damage bonuses


	- Cunning

		- New Skill: Dexterity
			Increases movement speed by 5% per point

		- Grim moved to tier 2
			Cooldown rate per point increased to 2%

		- C0unter strike reworked: Advanced Training
			Now improves shield recharge delay by 5% per point and fire rate by 3% per point

		- Rising Sh0t
			Gun damage reduced to 1.5% per stack  per point

		- F0ll0wthr0ugh moved to tier 3
			Removed melee damage, lowered movement speed to 6% per point


	- Bloodshed

		- Be Like Water reworked: Duality
			Increases gun damage, melee damage and shield capacity by 3% per point

		- Fearless moved to tier 2
			Now increases cooldown rate by 3% per point and regens 0.8% of your health per point while shields are down

		- Ambush moved to tier 2

		- Execute moved to tier 2

		- Unf0reseen moved to tier 3
			Now also boosts cooldown rate by 1.5% per point

		- Resurgence moved tier 3 and reworked
			Now is a single-point gamechanger that heals 50% of your max health over 1 second when you get a melee kill

		- Ir0n Hand moved to tier 3
			Kill skill that provides 5% melee damage per point

		- Like the Wind
			Now provides 4% damage reduction while moving per point, and 4% movement speed per point


	> Gaige

	- Passive Bonuses:
		+5% Chance for bullets to ricochet (Close Enough without the damage penalty)
		+5% Damage over Time damage
		+6% chance to gain another stack when you gain an Anarchy stack


	- Global

		- Deathtrap's base cooldown was reduced to 42 seconds
		- The only remaining Deathtrap ability skills are Robot Rampage and Explosive Clap


	- Best Friends Forever

		- Close Enough and Buck Up are just removed
			(Close Enough was converted into the passive bonus of the skill tree,
			 but i just personally dislike the inconsistensies of Buck Up)


		- Potent As a Pony
			health was increased to 5% per point for Gaige, and 10% for Deathtrap

		- Cooking Up Trouble
			now activates while your gun's magazine is half-full instead of needing it to be full.

		- Fancy Mathematics
			now has a consistent buff instead of relying on how much health you have

		- Robot Rampage moved to tier 2
			Now also gives 25% melee damage to Gaige.

		- Upshot Robot
			now increases Reload Speed, Fire Rate and Movement Speed by 1% for each stack,
			and the duration regained on kill was reduced to 1 second.

		- Unstoppable Force
			movement speed was reduced to 4% per point, but the shield regeneration
		  	was replaced with 7% of your shield being instantly regained on kill per point

		- Explosive Clap
			Now also gives 50% melee damage to Gaige.

		- Made of Sterner Stuff
			damage resistance was increased to 2% per point, and the DT melee damage was removed.
			(not cuz i thought it needed a nerf, but more so that i thought it was unnecessary)

		- New Skill: Lazer Death Robot Lady™
			Increases Critical Damage by 8% per point.


	- Little Big Trouble

		- More Pep now increases status chance and DoT duration by 6% per point

		- New Skill: Unlikely Precision
			Kill Skill. increases accuracy by 6% and reload speed by 4% per point

		- Strength of Five Gorillas now gives you 4% gun damage and boosts *all* DT damage by 10% per point

		- Electric Burn's effect was completely switched; corrosive and fire DoT damage now apply shock DoTs on the enemy

		- Interspersed Outburst renamed to Battery
			Now also increases gun damage by 6% per point for every stack of Battery you have

		- Make It Sparkle was moved to earlier in the tree, and Shock Storm now functions as the tree's Capstone


	- Ordered Chaos

		- Anarchy damage buff was reduced to 1.5% per stack

		- Smaller Lighter Faster's maximum rank is now 5, but the magazine penalty was raised to 3% per point

		- Annoyed Android now provides 5% movement speed to gaige per point

		- New Skill: Double Tap
			3-point skill that gives you 7% double shot chance per point

		- Blood Soaked Shields now increases shield by 8% per point, while reducing max HP by 4%.
			BSS's shield regeneration effect was moved to Unstoppable Force

		- New Skill: Kill Switch
			Increases kill skill duration by 5% per point

		- New(ish) Skill: Radical  (Reworked  Typecast Iconoclast)
			Kill Skill. increases Grenade Damage by 6% per point

		- New(ish) Skill: Devil's Clutch (Reworked With Claws into a standard skill)
			Kill Skill. increases fire rate and swap speed by 6% per point

		- New Skill and Capstone: Hammer of (In)Justice
			While Discord is active, you gain +30% movement speed and +200% melee damage




	> Krieg

	- Passive Bonuses:
		+0.5 seconds to base bloodlust stack duration
		+5% Movement Speed
		+10% Damage over Time duration


	- Buzz Axe Rampage

		- No longer has a cooldown, and has a practically infinite duration. Pressing the action skill
		  button during the rampage ends it
     
		- Melee damage was reduced from 500x to 2.25x
			(Melee as a whole gets a buff, so this compensates for it, as krieg already had *plenty* of damage)


	- Bloodlust

 		- Reworked Bloodlust
   			Bloodlust is now a 1-point skill you opt into in the first tier of the tree

			There is no longer a cap on Bloodlust stacks, nor a delay between when you can gain stacks
			Bloodlust stacks now last for 6 seconds by default, and gain reduced duration the more
			stacks you have

			Each stack of bloodlust by default grants you 0.4% global damage


		- Taste of Blood
			Moved to tier 1
			Dealing melee damage gives stacks which increase your total Bloodlust stack count without
			being affected by quicker decay rates at higher stack counts

			+4 Bloodlust stacks per Taste of Blood stack, and an additional +2 per point
   

		- New(ish) skill: Endurance (reworked Blood Trance)
			Moved to tier 2
			Grants 0.1% damage reduction per bloodlust stack. Additional 0.06% bonus while in BXR

   		- Blood Overdrive
			Melee Damage has been reduced to +0.2% per bloodlust stack point
			No longer reduces grenade fuse time
			Now boosts fire rate by +0.1% per bloodlust stack per point

		- Blood Bath
			Lowered to 0.3% gun damage per bloodlust stack  per point

  		- Blood Twitch
    			Moved to tier 4
       			Now passively boosts swap speed by +4% per point and buzzaxe throw speed by +3% per point
			Killing an enemy gives you +0.3% swap speed and +0.07% buzzaxe throw speed per bloodlust
			stack per point (Does now show up on the skill tree as a kill skill but benefits from
			kill skill duration boosts)
			
		- Boiling Blood
			Now gives 4% movement speed per point

		- New(ish) Skill: Blood Barrage (reworked Bloody Revival)
			Moved to tier 5
			Grants +5% chance to not consume ammo while firing a gun per point
			Gains an additional +0.12% free ammo chance per stack of bloodlust per point
	
	- Mania

		- Empty the Rage
			Now grants 3% gun damage per point, and then additional 5% when shields are down

		- Feed the Meat
			Max health reduced to 8% per point

		- Fuel the Rampage
			Now gives a passive 0.6% health regen per point

		- Silence the Voices
			Melee Damage reduced down to +30% per point
			Now drains a bit of your HP when you melee someone, instead of having a chance
			to hit yourself with melee

		- New Skill: Bloodthirst Aegis
			Maximum of 3 points
			You instantly refill 25% of your shield capacity on kill per point


	- Hellborn

		- Overview
			Heavily reduced self-burn damage
			Self-burn can now be proc'd with any status effect naturally, not just burn
			Self-Burn chance per point in BBB and FtF was increased to 10% per point

		- Burn, Baby, Burn
			Now grants 6% DoT damage while on fire

		- Fuel the Fire
			Status chance reduced to 10% per point

		- Delusional Damage reworked: Flametongue
			Each melee attack now always applies an additional fire DoT on enemies. This has a chance of also lighting yourself
			on fire

   		- Flametongue, Hellfire Halitosis and Raving Retribution

			Damage caused by these 3 skills have been changed so that they are unaffected by regular
			fire damage health type modifiers.

			They essentially now deal non-elemental damage that benefit from fire damage bonuses on gear




## Unique Items

	> Now, this will not be a full list of all the changes to every unique item. That would be a really long list, and
	  i still want to keep some semblance of discovery. This part is here more for what you can expect. Some examples.


	  Every unique gun has been looked over in some way. Some guns did not change at all, or in very small ways. Some guns were
	  nerfed/buffed, some guns were readjusted to be closer to what they were in vanilla after indirect changes like through
	  weapon types. A lot of guns were given a new identity,  such as the Patriot now being a very slow, but high damage and
	  high-mag vladof sniper. Some guns were replaced, which is more detailed in the next part.

	  The power of each gun was, of course, looked over, and hopefully more things are more powerful than what they used to be.
	  Try things out, use things you wouldn't otherwise. I especially recommend trying the items that are basically memes in vanilla.


	  A lot of unique guns were given a new visual barrel to hopefully give some variety in the look of uniques within a weapon type.
	  To give that feeling of "oh, this is different."


	  Also, yes, the Grog is nerfed.
	  
	
	> Replaced unique guns
	
		As stated before, there are some items that were completely replaced to allow them to be much cooler than they previously
		were. None of the drop locations of any of the items listed here have been moved from where the original item drops in
		vanilla.

		> Hammer (Dog)
			-Exceptionally high fire rate and shoots explosive gyrojets that have added grenade splash damage
		
		> Spy (Commerce)
			-High crit damage hyperion SMG (basically like a smaller version of the Bitch)
		
		> Destroyer (Seraphim)
			-Aiming down sights causes the gun to fire a continuous burst until its mag is empty
			-Good base damage, slightly increased crit damage, lower mag.
		
		> Eraser (Carnage)
			-Shoots 5 gyrojets in a straight line with varying speeds, much higher base damage



	> *Completely new Legendary items* (1.1.0)

		Completely new items in the mod i will say the description of simply so that you know how you can play with the new toys
		and know what to expect



	==== [ Guns ] ====


		> Rupture (Bandit AR) - Wilhelm
			-*Very* low mag and high reload speed.
			-Always 2 projectiles/ammo per shot.
			-Reloading causes an explosive nova around you.


		> Swordfish (Jakobs AR) - Assassins
			-Good hip-fire accuracy.
			-Aiming causes you to deplete all remaining ammo in your mag and increases the shot's damage by 75% for each
			 ammo consumed


		> Sigil (Tediore Launcher) - Hyperius the Invincible
			-Much faster innate swap speed.
			-Shooting the gun grants you a buff for 5 seconds that heals 8% of your max HP per second instead of dealing damage.
			 Effect does not stack.


		> Blitz (Vladof Launcher) - Bunker
			-Does not have the standard vladof free ammo effect, instead has an extremely high chance to not consume ammo per
			 shot.
			-Extremely fast fire rate, heavily lowered base damage.
			-Always 1 mag.


		> Patience (Jakobs Pistol) - World Drop Only
			-3 Ammo per shot, highly increased weapon damage and crit damage.
			-After you shoot this gun, your gun damage as a whole is decreased until you haven't shot it for a short duration.


		> Orb of Storms (Tediore pistol) - Handsome Sorcerer
			-Shoots a very slow moving ball that periodically creates large shock explosions that deal high damage.
			-Slow fire rate, massive ammo cost.


		> Beartrap (Bandit shotgun) - Der Monstrositat
			- 3 pellets, 3 ammo per shot.
			- on hit, pellets create 7 additional pellets in a ring around the initial impact,
			  which converge in the center and keep flying until hitting something


		> Tigris (Jakobs shotgun) - Sheriff of Lynchwood
			-Always spawns as fire, corrosive or shock.
			-100% status chance, very high status damage
			-Shots have a chance to also slag enemies.
			- 2-shot burst


		> Laser (Sub)Machinegun (Dahl SMG) - Ol' Slappy
			-Always full auto, massive mag size and very fast fire rate.
			-2 projectiles per shot, 3 ammo per shot.
			-Slower bullet speed.


		> Daedalus (Hyperion SMG) - Bad Maw
			-6-round burst.
			-Shooting the gun causes 4 additional shots to rain down from above where you hit.


		> Fate (Dahl sniper) - Warrior
			-Very high ammo cost, 1 shot in the mag.
			-Shooting creates a stationary laser that deals continuous damage to all enemies inside


		> Gubber (Vladof sniper) - Laney White
			-3 Projectiles per shot, 3 ammo per shot, high mag size.
			-Fires slow, arcing projectiles that ricochet from surfaces and between enemies.
			-No standard sniper crit bonus, but instead gets higher base damage.


		 [1.2.0]

		> Pyrana (Vladof Pistol) - Rue, the Love Thresher
			-Slow firing x3 vladof pistol with lower mag
			-Killing an enemy grants the Pyrana highly increased fire rate and mag size for 5 seconds


		> Pocket Salvo (Tediore Shotgun) - Mortar
			-Shoots arcing projectiles that ricochet multiple times and create a large explosion on each ricochet,
			  dealing +100% grenade splash


		> Gladiator (Hyperion Sniper) - Terramorphous the Invincible
			-Applies a new Bleed status effect, dealing DoT and increasing the enemy's damage taken by 15%.
			 This status effect can not stack


		> Quicksilver (Tediore SMG) - World Drop Only
			-Increases movement speed while held slightly, has increased fire rate and a ridiculously fast reload speed.


   		 [1.2.5]

      		> Knell (Hyperion Pistol) - Gravediggers
			-High base damage, 1.5x base critical damage, 3 ammo per shot.
			-Critically hitting an enemy causes the Knell to not consume ammo for 2 seconds.



		> Obliterator (Torgue Shotgun) - Saturn
			-5 pellets per shot, high fire rate and mag size
			-Pellets create a large explosion on hit, but deal no impact damage
			-Upon hitting an enemy, each pellet of the Obliterator grants you a 3% Global Damage buff, which persists
   			 even after switching weapons.


		[1.2.6]

	       	> Plaguebearer - Plague Rats
			- 4 ammo per shot, 5 pellets per shot, reduced fire rate and accuracy
			- Corroding enemies grants stacks which are expended on melee to create a corrosive nova, increasing
			  damage of the nova per stack
	
	
		> Sucker Punch - Foreman Jasper
			- Full auto with reduced base fire rate and increased damage. Always comes without a sight, and a
			  bayonet that adds +0.5x melee damage
	
			- Dealing melee damage causes you to gain highly increased cooldown rate, movement speed and reload
			  speed for 7 seconds



	==== [ Shields ] ====


		> Ankheg (Hyperion Shield) - Black Queen
			- Good shield capacity
			- Increased maximum health
			- Doesn't have recharge rate/delay at all. Instead has a constant passive shield regeneration effect.
				Shield parts that affect shield recharge rate also change the power of this effect.

    	==== [ Class Mods ] ====

	> E-Tech Class Mods

		The point of these is that they can be equipped by any character, and have character independant boosts.

  		> Desperado - Dropped by badasses in Bandit Slaughter in UVHM
			- High passive critical damage
			- Critically killing an enemy grants a stack of Desperado, granting you +10% Bullet Damage.
			  Stacks persist and stack indefinitely until you get a bullet kill that is not made with
			  a critical hit.

     
		> Death Kiss - Dropped by badasses in Creature Slaughter in UVHM
			- Increased Slag Damage and Max Health
   			- Slagged enemies are Blighted, draining their HP equal to your maximum health per second.
				Blight drain value is increased by slag damage and status damage boosts.




