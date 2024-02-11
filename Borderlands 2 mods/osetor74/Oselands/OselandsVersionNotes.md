=============== [ 1.2.7.1 ] ===============

	- Fixed a bug where Axton's Metal Storm would stop working after entering a vehicle


=============== [ 1.2.7 ] ===============

	- Fixed a bug where weapons that had higher than 2x critical damage added everything above 2x
	  twice (i.e 2.3x weapon was actually being considered as 2.6x)

	- Fixed slag damage double-dipping with global damage boosts

	- Increased base enemy HP, reduced how fast it scales per level
	- Increased base enemy damage, made enemy damage scaling far more consistent
		- Early game is more difficult (and thus more exciting), but equalizes towards the later levels


  	- Removed all minimum-level requirements from white-rarity items
	- Removed white-rarity rocket launchers from the general world drop pool entirely
	- Made white items no longer drop above level 12

 	- Fixed inconsistency with legendary relic world drop weights
		- Now every single one is weighted equally


 	- Elemental Damage Changes

		- Removed damage penalties from elemental parts on guns (was already absent on slag guns)

		- Fire/Corrosive vs correct health type	-> 1.1x damage (from 1.2x)
		- Fire/corrosive vs wrong health type 	-> 0.7x (from 0.6x)
		- Shock vs shield 			-> 1.2x damage (unchanged)
		- Shock vs wrong health type 		-> 0.9x damage (from 0.95x)
		- Slag vs all health types		-> 0.95x damage (from 1.0x)

		*Overall should keep your damage output similar to before, but makes reading weapon cards easier,
		 as you have one less wierd multiplier to worry about.


	- Removed swap speed bonuses from UVHM
	- Massively improved base swap speeds for all weapon types
		*Swap-out time is now the same for every single weapon type, and while swap-in time still differs
		 between weapon types, they are also quickened. No longer do you need to be in UVHM to have tolerable
		 weapon swap times.


	- Spiker E-Tech pistols
		- Reduced delay for the projectile to explode from 1.5 seconds to 0.25
		- Tripled splash radius
		- Further reduced fire rate and increased damage


	- Made it possible to apply status effects to constructors, Saturn and Uranus

 	- Fixed Heavy Nomads sometimes not spawning with any weapons in Southpaw at very low levels in
	  normal mode


   		== Unique item changes ==

	- Rapier
		- Periodic melee damage bonus has been changed from +2.5 PostAdd to the melee modifier
		  to instead increase the damage dealt by your next melee attack to have +50% increased
		  damage

			- Same modifier as what is used by Death Mark and Condition Overload, and
			  the skill descriptions of those 2 skills have been slightly updated to
			  hopefully make that clear
			- Retains the 5 second cooldown

			- This *is* an overall nerf to this effect, but it also makes it far easier to
			  understand. This does now make regular melee bonuses more valuable again as it is
			  a multiplier to them


	- Daedalus
		- Massively improved the accuracy
			(Now you can actually use the gun)
		- Improved material


	- Pocket Salvo
		- Increased explosion radius when impacting the environment by about 25%
		  (this also makes it use a larger visual explosion, making the explosions
		  look way stronger than previously)

	- Thunder
		- Significantly increased reload speed, and increased fire rate

	- Rupture
		- Increased how much the weapon's 2 bullets spread from each other each shot
		 *looked wierd because both bullets were basically always going in the same direction


	- Made 12 pounder not be able to drop with a tediore grip, to avoid it sometimes having 0 mag size


