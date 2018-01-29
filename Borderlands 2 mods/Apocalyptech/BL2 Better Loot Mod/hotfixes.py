#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# These classes are just for convenience so that I can manage hotfixes
# inside generate-source.py.  While testing, I often don't bother merging
# in my mod using FilterTool, opting instead to just execut it directly
# from the console, so if I want to be doing hotfixes, I've gotta do them
# properly, I've got to make sure to include the Gearbox base hotfixes.
# And of course I'd also like to generate a version which is more suitable
# for FilterTool which *only* includes the "<hotfix>" lines and not the
# Transient.SparkServiceConfiguration_6 stuff at the end.  Anyway, these
# classes let me do that kind of thing pretty easily.

class Hotfix(object):
    """
    Class to hold info about a specific hotfix.  Basically just a glorified
    dict, but whatever.
    """

    def __init__(self, key, value, activated=True):
        self.key = key
        self.value = value
        self.activated = activated

    def get_xml(self):
        """
        Returns an XMLish string suitable for inclusion in a FilterTool-like
        file, for the specified hotfix name.  Note that the FilterTool
        syntax isn't *actually* XML.
        """
        if self.activated:
            active = 'on'
        else:
            active = 'off'
        return '#<hotfix><key>"{key}"</key><value>"{value}"</value><{active}>'.format(
                key=self.key,
                value=self.value,
                active=active,
                )

