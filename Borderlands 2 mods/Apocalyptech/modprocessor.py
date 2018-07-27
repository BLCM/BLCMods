#!/usr/bin/env python3
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

import re
import io
import os
import sys
import argparse

# This is a small library to aid in my own Borderlands 2/Pre-Sequel modding.
# FilterTool's file format lent itself very well to using code-assisted
# templates for mod creation, with only some limited text processing required
# to turn a multiline set statement like this:
#
#   set GD_Foo.Bar.Baz BalancedItems
#   (
#       (
#             ItmPoolDefinition=ItemPoolDefinition'GD_Whatever'
#             InvBalanceDefinition=None,
#             Probability=(
#                 BaseValueConstant=1,
#                 BaseValueAttribute=None,
#                 InitializationDefinition=None,
#                 BaseValueScaleConstant=1
#             ),
#             bDropOnDeath=True
#         )
#     )
#
# ... into a nice single-line statement which FT would understand.
#
# BLCMM's native file format, being much closer to "real" XML, is much more
# cumbersome to work with by hand, though, so now I'm using a custom
# intermediate file format which I can then translate into BLCM-format.  It's
# extraordinarily similar to the original FT-style format, with a few differences:
#
#   * The very first line of the file must be "BL2" or "TPS", to specify the type of
#     patch.
#
#   * Hotfixes are specified with one of the following:
#
#       patch set foo bar baz
#       level LevelName set foo bar baz
#       demand Package set foo bar baz
#
#     (This new way of specifying hotfixes is actually a heck of a lot simpler than
#     my previous way of handling them, in fact.)
#
#   * Only Categories support the <off> tag at the end, and anything underneath an
#     <off> Category will always be turned off.
#
#   * Categories marked with <mut> will always have the first option enabled and the
#     rest disabled.
#
#   * Categories can be locked by adding <lock> to the end, as with <off> or <mut>.
#
#   * The off/mut/lock tags are case-insensitive.
#
# This is actually intended to be used programmatically from my various
# generate-mod.py generators, via one of these methods:
#
#   * ModProcessor.human_to_blcm(df, odf)
#   * ModProcessor.human_str_to_blcm(modstring, odf)
#   * ModProcessor.human_str_to_blcm_filename(modstring, output_filename)
#
# They each take two arguments: an input file (or string) and an output file (or
# filename).
#
# You can, however, call this interactively, in which case it will work just
# like my old `conv_to_mod.py` script: it'll expect a ModName-source.txt, and
# output a ModName.blcm in its place.