=============== [ 1.2.6 ] ===============

	- Improved the look of weapon card attributes

		- Includes stuff like the weapon's critical damage, ammo cost, melee damage bonuses etc

		- Melee damage bonuses on weapons are now shown as an addition to the base multiplier,
		  because that is how they always function


	- Adjusted the threshold when items and enemies stop benefiting from level increases from 72 to 69.

		- Since i made it so that you stop gaining skill points at level 69, it makes sense that
		  all level scaling stops at that point as well. Guns will have slightly lower damage, 
		  in general most things will have slightly lower values, but the balance of the game has
		  not changed at all.


	- Fixed the player having a lower than intended amount of skill points if they had set the level scaling
	  threshold below level 69	
	

	- Fixed Bandit SMGs doing 0 damage when hitting crit spots


	- Fixed global damage modifiers not applying to instances of corrosive damage


	- Sprinting now multiplies your speed by 1.3x instead of giving +30% movement speed
		- Provided by ZetaDaemon



	
	- Global Melee Changes


		- Increased base melee damage in general

			- At level 1 you'll be doing about 12% more damage with melee attacks than before, and
			  +77% more damage than before at level 69


		- Increased all player base melee attacks to have a range of 360 (previously 330, now same as
		  Buzzaxe Rampage)


		- Increased the range of melee attacks made with bayoneted gun from 360 to 396 (10% longer)


	- Weapons with bayonets now passively grant you +15% movement speed while holding them.
	  This also applies to unique weapons that always come with one.





	- Zer0

		- Decepti0n

			- Melee Damage bonus is now an additive modifier to your base melee damage multiplier,
			  stacking additively with bayonets and being multiplicative with regular +% melee damage
			  bonuses

			- Maximum melee damage value has been reduced down from 4.5 to 2.5



		- Ir0n Hand

			- Increased melee damage bonus from 5% to 7%




	- Krieg

		- Reworked Buzzaxe Rampage

			- No longer has a cooldown and has a practically infinite duration. Pressing the action skill
			  button during the rampage ends it
				- Provided by ZetaDaemon

			- Melee damage multiplier reduced from 2.5x to 2.25x


		- Release the Beast

			- While in RtB, BXR's near-infinite duration gets reduced down to 15 seconds, and prevents you
			  from ending the rampage early
				- Also provided by ZetaDaemon




		- Reworked Bloodlust
		
			- Bloodlust is now a 1-point skill you opt into in the first tier of the tree

			- There is no longer a cap on Bloodlust stacks, nor a delay between when you can gain stacks
			- Bloodlust stacks now last for 6 seconds by default, and gain reduced duration the more
			  stacks you have

			- Each stack of bloodlust by default grants you 0.4% global damage

			- Passive bonus from reaching 5 points in a skill in the Bloodlust tree is replaced with
			  +0.5 seconds to the base duration of Bloodlust stacks


		- Blood Filled Guns

			- Due to the lot more volatile nature of the new Bloodlust stacks, the mag size bonus per
			  stack of bloodlust has been brought back from 0.4% per stack to 0.5%


		- Taste of Blood

			- Now located on the 1st tier of the Bloodlust tree, next to Blood-Filled Guns and Bloodlust

			- Dealing melee damage gives stacks which increase your total Bloodlust stack count without
			  being affected by quicker decay rates at higher stack counts


		- Endurance (Replacing Blood Trance)

			- You gain a damage reduction buff per stack of Bloodlust. Further increased in BXR


		- Blood Overdrive

			- Now can also proc from instances of status damage alongside bullet damage.
			- Now also grants fire rate per stack of bloodlust
			- No longer reduces grenade fuse time


		- Blood Twitch

			- now located on the 4th tier of the Bloodlust tree

			- Grants a passive bonus to swap speed and buzzaxe throw speed. bonuses are further increased
			  after a kill per stack of Bloodlust.


		- Blood Barrage

			- Now located on the 5th tier of the Bloodlust tree

			- Reduceed down to a 3-point maximum
			- Grants free ammo chance, and an additional bonus per stack of bloodlust




		- Flametongue, Hellfire Halitosis and Raving Retribution

			- Damage caused by these 3 skills have been changed so that they are unaffected by regular
			  fire damage health type modifiers.

			  They essentially now deal non-elemental damage that benefit from fire damage on gear



		- Class Mods

			- Barbarian
				- Now boosts Blood Twitch instead of Blood Barrage, as it now has the same functionality
				  as what Blood Barrage previously did

			- Legendary Psycho
				- Now boosts Taste of Blood instead of Blood Twitch, because it is now the other tier 1
				  Bloodlust skill

			- Slayer of Terramorphous
				- Now also grants 2 points to Blood Barrage


    	- Gaige

		- Robot Rampage
			- Melee Damage boost has been reduced down from +50% to +25%

   		- Explosive Clap
			- Melee Damage boost has been reduced down from +75% to +50%


		- Hammer of (In)justice

			- Effect is now active while Discord is active instead of being a Kill Skill
			- Melee Damage boost has been reduced down from +400% to +200%




		== Unique item changes ==


	- Quicksilver

		- Increased passive movement speed while holding the gun from 25% to 35%
			- This is to make sure it still sticks out from the crowd as bayoneted guns now also boost
			  movement speed. Quicksilver stays as a very noticable increase from them.



	- Added a new legendary Bandit SMG: Plaguebearer
		- 4 ammo per shot, 5 pellets per shot, reduced fire rate and accuracy
		- Corroding enemies grants stacks which are expended on melee to create a corrosive nova, increasing
		  damage of the nova per stack

		- ~10% drop chance from Plague Rat enemies


	- Added a new legendary Dahl Pistol: Sucker Punch
		- Full auto with reduced base fire rate and increased damage. Always comes without a sight, and a
		  bayonet that adds +0.5x melee damage

		- Dealing melee damage causes you to gain highly increased cooldown rate, movement speed and reload
		  speed for 7 seconds

		- Dedicated drop from Foreman Jasper in Opportunity


	- Rapier
		- Reduced base melee damage bonus from +1.25x to +0.5x (can still get bandit/torgue grip for an
		  additional +0.25x)

		- Every 5 seconds grants a large boost to your melee damage multiplier, which is applied bayonets and
		  other regular melee damage boosts. Multiplicative with boosts like backstab or execute.


	- Law
		- Dealing melee damage causes your shield to start recharging immediately