class Hotfixes(object):
    """
    Basically just a container class to store all of the
    Hotfixes we're interested in, for ease of use
    """

    def __init__(self):
        self.hotfixes = []
        self.hotfix_lookup = {}

        # Add in all the default Gearbox-provided patches by default.  This'll
        # allow us to not worry about polluting the master generation file
        # with this sort of cruft.
        self.add_hotfix('gearbox0', 'SparkLevelPatchEntry-gearbox0',
            ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase1,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.700000,.8')
        self.add_hotfix('gearbox1', 'SparkLevelPatchEntry-gearbox1',
            ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase2,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.400000,.5')
        self.add_hotfix('gearbox2', 'SparkLevelPatchEntry-gearbox2',
            ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase3,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.200000,.3')
        self.add_hotfix('gearbox3', 'SparkLevelPatchEntry-gearbox3',
            ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase4,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.100000,.2')
        self.add_hotfix('gearbox4', 'SparkLevelPatchEntry-gearbox4',
            ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase5,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.075000,.1')
        self.add_hotfix('gearbox5', 'SparkOnDemandPatchEntry-gearbox5',
            "GD_Siren_Streaming,GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2,ValueFormula.Level.InitializationDefinition,AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerMeleeDamage',AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerSkillDamage'")
        self.add_hotfix('gearbox6', 'SparkOnDemandPatchEntry-gearbox6',
            'GD_Siren_Streaming,GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2,ValueFormula.Level.BaseValueScaleConstant,1.000000,3.5')
        self.add_hotfix('gearbox7', 'SparkOnDemandPatchEntry-gearbox7',
            'GD_Assassin_Streaming,GD_Assassin_Skills.Misc.Att_DeathMark_BonusDamage,BaseValue.BaseValueConstant,0.200000,.8')
        self.add_hotfix('gearbox8', 'SparkLevelPatchEntry-gearbox8',
            'SouthpawFactory_P,GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1,DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1')
        self.add_hotfix('gearbox9', 'SparkLevelPatchEntry-gearbox9',
            'SouthpawFactory_P,GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2,DefaultItemPoolList[4].PoolProbability.BaseValueScaleConstant,0.250000,1')
        self.add_hotfix('gearbox10', 'SparkLevelPatchEntry-gearbox10',
            'SouthpawFactory_P,GD_Population_Psycho.Balance.Unique.PawnBalance_Assassin3,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,0.250000,1')
        self.add_hotfix('gearbox11', 'SparkLevelPatchEntry-gearbox11',
            'SouthpawFactory_P,GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4,DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1')
        self.add_hotfix('gearbox12', 'SparkPatchEntry-gearbox12',
            'GD_Itempools.Runnables.Pool_FourAssassins,BalancedItems[1].Probability.InitializationDefinition,None,GD_Balance.Weighting.Weight_1_Common')
        self.add_hotfix('gearbox13', 'SparkLevelPatchEntry-gearbox13',
            ',GD_Sage_Rare_Scaylion.Population.PawnBalance_Sage_Rare_Scaylion,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100')
        self.add_hotfix('gearbox14', 'SparkLevelPatchEntry-gearbox14',
            ',GD_Sage_Rare_Drifter.Balance.PawnBalance_Sage_Rare_Drifter,DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100')
        self.add_hotfix('gearbox15', 'SparkLevelPatchEntry-gearbox15',
            ',GD_Sage_Rare_Rhino.Population.PawnBalance_Sage_Rare_Rhino,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100')
        self.add_hotfix('gearbox16', 'SparkLevelPatchEntry-gearbox16',
            ',GD_Sage_Rare_Skag.Population.PawnBalance_Sage_Rare_Skag,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100')
        self.add_hotfix('gearbox17', 'SparkLevelPatchEntry-gearbox17',
            ',GD_Sage_Rare_Spore.Population.PawnBalance_Sage_Rare_Spore,DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100')
        self.add_hotfix('gearbox18', 'SparkPatchEntry-gearbox18',
            'GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueAttribute,None,D_Attributes.Projectile.ProjectileDamage')
        self.add_hotfix('gearbox19', 'SparkPatchEntry-gearbox19',
            'GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueScaleConstant,1.000000,.25')
        self.add_hotfix('gearbox20', 'SparkPatchEntry-gearbox20',
            'GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectChance.BaseValueConstant,1.000000,20')
        self.add_hotfix('gearbox21', 'SparkOnDemandPatchEntry-gearbox21',
            'GD_Assassin_Streaming,GD_Assassin_Skills.Sniping.Velocity,SkillEffectDefinitions[0].ModifierType,MT_PostAdd,MT_Scale')
        self.add_hotfix('gearbox22', 'SparkOnDemandPatchEntry-gearbox22',
            'GD_Tulip_Mechro_Streaming,GD_Tulip_Mechromancer_Skills.LittleBigTrouble.WiresDontTalk,SkillEffectDefinitions,,((AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockDamageModifier,bIncludeDuelingTargets=False,bIncludeSelfAsTarget=False,bOnlyEffectTargetsInRange=False,bExcludeNonPlayerCharacters=False,EffectTarget=TARGET_Self,TargetInstanceDataName=,TargetCriteria=CRITERIA_None,ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),GradeToStartApplyingEffect=1,PerGradeUpgradeInterval=1,PerGradeUpgrade=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),BonusUpgradeList=),(AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockStatusDamageModifier,bIncludeDuelingTargets=False,bIncludeSelfAsTarget=False,bOnlyEffectTargetsInRange=False,bExcludeNonPlayerCharacters=False,EffectTarget=TARGET_Self,TargetInstanceDataName=,TargetCriteria=CRITERIA_None,ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),GradeToStartApplyingEffect=1,PerGradeUpgradeInterval=1,PerGradeUpgrade=(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),BonusUpgradeList=))')

        self.num_gearbox_patches = len(self.hotfixes)

    def __format__(self, format):
        """
        Convenience function which allows us to use string formatting of
        the sort {hotfixes:hotfixname} in our string templates.
        """
        return self.get_hotfix(format).get_xml()

    def add_hotfix(self, name, key, value, activated=True):
        """
        Adds the specified hotfix.  `name` is a simple name that can be
        used in code to refer to the hotfix in the future.  `key` and
        `value` are the actual key/value for the hotfix.  `activated` is
        a boolean specifying whether the hotfix should be active by default.
        """
        if name in self.hotfix_lookup:
            raise Exception('"{}" already exists as a hotfix'.format(name))
        hotfix = Hotfix(key, value, activated=activated)
        self.hotfix_lookup[name] = hotfix
        self.hotfixes.append(hotfix)

    def get_hotfix(self, name):
        """
        Gets the Hotfix object associated with the given name
        """
        return self.hotfix_lookup[name]

    def get_hotfix_xml(self, name):
        """
        Gets hotfix XML(ish) for the specified hotfix
        """
        return self.get_hotfix(name).get_xml()

    def get_gearbox_hotfix_xml(self, indent='    '):
        """
        Generates an XML stanza to include all our default gearbox patches,
        which can be included at the top of a standalone patch file.
        Optionally pass in `indent` to put some custom line indentation in
        front of each generated line.
        """
        output_lines = []
        output_lines.append('{}#<Original Gearbox hotfix data - Do not uncheck>'.format(indent))
        for gb_patch_num in range(self.num_gearbox_patches):
            hotfix = self.get_hotfix('gearbox{}'.format(gb_patch_num))
            output_lines.append('')
            output_lines.append('{indent}    {xml}'.format(indent=indent, xml=hotfix.get_xml()))
        output_lines.append('')
        output_lines.append('{}#</Original Gearbox hotfix data - Do not uncheck>'.format(indent))
        return "\n".join(output_lines)

    def get_transient_defs(self):
        """
        Returns the Transient.SparkServiceConfiguration_6 text necessary to
        actually activate all of our included hotfixes.
        """
        return_lines = []
        keys = []
        values = []

        # Get all our keys+values that we're adding
        for hotfix in self.hotfixes:
            if hotfix.activated:
                keys.append(hotfix.key)
                values.append(hotfix.value)

        if len(keys) > 0:
            return_lines.append('set Transient.SparkServiceConfiguration_6 Keys ({})'.format(
                ','.join(['"{}"'.format(key) for key in keys])))
            return_lines.append('')
            return_lines.append('set Transient.SparkServiceConfiguration_6 Values ({})'.format(
                ','.join(['"{}"'.format(value) for value in values])))
            return_lines.append('')

        return "\n".join(return_lines)
