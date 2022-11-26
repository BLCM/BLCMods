=============== [ 1.2.1 ] ===============

	- Integrated the Less Dumb Visuals mod (by MikeyRay) into Oselands, and configured it so that it's not *that* far
	  from vanilla, but still an improvement. All the options for the mod can be found in the main Oselands file

		== Unique item changes ==

	- Cursed Pirates now have a 7.5% chance to drop the Eternal Youth
	- Chance for Immortal Skeletaurs to drop the Deathless has been increased from 4.5% to 7.5%
		*Legendary dedicated drops are set to 15% by default, and the rate is halved for these enemies

	- Orb of Storms
		-Internally reworked how the weapon's projectile is handled, which fixes the ability to
		 transfer other guns' base damage onto the explosions



=============== [ 1.2.0 ] ===============

	- Added a new message when executing the mod that gets printed in your console, instead of it being said in chat

	- Revamped elemental damage multipliers and adjusted enemy health to compensate

		New Multipliers:
		Non-Elemental(NE)/Explosive/Slag vs all health types: 1x
		Fire/Corrosive vs right health type: 1.2x
		Fire/corrosive vs wrong health type: 0.6x
		Shock vs shield: 1.5x
		Shock vs other health types: 0.95x

		-Enemy health is reduced to basically match how much damage you would've had to deal against them anyway;
		 killing an enemy with 1x NE will be just as difficult now as it would've been with 1.4x NE previously

		-Reduced elemental damage penalties on guns from -20% to -10%. This penalty was removed entirely from slag guns.
			-Fire/Corrosive guns against their right health type will now deal ~15% increased damage when
			 compared to NE


		*Overall, this means that fire/corrosive against their respective health types will now be stronger than they were
		 before. I did some tests and found that they weren't doing as much damage as i thought they were, which also lead to some
		 items being incorrectly balanced.
		 Normalizing damage multipliers to consider 1x as the base also makes calculating damage less of a nightmare


	- Reduced enemy additional health scaling
		(basically they have an additional multiplier to their health that is intended to match the player gaining skills with levels,
		 and the multiplier scales with their level as well, so their health scaling is not truly linear)


	*Player health and shield were increased by 20% in previous updates as a sort of compensation for elemental changes in oselands.
	 Now that elements have been brought back, technically there isn't a reason to keep that 20% increase, but i'm still going to
	 in hopes that it still improves the player experience through the mod.


	- Critical Damage on weapons is now listed as the full multiplier of that gun (2.0x base + other modifiers) rather than a +% bonus
	- Critical Damage on weapons is now a completely separate multiplier from other sources of crit damage

		*critical damage above 2x still transfers when playing salvador


	- Tweaks to the Southpaw Steam & Power

		-The following enemy types were changed to be considered armored instead of flesh:
			Standard and Badass Psychos
			Standard and Shielded Nomads (excluding badass)

		-Increased the health of the standard variants of the aformentioned enemy types by a considerable amount


		- Massively increased legendary world drop chances of all 4 Assassins in Southpaw, with Rouf gaining an even higher boost

		- Increased XP gain in Southpaw by 1.5x


		*Why am i doing such big changes to this area specifically? i belive it to be the best designed area in the game after
		 Digi Peak, so i want it to make it *even* better. I want to give you a reason to be there for not just having fun
		 while mobbing. I want it to be actually worth it to run that area


	- Made all flat Max Health and Shield Capacity boosts/penalties on class mods apply to your base stats
	  rather than it adding on top after other % boosts. (basically just a buff/nerf respectively if you have both kinds of boosts at the same time)

	- Made Salvador's Raider class mod's accuracy apply to all guns and not just assault rifles.


	- Added a new rarity for unique guns and items (previously blue, purple and e-tech red text items)
		-This rarity appears between E-Tech and Legendary, making it easier to separate those from the rest of the
		 items in their previous rarity.

		-The purple-rarity x4 version of the magic missile was turned into a legendary


	- Brought back damage resistance as a secondary stat on relics
		-Now is just a global damage resistance rather than reducing individual elemental resistances



	- Made it so *all* Tediore guns retain their maximum reload damage until their magazines are at half. After that it scales the damage down
	  as if you would be going from 100% mag to 0% mag previously

	- Revamped the damage formula on Tediore shotgun reloads to make them a lot more consistent and comparable to the other weapon types.
		the damage formula for them now is:

		listed card damage * current ammo in the mag (retaining the change above this) * 5 * (1 + (0.05 * projectile count))


		Tediore shotguns actually good for reloading now.


	- Replaced the 35% increased pellet count buff i gave to non-unique tediore shotguns and the Deliverance with a flat +3 bonus
	  This means that it is further increased by vertical grip


	- Increased Dahl AR damage by 5%
	- Increased Dahl AR ADS burst count to 4

	- Removed the last remaining matching bonuses from dahl parts which i wasn't aware were there
		(shorter bursts on dahl-barreled dahl guns, slightly smaller mag sizes on dahl ARs and SMGs)

	- Nova shields now activate when you take damage instead of when shield breaks, with a 5 second cooldown instead of needing to recharge to full
	- Nova shields now gain additional damage based on 30% of your maximum shield capacity

	- Removed more irrelevant UI elements from various guns

	- Made Krieg's Wound class mod's skill effect use Salvador's  Ain't Got Time To Bleed  skill icon while it is active and visible on the HUD


	- Made King/Queen Spiderants and Mortar use the badass item drop pool rather than the standard enemy drop pool

	- Adjusted the ratio between legendary and pearl drops from world drops slightly
		-World Drops are now even more likely to be legendary instead of pearlescent.
		
		*This is mostly to compensate for the fact that there's more items now


		== Unique item changes ==

	- Added descriptive text to many unique guns that had effects that weren't apparent from just shooting the gun in the sky
		*you could argue that them being mysterious is a feature that makes them more interesting, but to that i say "fuck y-


	- Added a new legendary relic: Eternal Youth
		-Reduces your max Shield Capacity to 10
		-While shield is full, you gain health regeneration equal to the equipped shield's recharge rate


	- Added new legendary guns:

		> Pyrana (Vladof Pistol) - Rue, the Love Thresher
			-Slow firing x3 vladof pistol with lower mag
			-Killing an enemy grants the Pyrana highly increased fire rate and mag size for 5 seconds

		> Pocket Salvo (Tediore Shotgun) - Mortar
			-Shoots arcing projectiles that ricochet multiple times and create a large explosion on each ricochet, dealing +100% grenade splash

		> Gladiator (Hyperion Sniper) - Terramorphous the Invincible (15% chance instead of 10%)
			-Applies a new Bleed status effect, dealing DoT and increasing the enemy's damage taken by 15%. This status effect can not stack

		> Quicksilver (Tediore SMG) - World Drop Only
			-Increases movement speed while held slightly, has increased fire rate and a ridiculously fast reload speed.


	- Added a set of E-Tech shields
		*The whole gimmick with all of these is that, much like Rough Rider, they have 0 shield capacity but grant other bonuses instead, either to
		 compensate for that lack of shield, or just giving the risk of sacrificing survivability to gain something else instead

		 Each E-Tech shield type has a 5% chance of dropping from a particular badass enemy type in the game, listed below:

			- Berserker shield (Bandit) - Badass Psychos
				-Dealing or taking damage causes you enter a rage, gaining movement speed and life steal while your health drains very quickly.

			- Titan Heart Shield (Hyperion) - Badass Loaders
				-Grants increased max health, and adds 10% of your maximum health value as amp damage to all your shots

			- Shatter Tank Shield (Pangolin) - Spiderant Kings/Queens (/their renamed versions in higher difficulties)
				-Reduces max health on top of the 0 capacity, but grants flat health regen



	- Terramorphous uniques
		- All items in this category (Teeth-, Blood-, Hide- and Breath of Terramorphous)
		  are now changed to Seraph rarity and will behave as such; all of these items now only start dropping
		  once you enter UVHM and you are always guaranteed one per kill.

		  Slayer of Terramorphous class mods are also changed to Seraph rarity and only drop in UVHM, but are held within a separate pool.


	- Teeth of Terramorphous
		-Improved spread; less points and narrower in general
		-Reduced the speed of the projectiles, meaning the final explosion happens much closer to you (leaning into the idea of like short-range bite)
		-Projectiles now pierce enemies, meaning you can hit both the impact splash and the final bite splash on the same enemy more effectively,
		 meaning you will generally do a lot more damage while also being much easier to use
		-Increased shot cost to 4, reduced pellet count from 12 to 8



	- Shadow of the Seraphs
		-Fixed the additional projectile not applying to salvador's off-hand

	- Red Hellion
		-Made it so the fire rate buff is not affected by if your movement speed is lower than the base. (i.e you went into FFYL)
		 If it is, it will now just consider you as moving at standard walking speed and not affect your fire rate in any way.

		-The fire rate buff is now capped at +100% movement speed, but also applies 75% of movement speed to fire rate instead of 50%
			-very small nerf to the characters that could get it really high regardless, but allows other characters
			 to use it much easier now as well

	- Magic Missile
		-Massively improved homing
		-Increased projectile speed
		-Massively lowered blast radius, but increased damage dealt

	- Rolling Thunder
		-Massively reduced self-damage on explosions created by contact with the world

	- Nasty Suprise
		-Massively improved damage and fuse time
		-Slightly increased blast radius

	- Blockhead
		-Increased splash radius
		-Splash now deals explosive damage (impact is still fire, making it a sort of hybrid damage gun)

	- Deliverance
		-Highly reduced the projectile speed of the reload
			(thanks to BL2.5. i don't actually know why or how it works, but it let me do what i wanted. you should go play bl2.5)

	- Destroyer
		-Increased gun damage and gave it 10% increased base crit damage

	- Tigris
		-Reduced DoT damage

	- World Piercer
		-Improved Accuracy

	- Hornet
		-Lowered fire rate
		-Reduced ADS burst count to 2
		-Highly increased base damage

	- Evil Smasher
		-Slightly increased damage
		-Activated buff no longer has a chance to activate at the start of a reload, and deactivates on the next reload.
			Instead, you now have a chance to get it whenever you deal or take non-DoT damage or *finish* a reload, and lasts for 4 seconds.

		-Buff's main weapon stats now applies to both hands while playing salvador, but only if you are holding the evil smasher in that hand.
		-Buff no longer boosts mag size, but instead that is now part of the gun itself intrinsically


	- Orc
		-Activated buff's stats now apply to both mainhand and offhand on salvador

	- Morningstar
		-made the stacks of the weapon's special effect use the new weapon critical damage attribute, meaning it is now multiplicative
		 with other critical damage bonuses from skills and other items
		-Stacks now use the same icon as Zer0's Headshot in vanilla
		-Reduced critical damage
		-Massively reduced critical damage granted by the weapon's special effect (60% per stack > 10%)

		*this item was really, really, really fucking strong, but is now more in-line with everything else

	- Little Evie
		-Increased weapon damage slightly
		-Made the stacks of the weapon's special effect be shown on your HUD
		-You now gain stacks on dealing bullet damage to enemies (4 second cooldown) and killing them

	- Tattler
		-Slightly increased damage

	- Bearcat
		-Reduced ammo cost from 4 to 2
		-Reduced damage very slightly
		-Reduced grenade AoE
		-Made the gun unable to apply DoTs

	- Unmaker (Peak Opener)
		-Fixed the weapon using an incorrect pearl rarity

	- Flame of the Firehawk
		-No longer needs to recharge to full to be able to do novas again once it starts recharging
		-Now only creates novas while you are doing DoT damage, as long as your shields are broken


	- Revamped the skin of the Mesa and Destroyer, Tinderbox, Shotgun 1340
	- Tweaked the skin of the Teeth of Terramorphous, Storm, Interfacer, Butcher, Retcher, Thunder

	- Fixed Moxxi's Endowment not properly listing Max Health secondary stats


=============== [ 1.1.5 ] ===============

	- Fixed Axton's Shock Trooper class mod not boosting electrocute damage properly
		(it was boosting fire DoT instead of shock DoT, so it didnt show up in the card)


	- Made it so you can accept Master Gee's quest immediately after the final story mission of the DLC
	  instead of needing to kill Hyperius first

	- Ported over a change from BL2.5 that makes it so Master Gee can not fit in the small cavern opening,
	  meaning you can no longer gate crush him
		(the fight is better by itself tho, trust me)

		- The times i've talked with the people behind 2.5 they've been open to stuff from that mod being reused elsewhere.
		  So, while i didn't directly ask for permission for this specific thing, they've given off the vibe that it would be cool.
		  If any of them decide to ask me to remove it, i shall

		- This also only includes the changes to the hitboxes of Gee, not any of the visual changes that BL2.5 does to him.


	- Corrected the health of Haderax
		- The health was massively lowered (to the point of one-shotting easily) for loot testing purposes.
		  Those changes are now fixed and it will now have the intended amount of health.

	- Greatly lowered burst interval on Hyperion SMGs
		- The main thing this affects rn is Daedalus to make it feel a lot better, but this future-proofs it for the chance that i make another one


	- Updated all the weights on vendors for both the standard slots and IOTD
		- Weights, especially in early levels, are more in your favor now. Way less white/green items after maybe level 15.

	- Reduced the gun damage penalty on all hyperion parts and critical damage accessories
		-Exception being the shotgun critical accessory


		== Unique item changes ==

	- Added a 'new' legendary relic: Deathless (replaces what would be the sniper damage Heart of the Ancients, which is the last of the bunch that have been unused)
		-Forces your health to be at 10% value or lower at all times
		-Massive boost to shield capacity and recharge rate

	- Added new dedicated loot sources for the various legendary relics in Oselands:
		- Ranger Emblem - Uranus*
		- Death Toll - Cassius
		- Medusa's Eye - Unmotivated Golem
		- Red Hellion - Badassasaurus Rex
		- Deathless - Immortal Skeletaur*

		*Ranger Emblem no longer drops from Ghost
		*Skeletaurs' chance to drop the Deathless is 3% instead of the standard 10% as they are a more common enemy.
		 Every other one is 10%


	- Added a new trophy item: Proof of a Hero
		- An effervescent rarity relic that barely does anything
		- Has a small chance to drop whenever you kill a raid boss (inlcuding OMGWTH), and will list the boss you got it from in its description
		- The chance to drop it is the same across every raid boss

			- Like mentioned above, this is a trophy item. A token of 'you got a cool thing'


	- Mesa
		-Increased both the base fire rate and the buff you get for aiming down


	- Tunguska
		-Massively reduced the self damage (but did not remove completely)


	- Infinity
		-Corrected status chance. Was waaaay higher than intended
		-Gave the gun its unique dva accessory back


	- Fireball
		-Massively increased blast radius (~ +200%)
		-Made the blast always guarantee a status effect
		-Increased DoT damage


	- Heart of the Ancients (the actual real one)
		-Made the critical damage bonus show up as a proper stat on the card
		-Made the critical damage bonus scale up with level and parts like other normal relic stats


	- Sigil
		-Gave the gun gemstone guns' bullet deflection
		-The health regen effect now shows its duration on your hud

	- Rupture
		-Increased reload explosion damage by ~33%

	- Beartrap
		-Fully reworked functionality:

			- 3 pellets, 3 ammo per shot.
			- on hit, pellets create 7 additional pellets in a ring around the initial impact,
			  which converge in the center and keep flying until hitting something


	- New Materials given to the following items:
		-Daedalus, Orb of Storms, Tigris,
		 Sigil, Patience, Fate, Rupture,
		 Laser (Sub)Machinegun, Ankheg*,
		 Swordfish, Volcano*, Gubber,
		 Blitz,

		* For everything except the marked items, you need to get a new version of
		  the item for these changes to apply


	- Did some small visual tweaking on the Bulwark of Purity and Retainer


=============== [ 1.1.4.2 ] ===============


	- Released the mod on GitHub


	- Integrated the No Space Cowboy mod by ZetaDaemon into oselands
		- Much like No More Orders, makes it so you don't need to have the Space Cowboy side quest active to get the loot midget spawn in Dahl Abandon


	- Made the player immune to being afflicted with slag status effects


		== Unique item changes ==

	- Changed the visual barrel of Mongol and World Piercer


	- Avenger
		-Added a new skin
		-increased fire rate

	- Tweaked the skin of the Unforgiven

	- Patience
		-Rebalanced stats
		-The duration of the damage penalty when you shoot the gun is now shown on your hud
		-The damage penalty now gets reduced over time rather than a binary choice of if you have the penalty or not
			This is linear; every 1/5th of the duration will reduce that penalty by 1/5th of the full value

	- Reworked Gub
		-Reduced from 3 pellets per shot to 1
		-Reduce ammo cost from 3 per shot to 2
		-Increased Base Damage and DoT Damage
		-Highly increased splash radius, and made it have a guaranteed chance of applying a status effect


=============== [ 1.1.4.1 ] ===============

	- Added a thing in the last update to apply the slower enemy bullet stuff to No-Beard's stinkpot
		- What i did didn't work, but it's fixed now


	- Removed Hyperion pistols from the E-Tech pistol pool
	- Removed E-Tech barrels from the standard purple-rarity, and gemstone, Hyperion pistol partlist	
		-Hyperion has a passive crit bonus, and the E-Tech barrel negates it.
		 Plus, Hyperion E-Tech pistols don't really do anything the other manufacturers can't


	- Fixed Aggression Relics not getting their main stat properly (gun damage or fire rate)

	- Fixed health regen effects on relics not working
	- Fixed Moxxi's Endowment not being able to get a Max Health secondary stat


	- Fixed Bad Maw not properly dropping the Daedalus Hyperion SMG

	- Made it so the chance for the Warrior legendary loot pool is 100% even outside of the story kill
		- Further emphasizing the lack of need to Read-Only farm and whatnot

	- Fixed Handsome Sorcerer being able to drop the Fate, since it was in the Warrior loot pool
		- Now instead it's a separate 10% chance from the warrior, ignoring the change above this

		(i had given the Handsome Sorcerer its own drop, so i didn't want you to only need to farm that one enemy to get both)



=============== [ 1.1.4 ] ===============

	- An update to the XP & Level Controller systems in the mod
		- Fixed some player scaling stuff not working properly if you kept the level threshold at 80op10
		- Fixed XP multiplier after level scaling not working properly
		- Overall simplified the whole system


	- Massively boosted the drop chance of blue and purple uniques that were given drop locations by UCP
		- Farming quest rewards is dumb. This change makes it so each of these drops (with some exceptions) practically have a
		  100% chance of dropping, because that is the chance you would have while farming a quest.
		- This chance is broken up into 2 chances (80% and 20%), meaning you have a near 100% chance of getting at least 1, but
		  a small chance (~16%) of getting 2 in the same run.
		

	- Added an additional random legendary chance to mimics
	- Mimics now have a high chance of dropping a random Tina DLC class mod on death

	- Made the additional legendary drop chances given to Son of Crawmerax by the UCP properly scale with the legendary weight in OP levels
		(up to tripled chance at OP10)

	- Added an additional random legendary chance to raid bosses in addition to their chances for specific types of legendaries

	- Replaced the Sand Hawk reward from Whoops with a random purple gun
	- Added Sand Hawk as a reward to Treasure of the Sands (the repeat of the final quest. This quest is repeatable thanks to UCP)

	- Removed drops below blue rarity from the chests in The Leviathan's Lair


	- Brought over UCP change of fixing a lot of red texts being an incorrect, more intense color



		== Unique item changes ==


	- Added a *new* Legendary Hyperion shield: Ankheg
		- Great shield capacity, increased max health
		- ignores the shield recharge rate/delay system entirely.
		  Instead it has an always-active shield regeneration rate mechanic, affected by shield parts that affect shield recharge rate


		- 10% drop chance from the Black Queen, and also is in the world drop legendary shield pool


	- Highly increased damage of the Badaboom
		-After doing some basic math, the damage with all 6 rockets combined was less than the single rocket that normal bandit launchers fire
		-Now, if you hit all 6 rockets, it will deal more total damage.


	- Increased the damage and magazine size of the Butcher

	- Reduced the rocket speed of the mongol slightly and made it unable to spawn with parts that would increase its rocket speed


	- Reworked the Shaped Glass pearlescent relic
		-Now affects most types of damage instead of just gun damage, and it's in a different part in the damage formula. Meaning it's even stronger.
		-Instead of giving a -100% max health debuff, it now doubles all damage taken from enemies.


	- The Unmaker now consumes 2 ammo per shot, but deals more damage

	- Increased gun damage and crit damage of the Unforgiven, but made it consume 3 ammo per shot

	- Changed Retainer to legendary rarity and made it drop in the legendary world drop pool



=============== [ 1.1.3 ] ===============

	- Increased base shield capacity and recharge rate by 20%, to match the boost that player health got

		- I am fully aware that this might be overkill, because the mod hasn't had it before this and so wasn't balanced for it either.
		  But for consistency, i want to try it out

		- Player health was increased as compensation for elemental changes (mainly the non-elemental, explosive, slag and shock changes)


	- Fixed incorrect dedicated legendary chances on the four assassins, Hyperius and Handsome Sorcerer

	- Fixed some things not working with the level threshold system
		-Environmental damage (barrels, frozen water)
		-the damage done by the default grenade when you have no mod equipped
		-Vehicles


	- **Massively** reduced the health of Dexiduous the Invincible
	- Increased the damage dealt by the explosions when you pop the zits on Dexiduous

	- Added additional legendary chances to Dexiduous so that it creates a large lootsplosion on death
		- The thing is so annoying to kill and get to even with the changes above, i figured you should be rewarded for the time you put into it


	- Gave Witch Doctors in both the Big Game Hunt DLC and Son of Crawmerax Headhunter DLC 
	  a highly increased chance to drop legendaries. This is further increased for badass variants


	- Reworked the loot gained from the chests after you kill Haderax
		- The chances for legendaries have been toned down to match the other raid bosses in the mod
		- The previously digi peak set items now have a 10% chance of spawning in their respective chests
			- Now basically acting as dedicated drops, and 'honors' their pearlescent rarity a little better

		- Now provide a somewhat even spread of the different types of items




		== Unique item changes ==

	- Changed the Funk Popper (replacing Unicornsplosion) to legendary rarity and added it to the world drop legendary shotgun pool

	- Fixed Nirvana not having the proper stats on its body
		-This results in a slight reduction to damage and mag size

	- Improved the skin of the Infection Cleaner, Retainer and Bulwark of Purity (replacing Easy Mode) to match the other changed rainbow skins

	- Fixed Retainer's description elements being in the wrong order

	- Peak Opener
		- Renamed to Unmaker
		- Now is pearlescent rarity
		- Added to the Gen1 pearlescent AR pool


=============== [ 1.1.2 ] ===============

	- Removed error messages on subsequent executions of the mod that cloned objects already exist
		- Theres still some errors about skill effects relating to the ogre? i removed the behavior of the ogre so i have no idea why they appear

	- Added tags in the mod file that make the mod look better when executing the mod through the Text Mod Loader  mod by apple1417


		== Unique item changes ==

	- Fixed an issue with the Fate sniper rifle that caused it to sometimes have 0 ammo in its mag


=============== [ 1.1.1 ] ===============

	- Fixed some of the loot pool changes from the previous update not taking effect
		- Legendary drops were essentially triple their intended value, and the skins weren't properly removed from the general pool

		- I thought this was important enough to make an update on

	- Was experimenting with increasing the XP gained from completing the quest Cleaning Up The Burg,
	  and i left it in because why not


=============== [ 1.1.0 ] ===============


	- *Completely new Legendary items*
		-I was going to put these in the unique item changes section at the bottom, but this is important enough to break the rules

		- Added 12 completely new legendary weapons.
			- The descriptions of these guns can be found in the Changelog text file, in the unique guns section.

			- Available in the world drop pools, dedicated drops listed below:

		> Rupture (Bandit AR) - Wilhelm
		> Swordfish (Jakobs AR) - Assassins

		> Sigil (Tediore Launcher) - Only from Hyperius the Invincible
		> Blitz (Vladof Launcher) - Bunker

		> Patience (Jakobs Pistol) - World Drop Only
		> Orb of Storms (Tediore pistol) - Handsome Sorcerer

		> Beartrap (Bandit shotgun) - Der Monstrositat
		> Tigris (Jakobs shotgun) - Sheriff of Lynchwood

		> Laser (Sub)Machinegun (Dahl SMG) - Ol' Slappy
		> Daedalus (Hyperion SMG) - Bad Maw

		> Fate (Dahl sniper) - Warrior
		> Gubber (Vladof sniper) - Laney White

		-None of these have their own unique skins. If i ever decide to update Oselands again, i might give them new skins.

	

	- Added a system where player, enemy and item stats do not scale after a level threshold.
		
		-i.e a level 73 gun would have the same stats as an op10 version with the same parts.

		-This threshold is by default set to 72, and has options for reverting back to vanilla op10, level 80 and level 60.

		-Setting the threshold to 80 or below means that you do not have to refarm in OP levels, which can make the
		 experience more enjoyable.

		-Enemies not scaling past a point also means that health doesn't get to scale as high past the player. Which
		 means that the enemies can be easier than if they scaled like in vanilla.
			-Level 60 items against level 60 enemies will be a bit easier than level 80, without even mentioning
			 that you get more skill points, essentially scaling past the enemies instead of the other way around.

		-Each option also has multiple sub-options for increased XP gain after the set threshold.
		 By default this is set to 1x, the same as before this update, with additional options for 3x and 5x
		 xp gain after the set threshold.


		-A small problem: the default grenade seems to ignore this entirely, so its damage keeps scaling past the threshold



	- Additional changes to overall loot acquisiton and chances, aiming to make loot drops better/more rewarding while still keeping it fair

		- Added an option to increase dedicated legendary chances.
			-Options for 10% (vanilla), 15% and 20%. Set to 10% by default.


		- Increased the chance for the "standard enemy guns and gear" pool to drop from 8.5% to 15%
		- Removed skin drops from said pool (they were essentially just taking up item drops)

		- Made VeryCommon and Common weights get reduced down to half their value between levels 30-80 instead of op0-op10

		- Increased Legendary weight from 0.025 to 0.0667 (still gets increased by 20% per OP level, up to a tripled value at OP10)
			(Vanilla 0.01)

		- Purple items in vending machines have a 20% chance to be replaced by a blue/purple unique of the same weapon type
			-Should give more opportunities for people to experience items they usually wouldn't


		- Brought down legendary multiplier in Terramorphous Peak and Winged Storm from 5x to 3x again, as i increased the legendary weight in general
			- The final chances will still be higher than before


		- The additional legendary chances from Raid Bosses as well as Muscles, Jimmy Jenkins and Loot Goon Goliaths were increased to 6.67% from 5%,
		  as a part of that increase to the legendary weight. Retains the OP level scaling.
			(At OP10 this will mean a 20% chance for those drops)



	- Rework to the Golden Chest in Sanctuary

		- Made it cost 20 Eridium, instead of golden keys

		- Now throws out 3 items in front of it, instead of spawning items within the chest itself
			- This also had the side effect of bypassing the need of watching the entire chest opening/closing animation to re-open it

		- Now also gives you gemstone guns, legendaries, and blue-rarity class mods (since they are actually good).



	- Halved status damage done against the player
	- Doubled movement speed while in FFYL

	- Halved the speed of dragons in the TTAoDK DLC areas, including the dragons of destruction


	- Removed the possibility of elemental resistance secondary stats spawning on all relics
		-I felt that they weren't as appealing as other secondary stats, and making the values too high could have consequences i can't think of

		-Maybe i will re-attempt it with like a universal resistance stat instead of one for each resistance type. I don't know

		-I did not entirely delete the parts, so any relics you would've had that has the stats will still have them.
		 Assuming you have Sanity Saver. Which you should, if you're playing Oselands.


	- Reworked/Fixed Resurgence's healing effect to now be 50% of your max health healed over 1 second
		(the skill just wasnt working properly before)

	

	- Removed minimum level requirements from non-launcher white rarity weapon pools
		- Now you can get every type of item right off the bat. Besides rocket launchers for obvious reasons

	- Removed minimum level requirements from all white rarity shield pools
		- No more are you locked to just tediore shields at the start of the game

	- Replaced Knuckledragger's white jakobs pistol drop with a random white rarity pistol

	- Made the chest right after Knuckledragger give you a random white rarity shotgun (instead of always being jakobs)
	  and a random white rarity AR/SMG/sniper (one of those 3)



		== Unique item changes ==

	- Added 3 'new' legendary relics (aka recycled unused items given a new coat of paint).
		-Available in the world drop pools


	   Including this here as i consider them pseudo-uniques:
	- Highly increased the damage of the Carbuncle e-tech torgue pistol
		-I managed to use these during playthroughs and compared to other e-tech weapons of similar levels and they were 
		 super underperforming for their ammo cost and just weren't fun to use. So, here is a change to that

	- Prazma Cannon
		- Massively lowered the speed of the main projectile
		- Highly increased the explosion radius of both the main projectile and child projectiles
		- Made the main projectile's explosion deal 50% more damage


	- Reworked Cobra
		- Now fires a torgue gyrojet-esque projectile with a massive 200% damage explosion when it hits something (still remains as "gun" splash)
		- 3 Ammo per shot, much higher base damage, essentially removes base crit multipliers
		- It's supposed to be more like a rocket-firing rifle than a sniper rifle


	- Increased the chance for the TMNT rats to drop a storm front from 2.5% to 5% (same as what UCP did)
	- Doubled the chance for the Thunderball Fist to drop from Captain Flynt and Sparky Flynt

	- Removed the possibility of vertical grip accessory spawning on Jolly Roger

	- Removed Flicker from the Legendary Siren class mod

	- Removed the possibility for the morningstar skill effect to stack



=============== [ 1.0.7 ] ===============

	- Added a toggle in the mod file that removes FFS content from the rest of the game, in case you don't have the DLC.

	- Reduced enemy damage by ~10% when you are in TVHM or UVHM, to compensate for elements as a whole becoming stronger
	- Fixed up enemy damage in UVHM to scale between levels 50-60 to then regain that damage back
		TVHM (especially the very start) was a very unexpected difficulty spike, unintentionally high.
		This means that endgame balance should be about the same as it was before, and TVHM still being harder than the end of normal mode,
		but should ease that transition a little bit


	- Increased XP gained from quests by 40%
		Even higher than what enemy XP got to incentivize doing quests and, much like increasing enemy XP, makes the story experience smoother

	- Increased XP gain by ~1.5x in UVHM after level 60
		This is an additional multiplier that applies to both enemies and quests
		Makes the post-story XP grind even easier


	- Fixed Flicker on Maya so that it also applies to other skills in the skill tree that apply their own Damage over Time effects (Smite, Backdraft, Cloud Kill etc)
	- Reduced Player Skill DoT by ~25% to compensate for the change above. But now you can boost flicker even further, making those skills even better
		Unfortunately, i can't do the same for Gaige's DoT skills, as that would end up making Electrical Burn get those buffs twice.
		So Shock and AGGGHH- can not benefit from those effects

	- Renamed Backdraft on Maya to Discharge to better suit the new effect the skill has in Oselands


	- Integrated the Loot Midget World mod into Oselands, originally created by Mopioid
		Makes Loot Midgets spawn in a lot more areas in the game, rather than being confined to a handful ones.
		Mod has been tweaked a little bit to fit better in oselands, namely removed a few possible spawn locations.


	- Gave Jimmy Jenkins additional legendary chances. UCP made him function like a standard loot midget, and i added additional ones that scale with OP levels
	- Gave Loot Goon Goliaths additional legendary chances, scales with OP levels
	- Gave Muscles additional legendary chances, scales with OP levels


	- Increased Legendary weight from 3x to 5x in Terramorphous Peak and Winged Storm
		I didn't feel like it was giving enough yet. Even at 5x the normal legendary world drop rate, world drops will still be fairly uncommon


	- Increased Raid Bosses' additional legendary chance from a 2% base to 5% base. Still gets scaled by OP levels.

	- Replaced Voracidous's 10% chance to drop a Gen1 Legendary Class mod with a 25% chance for a Gen2 Legendary Class Mod
		Voracidous was given a new loot pool for Gen1 class mods which scales with OP levels (along with other raid bosses),
		so this is a way of making voracidous's drops a little more unique


	- Further reduced Raid Boss HP, some more than others


	- Adjusted Elemental Resistances to be a lot less harsh when using an unfavorable element against an enemy
		They are still noticable, but not 'remove 2/3 of your damage' noticable.
		i.e instead of 25% resistance that drops down to 50% in TVHM with fire, it's now 15/0%. In comparison to the highest elemental multiplier
		which would go from +50% damage against flesh to +75% damage in TVHM. So there is a gap of ~75%

	-Adjusted Shock damage multiplier in normal mode a little bit to give it a better damage curve that fits with all the other damage types


	- Made every round in each circle of slaughter repeatable once you've completed them at least once



	- Further nerfed elemental relics, as i felt they still gave too much power too easily.
		Max value at Level 80 went from 30% to 17% for fire/corrosive/shock. Slightly higher for explosive and slag.
		Bone of the Ancients was brought down accordingly as well.

		Do note that i think they will be just all-around good options in pretty much any situation anyway


	- Aggression Relics
		-Due to some changes i did internally, the gun damage/fire rate on aggression relics you already had gotten as drops will not work
		-Fixed rarer aggresion relic drops instead dropping the lower tier aggression relics

		- Lowered Values in a similar vein to elemental relics, though they are still higher


	- Improved chances for relics to be higher rarities in general

	- Reduced value of fire rate secondary stats on relics


	- Removed item level variation from items in vending machines


	- Added additional base status chance to slag elemental parts on guns



		== Unique item changes ==

	- Replaced the Lucrative Opportunity relic with the Loaded Dice
		gives you a somewhat small multiplicative buff to world drop legendary chances
		also applies to loot midgets and raid bosses' additional legendary drops


	- Law was reworked; now it is simply a 2-shot burst jakobs pistol.

	- Further reduced Gub damage and status chance

	- Lowered the speed of Impaler's spike projectiles
		This makes it home in on enemies easier, making it generally more consistent

	- Reduced Transformer shock damage to 10% and fire rate to 15%

	- Reduced Blockhead's damage

	- Reduced Death Toll relic's fire rate to match aggression relics

	- Reduced Sheriff's Badge relic's fire rate slightly



=============== [ 1.0.6 ] ===============

	- Doubled legendary world drop weight while in Digistruct Peak, the 3 Circles of Slaughter, Leviathan's Lair and Torgue's Arena (the big one in his DLC)

	- Changed Terramorphous's and Dragons of Destruction's doubled legendary world drop weight to instead be tripled.

	- Gave Hyperius, Master Gee and Voracidous a legendary pool for guns, shields, grenades and class mods individually that each have a 2% chance to drop.
		This scales with OP levels, with the chance doubling at OP5 and tripling at OP10.
		Pyro Pete already had this functionality

	- Added Cobra to the world drop sniper pool



	- Updated enemies to now also spawn with purple and legendary rarity items (by Temmmmy)

	- Fixed explosive snipers missing a muzzle flash (by ZetaDaemon)



	- Increased Deathtrap's base damage by 15%
	- Lowered Strength of 5 Gorillas' Deathtrap damage from 10% per point to 8%
		The final amount of damage you get will still be higher than before, but this also means that deathtrap
		is more powerful when you are playing the story as well.
		Reduces the effectiveness of Roid Shields a little bit

	- Increased Duty Calls critical damage from 4% per point to 5%
	- Changed Axton's Gunpowder skill tree passive buff from 4% magazine size to 4% gun damage.
		now also properly works for the Ranger skill

	- Added a part to Flicker's description on Maya that states that it only works with guns and grenades

	- Removed Restoration from Maya's skill tree
		Because co-op doesn't work.
		The skill has been removed from class mods as well.



	- Removed skill point variation on purple rarity class mods
		Makes it so purple rarity class mods are always 5/4/4 instead of having the chance for 5/4/3 and 5/3/4 as well (Level 50+ values ofc)

	- Added Onslaught back onto Axton's Legendary Ranger class mod

	- Replaced Mind's Eye on Nurse with Wreck
	- Replaced Suspension on Cleric with Sustenance

	- Tweaked the manufacturers of each character's class mods to try to better spread them out throughout all of them,
	  hopefully promoting more possible allegiance runs and in general switch things up a little bit
		This change does not apply to class mods you already had.

	- Added completely **new** class mods to fill the manufacturer spots where they did not have a non-unique class
	  mod after the previous change. This does not include every character yet, i will attempt to get those done in the future

		- Axton: Bandit(Outlaw)
		- Salvador: Dahl(Machine)



	- Made white rarity relics' stats always be the highest value they could be

	- Reduced Blood of the Seraphs' life steal from 10% to 5%



		== Unique item changes ==

	- Fixed Chere-amie incorrectly having explosive damage splash

	- Increased the damage of the Sloth

	- Massively reduced the damage of the Gub
	- Increased Gub ammo cost per shot from 2 to 3

	- Made Sham spawn with every part manufacturer except Maliwan.
		- Sham does not benefit from +Special boosts anymore, and Maliwan's only job
		  is to be the highest +Special boost, so it has no reason to spawn on the Sham
		- Also applies to Maliwan capacitors, so you are unable to get elemental immunities on it.


=============== [ 1.0.5 ] ===============

	- Heavily lowered voracidous's ludicrously high shield.
		This change only works in UVHM, but you aren't intended to fight raids outside of UVHM anyway.


	- Increased magazine size of Torgue Assault Rifles a little bit

	- Ported over from UCP a section in the Badass Rank screen that says that the mod is running (Tweaked to say the name of the mod of course)

	- Included a fix that makes Headhunter DLCs and Fight For Sanctuary properly scale in TVHM (by Temmmmmy)

	- Removed a UI element from Axton's Legendary Gunner that said that it increased cooldown rate
	- Increased the Sabre Turret's damage by ~20%

	- Doubled the status chance/damage stats on *non-unique* weapon parts. Also added them to parts that seemed to have lacked them.
		This should give even wider variation on the stats on the item cards, as well as give status effects even further power in general.

	- Fixed non-shock spike shields not actually doing any damage

	- Gave Chubbies/Tubbies a 20% chance to drop an additional legendary item (has a chance to be Pearlescent too. Same logic as loot midgets)

	- Reduced OOO spawn rate from 5%(UCP) to 3%. Twister drop is still guaranteed when you kill him.

	- Made Slag's status effect duration scale with effects that increase status effect duration (mainly krieg and gaige)


	== Unique item changes ==

	- Updated the unforgiven's stats and made it fall more in line with the stats of other slow firing jakobs pistols

	- Increased the damage of the Retcher
		Additionally, removed the possibility of it spawning with critical damage parts

	- Increased the damage of the Logan's Gun

	- Reduced the damage of the Emperor

	- Slightly increased fire rate and damage of the Fremington's Edge

=============== [ 1.0.4 ] ===============

	- Universally increased base reload speed of every weapon type by ~8-10%
		There isn't really any consistency to this, i just did what felt good. Some go above the 10%, but i tried to keep most around that area

	- Non-Unique Tediore shotguns (and Deliverance) now have a passive 35% increased pellet count
		-Damage per pellet was reduced to compensate. This overall increases the damage of the throw reload.
		-The other unique tediore shotguns were re-adjusted to make sure that they were still good

	- Adjusted E-Tech shotguns, with a complete rework of Tediore e-techs
		-Tediore E-Tech shotguns now guarantee a DoT on their throw, and said DoT is based on the card damage value rather than the DoT damage
		-Renamed to Corruptor

	- Removed mentions from Maya's and Zer0's skills that mention that the effects would apply to both you and teammates. Now it's just for you
		I didn't bother editing skills such as elated or res, as those were there to begin with. I mainly just removed the ones i put in myself.

	- Ported over a fix from UCP for the skyrocket to make it scale with OP levels

	- Ported over Legendary Class Mod skins from the UCP
		(Tweaked for the legendary class mods that were replaced in Oselands to have the appropriate skin)

	- Gave new skins to the Sawbar, Storm and Bearcat


=============== [ 1.0.3 ] ===============

	- Increased the cooldown rate gained from Nuke from 20% to 50%
	- Adjusted Burn Damage on Axton's Slayer of Terramorphous class mod
	- Fixed a bug with the Gunpowder passive bonus on the Ranger skill that bugged out your magazine.
		As a side effect, said passive bonus does not work on that skill anymore.

	- 1340 Shield now gives you 25% magazine size

	- Fixed a UI bug if you got a Fire Rate secondary stat on a Moxxi's Endowment

	- Gave Unforgiven a new skin


=============== [ 1.0.2 ] ===============

	- Improved fire rate and reload speed of tediore pistols
	- Improved fire rate of tediore SMGs

	- Removed DoT resistances from Hyperius's loaders


=============== [ 1.0.1 ] ===============

	- Fixed some UI on salvador class mods
	- Adjusted elemental damage modifiers and when the values get applied
	- Fixed backpack SDUs not giving you +4 mag


=============== [ 1.0 ] ===============

	- Mod Released. Amazing, i know.