=============== [ 1.2.5.1 ] ===============

	- Fixed Voracidous not dropping their dedicated seraph items

	- Fixed Pyro Pete dropping 3 seraph items from his pool every kill instead of 1, as well as some of
	  those drops working regardless of playthrough

	- Fixed Terramorphous, Master Gee, Pyro Pete, Voracidous, Dexiduous and the Ancient Dragons of Destruction
	  not being able to drop the Pearl of Power


	- The magazine of PBFGs have been increased by 1 to avoid them being able to appear with 0 magazine size


	- Minor fixes to character skill descriptions


	- Brought over improvements to Deathtrap's AI by Zazk0u27. It should make him a lot more consistent and
	  effective.



=============== [ 1.2.5 ] ===============

	- Fixed standard enemy drop pool not being able to drop eridium and legendary tokens

	- Reduced the drop chance of the Desperado class mod from badasses in Bandit Slaughter from 5% to 2%

	
		== Unique item changes ==

	- Added a new legendary Hyperion pistol: Knell
		-3 ammo per shot, reduced crit damage but much higher base damage, massively reduced mag size
		-Scoring a critical hit activates a buff that grants infinite ammo to the Knell for 2 seconds


		- 7.5% chance to drop from Gravedigger enemies (at the default option of 15% dedicated legendary drops).


	- Added a new legendary Torgue shotgun: Obliterator
		-5 pellets per shot, increased fire rate and mag size. Swapping to and from the weapon is also
		 faster.
		-Pellets activate a buff on hit that gives you +3% global damage. No stack limit and
		 stacks persist after switching weapons.
		-Pellets create a massive explosion when hitting an enemy (rocket damage) but deal no impact damage
			-Also means it can not crit


		-Dedicated drop from Saturn


	- Added a new Seraph relic: Pearl of Power
		-Rolls one of the 6 vault hunters and gives skill point bonuses to skills of that vault hunter
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

		-Guaranteed to get one as a drop every time you kill *any* raid boss while in UVHM.
		 The drop is more heavily weighted for the character you are currently playing.
			


	- Added a new legendary relic: Temporal Teardrop
		-A small cooldown rate boost
		-Your action skill cools down even while it is active, at half of its regular rate

		-World drop only



	- Added a new E-Tech Shield: Chromatic Hydra 
		-0 capacity, like all E-Tech shields in this mod
		-High adaptive shield effect value
		-Overrides existing elemental damage multipliers towards all health types (health, shield, armor)
		 when dealing damage to enemies with a new value (essentially nullifying both the penalties *and*
		 unique benefits of each damage type and giving you a more general multiplier instead)


		- 5% drop chance from elemental badass skags



	- Added a new E-Tech Class Mod: Death Kiss
		-Can be used by any class, like all E-Tech class mods in this mod
		-Applies the Blight effect previously found on the Medusa's Eye relic
			-Slagged enemies get a constant health drain equal to your max health per second


		- 2% chance to drop from badasses in the Natural Selection Annex (creature slaughter)
		 while you are in UVHM.


	- Gub
		-Reworked (again) to be a fast firing bandit pistol with heavily arcing bullets. No longer
		 deals splash damage.



	- Removed the Blight effect from Medusa's Eye. The rest of the item was unchanged

	- Made the Titan Heart shield's amp damage effect apply to Salvador's left hand.


	- Updated the Tracer shotgun bullet and massively improved the weapon's accuracy
	- Gave a red text to the Loaded Dice relic


