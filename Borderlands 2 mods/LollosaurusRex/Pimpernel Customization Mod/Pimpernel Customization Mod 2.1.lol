<BLCMM v="1">
#<!!!You opened a file saved with BLCMM in FilterTool. Please update to BLCMM to properly open this file!!!>
	<head>
		<type name="BL2" offline="false"/>
	</head>
	<body>
		<category name="Pimpernel Customization Mod 2.1">
			<comment> _     ____  _     _     ____ </comment>
			<comment>/ \   /  _ \/ \   / \   /  _ \</comment>
			<comment>| |   | / \|| |   | |   | / \|</comment>
			<comment>| |_/\| \_/|| |_/\| |_/\| \_/|</comment>
			<comment>\____/\____/\____/\____/\____/</comment>
			<category name="Description">
				<comment>Pimpernel Customization Mod 2.1 by Lollo(saurusRex)</comment>
				<comment> </comment>
				<comment>Enables the customization of the Pimpernel.</comment>
				<comment>These customizations include various optional skins and cosmetic barrel changes.</comment>
				<comment> </comment>
				<comment>With the barrel customizations, two can be selected to be shown at the same time, creating unique mash-ups of barrels.</comment>
				<comment>All the skins are recolors, done by me, unless otherwise stated.</comment>
				<comment></comment>
				<comment>All Settings are set to default to start.</comment>
				<comment></comment>
				<comment>Thank you for using my mod :) </comment>
				<comment>Feel free to change this mod but please DO NOT REHOST IT</comment>
			</category>
			<category name="Primary Barrel Choice" MUT="true">
				<comment>Each manufacturer's barrel is fully working and selectable. This includes the E-Tech/Alien barrel with its flaps.</comment>
				<comment></comment>
				<comment>Album Link: https://imgur.com/a/FMFWvFi</comment>
				<comment> </comment>
				<comment>Hint: Look inside the barrel folders for a direct link</comment>
				<category name="Dahl Barrel (Default)">
					<comment>Cosmetic Dahl Barrel</comment>
					<comment>Image: https://i.imgur.com/Z87nHx0.png</comment>
					<category name="Code">
						<code profiles="default">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Dahl</code>
					</category>
				</category>
				<category name="Maliwan Barrel">
					<comment>Cosmetic Maliwan Barrel</comment>
					<comment>Image: https://i.imgur.com/zqfOvaT.png</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Maliwan</code>
					</category>
				</category>
				<category name="Vladof Barrel">
					<comment>Cosmetic, working Vladof Barrel</comment>
					<comment>Image: https://i.imgur.com/X5dx7uh.png</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Vladof</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel bIsSpinningEnabled True</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel NumPhysicalBarrelsToFireFrom 2</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel BoneControllers ((BoneName="Vladoff_Gatling",ControlType=WEAP_BONE_CONTROL_BarrelSpinner,bUseInFirstPerson=True,bUseInThirdPerson=True,ControlTemplate=WillowSkelControlLerpSingleBone'GD_Weap_SniperRifles.Barrel.SR_Barrel_Vladof:WillowSkelControlLerpSingleBone_0'))</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel SpinUpDuration (BaseValueConstant=0.500000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel SpinDownDuration (BaseValueConstant=0.500000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel StartingSpinUpFireIntervalMultiplier 1.000000</code>
					</category>
				</category>
				<category name="Jakobs Barrel">
					<comment>Cosmetic Jakobs Barrel</comment>
					<comment>Image: https://i.imgur.com/9TPnJBf.png</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Jakobs</code>
					</category>
				</category>
				<category name="Hyperion Barrel">
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Hyperion</code>
					</category>
					<comment>Cosmetic Hyperion Barrel</comment>
					<comment>Image: https://i.imgur.com/UXO3y8W.png</comment>
				</category>
				<category name="E-Tech Barrel">
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Alien</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel NumPhysicalBarrelsToFireFrom 0</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel BoneControllers ((BoneName="Alien_Top_L_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_0'),(BoneName="Alien_Top_R_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_1'),(BoneName="Alien_Bottom_L_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_2'),(BoneName="Alien_Bottom_R_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_3'))</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel bIsSpinningEnabled False</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel bFlapsEnabled True</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel FlapsExpandDuration (BaseValueConstant=2.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel FlapsCollapseDuration (BaseValueConstant=0.500000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel MuzzleFlashPSTemplates EffectCollectionDefinition'GD_Weap_SniperRifles.Effects.SR_ETech_MuzzleFlashes'</code>
					</category>
					<comment>Cosmetic, working E-Tech/Alien Barrel</comment>
					<comment>Images: </comment>
					<comment>	Still: https://i.imgur.com/9LUGE9q.png</comment>
					<comment>Firing: https://i.imgur.com/AXpGOiy.png</comment>
				</category>
			</category>
			<category name="Secondary Barrel Type" MUT="true">
				<comment>Along with a choice of a primary barrel, a secondary barrel can be chosen.</comment>
				<comment>This allows for unique mash-ups of two different types of barrels.</comment>
				<comment> </comment>
				<comment>Showcasing all the possible combination would be too much, instead I will show some of my favorites.</comment>
				<comment></comment>
				<comment>Album Link: https://imgur.com/a/yLZM1Ud</comment>
				<comment></comment>
				<comment>- Maliwan + Jakobs: https://i.imgur.com/vu814Cy.png</comment>
				<comment>- Hyperion + E-Tech: https://i.imgur.com/k6PKvlo.png</comment>
				<comment>- Jakobs + Hyperion: https://i.imgur.com/PiFvkQf.png</comment>
				<comment>- Jakobs + E-Tech: https://i.imgur.com/rf3TmC6.png</comment>
				<comment>- Jakobs + Vladof: https://i.imgur.com/xJQ3ZJt.png</comment>
				<comment></comment>
				<comment>Be aware that having more than one barrel is not by design and therefore many combinations will experience clipping.</comment>
				<category name="None (Default)">
					<comment>Secondary Barrel Disabled (Default)</comment>
					<category name="Code">
						<code profiles="default">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_None</code>
					</category>
				</category>
				<category name="Dahl">
					<comment>Secondary Cosmetic Dahl Barrel</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_Dahl</code>
					</category>
				</category>
				<category name="Maliwan Barrel">
					<comment>Secondary Cosmetic Maliwan Barrel</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_Maliwan</code>
					</category>
				</category>
				<category name="Vladof Barrel">
					<comment>Secondary, Cosmetic, and Fully Working Vladof Barrel</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_Vladof</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel bIsSpinningEnabled True</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel NumPhysicalBarrelsToFireFrom 2</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel BoneControllers ((BoneName="Vladoff_Gatling",ControlType=WEAP_BONE_CONTROL_BarrelSpinner,bUseInFirstPerson=True,bUseInThirdPerson=True,ControlTemplate=WillowSkelControlLerpSingleBone'GD_Weap_SniperRifles.Barrel.SR_Barrel_Vladof:WillowSkelControlLerpSingleBone_0'))</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel SpinUpDuration (BaseValueConstant=0.500000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel SpinDownDuration (BaseValueConstant=0.500000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel StartingSpinUpFireIntervalMultiplier 1.000000</code>
					</category>
				</category>
				<category name="Jakobs Barrel">
					<comment>Secondary Cosmetic Jakobs Barrel</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_Jakobs</code>
					</category>
				</category>
				<category name="Hyperion">
					<comment>Secondary Cosmetic Hyperion Barrel</comment>
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_Hyperion</code>
					</category>
				</category>
				<category name="E-Tech Barrel">
					<category name="Code">
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_Alien</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel NumPhysicalBarrelsToFireFrom 0</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel BoneControllers ((BoneName="Alien_Top_L_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_0'),(BoneName="Alien_Top_R_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_1'),(BoneName="Alien_Bottom_L_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_2'),(BoneName="Alien_Bottom_R_Flap",ControlType=WEAP_BONE_CONTROL_Flap,bUseInFirstPerson=True,bUseInThirdPerson=False,ControlTemplate=WillowSkelControl_RotateFlapFromFiring'GD_Weap_SniperRifles.Barrel.SR_Barrel_Alien_RailGun:WillowSkelControl_RotateFlapFromFiring_3'))</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel bIsSpinningEnabled False</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel bFlapsEnabled True</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel FlapsExpandDuration (BaseValueConstant=2.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel FlapsCollapseDuration (BaseValueConstant=0.500000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)</code>
						<code profiles="">set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel MuzzleFlashPSTemplates EffectCollectionDefinition'GD_Weap_SniperRifles.Effects.SR_ETech_MuzzleFlashes'</code>
					</category>
					<comment>Secondary, Cosmetic, and Fully Working E-Tech/Alien Barrel</comment>
				</category>
			</category>
			<category name="Skin Choice" MUT="true">
				<comment>Skins can be changed in-game. </comment>
				<comment>Within BLCMM, choose whatever skin you want and save file.</comment>
				<comment>Execute within game at any time to change the skin.</comment>
				<comment> </comment>
				<comment>Album Link: https://imgur.com/a/a8unn36</comment>
				<comment> </comment>
				<comment>Hint: Look inside each skin folder for a discription and direct link :)</comment>
				<category name="Default Skin">
					<comment>Simple enough, the default skin for the Pimpernel</comment>
					<comment>Image: https://i.imgur.com/qIW936D.png</comment>
					<category name="Code">
						<code profiles="default">set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=1.000000,G=0.880710,B=0.696144,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=1.239821,G=1.740337,B=0.923082,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.144101,G=0.165740,B=0.065018,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=1.573880,G=0.960620,B=0.443511,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=0.339223,G=0.204710,B=0.170138,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=0.771362,G=1.233393,B=1.471519,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=1.573880,G=0.960620,B=0.443511,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=1.011173,G=0.368309,B=0.011210,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.640860,G=0.174031,B=0.000324,A=1.000000),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.375677,G=0.375677,B=0.375677,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))</code>
					</category>
				</category>
				<category name="Default Skin with more Gold">
					<comment>This makes the previously silver/ grey parts on the gun gold, with the rest being default.</comment>
					<comment>Image: https://i.imgur.com/xr57AGt.png</comment>
					<category name="Code">
						<code profiles="">set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=1.000000,G=0.880710,B=0.696144,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=1.239821,G=1.740337,B=0.923082,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.144101,G=0.165740,B=0.065018,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=1.57,G=0.96,B=0.44,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=1.01,G=0.368,B=0.01,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=0.64,G=0.17,B=0,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=1.573880,G=0.960620,B=0.443511,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=1.011173,G=0.368309,B=0.011210,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.640860,G=0.174031,B=0.000324,A=1.000000),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.375677,G=0.375677,B=0.375677,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))</code>
					</category>
				</category>
				<category name="Battleworn">
					<comment>This is the first skin I made and features a dark grey/ red body. </comment>
					<comment>There are sections where grey and/or red shine through better, adding a worn and bloodied look to the gun.</comment>
					<comment>Image: https://i.imgur.com/4SXbkWT.png</comment>
					<category name="Code">
						<code profiles="">set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=1.39,G=0,B=0,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=0.79,G=0.47,B=0.47,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.47,G=0.79,B=0.79,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=1.57,G=0.96,B=0.44,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=1.01,G=0.368,B=0.01,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=0.64,G=0.17,B=0,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=1.573880,G=0.960620,B=0.443511,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=1.011173,G=0.368309,B=0.011210,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.640860,G=0.174031,B=0.000324,A=1.000000),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.375677,G=0.375677,B=0.375677,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))</code>
					</category>
				</category>
				<category name="Greener on the Other Side 1">
					<comment>This skin changes the body to a pine-greeen color with pimpernel-red accents and wood/ brass coloring.</comment>
					<comment>Image: https://i.imgur.com/JiPWe9Q.png</comment>
					<category name="Code">
						<code profiles="">set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=0.5,G=0.5,B=0.5,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=0.6,G=0.2,B=0,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.7,G=0,B=0,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=.3,G=0.08,B=0.08,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=2.42,G=1,B=0.41,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=5,G=1.2,B=0.41,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=0,G=0,B=0,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=0.25,G=0.01,B=0.01,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.25,G=0.01,B=0.01,A=1),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.03,G=0.5,B=0.5,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))</code>
					</category>
				</category>
				<category name="Greener on the Other Side 2">
					<comment>This skin changes the body to a pine-greeen color with pimpernel-red accents and lighter wood/ ivory coloring.</comment>
					<comment>Image: https://i.imgur.com/XijipzM.png</comment>
					<category name="Code">
						<code profiles="">set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=0.5,G=0.5,B=0.5,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=0.6,G=0.2,B=0.3,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.7,G=0,B=0,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=2.55,G=1.92,B=0.77,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=1.3,G=0.8,B=0.35,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=2.55,G=1.92,B=0.77,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=0,G=0,B=0,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=0.25,G=0.01,B=0.01,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.25,G=0.01,B=0.01,A=1),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.03,G=0.5,B=0.5,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))</code>
					</category>
				</category>
				<category name="Greener on the Other Side with more Gold">
					<comment>This skin features the same pine-green body and red accents but now includes the same gold coloring as the gold-ified default skin.</comment>
					<comment>Image: https://i.imgur.com/HgHQAOA.png</comment>
					<category name="Code">
						<code profiles="">set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=0.5,G=0.5,B=0.5,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=0.6,G=0.2,B=0,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.7,G=0,B=0,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=1.57,G=0.96,B=0.44,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=1.01,G=0.368,B=0.01,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=0.64,G=0.17,B=0,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=0,G=0,B=0,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=0.25,G=0.01,B=0.01,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.25,G=0.01,B=0.01,A=1),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.03,G=0.5,B=0.5,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))</code>
					</category>
				</category>
			</category>
		</category>
	</body>
