<BLCMM v="1">
#<!!!You opened a file saved with BLCMM in FilterTool. Please update to BLCMM to properly open this file!!!>
	<head>
		<type name="BL2" offline="false"/>
	</head>
	<body>
		<category name="Chain Reaction Mod 1.0">
			<comment> _     ____  _     _     ____ </comment>
			<comment>/ \   /  _ \/ \   / \   /  _ \</comment>
			<comment>| |   | / \|| |   | |   | / \|</comment>
			<comment>| |_/\| \_/|| |_/\| |_/\| \_/|</comment>
			<comment>\____/\____/\____/\____/\____/</comment>
			<category name="Description">
				<comment>Chain Reaction Mod by Lollo</comment>
				<comment>Changes the percentage chance to reflect per point allocated in Chain Reaction. </comment>
				<comment>Choices of: 8% (default), 9% (45% at 5/5, 99% at 11/5), 20% (100% at 5/5), and 100% (with a single point)</comment>
				<comment>    Note: Values above 100% have no further effect.</comment>
				<comment> </comment>
				<comment>Mod made by me. Feel free to cannabalize it, but please DO NOT REHOST IT! </comment>
				<comment>Thanks :)</comment>
			</category>
			<category name="Chance to Reflect" MUT="true">
				<category name="Default (8% per point)">
					<hotfix name="Chain Reaction Buff" package="GD_Siren_Streaming">
						<code profiles="default">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].AttributeToModify AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="default">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].BaseModifierValue.BaseValueConstant 0.08</code>
						<code profiles="default">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].PerGradeUpgrade.BaseValueConstant 0.08</code>
						<code profiles="default">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Attribute AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="default">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Description Ricochet Chance: $NUMBER$</code>
					</hotfix>
				</category>
				<category name="Slightly Buffed (9% per point)">
					<hotfix name="Chain Reaction Buff" package="GD_Siren_Streaming">
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].AttributeToModify AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].BaseModifierValue.BaseValueConstant 0.09</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].PerGradeUpgrade.BaseValueConstant 0.09</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Attribute AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Description Ricochet Chance: $NUMBER$</code>
					</hotfix>
				</category>
				<category name="Pretty Heckin' Buffed (20% per point)">
					<hotfix name="Chain Reaction Buff" package="GD_Siren_Streaming">
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].AttributeToModify AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].BaseModifierValue.BaseValueConstant 0.20</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].PerGradeUpgrade.BaseValueConstant 0.20</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Attribute AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Description Ricochet Chance: $NUMBER$</code>
					</hotfix>
				</category>
				<category name="SUPER BUFFED (100% per point)">
					<hotfix name="Chain Reaction Buff" package="GD_Siren_Streaming">
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].AttributeToModify AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].BaseModifierValue.BaseValueConstant 1.00</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction SkillEffectDefinitions[0].PerGradeUpgrade.BaseValueConstant 1.00</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Attribute AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'</code>
						<code profiles="">set GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0 Description Ricochet Chance: $NUMBER$</code>
					</hotfix>
				</category>
			</category>
		</category>
	</body>
</BLCMM>

#Commands:

#Direct-Execute Warning:
say WARNING: "Chain Reaction Mod 1.0" must be imported into BLCMM to run properly with UCP or other mods.