=============== [ 1.2.4.1 ] ===============

	- You now gain your first skill point at level 2 instead of 5

	- You now stop gaining skill points after level 69. This grants you a total of 68 skill points, which is equal
	  to how much you would have had with the old level 72 cap.

		*the reduction in total amount of skill points in theory means more decision making in your build,
		 leading to more possible build diversity. In reality this is still a high amount of skill points,
		 but at the very least it's not limiting.


	- Salvador Skill Changes

		- New skill added to tier 5 Brawn: Provoke
			-Taking damage causes you to gain stacks that give you improved shield recharge delay
			-This effect is further boosted by the amount of points you have spent in Incite
			-No stack limit, no cooldown on being able to get stacks
			-maximum of 3 points


	- Krieg Skill Changes

		- New skill added to tier 5 Mania: Bloodthirst Aegis
			-Killing an enemy instantly refills 25% of your shield capacity
			-maximum of 3 points



	- Axton Skill Changes

		- Laser Sight
			-Maximum point cap has been reduced from 5 to 3
			-Now gives 0.4 ammo regen per point instead of 0.25
			-Now gives 10% accuracy per point instead of 5%

		- Crisis Management
			-Gun damage boost has been changed to 5% global damage per point
			-Fixed damage reduction buff not working

		- Resourceful
			-Increased mag size per point from 3% to 4%

		- Last Ditch Effort
			-Gun damage boost has been changed to 4% global damage per point


		== Unique item changes ==

	- Cradle
		-Fixed damage formula not working properly, causing the item to basically always deal level 1 damage
		-Fixed the item not getting shield damage bonuses
		-Massively increased base damage