class ModProcessor(object):

    # GBX Hotfixes
    gbx_hotfixes = {
            'BL2': [
                ('SparkLevelPatchEntry-GBX_fixes1',
                    ",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase1," +
                    "ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant," +
                    "0.700000,.8"),
                ('SparkLevelPatchEntry-GBX_fixes2',
                    ",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase2," +
                    "ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant," +
                    "0.400000,.5"),
                ('SparkLevelPatchEntry-GBX_fixes3',
                    ",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase3," +
                    "ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant," +
                    "0.200000,.3"),
                ('SparkLevelPatchEntry-GBX_fixes4',
                    ",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase4," +
                    "ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant," +
                    "0.100000,.2"),
                ('SparkLevelPatchEntry-GBX_fixes5',
                    ",GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase5," +
                    "ConditionalInitialization.ConditionalExpressionList[4].BaseValueIfTrue.BaseValueConstant," +
                    "0.075000,.1"),
                ('SparkLevelPatchEntry-GBX_Fixes6',
                    "SouthpawFactory_P," +
                    "GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1," +
                    "DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1"),
                ('SparkLevelPatchEntry-GBX_Fixes7',
                    "SouthpawFactory_P," +
                    "GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2," +
                    "DefaultItemPoolList[4].PoolProbability.BaseValueScaleConstant,0.250000,1"),
                ('SparkLevelPatchEntry-GBX_Fixes8',
                    "SouthpawFactory_P," +
                    "GD_Population_Psycho.Balance.Unique.PawnBalance_Assassin3," +
                    "DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,0.250000,1"),
                ('SparkLevelPatchEntry-GBX_Fixes9',
                    "SouthpawFactory_P," +
                    "GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4," +
                    "DefaultItemPoolList[3].PoolProbability.BaseValueScaleConstant,0.250000,1"),
                ('SparkLevelPatchEntry-GBX_fixes10',
                    ",GD_Sage_Rare_Scaylion.Population.PawnBalance_Sage_Rare_Scaylion," +
                    "DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100"),
                ('SparkLevelPatchEntry-GBX_fixes11',
                    ",GD_Sage_Rare_Drifter.Balance.PawnBalance_Sage_Rare_Drifter," +
                    "DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100"),
                ('SparkLevelPatchEntry-GBX_fixes12',
                    ",GD_Sage_Rare_Rhino.Population.PawnBalance_Sage_Rare_Rhino," +
                    "DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100"),
                ('SparkLevelPatchEntry-GBX_fixes13',
                    ",GD_Sage_Rare_Skag.Population.PawnBalance_Sage_Rare_Skag," +
                    "DefaultItemPoolList[1].PoolProbability.BaseValueScaleConstant,1.000000,100"),
                ('SparkLevelPatchEntry-GBX_fixes14',
                    ",GD_Sage_Rare_Spore.Population.PawnBalance_Sage_Rare_Spore," +
                    "DefaultItemPoolList[0].PoolProbability.BaseValueScaleConstant,1.000000,100"),
                ('SparkOnDemandPatchEntry-GBX_fixes15',
                    "GD_Assassin_Streaming,GD_Assassin_Skills.Sniping.Velocity," +
                    "SkillEffectDefinitions[0].ModifierType,MT_PostAdd,MT_Scale"),
                ('SparkOnDemandPatchEntry-GBX_fixes16',
                    "GD_Tulip_Mechro_Streaming," +
                    "GD_Tulip_Mechromancer_Skills.LittleBigTrouble.WiresDontTalk,SkillEffectDefinitions,," +
                    "((AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockDamageModifier," +
                    "bIncludeDuelingTargets=False,bIncludeSelfAsTarget=False,bOnlyEffectTargetsInRange=False," +
                    "bExcludeNonPlayerCharacters=False,EffectTarget=TARGET_Self,TargetInstanceDataName=," +
                    "TargetCriteria=CRITERIA_None,ModifierType=MT_Scale,BaseModifierValue=" +
                    "(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None," +
                    "BaseValueScaleConstant=1.000000),GradeToStartApplyingEffect=1,PerGradeUpgradeInterval=1," +
                    "PerGradeUpgrade=(BaseValueConstant=0.030000,BaseValueAttribute=None," +
                    "InitializationDefinition=None,BaseValueScaleConstant=1.000000),BonusUpgradeList=)," +
                    "(AttributeToModify=D_Attributes.DamageTypeModifers.InstigatedShockStatusDamageModifier," +
                    "bIncludeDuelingTargets=False,bIncludeSelfAsTarget=False,bOnlyEffectTargetsInRange=False," +
                    "bExcludeNonPlayerCharacters=False,EffectTarget=TARGET_Self,TargetInstanceDataName=," +
                    "TargetCriteria=CRITERIA_None,ModifierType=MT_Scale,BaseModifierValue=" +
                    "(BaseValueConstant=0.030000,BaseValueAttribute=None,InitializationDefinition=None," +
                    "BaseValueScaleConstant=1.000000),GradeToStartApplyingEffect=1,PerGradeUpgradeInterval=1," +
                    "PerGradeUpgrade=(BaseValueConstant=0.030000,BaseValueAttribute=None," +
                    "InitializationDefinition=None,BaseValueScaleConstant=1.000000),BonusUpgradeList=))"),
                ('SparkOnDemandPatchEntry-GBX_fixes17',
                    "GD_Siren_Streaming," +
                    "GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2," +
                    "ValueFormula.Level.InitializationDefinition," +
                    "AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerMeleeDamage'," +
                    "AttributeInitializationDefinition'GD_Balance_HealthAndDamage.HealthAndDamage.Init_PlayerSkillDamage'"),
                ('SparkOnDemandPatchEntry-GBX_fixes18',
                    "GD_Siren_Streaming," +
                    "GD_Siren_Skills.Misc.Init_BlightPhoenix_DamageCalc_Part2," +
                    "ValueFormula.Level.BaseValueScaleConstant,1.000000,3.5"),
                ('SparkOnDemandPatchEntry-GBX_fixes19',
                    "GD_Assassin_Streaming," +
                    "GD_Assassin_Skills.Misc.Att_DeathMark_BonusDamage," +
                    "BaseValue.BaseValueConstant,0.200000,.8"),
                ('SparkPatchEntry-GBX_fixes20',
                    "GD_Itempools.Runnables.Pool_FourAssassins,BalancedItems[1].Probability.InitializationDefinition," +
                    "None,GD_Balance.Weighting.Weight_1_Common"),
                ('SparkPatchEntry-GBX_fixes21',
                    "GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140," +
                    "BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueAttribute," +
                    "None,D_Attributes.Projectile.ProjectileDamage"),
                ('SparkPatchEntry-GBX_fixes22',
                    "GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140," +
                    "BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueScaleConstant,1.000000,.25"),
                ('SparkPatchEntry-GBX_fixes23',
                    "GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140," +
                    "BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectChance.BaseValueConstant,1.000000,20"),
                ],
            'TPS': [
                ('SparkOnDemandPatchEntry-GBX_Fixes1',
                    "GD_Gladiator_Streaming," +
                    "GD_Gladiator_Skills.Projectiles.ShieldProjectile:BehaviorProviderDefinition_0," +
                    "BehaviorSequences[0].BehaviorData2[26].LinkedVariables.ArrayIndexAndLength,2686977,0"),
                ('SparkOnDemandPatchEntry-GBX_Fixes2',
                    "GD_Gladiator_Streaming," +
                    "GD_Gladiator_Skills.Projectiles.ShieldProjectile:BehaviorProviderDefinition_0," +
                    "BehaviorSequences[0].BehaviorData2[49].LinkedVariables.ArrayIndexAndLength,8323073,0"),
                ('SparkOnDemandPatchEntry-GBX_Fixes3',
                    "GD_Gladiator_Streaming," +
                    "GD_Gladiator_Skills.Projectiles.ShieldProjectile:BehaviorProviderDefinition_0.OzBehavior_ActorList_1," +
                    "BehaviorSequences[0].BehaviorData2[32].Behavior.SearchRadius,500.000000,2048"),
                ('SparkPatchEntry-GBX_Fixes4',
                    "GD_Ma_Chapter03.M_Ma_Chapter03:Objset_cmp_Pt0_06_ReopenDataStream," +
                    "Objectiveset_cmp.ObjectiveDefinitions,," +
                    "(GD_Ma_Chapter03.M_Ma_Chapter03:Pt0_06_ReopenDataStream," +
                    "GD_Ma_Chapter03.M_Ma_Chapter03:Pt0_04_GetToDataStream,GD_Ma_Chapter03.M_Ma_Chapter03:RetrieveHSource)"),
                ('SparkPatchEntry-GBX_Fixes5',
                    "Weap_Pistol.GestaltDef_Pistol_GestaltSkeletalMesh:SkeletalMeshSocket_260," +
                    "RelativeLocation,,(X=-0.05,Y=55.0,Z=13.7)"),
                ('SparkPatchEntry-GBX_Fixes6',
                    "Weap_Pistol.GestaltDef_Pistol_GestaltSkeletalMesh:SkeletalMeshSocket_268," +
                    "RelativeLocation,,(X=0.02,Y=36.0,Z=15.45)"),
                ('SparkPatchEntry-GBX_Fixes7',
                    "Weap_Pistol.GestaltDef_Pistol_GestaltSkeletalMesh:SkeletalMeshSocket_270," +
                    "RelativeLocation.Z,,14.2"),
                ('SparkPatchEntry-GBX_Fixes8',
                    "GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140," +
                    "BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueAttribute," +
                    "None,D_Attributes.Projectile.ProjectileDamage"),
                ('SparkPatchEntry-GBX_Fixes9',
                    "GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140," +
                    "BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectDamage.BaseValueScaleConstant,1.000000,.25"),
                ('SparkPatchEntry-GBX_Fixes10',
                    "GD_Shields.Projectiles.Proj_LegendaryBoosterShield:BehaviorProviderDefinition_1.Behavior_Explode_140," +
                    "BehaviorSequences[0].BehaviorData2[7].Behavior.StatusEffectChance.BaseValueConstant,1.000000,20"),
                ('SparkPatchEntry-GBX_Fixes11',
                    "GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare,BalancedItems,," +
                    "+(ItmPoolDefinition=None,InvBalanceDefinition=" +
                    "GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine," +
                    "Probability=(BaseValueConstant=0,BaseValueAttribute=None," +
                    "InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon,BaseValueScaleConstant=1)," +
                    "bDropOnDeath=True)"),
                ('SparkPatchEntry-GBX_Fixes12',
                    "GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare,BalancedItems,," +
                    "+(ItmPoolDefinition=None,InvBalanceDefinition=" +
                    "gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful,Probability=" +
                    "(BaseValueConstant=0,BaseValueAttribute=None,InitializationDefinition=" +
                    "GD_Balance.Weighting.Weight_2_Uncommon,BaseValueScaleConstant=1),bDropOnDeath=True)"),
                ('SparkPatchEntry-GBX_Fixes13',
                    "GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare,BalancedItems,," +
                    "+(ItmPoolDefinition=None,InvBalanceDefinition=" +
                    "GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn,Probability=" +
                    "(BaseValueConstant=0,BaseValueAttribute=None," +
                    "InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon," +
                    "BaseValueScaleConstant=1),bDropOnDeath=True)"),
                ('SparkPatchEntry-GBX_Fixes14',
                    "GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare,BalancedItems,," +
                    "+(ItmPoolDefinition=None,InvBalanceDefinition=" +
                    "GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon," +
                    "Probability=(BaseValueConstant=0,BaseValueAttribute=None," +
                    "InitializationDefinition=GD_Balance.Weighting.Weight_2_Uncommon," +
                    "BaseValueScaleConstant=1),bDropOnDeath=True)"),
                ('SparkLevelPatchEntry-GBX_Fixes15',
                    ",GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker," +
                    "PlayThroughs[0].CustomItemPoolList,," +
                    "+(ItemPool=GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget,PoolProbability=" +
                    "(BaseValueConstant=1.000000,BaseValueAttribute=" +
                    "GD_Itempools.DropWeights.DropODDS_BossUniqueRares,InitializationDefinition=None," +
                    "BaseValueScaleConstant=1.000000))"),
                ('SparkLevelPatchEntry-GBX_Fixes16',
                    ",GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker," +
                    "PlayThroughs[1].CustomItemPoolList,," +
                    "+(ItemPool=GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget,PoolProbability=" +
                    "(BaseValueConstant=1.000000,BaseValueAttribute=" +
                    "GD_Itempools.DropWeights.DropODDS_BossUniqueRares,InitializationDefinition=None," +
                    "BaseValueScaleConstant=1.000000))"),
                ('SparkLevelPatchEntry-GBX_Fixes17',
                    "Laser_P,GD_Challenges.Co_LevelChallenges.EyeOfHelios_TreadCarefully," +
                    "ChallengeType,ECT_DesignerTriggered,ECT_LevelObject"),
                ('SparkLevelPatchEntry-GBX_Fixes18',
                    "Outlands_P," +
                    "Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionRemoteEvent_0," +
                    "OutputLinks[0].Links[0].LinkedOp," +
                    "GearboxSeqAct_TriggerDialogName'Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence." +
                    "GearboxSeqAct_TriggerDialogName_48',Outlands_SideMissions.TheWorld:PersistentLevel." +
                    "Main_Sequence.WillowSeqAct_MissionCustomEvent_14"),
                ('SparkLevelPatchEntry-GBX_Fixes19',
                    "Outlands_P," +
                    "Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WillowSeqAct_MissionCustomEvent_14," +
                    "OutputLinks[0].Links,,((LinkedOp=GearboxSeqAct_TriggerDialogName'Outlands_SideMissions.TheWorld:" +
                    "PersistentLevel.Main_Sequence.GearboxSeqAct_TriggerDialogName_48',InputLinkIdx=0))"),
                ('SparkLevelPatchEntry-GBX_Fixes20',
                    "Outlands_P," +
                    "Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.GearboxSeqAct_TriggerDialogName_49," +
                    "OutputLinks[0].Links,,()"),
                ('SparkLevelPatchEntry-GBX_Fixes21',
                    "Outlands_P," +
                    "Outlands_SideMissions.TheWorld:PersistentLevel.WillowPopulationEncounter_0,Waves[2].MemberOpportunities,," +
                    "(PopulationOpportunityDen'Outlands_SideMissions.TheWorld:PersistentLevel.PopulationOpportunityDen_2'," +
                    "PopulationOpportunityDen'Outlands_SideMissions.TheWorld:PersistentLevel.PopulationOpportunityDen_8',None)"),
                ],
        }

    def __init__(self, hotfix_prefix='ApocHotfix'):
        self.hotfix_prefix = hotfix_prefix
        self.set_commands = []
        self.hotfix_commands = []
        self.patch_type = None
        self.mod_name = None
        self.last_hotfix = None
        self.need_to_close_hotfix = False
        self.format_strings = {}

    def line(self, line, odf, indent=0):
        """
        Outputs a line to an output file using the specified indentation
        """
        print('{}{}'.format("\t"*indent, line), file=odf)

    def output_hotfixes(self, odf):
        """
        Outputs our hotfixes in `set Transient` format to the given file
        """
        keys = []
        values = []
        for (key, value) in self.gbx_hotfixes[self.patch_type] + self.hotfix_commands:
            keys.append(key)
            values.append(value)
        self.line('set Transient.SparkServiceConfiguration_6 Keys ({})'.format(
            ','.join(['"{}"'.format(s) for s in keys])
            ), odf)
        self.line('set Transient.SparkServiceConfiguration_6 Values ({})'.format(
            ','.join(['"{}"'.format(s) for s in values])
            ), odf)

    def process_comment(self, comment, odf, indent):
        """
        Processes a comment at the given indent
        """
        self.line('<comment>{}</comment>'.format(comment), odf, indent)

    def get_set_cmd(self, line, df):
        """
        Returns a full `set` command starting with the given line, read from
        the file df.
        """
        set_cmd_parts = [line]
        line = df.readline()
        while line != '':
            stripped = line.strip()
            if stripped == '':
                break
            else:
                if len(set_cmd_parts) == 1 and set_cmd_parts[0][-1] != '(':
                    set_cmd_parts.append(' ')
                set_cmd_parts.append(stripped)
            line = df.readline()
        return ''.join(set_cmd_parts)

    def output_command(self, cmd, odf, indent, active):
        """
        Outputs the specified command to odf, at the given indent and active.
        """

        if active:
            profile_str = 'default'
        else:
            profile_str = ''

        self.line('<code profiles="{}">{}</code>'.format(
            profile_str, cmd), odf, indent)

    def process_set(self, line, df, odf, indent, active):
        """
        Processes the given set command, from the file df, writing to the file
        odf, at the given indent level.
        """

        set_cmd = self.get_set_cmd(line, df)
        if active:
            self.set_commands.append(set_cmd)
        self.output_command(set_cmd, odf, indent, active)

    def close_hotfix(self, new_hotfix, odf, indent):
        """
        Checks to see if we need to close out a hotfix area, given a new
        hotfix type.  Closes the previous hotfix if need be.  Returns
        True if no hotfixes are open once we're done, or False if we can
        remain inside an existing hotfix
        """
        to_ret = True
        if self.need_to_close_hotfix:
            if self.last_hotfix != new_hotfix:
                self.line('</hotfix>', odf, indent)
            else:
                to_ret = False
        self.last_hotfix = new_hotfix
        self.need_to_close_hotfix = False
        return to_ret

    def register_hotfix(self, keytype, value):
        """
        Registers the specified hotfix
        """
        new_id = '{}-{}{}'.format(keytype, self.hotfix_prefix, len(self.hotfix_commands)+1)
        self.hotfix_commands.append((new_id, value.replace('"', '\\"')))

    def process_hf_patch(self, line, df, odf, indent, active):
        """
        Process a patch-style hotfix
        """
        (junk, command) = line.split(' ', 1)
        if self.close_hotfix('patch', odf, indent):
            self.line('<hotfix name="{}">'.format(self.hotfix_prefix), odf, indent)
        set_cmd = self.get_set_cmd(command, df)
        self.output_command(set_cmd, odf, indent+1, active)
        self.need_to_close_hotfix = True
        if active:
            (cmd, object_name, attribute_name, value) = set_cmd.split(' ', 3)
            self.register_hotfix('SparkPatchEntry', '{},{},,{}'.format(
                object_name, attribute_name, value))

    def process_hf_level(self, line, df, odf, indent, active):
        """
        Process a level-style hotfix
        """
        (junk, level, command) = line.split(' ', 2)
        if self.close_hotfix('level {}'.format(level), odf, indent):
            self.line('<hotfix name="{}" level="{}">'.format(self.hotfix_prefix, level), odf, indent)
        set_cmd = self.get_set_cmd(command, df)
        self.output_command(set_cmd, odf, indent+1, active)
        self.need_to_close_hotfix = True
        if active:
            if level == 'None':
                level = ''
            (cmd, object_name, attribute_name, value) = set_cmd.split(' ', 3)
            self.register_hotfix('SparkLevelPatchEntry', '{},{},{},,{}'.format(
                level, object_name, attribute_name, value))

    def process_hf_demand(self, line, df, odf, indent, active):
        """
        Process a demand-style hotfix
        """
        (junk, demand, command) = line.split(' ', 2)
        if self.close_hotfix('demand {}'.format(demand), odf, indent):
            self.line('<hotfix name="{}" package="{}">'.format(self.hotfix_prefix, demand), odf, indent)
        set_cmd = self.get_set_cmd(command, df)
        self.output_command(set_cmd, odf, indent+1, active)
        self.need_to_close_hotfix = True
        if active:
            if demand == 'None':
                demand = ''
            (cmd, object_name, attribute_name, value) = set_cmd.split(' ', 3)
            self.register_hotfix('SparkOnDemandPatchEntry', '{},{},{},,{}'.format(
                demand, object_name, attribute_name, value))

    def process_category(self, line, df, odf, indent, active):
        """
        Processes a category starting with the given line, having been
        read from the file df, writing to odf, at the specified indent
        level.  Pass `active=False` if statements in this category should
        not be active.
        """
        match = re.match('^#<(.*?)>(<off>)?(<mut>)?(<lock>)?$', line, re.I)
        if not match:
            raise Exception('Category format not recognized: {}'.format(line))
        cat_name = match.group(1)
        if self.mod_name is None:
            self.mod_name = cat_name
        cat_enabled = match.group(2) is None
        cat_mut = match.group(3) is not None
        cat_lock = match.group(4) is not None
        if not cat_enabled:
            active = False
        if cat_lock:
            lock_str = ' locked="true"'
        else:
            lock_str = ''
        if cat_mut:
            mut_str = ' MUT="true"'
        else:
            mut_str = ''
        self.line('<category name="{}"{}{}>'.format(cat_name.replace('"', '\\"'), lock_str, mut_str), odf, indent)
        indent += 1

        internal_cat_count = 0
        line = df.readline()
        while line != '':
            stripped = line.strip()
            if stripped == '':
                pass
            elif stripped.startswith('#</'):
                self.close_hotfix(None, odf, indent)
                break
            elif stripped.startswith('#<'):
                self.close_hotfix(None, odf, indent)
                internal_cat_count += 1
                internal_cat_active = active
                if cat_mut and internal_cat_count > 1:
                    internal_cat_active = False
                self.process_category(stripped, df, odf, indent, internal_cat_active)
            elif stripped.startswith('set '):
                self.close_hotfix(None, odf, indent)
                self.process_set(stripped, df, odf, indent, active)
            elif stripped.startswith('patch '):
                self.process_hf_patch(stripped, df, odf, indent, active)
            elif stripped.startswith('level '):
                self.process_hf_level(stripped, df, odf, indent, active)
            elif stripped.startswith('demand '):
                self.process_hf_demand(stripped, df, odf, indent, active)
            else:
                self.close_hotfix(None, odf, indent)
                self.process_comment(stripped, odf, indent)
            line = df.readline()

        indent -= 1
        self.line('</category>', odf, indent)

    def human_to_blcm(self, df, odf):
        """
        Takes a file object containing a human-readable mod, and writes to
        another file object with a version which pretends to have been
        written by BLCMM.
        """
        self.patch_type = df.readline().strip()
        if self.patch_type != 'BL2' and self.patch_type != 'TPS':
            raise Exception('Unknown patch type found: {} (should be BL2 or TPS)'.format(self.patch_type))
        self.line('<BLCMM v="1">', odf)
        self.line('#<!!!You opened a file saved with BLCMM in FilterTool. Please update to BLCMM to properly open this file!!!>', odf)
        self.line('<head>', odf, 1)
        self.line('<type name="{}" offline="false"/>'.format(self.patch_type), odf, 2)
        # Exported mods don't actually include any profiles
        #self.line('<profiles>', odf, 2)
        #self.line('<profile name="default" current="true"/>', odf, 3)
        #self.line('</profiles>', odf, 2)
        self.line('</head>', odf, 1)
        self.line('<body>', odf, 1)

        self.process_category(df.readline().strip(), df, odf, 2, True)

        self.line('</body>', odf, 1)
        self.line('</BLCMM>', odf)

        if len(self.set_commands) > 0:
            self.line('', odf)
            self.line('#Commands:', odf)
            for cmd in self.set_commands:
                self.line(cmd, odf)

        if len(self.hotfix_commands) > 0:
            self.line('', odf)
            self.line('#Direct-Execute Warning:', odf)
            self.line('say WARNING: "{}" must be imported into BLCMM to run properly with UCP or other mods.'.format(self.mod_name), odf)
            self.line('', odf)
            self.line('#Hotfixes:', odf)
            self.output_hotfixes(odf)

        self.line('', odf)

    def human_str_to_blcm(self, modstring, odf):
        """
        Takes a string containing a human-readable mod, and writes to
        a file object with a version which pretends to have been
        written by BLCMM.
        """
        self.human_to_blcm(io.StringIO(modstring), odf)

    def human_str_to_blcm_filename(self, modstring, output_filename):
        """
        Takes a string containing a human-readable mod, and writes to
        a filename with a version which pretends to have been
        written by BLCMM.
        """
        with open(output_filename, 'w') as odf:
            self.human_to_blcm(io.StringIO(modstring), odf)

    def register_str(self, name, line):
        """
        Registers a string with the name `name` which we can then pull in
        later with format strings.
        """
        self.format_strings[name] = line

    def __format__(self, format_str):
        """
        Convenience function which allows us to use string formatting of
        the sort {mp:name} in our string templates, to put arbitrary code-
        generated strings in place without too much fuss.
        """
        return self.format_strings[format_str]

    def get_balanced_items(self, items):
        """
        Returns a string containing a BalancedItems array with the given `items`.
        Each element of the list `items` should be a tuple, the first element
        being the itempool class name, the second being the weight of that
        item, and the third (optional) being an `invbalance` (or None).  If `None`,
        the item will be put into the ItmPoolDefinition attribute - otherwise it
        will be put into the InvBalanceDefinition attribute, with the given
        `invbalance` string as the type of object being linked to (most commonly
        either WeaponBalanceDefinition or InventoryBalanceDefinition).  An
        optional fourth element will be the BaseValueScaleConstant of the item,
        which will default to 1, otherwise.  An optional *fifth* element can be
        specified to determine whether or not the item/pool will be Actually
        Dropped (defaults to `True`).

        This *could* be a staticmethod, but since we're always gonna have a
        ModProcessor object around anyway, who cares.
        """
        bal_items = []
        new_items = []
        for item in items:
            if len(item) == 2:
                new_items.append((item[0], item[1], None, 1, True))
            elif len(item) == 3:
                new_items.append((item[0], item[1], item[2], 1, True))
            elif len(item) == 4:
                new_items.append((item[0], item[1], item[2], item[3], True))
            else:
                new_items.append((item[0], item[1], item[2], item[3], item[4]))
        for (classname, weight, invbalance, scale, item_drop) in new_items:
            if classname:
                if invbalance:
                    itmpool = 'None'
                    invbal = "{}'{}'".format(invbalance, classname)
                else:
                    itmpool = "ItemPoolDefinition'{}'".format(classname)
                    invbal = 'None'
            else:
                itmpool = 'None'
                invbal = 'None'
            if item_drop:
                drop_string = 'True'
            else:
                drop_string = 'False'
            bal_items.append("""(
                    ItmPoolDefinition={},
                    InvBalanceDefinition={},
                    Probability=(
                        BaseValueConstant={},
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={}
                    ),
                    bDropOnDeath={}
                )""".format(itmpool, invbal, weight, round(scale, 6), drop_string))
        return '({})'.format(','.join(bal_items))

    def set_bi_item_pool(self, reg_name, classname, index, item,
            level='None', weight=1, scale=1, invbalance=None):
        """
        Sets an entire BalancedItem structure as a hotfix, and saves it as the
        given `reg_name`.  The class to set is given in `classname`.  The given
        `index` of the BalancedItems structure will be set to `item`.  If
        `invbalance` is not given, it will default to `ItemPoolDefinition`.
        An optional `level` can be specified (will default to `None` otherwise),
        and `weight` and `scale` can be used to specify a weight other than `1`.
        """
        if invbalance:
            itmpool = 'None'
            invbal = "{}'{}'".format(invbalance, item)
        else:
            itmpool = "ItemPoolDefinition'{}'".format(item)
            invbal = 'None'
        self.register_str(reg_name,
                """level {} set {} BalancedItems[{}]
                (
                    ItmPoolDefinition={},
                    InvBalanceDefinition={},
                    Probability=(
                        BaseValueConstant={},
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={}
                    ),
                    bDropOnDeath=True
                )""".format(level, classname, index, itmpool, invbal, weight, scale)
            )

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Converts apocalyptech\'s custom human-editable Borderlands mod files into BLCMM format',
        epilog='The source filename must have a suffix of "-source.txt", and the '
            'destination filename will have the same name minus "-source".  The '
            '"filename" argument can be either the source or destination filename, '
            'and the utility should figure out what to do from there.'
        )
    parser.add_argument('-f', '--force',
        action='store_true',
        help='Force overwriting the destination file')
    parser.add_argument('filename', nargs=1)
    args = parser.parse_args()

    input_file = args.filename[0]
    if input_file[-11:] == '-source.txt':
        source_file = input_file
        dest_file = '{}.blcm'.format(input_file[:-11])
    else:
        source_file = '{}-source.txt'.format(input_file)
        dest_file = '{}.blcm'.format(input_file)
    print('Chosen source filename: {}'.format(source_file))
    print('Chosen destination filename: {}'.format(dest_file))

    # Check to make sure our source file exists
    if not os.path.exists(source_file):
        print('File "{}" does not exist!'.format(source_file))
        sys.exit(1)

    # Ask to overwrite if the dest file exists and we're not forcing
    if os.path.exists(dest_file) and not args.force:
        user_resp = input('File "{}" exists already.  Overwrite it? [y|N] >'.format(dest_file))
        if len(user_resp) > 0 and user_resp[0].lower() == 'y':
            print('Continuing...')
        else:
            print('Exiting!')
            sys.exit(2)

    # Now do the processing
    print('Writing to "{}"'.format(dest_file))
    with open(source_file, 'r') as df:
        with open(dest_file, 'w') as odf:
            mp = ModProcessor()
            mp.human_to_blcm(df, odf)

    # Report that we're done
    print('Done!')