#Hotfixes:
set Transient.SparkServiceConfiguration_6 Keys ("SparkLevelPatchEntry-GBX_fixes1","SparkLevelPatchEntry-GBX_fixes2","SparkLevelPatchEntry-GBX_fixes3","SparkLevelPatchEntry-GBX_fixes4","SparkLevelPatchEntry-GBX_fixes5","SparkLevelPatchEntry-GBX_Fixes6","SparkLevelPatchEntry-GBX_Fixes7","SparkLevelPatchEntry-GBX_Fixes8","SparkLevelPatchEntry-GBX_Fixes9","SparkLevelPatchEntry-GBX_fixes10","SparkLevelPatchEntry-GBX_fixes11","SparkLevelPatchEntry-GBX_fixes12","SparkLevelPatchEntry-GBX_fixes13","SparkLevelPatchEntry-GBX_fixes14","SparkOnDemandPatchEntry-GBX_fixes15","SparkOnDemandPatchEntry-GBX_fixes16","SparkOnDemandPatchEntry-GBX_fixes17","SparkOnDemandPatchEntry-GBX_fixes18","SparkOnDemandPatchEntry-GBX_fixes19","SparkPatchEntry-GBX_fixes20","SparkPatchEntry-GBX_fixes21","SparkPatchEntry-GBX_fixes22","SparkPatchEntry-GBX_fixes23","SparkOnDemandPatchEntry-Chain Reaction Buff1","SparkOnDemandPatchEntry-Chain Reaction Buff2","SparkOnDemandPatchEntry-Chain Reaction Buff3","SparkOnDemandPatchEntry-Chain Reaction Buff4","SparkOnDemandPatchEntry-Chain Reaction Buff5")
set Transient.SparkServiceConfiguration_6 Values (",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase1,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.700000,.8",",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase2,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.400000,.5",",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase3,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.200000,.3",",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase4,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.100000,.2",",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase5,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.075000,.1","SouthpawFactory_P,GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1,DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1","SouthpawFactory_P,GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2,DefaultItemPoolList[4].PoolProbability.BaseValueScaleConstant,0.250000,1","SouthpawFactory_P,GD_Population_Psycho.Balance.Unique.PawnBalance_Assassin3,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,0.250000,1","SouthpawFactory_P,GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4,DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1",",GD_Sage_Rare_Scaylion.Population.PawnBalance_Sage_Rare_Scaylion,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100",",GD_Sage_Rare_Drifter.Balance.PawnBalance_Sage_Rare_Drifter,DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100",",GD_Sage_Rare_Rhino.Population.PawnBalance_Sage_Rare_Rhino,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100",",GD_Sage_Rare_Skag.Population.PawnBalance_Sage_Rare_Skag,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100",",GD_Sage_Rare_Spore.Population.PawnBalance_Sage_Rare_Spore,DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100","GD_Assassin_Streaming,GD_Assassin_Skills.Sniping.Velocity,SkillEffectDefinitions[0].ModifierType,MT_PostAdd,MT_Scale","GD_Tulip_Mechro_Streaming,GD_Tulip_Mechromancer_Skills.LittleBigTrouble.WiresDontTalk,SkillEffectDefinitions,,((AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockDamageModifier,bIncludeDuelingTargets=False,bIncludeSelfAsTarget=False,bOnlyEffectTargetsInRange=False,bExcludeNonPlayerCharacters=False,EffectTarget=TARGET_Self,TargetInstanceDataName=,TargetCriteria=CRITERIA_None,ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),GradeToStartApplyingEffect=1,PerGradeUpgradeInterval=1,PerGradeUpgrade=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),BonusUpgradeList=),(AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockStatusDamageModifier,bIncludeDuelingTargets=False,bIncludeSelfAsTarget=False,bOnlyEffectTargetsInRange=False,bExcludeNonPlayerCharacters=False,EffectTarget=TARGET_Self,TargetInstanceDataName=,TargetCriteria=CRITERIA_None,ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),GradeToStartApplyingEffect=1,PerGradeUpgradeInterval=1,PerGradeUpgrade=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),BonusUpgradeList=))","GD_Siren_Streaming,GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2,ValueFormula.Level.InitializationDefinition,AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerMeleeDamage',AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerSkillDamage'","GD_Siren_Streaming,GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2,ValueFormula.Level.BaseValueScaleConstant,1.000000,3.5","GD_Assassin_Streaming,GD_Assassin_Skills.Misc.Att_DeathMark_BonusDamage,BaseValue.BaseValueConstant,0.200000,.8","GD_Itempools.Runnables.Pool_FourAssassins,BalancedItems[1].Probability.InitializationDefinition,None,GD_Balance.Weighting.Weight_1_Common","GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueAttribute,None,D_Attributes.Projectile.ProjectileDamage","GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueScaleConstant,1.000000,.25","GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectChance.BaseValueConstant,1.000000,20","GD_Siren_Streaming,GD_Siren_Skills.Cataclysm.ChainReaction,SkillEffectDefinitions[0].AttributeToModify,,AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'","GD_Siren_Streaming,GD_Siren_Skills.Cataclysm.ChainReaction,SkillEffectDefinitions[0].BaseModifierValue.BaseValueConstant,,0.08","GD_Siren_Streaming,GD_Siren_Skills.Cataclysm.ChainReaction,SkillEffectDefinitions[0].PerGradeUpgrade.BaseValueConstant,,0.08","GD_Siren_Streaming,GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0,Attribute,,AttributeDefinition'D_Attributes.BulletReflection.BulletReflectionOffEnemyChance'","GD_Siren_Streaming,GD_Siren_Skills.Cataclysm.ChainReaction:AttributePresentationDefinition_0,Description,,Ricochet Chance: $NUMBER$")