=============== [ 1.2.4 ] ===============

	- Further fixed elemental tracers (provided to me by ZetaDaemon)

	- Pyro Pete (Raid)
		-Further increased movement speed from 600 to 1000 (vanilla value = 400)
		-Reduced shield capacity to ~1/10th of its previous value
		-Increased max health by a little over 3x

		*With these changes you'll be spending less time in phase 1 and more in phase 2 and makes him generally a more
		 threatening presence since he can move around the arena easier


	- Axton class mod changes

		- Legendary Soldier
			-Removed Impact and Healthy skill boosts

		- Legendary Pointman
			-Added Expertise and Resourceful skill boosts


	- Maya class mod changes

		- Legendary Siren
			-Removed Mind's Eye skill boost


	- Zer0 skill changes

		- New skill added to tier 5 of Sniping: Arsenal
			-Increases bullet damage, grenade damage, rocket damage and melee damage (multiplicative) by 2% per point

		- At 0ne with the Gun
			-Reduced % mag size boost from 5% to 3% per point

		- Death Mark
			-Fixed skill not applying to nova damage

		- C0nditi0n 0verl0ad
			-Fixed the skill not providing skill tree passive bonuses when fully specced
			-Fixed skill not applying to nova damage


	- Fixed Hyperius and Gee not being able to drop their Proof of a Hero relic


	- Fixed E-Tech shield drop rates from badasses being much, much lower than intended
		-Now they are properly around 5% chance from their respective drop source (0.35x of the standard dedicated
		 legendary chance, which is increased to 15% by default in Oselands).
		 As a refresher:

			- Berserker shield (Bandit) - Badass Psychos
				-Dealing or taking damage causes you enter a rage, gaining movement speed and life steal while your
				 health drains quickly.

			- Titan Heart Shield (Hyperion) - Badass Loaders
				-Grants increased max health, and adds 10% of your maximum health value as amp damage to all your shots

			- Shatter Tank Shield (Pangolin) - Spiderant Kings/Queens (/their renamed versions in higher difficulties)
				-Reduces max health on top of the 0 capacity, but grants high flat health regen



		== Unique item changes ==

	- Added a new *E-Tech* class mod

		*The idea for these is that each one will be shared across all characters rather than being character specific.
		 Thus they do not boost skills but act more like secondary, powerful relics with activated effects and niche
		 stats that you might not be able to get on a particular character otherwise

		- Desperado
			-Increased Crit damage
			-Reduces base reload time of all of your guns by 0.5 seconds (i.e before reload speed boosts are taken into account)
			-Critically killing an enemy with a bullet gives +10% bullet damage, stacking indefinitely and losing all stacks
			 upon getting a bullet kill that is not a crit.

			-5% chance to drop from any badass enemy within Fink's Slaughterhouse while you are in UVHM.


	- Red Hellion
		-Fixed fire rate buff being completely broken

	- Eraser (Carnage replacement)
		-Updated the firing mode of the weapon to be much closer to what i originally had in mind for it
			much closer to the reference material as well, and just makes the gun way, way more manageable to use
			(explaining exact change is difficult via text. Just use it for yourself)
		-Removed crit bonus, highly increased base damage

	- Shredifier
		-Massively lowered fire rate and practically nullified the natural vladof barrel wind-up
		-Now gains 5% increased fire rate for 5 seconds when you hit an enemy, stacking infinitely
		-Now also has 50% chance to not consume ammo
		-Reduced base damage

	- Hellfire
		-Now has a *chance* on impact to create a fire explosion, rather than always dealing splash damage
			-Base damage is equal to 175% of the weapon's status damage
			-Impact damage dealt is considered Status Damage, and benefits from boosts to Status Damage
			-Benefits from 50% of your gun damage bonuses
			-Always applies a fire DoT

		-Increased damage
		-Highly increased status damage
		-Made the weapon's standard status chance pretty much nonexistant
		-Slightly reduced fire rate

	- World Piercer
		-Fixed the weapon having unintentionally massively reduced damage

	- Comically Large Blunderbuss
		-Removed the weapon's ability to crit, now instead deals pure bullet splash damage when
		 the bullets hit enemies
			-Also fixed the weapon having unintentionally massively reduced damage

		-Increased pellet count from 5 to 8 (so basically just a 60% damage increase)
		-Increased damage by ~50%
		-Reduced mag size down to 1
		-Massively improved reload speed
		-Increased recoil for comedic effect
		-Increased bullet speed by 50%
		
		
	- Swordfish
		-Increased the damage gained per remaining ammo in the mag when ADS'ing from 50% to 75%