</BLCMM>

#Commands:
set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel GestaltModeSkeletalMeshName SR_Barrel_Dahl
set GD_Orchid_BossWeapons.SniperRifles.SR_Barrel_Dahl_Pimpernel AdditionalGestaltModeSkeletalMeshNames SR_Barrel_None
set Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel VectorParameterValues ((ParameterName="p_AColorHilight",ParameterValue=(R=1.000000,G=0.880710,B=0.696144,A=1.000000),ExpressionGUID=(A=384292798,B=1221323751,C=-2145405772,D=1872194118)),(ParameterName="p_AColorMidtone",ParameterValue=(R=1.239821,G=1.740337,B=0.923082,A=1.000000),ExpressionGUID=(A=1102826245,B=1256298978,C=-1429881438,D=-507521102)),(ParameterName="p_AColorShadow",ParameterValue=(R=0.144101,G=0.165740,B=0.065018,A=1.000000),ExpressionGUID=(A=1481234158,B=1129012376,C=-688827739,D=-2119135160)),(ParameterName="p_BColorHilight",ParameterValue=(R=1.573880,G=0.960620,B=0.443511,A=1.000000),ExpressionGUID=(A=170714760,B=1132476783,C=-275668290,D=655702143)),(ParameterName="p_BColorMidtone",ParameterValue=(R=0.339223,G=0.204710,B=0.170138,A=1.000000),ExpressionGUID=(A=473594356,B=1338758895,C=824823946,D=864253813)),(ParameterName="p_BColorShadow",ParameterValue=(R=0.771362,G=1.233393,B=1.471519,A=1.000000),ExpressionGUID=(A=-429590341,B=1156435294,C=-1015192901,D=687313413)),(ParameterName="p_CColorHilight",ParameterValue=(R=1.573880,G=0.960620,B=0.443511,A=1.000000),ExpressionGUID=(A=759765673,B=1280874949,C=257367956,D=-932702788)),(ParameterName="p_CColorMidtone",ParameterValue=(R=1.011173,G=0.368309,B=0.011210,A=1.000000),ExpressionGUID=(A=110180441,B=1232792373,C=-1232281417,D=-1030626065)),(ParameterName="p_CColorShadow",ParameterValue=(R=0.640860,G=0.174031,B=0.000324,A=1.000000),ExpressionGUID=(A=716329441,B=1214803259,C=-238071112,D=-1004122047)),(ParameterName="p_EmissiveColor",ParameterValue=(R=0.000000,G=0.000000,B=0.000000,A=0.000000),ExpressionGUID=(A=-2074486426,B=1296399582,C=-2021314681,D=-350758005)),(ParameterName="p_ReflectColor",ParameterValue=(R=6.702296,G=6.702296,B=6.702296,A=1.000000),ExpressionGUID=(A=295058103,B=1318551573,C=-2045449573,D=-547597976)),(ParameterName="p_ReflectionChannelScale",ParameterValue=(R=0.500000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1869386622,B=1303200947,C=-1616405849,D=714558284)),(ParameterName="p_DecalScalePosition",ParameterValue=(R=4.000000,G=7.110000,B=0.831000,A=0.558600),ExpressionGUID=(A=395540170,B=1243133493,C=-1264190552,D=123075385)),(ParameterName="p_DecalColor",ParameterValue=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),ExpressionGUID=(A=1691998600,B=1239094551,C=2074257317,D=1844701893)),(ParameterName="p_PatternScalePosition",ParameterValue=(R=4.263599,G=6.516000,B=-0.004000,A=0.090700),ExpressionGUID=(A=-2005018406,B=1132497243,C=-39915121,D=208423616)),(ParameterName="p_PatternChannelScale",ParameterValue=(R=1.000000,G=0.600000,B=0.000000,A=0.000000),ExpressionGUID=(A=439432319,B=1091149893,C=-1991909502,D=1816944627)),(ParameterName="p_PatternColor",ParameterValue=(R=0.375677,G=0.375677,B=0.375677,A=1.000000),ExpressionGUID=(A=676539706,B=1125682796,C=1871983293,D=-2049503601)))

