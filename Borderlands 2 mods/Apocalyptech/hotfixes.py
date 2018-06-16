#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2018, CJ Kucera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
        self.value = ''.join([l.strip() for l in value.splitlines()]).replace('"', '\\"')
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

    def __init__(self, nameprefix='Apoc', include_gearbox_patches=False, game='bl2'):
        self.nameprefix = nameprefix
        self.hotfixes = []
        self.hotfix_lookup = {}
        self.ids = {}

        if game != 'bl2' and game != 'tps':
            raise Exception('Valid `game` arguments are "bl2" and "tps"')

        # Add in all the default Gearbox-provided patches if we're told to.
        # This'll # allow us to not worry about polluting the master
        # generation file with this sort of cruft.
        if include_gearbox_patches:
            if game == 'bl2':
                self.add_level_hotfix('gearbox0', 'Gearbox',
                    ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase1,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.700000,.8')
                self.add_level_hotfix('gearbox1', 'Gearbox',
                    ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase2,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.400000,.5')
                self.add_level_hotfix('gearbox2', 'Gearbox',
                    ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase3,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.200000,.3')
                self.add_level_hotfix('gearbox3', 'Gearbox',
                    ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase4,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.100000,.2')
                self.add_level_hotfix('gearbox4', 'Gearbox',
                    ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase5,ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant,0.075000,.1')
                self.add_demand_hotfix('gearbox5', 'Gearbox',
                    "GD_Siren_Streaming,GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2,ValueFormula.Level.InitializationDefinition,AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerMeleeDamage',AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerSkillDamage'")
                self.add_demand_hotfix('gearbox6', 'Gearbox',
                    'GD_Siren_Streaming,GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2,ValueFormula.Level.BaseValueScaleConstant,1.000000,3.5')
                self.add_demand_hotfix('gearbox7', 'Gearbox',
                    'GD_Assassin_Streaming,GD_Assassin_Skills.Misc.Att_DeathMark_BonusDamage,BaseValue.BaseValueConstant,0.200000,.8')
                self.add_level_hotfix('gearbox8', 'Gearbox',
                    'SouthpawFactory_P,GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1,DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1')
                self.add_level_hotfix('gearbox9', 'Gearbox',
                    'SouthpawFactory_P,GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2,DefaultItemPoolList[4].PoolProbability.BaseValueScaleConstant,0.250000,1')
                self.add_level_hotfix('gearbox10', 'Gearbox',
                    'SouthpawFactory_P,GD_Population_Psycho.Balance.Unique.PawnBalance_Assassin3,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,0.250000,1')
                self.add_level_hotfix('gearbox11', 'Gearbox',
                    'SouthpawFactory_P,GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4,DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1')
                self.add_reg_hotfix('gearbox12', 'Gearbox',
                    'GD_Itempools.Runnables.Pool_FourAssassins,BalancedItems[1].Probability.InitializationDefinition,None,GD_Balance.Weighting.Weight_1_Common')
                self.add_level_hotfix('gearbox13', 'Gearbox',
                    ',GD_Sage_Rare_Scaylion.Population.PawnBalance_Sage_Rare_Scaylion,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100')
                self.add_level_hotfix('gearbox14', 'Gearbox',
                    ',GD_Sage_Rare_Drifter.Balance.PawnBalance_Sage_Rare_Drifter,DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100')
                self.add_level_hotfix('gearbox15', 'Gearbox',
                    ',GD_Sage_Rare_Rhino.Population.PawnBalance_Sage_Rare_Rhino,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100')
                self.add_level_hotfix('gearbox16', 'Gearbox',
                    ',GD_Sage_Rare_Skag.Population.PawnBalance_Sage_Rare_Skag,DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100')
                self.add_level_hotfix('gearbox17', 'Gearbox',
                    ',GD_Sage_Rare_Spore.Population.PawnBalance_Sage_Rare_Spore,DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100')
                self.add_reg_hotfix('gearbox18', 'Gearbox',
                    'GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueAttribute,None,D_Attributes.Projectile.ProjectileDamage')
                self.add_reg_hotfix('gearbox19', 'Gearbox',
                    'GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueScaleConstant,1.000000,.25')
                self.add_reg_hotfix('gearbox20', 'Gearbox',
                    'GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectChance.BaseValueConstant,1.000000,20')
                self.add_demand_hotfix('gearbox21', 'Gearbox',
                    'GD_Assassin_Streaming,GD_Assassin_Skills.Sniping.Velocity,SkillEffectDefinitions[0].ModifierType,MT_PostAdd,MT_Scale')
                self.add_demand_hotfix('gearbox22', 'Gearbox',
                    """GD_Tulip_Mechro_Streaming,GD_Tulip_Mechromancer_Skills.LittleBigTrouble.WiresDontTalk,SkillEffectDefinitions,,
                    (
                        (
                            AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockDamageModifier,
                            bIncludeDuelingTargets=False,
                            bIncludeSelfAsTarget=False,
                            bOnlyEffectTargetsInRange=False,
                            bExcludeNonPlayerCharacters=False,
                            EffectTarget=TARGET_Self,
                            TargetInstanceDataName=,
                            TargetCriteria=CRITERIA_None,
                            ModifierType=MT_Scale,
                            BaseModifierValue=(
                                BaseValueConstant=0.030000,
                                BaseValueAttribute=None,
                                InitializationDefinition=None,
                                BaseValueScaleConstant=1.000000
                            ),
                            GradeToStartApplyingEffect=1,
                            PerGradeUpgradeInterval=1,
                            PerGradeUpgrade=(
                                BaseValueConstant=0.030000,
                                BaseValueAttribute=None,
                                InitializationDefinition=None,
                                BaseValueScaleConstant=1.000000
                            ),
                            BonusUpgradeList=
                        ),
                        (
                            AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockStatusDamageModifier,
                            bIncludeDuelingTargets=False,
                            bIncludeSelfAsTarget=False,
                            bOnlyEffectTargetsInRange=False,
                            bExcludeNonPlayerCharacters=False,
                            EffectTarget=TARGET_Self,
                            TargetInstanceDataName=,
                            TargetCriteria=CRITERIA_None,
                            ModifierType=MT_Scale,
                            BaseModifierValue=(
                                BaseValueConstant=0.030000,
                                BaseValueAttribute=None,
                                InitializationDefinition=None,
                                BaseValueScaleConstant=1.000000
                            ),
                            GradeToStartApplyingEffect=1,
                            PerGradeUpgradeInterval=1,
                            PerGradeUpgrade=(
                                BaseValueConstant=0.030000,
                                BaseValueAttribute=None,
                                InitializationDefinition=None,
                                BaseValueScaleConstant=1.000000
                            ),
                            BonusUpgradeList=
                        )
                    )""")

            else:
                self.add_demand_hotfix('gearbox0', 'Gearbox',
                    """GD_Gladiator_Streaming,
                    GD_Gladiator_Skills.Projectiles.ShieldProjectile:BehaviorProviderDefinition_0,
                    BehaviorSequences[0].BehaviorData2[26].LinkedVariables.ArrayIndexAndLength,
                    2686977,0""")
                self.add_demand_hotfix('gearbox1', 'Gearbox',
                    """GD_Gladiator_Streaming,
                    GD_Gladiator_Skills.Projectiles.ShieldProjectile:BehaviorProviderDefinition_0,
                    BehaviorSequences[0].BehaviorData2[49].LinkedVariables.ArrayIndexAndLength,
                    8323073,0""")
                self.add_demand_hotfix('gearbox2', 'Gearbox',
                    """GD_Gladiator_Streaming,
                    GD_Gladiator_Skills.Projectiles.ShieldProjectile:BehaviorProviderDefinition_0.OzBehavior_ActorList_1,
                    BehaviorSequences[0].BehaviorData2[32].Behavior.SearchRadius,
                    500.000000,2048""")
                self.add_level_hotfix('gearbox3', 'Gearbox',
                    """Outlands_P,
                    Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionRemoteEvent_0,
                    OutputLinks[0].Links[0].LinkedOp,GearboxSeqAct_TriggerDialogName'Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.GearboxSeqAct_TriggerDialogName_48',
                    Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WillowSeqAct_MissionCustomEvent_14""")
                self.add_level_hotfix('gearbox4', 'Gearbox',
                    """Outlands_P,
                    Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WillowSeqAct_MissionCustomEvent_14,OutputLinks[0].Links,,
                    ((LinkedOp=GearboxSeqAct_TriggerDialogName'Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.GearboxSeqAct_TriggerDialogName_48',
                    InputLinkIdx=0))""")
                self.add_level_hotfix('gearbox5', 'Gearbox',
                    """Outlands_P,
                    Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.GearboxSeqAct_TriggerDialogName_49,
                    OutputLinks[0].Links,,()""")
                self.add_level_hotfix('gearbox6', 'Gearbox',
                    """Outlands_P,
                    Outlands_SideMissions.TheWorld:PersistentLevel.WillowPopulationEncounter_0,Waves[2].MemberOpportunities,,
                    (
                        PopulationOpportunityDen'Outlands_SideMissions.TheWorld:PersistentLevel.PopulationOpportunityDen_2',
                        PopulationOpportunityDen'Outlands_SideMissions.TheWorld:PersistentLevel.PopulationOpportunityDen_8',
                        None
                    )""")
                self.add_reg_hotfix('gearbox7', 'Gearbox',
                    """GD_Ma_Chapter03.M_Ma_Chapter03:ObjSet_Pt0_06_ReopenDataStream,ObjectiveSet.ObjectiveDefinitions,,
                    (
                        GD_Ma_Chapter03.M_Ma_Chapter03:Pt0_06_ReopenDataStream,
                        GD_Ma_Chapter03.M_Ma_Chapter03:Pt0_04_GetToDataStream,
                        GD_Ma_Chapter03.M_Ma_Chapter03:RetrieveHSource
                    )""")
                self.add_reg_hotfix('gearbox8', 'Gearbox',
                    'Weap_Pistol.GestaltDef_Pistol_GestaltSkeletalMesh:SkeletalMeshSocket_260,RelativeLocation,,(X=-0.05,Y=55.0,Z=13.7)')
                self.add_reg_hotfix('gearbox9', 'Gearbox',
                    'Weap_Pistol.GestaltDef_Pistol_GestaltSkeletalMesh:SkeletalMeshSocket_268,RelativeLocation,,(X=0.02,Y=36.0,Z=15.45)')
                self.add_reg_hotfix('gearbox10', 'Gearbox',
                    'Weap_Pistol.GestaltDef_Pistol_GestaltSkeletalMesh:SkeletalMeshSocket_270,RelativeLocation.Z,,14.2')
                self.add_reg_hotfix('gearbox11', 'Gearbox',
                    """GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,
                    BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueAttribute,
                    None,
                    D_Attributes.Projectile.ProjectileDamage""")
                self.add_reg_hotfix('gearbox12', 'Gearbox',
                    """GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,
                    BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueScaleConstant,
                    1.000000,
                    .25""")
                self.add_reg_hotfix('gearbox13', 'Gearbox',
                    """GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140,
                    BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectChance.BaseValueConstant,
                    1.000000,
                    20""")
                self.add_reg_hotfix('gearbox14', 'Gearbox',
                    """GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare,
                    BalancedItems,,
                    +(
                        ItmPoolDefinition=None,
                        InvBalanceDefinition=GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine,
                        Probability=(
                            BaseValueConstant=0,
                            BaseValueAttribute=None,
                            InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon,
                            BaseValueScaleConstant=1
                        ),
                        bDropOnDeath=True
                    )""")
                self.add_reg_hotfix('gearbox15', 'Gearbox',
                    """GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare,
                    BalancedItems,,
                    +(
                        ItmPoolDefinition=None,
                        InvBalanceDefinition=gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful,
                        Probability=(
                            BaseValueConstant=0,
                            BaseValueAttribute=None,
                            InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon,
                            BaseValueScaleConstant=1
                        ),
                        bDropOnDeath=True
                    )""")
                self.add_reg_hotfix('gearbox16', 'Gearbox',
                    """GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare,
                    BalancedItems,,
                    +(
                        ItmPoolDefinition=None,
                        InvBalanceDefinition=GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn,
                        Probability=(
                            BaseValueConstant=0,
                            BaseValueAttribute=None,
                            InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon,
                            BaseValueScaleConstant=1
                        ),
                        bDropOnDeath=True
                    )""")
                self.add_reg_hotfix('gearbox17', 'Gearbox',
                    """GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare,
                    BalancedItems,,
                    +(
                        ItmPoolDefinition=None,
                        InvBalanceDefinition=GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon,
                        Probability=(
                            BaseValueConstant=0,
                            BaseValueAttribute=None,
                            InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon,
                            BaseValueScaleConstant=1
                        ),
                        bDropOnDeath=True
                    )""")
                self.add_level_hotfix('gearbox18', 'Gearbox',
                    """,GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker,
                    PlayThroughs[0].CustomItemPoolList,,
                    +(
                        ItemPool=GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget,
                        PoolProbability=(
                            BaseValueConstant=1.000000,
                            BaseValueAttribute=GD_Itempools.DropWeights.DropODDS_BossUniqueRares,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        )
                    )""")
                self.add_level_hotfix('gearbox19', 'Gearbox',
                    """,GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker,
                    PlayThroughs[1].CustomItemPoolList,,
                    +(
                        ItemPool=GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget,
                        PoolProbability=(
                            BaseValueConstant=1.000000,
                            BaseValueAttribute=GD_Itempools.DropWeights.DropODDS_BossUniqueRares,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        )
                    )""")
                self.add_level_hotfix('gearbox20', 'Gearbox',
                    """Laser_P,
                    GD_Challenges.Co_LevelChallenges.EyeOfHelios_TreadCarefully,
                    ChallengeType,
                    ECT_DesignerTriggered,
                    ECT_LevelObject""")

        self.num_gearbox_patches = len(self.hotfixes)

    def __format__(self, format):
        """
        Convenience function which allows us to use string formatting of
        the sort {hotfixes:hotfixname} in our string templates.
        """
        return self.get_hotfix(format).get_xml()

    def num_hotfixes(self):
        """
        Returns the number of hotfixes we currently have
        """
        return len(self.hotfixes)

    def next_id(self, key):
        """
        Returns the next ID to use for the given key.  Indexes will start
        at zero and increment from there.
        """
        key = key.lower()
        if key in self.ids:
            self.ids[key] += 1
        else:
            self.ids[key] = 0
        return self.ids[key]

    def _add_hotfix(self, name, prefix, key, value, activated=True):
        """
        Adds the specified hotfix.  `name` is a simple name that can be
        used in code to refer to the hotfix in the future.  `prefix` is the
        initial text of the hotfix key, which should always be SparkPatchEntry,
        SparkLevelPatchEntry, or SparkOnDemandPatchEntry, though we don't
        actually check for that.  `key` is the unique identifier for the patch,
        sans numeric suffix.  `value` is the actual value for the hotfix.
        `activated` is a boolean specifying whether the hotfix should be
        active by default.

        The full key for the hotfix will be set to:

            {prefix}-{nameprefix}{key}{x}

        where {nameprefix} is the name prefix for the whole Hotfixes object
        (which defaults to "Apoc"), and {x} is an internally generated counter.
        """
        if name in self.hotfix_lookup:
            raise Exception('"{}" already exists as a hotfix'.format(name))
        hotfix = Hotfix('{}-{}{}{}'.format(prefix, self.nameprefix, key, self.next_id(key)),
                value, activated=activated)
        self.hotfix_lookup[name] = hotfix
        self.hotfixes.append(hotfix)

    def add_reg_hotfix(self, name, key, value, activated=True):
        """
        Adds the specified regular hotfix.  `name` is a simple name
        that can be used in code to refer to the hotfix in the future.
        `key` is the base key for the patch, and `value` is the value
        of the hotfix.  `activated` is a boolean specifying whether
        the hotfix should be active by default.
        """
        self._add_hotfix(name, 'SparkPatchEntry', key, value, activated=activated)

    def add_level_hotfix(self, name, key, value, activated=True):
        """
        Adds the specified level hotfix.  `name` is a simple name
        that can be used in code to refer to the hotfix in the future.
        `key` is the base key for the patch, and `value` is the value
        of the hotfix.  `activated` is a boolean specifying whether the
        hotfix should be active by default.
        """
        self._add_hotfix(name, 'SparkLevelPatchEntry', key, value, activated=activated)

    def add_demand_hotfix(self, name, key, value, activated=True):
        """
        Adds the specified level hotfix.  `name` is a simple name
        that can be used in code to refer to the hotfix in the future.
        `key` is the base key for the patch, and `value` is the value
        of the hotfix.  `activated` is a boolean specifying whether the
        hotfix should be active by default.
        """
        self._add_hotfix(name, 'SparkOnDemandPatchEntry', key, value, activated=activated)

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
        Generates an XMLish stanza to include all our default gearbox patches,
        which can be included at the top of a standalone patch file.
        Optionally pass in `indent` to put some custom line indentation in
        front of each generated line.
        """
        if self.num_gearbox_patches == 0:
            return ''
        else:
            output_lines = []
            output_lines.append('{}#<Original Gearbox hotfix data - Do not uncheck>'.format(indent))
            for gb_patch_num in range(self.num_gearbox_patches):
                hotfix = self.get_hotfix('gearbox{}'.format(gb_patch_num))
                output_lines.append('')
                output_lines.append('{indent}    {xml}'.format(indent=indent, xml=hotfix.get_xml()))
            output_lines.append('')
            output_lines.append('{}#</Original Gearbox hotfix data - Do not uncheck>'.format(indent))
            return "\n".join(output_lines)

    def get_transient_defs(self, offline=False):
        """
        Returns the Transient.SparkServiceConfiguration_6 text necessary to
        actually activate all of our included hotfixes.  Pass `offline=True`
        to generate offline hotfix statements instead.
        """
        return_lines = []
        keys = []
        values = []

        # Offline setup
        if offline:
            return_lines.append('set Transient.SparkServiceConfiguration_0 ServiceName Micropatch')
            return_lines.append('')
            return_lines.append('set Transient.SparkServiceConfiguration_0 ConfigurationGroup Default')
            return_lines.append('')
            spark_num = 0
        else:
            spark_num = 6

        # Get all our keys+values that we're adding
        for hotfix in self.hotfixes:
            if hotfix.activated:
                keys.append(hotfix.key)
                values.append(hotfix.value)

        # Output the hotfix keys/values
        if len(keys) > 0:
            return_lines.append('set Transient.SparkServiceConfiguration_{} Keys ({})'.format(
                spark_num,
                ','.join(['"{}"'.format(key) for key in keys])))
            return_lines.append('')
            return_lines.append('set Transient.SparkServiceConfiguration_{} Values ({})'.format(
                spark_num,
                ','.join(['"{}"'.format(value) for value in values])))
            return_lines.append('')

        # More Offline setup
        if offline:
            return_lines.append('set Transient.GearboxAccountData_1 Services (Transient.SparkServiceConfiguration_0)')
            return_lines.append('')

        return "\n".join(return_lines)