=============== [ 1.2.3 ] ===============

	- Further improved compatibility with BL2:Wonderlands and made it easier for me to update Oselands without needing
	  to update BL2:WL every time alongside it.
		*Though, ironically for this to work you also need to update BL2:WL

	- Adjusted legendary token drop rates
		-While you are in UVHM, each token drop now drops either 1 or 2 tokens

		-Fixed Badass drop pool torgue token drops not scaling with the legendary weight in OP levels
		-Fixed SuperBadass and UltimateBadass drop pools not including torgue token drops


	- Fixed some Nova shields still having their old functionality even though they said it creates a nova on taking damage


	- Axton skill and Class Mod changes

		- Crisis Management
			-Now is a spectrum based on how low your shield is rather than binary on/off for if your shield is broken or not
				(linear bonus based on % empty, so 0 bonus at full shield, full bonus at 0 shield)
			-Increased damage reduction per point to Sup to 7%

		- Resourceful
			-Now also grants 3% mag size per point


		- Legendary Soldier class mod
			-Removed mag size bonus

		- Specialist class mod
			-Now also boosts mag size


	- Zer0 skill changes

		- At 0ne With The Gun
			-Maximum skill rank reduced to 4 points
			-Skill now *only* grants +5% magazine size per point, as well as a flat amount after other calculation
				The flat amount is +1 when you spec into the skill, and increases to +2 when you max the skill.
			-Now applies to every weapon type
				(Rocket launchers have a reduced effect; maximum bonus of +1 when the skill is maxed)

		- Critical Ascensi0n
			-Removed critical damage bonus from stacks
			-Gun Damage bonus from stacks is now multiplicative with other gun damage bonuses


	- Salvador skill changes

		- Money Shot
			-Skill description now mentions that the gun damage bonus is multiplicative

		- No Kill Like Overkill
			-Updated skill description to be more accurate to the actual function of the skill.

	- Maya skill changes

		- Reaper
			-Now lists damage bonus as bullet damage as that is more accurate to how the skill functions




	- Pretty drastically increased drop rates on general item drops from enemies across the board

	- Added Gen2 legendary class mods to the world drop legendary class mod pools
		-These still require you to be level 62 or above.
		-The split between Gen1/Gen2 from world drops is now 40/60, meaning you will still get more of the gen1 class mods of your
		 particular character than any one specific gen2 class mod of the same character

	- Further increased the weighting on class mods dropping for whatever character you are playing at that time
		-Every class mod drop now has a 75% chance to be for the character you are playing


	- Added more legendary drops to raid bosses as a whole
	- Replaced the tripled world drop chance of terramorphous and the ancient dragons with the same bonus legendary drops as other raids

	- Added an additional 100% chance for Voracidous to drop a Gen2 legendary class mod on top of the 25% chance that i already gave it
		-This means you can also get 2 in the same kill


	- Fixed Pyro Pete and the Ancient Dragons of Destruction not being able to drop their Proof of a Hero relic
	- Fixed some raid bosses having 2 chances of dropping their Proof of a Hero relic each kill


		== Unique item changes ==

	- Deathless
		-Fixed the health drain effect breaking completely while you were afflicted with a DoT effect



