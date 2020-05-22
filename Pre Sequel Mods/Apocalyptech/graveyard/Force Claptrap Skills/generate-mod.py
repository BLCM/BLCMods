#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

from modprocessor import ModProcessor
mp = ModProcessor()

output_filename='Force Claptrap Skills.blcm'

lines = []
lines.append("""TPS
#<Force Claptrap Skills>

""")

for ws in [
        'Weight_AmmoLow',
        'Weight_BadassPresent',
        'Weight_BossPresent',
        'Weight_Coop',
        'Weight_EnemyPresent',
        'Weight_FFYL',
        'Weight_HealthHigh',
        'Weight_HealthLow',
        'Weight_MeleeEnemy',
        'Weight_ShieldEmpty',
        'Weight_ShieldHigh',
        'Weight_ShieldLow',
        'Weight_ShotEnemy',
        'Weight_Solo',
        'Weight_Subroutine',
        'Weight_ThrewGrenade',
        ]:
    lines.append("""demand GD_Prototype_Streaming set GD_Prototype_Skills_GBX.WeightSkills.{} SkillEffectDefinitions
        (
            ( 
                AttributeToModify=DesignerAttributeDefinition'GD_Prototype_Skills_GBX.Misc.Weights.Att_Weight_MedBot', 
                bIncludeDuelingTargets=False, 
                bIncludeSelfAsTarget=False, 
                bOnlyEffectTargetsInRange=False, 
                bExcludeNonPlayerCharacters=False, 
                EffectTarget=TARGET_Self, 
                TargetInstanceDataName=, 
                TargetCriteria=CRITERIA_None, 
                ModifierType=MT_PreAdd, 
                BaseModifierValue=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=DesignerAttributeDefinition'GD_Prototype_Skills_GBX.Misc.Weights.Att_WeightBonus_Large', 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ), 
                GradeToStartApplyingEffect=1, 
                PerGradeUpgradeInterval=1, 
                PerGradeUpgrade=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ), 
                BonusUpgradeList= 
            ),
            (
                AttributeToModify=DesignerAttributeDefinition'GD_Prototype_Skills_GBX.Misc.Weights.Att_Weight_Sacrifice', 
                bIncludeDuelingTargets=False, 
                bIncludeSelfAsTarget=False, 
                bOnlyEffectTargetsInRange=False, 
                bExcludeNonPlayerCharacters=False, 
                EffectTarget=TARGET_Self, 
                TargetInstanceDataName=, 
                TargetCriteria=CRITERIA_None, 
                ModifierType=MT_PreAdd, 
                BaseModifierValue=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=DesignerAttributeDefinition'GD_Prototype_Skills_GBX.Misc.Weights.Att_WeightBonus_Large', 
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000 
                ), 
                GradeToStartApplyingEffect=1, 
                PerGradeUpgradeInterval=1, 
                PerGradeUpgrade=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ), 
                BonusUpgradeList= 
            )
        )
        """.format(ws))
    lines.append('')

lines.append('#</Force Claptrap Skills>')

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