=============== [ 1.2.2 ] ===============

	- Rocket launcher damage is now *massively* diminished when transfering it to other weapons (i.e pimperhabbing)

	- Fixed the Damage Reduction on Resistance relics being massively lower than intended

	- Most bullets fired by elemental shotguns now have the color of that element
	- Reduced the speed of standard Hyperion shotgun bullets so that they are more in-line (but still faster than)
	  other shotgun bullets


	- Legendary Drop Changes

		- Adjusted the weighting of each item category from legendary world drops. Previously the chances were all over
		  the place, but now it should be more consistent

			- In essence, you will now see more legendary guns compared to every other item category (since they have
			  the most amount of items), as well as less legendary class mods and relics at lower levels, but more
			  of them at higher levels.

			*This does not directly affect the chances for drops themselves, just the distribution between the different
			 item categories whenever you do get a world drop legendary


	- Legendary Vendors

		- Torgue tokens now drop everywhere in the game from enemies

		- Torgue vendors have been reworked to now only sell random world drop legendaries.
			-Different areas in Torgue DLC are assigned different items so it is easier to get an item you'd want:

			arena - shotgun, launcher
			moxxi's bar - SMG, pistol
			beatdown - AR, sniper
			beatdown bar - COM, relic
			forge - grenade, shield
			southern raceway - random
			badass crater - random


	- Player Melee Damage changes

		- The base melee damage formula of pretty much all characters has been changed so that there is an additional
		  boost per level, adding an additional multiplier to your overall damage that scales up over time.
		  You can think of it as exponential scaling (it's not) instead of pure linear scaling like it was before, if
		  that makes it easier to visualize

		  	Krieg already had this buff, making his melee damage stronger by default before taking into account
		  	Buzzaxe Rampage and his melee damage skills

			This increased buff is equal to 2% * your player level, which means that at level 72 and above, your
			melee damage (including added roid damage) will be 2.44x its previous value

		- Krieg now shares the same base melee damage multiplier as every other character
		  (2.5x instead of 2x with an additional multiplier that eventually ends up making it better than the rest)

			This means that Krieg's basic melee attacks now deal 25% more damage than before, and combined
			with the change above means that his base melee damage is identical to everyone else's base as well.


	- Krieg skill changes

		- Buzzaxe Rampage
			-Now lists the melee damage as a multiplier rather than the total %
			(it has always been a multiplier, in-game just listed the full melee damage % you would have when using it)
			-Multiplier reduced from 3x to 2.5x to compensate for the global melee changes

			*Overall, melee krieg will be dealing slightly more damage due to the earlier changes


	- Zer0 skill changes

		- Decepti0n
			-Maximum Melee Damage reduced from 650% to 450%

		- Death Bl0ss0m
			-Now reduces Death Mark's bonus damage down from 80% to 30% when you spec into this skill

		- New skill added to tier 5 of Bloodshed: C0nditi0n 0verl0ad
			-Increases your damage dealt to enemies by 3% per point for each unique damaging status effect on them


	- Axton skill changes

		- Laser sight
			-Now grants ammo regeneration for 3 seconds upon critically hitting an enemy

		- Metal Storm
			-Reduced fire rate per point from 12% to 8%
			-Reduced recoil reduction per point from 15% to 10%
			-Visually looks like a passive skill on the tree, but functionally has not changed

		- Ranger
			-Stat bonuses increased from 2% per point to 3%

		- New skill added to tier 5 of Gunpowder: Overclocked
			-Increases the damage dealt by shield damage abilities (nova, spike, etc)
			-Maximum of 3 points, 20% at max

			*Seems to not work for the Cradle's shield break effect, but i'll try to fix that for the next update

		- New skill added to tier 6 of Gunpowder: Stormweaver
			-Grants 15% fire rate, and +5% for every point you currently have in Metal Storm

			*This is basically a secondary capstone and an incentive to go that far down the tree.
			 A part of Metal Storm's power has been taken away, and this skill grants that power back
			 even stronger, since it's a passive fire rate buff.

		- Nuke
			-Damage now scales with your grenade damage bonuses
			-Damage now scales with your explosive damage bonuses
			-Massively reduced damage of the fire DoT caused by the Nuke
			-Cooldown Rate granted by the skill reduced from 50% to 30%


	- Salvador skill changes

		- Lay Waste
			-Fixed on-kill effect not actually working
			-On-kill effect now shows up as a kill skill, and benefits from increases to kill skill duration


	- Pounder (Dahl AR)
		- Fixed critical damage bonus not showing up properly on the card
		- Increased fire rate


	- - Fixed a few compatibility issues with BL2:Wonderlands


		== Unique item changes ==

	- Medusa's Eye
		-Damage increase against slagged enemies is now replaced with a new "Blight" extension for slag

			- Drains slagged enemies by 100% of your max health per second, increasing by your
			  slag damage and status damage bonuses. Can not kill enemies; instead leaves them at
			  5% of their HP

			*Plan is to give this effect to multiple other items in other item slots

	- Skin of the Ancients
		-Now has the highest damage reduction buff on any relic
		-Increases the damage dealt by shield damage abilities by 20%

	- Maggie
		-Now uses the shotgun crosshairs
		-Separated the pellets in the shotgun spread more from each other, but made the minimum accuracy
		 of the gun better.

	- Florentine
		-Now shoots 2 orbs every shot; one that deals fully shock damage and one that deals fully slag
		 damage. Each one has +100% grenade splash of their according damage type
		-Reduced base damage to compensate

	- Evil Smasher
		-Accuracy from the weapon's buff now also applies to main hand and offhand separately

	- Grog Nozzle
		-Drunk effect now applies to both your main hand and offhand equally while playing salvador

	- Madhous
		-Pellet count increase effect now applies only to the Madhous

	- Deliverance
		-Fixed throw reload not shooting



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
