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

# Python script to generate my Uranus Mod.

import sys

try:
    from modprocessor import ModProcessor
    mp = ModProcessor()
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink modprocessor.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

###
### Output variables
###

mod_name = 'Uranus'
mod_version = '1.0.0-prerelease'
output_filename = '{}.blcm'.format(mod_name)
scaling = 0.4

###
### Generate hotfixes!
###

# Convenience wrapper
def hotfix(name, classname, attr, value):
    global mp
    mp.register_str(name,
        'level {} set {} {} {}'.format('Stockade_P', classname, attr, value))

hotfix('name',
    'GD_Population_Loader.Balance.Unique.PawnBalance_LoaderGiant',
    'PlayThroughs[0].DisplayName',
    'Uranus')

hotfix('pool',
    'GD_Population_Loader.Balance.Unique.PawnBalance_LoaderGiant',
    'DefaultItemPoolList',
    """(
        (
            ItemPool = ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1',
            PoolProbability = 
            (
                BaseValueConstant = 1.000000,
                BaseValueAttribute = None,
                InitializationDefinition = None,
                BaseValueScaleConstant = 1.000000
            )
        )
    )""")

hotfix('pool_included',
    'GD_Population_Loader.Balance.Unique.PawnBalance_LoaderGiant',
    'DefaultItemPoolIncludedLists',
    '()')

hotfix('attributes',
    'GD_LoaderUltimateBadass.Character.CharClass_LoaderUltimateBadass',
    'AttributeStartingValues',
    """(
        (
            Attribute = AttributeDefinition'GD_Balance_HealthAndDamage.AIParameters.Attribute_HealthMultiplier',
            BaseValue = 
            (
                BaseValueConstant = .000001,
                BaseValueAttribute = None,
                InitializationDefinition = None,
                BaseValueScaleConstant = 1.000000
            )
        ),
        (
            Attribute = AttributeDefinition'GD_Balance_HealthAndDamage.AIParameters.Attribute_EnemyNonWeaponDamageMultiplier',
            BaseValue = 
            (
                BaseValueConstant = 0.000001,
                BaseValueAttribute = None,
                InitializationDefinition = None,
                BaseValueScaleConstant = 1.000000
            )
        ),
        (
            Attribute = AttributeDefinition'GD_Balance_Experience.Attributes.Attribute_ExperienceMultiplier',
            BaseValue = 
            (
                BaseValueConstant = 0.000000,
                BaseValueAttribute = None,
                InitializationDefinition = AttributeInitializationDefinition'GD_AI_Balance.XP.XPMultiplier_01_Chump',
                BaseValueScaleConstant = 1.000000
            )
        ),
        (
            Attribute = AttributeDefinition'D_Attributes.DamageSourceModifiers.ReceivedGrenadeDamageModifier',
            BaseValue = 
            (
                BaseValueConstant = 100.00000,
                BaseValueAttribute = None,
                InitializationDefinition = None,
                BaseValueScaleConstant = 1.000000
            )
        ),
        (
            Attribute = AttributeDefinition'GD_Balance_HealthAndDamage.AIParameters.Attribute_DamageToVehiclesOnCollisionMultiplier',
            BaseValue = 
            (
                BaseValueConstant = 0.000001,
                BaseValueAttribute = None,
                InitializationDefinition = None,
                BaseValueScaleConstant = 1.000000
            )
        )
    )""")

# Don't think this works
hotfix('pitch',
    'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass',
    'DialogReplicatedData.Pitch',
    '5')

# Body scale - either of these seem to work?
hotfix('body_scale',
    'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:SkeletalMeshComponent_1051',
    'Scale',
    round(5*scaling,6))
#hotfix('body_scale',
#    'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass',
#    'DrawScale',
#    round(1*scaling,6))

# "Regular" gun turrets
hotfix('turret_scale',
    'GD_BigLoaderTurret.Character.Pawn_BigLoaderTurret:SkeletalMeshComponent_2220',
    'Scale',
    round(1.5*scaling,6))

# Arms
# 5128 = left arm
# 5130 = right arm
# dunno about the other two.
for (idx, smc) in enumerate([5128, 5129, 5130, 5131]):
    hotfix('arm_scale_{}'.format(idx),
        'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:StaticMeshComponent_{}'.format(smc),
        'Scale',
        round(8*scaling,6))

# Collision Cubes?  No idea what they actually do.
for (idx, smc) in enumerate([5144, 5145]):
    hotfix('collisioncube_scale_{}'.format(idx),
        'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:StaticMeshComponent_{}'.format(smc),
        'Scale',
        round(0.15*scaling,6))

# Shoulder Rocket Pods
# (we don't actually want to scale these; the default scale of 1 seems to make 'em just
# scale along with the main body)
#for (idx, smc) in enumerate([1052, 1053]):
#    hotfix('rocketpod_scale_{}'.format(idx),
#        'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:SkeletalMeshComponent_{}'.format(smc),
#        'Scale',
#        round(1*scaling,6))

# Shoulderpads?  Or something?
# (We don't actually want to scale these, btw - the default scale of 1 seems to make 'em
# scale along with the main body)
#for (idx, smc) in enumerate([5134, 5135, 5138, 5139, 5140, 5141]):
#    hotfix('shoulder_scale_{}'.format(idx),
#        'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:StaticMeshComponent_{}'.format(smc),
#        'Scale',
#        round(1*scaling,6))

# No idea - HyperionBotAttachments.Mesh.HyperionBotAttachments_24 (default 1/2)
for (idx, smc) in enumerate([5136, 5137]):
    hotfix('unknown_24_scale_{}'.format(idx),
        'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:StaticMeshComponent_{}'.format(smc),
        'Scale',
        round(.5*scaling,6))

# No idea - HyperionBotAttachments.Mesh.HyperionBotAttachments_3 (default 1)
for (idx, smc) in enumerate([5132, 5133]):
    hotfix('unknown_3_scale_{}'.format(idx),
        'GD_LoaderUltimateBadass.Character.Pawn_LoaderUltimateBadass:StaticMeshComponent_{}'.format(smc),
        'Scale',
        round(1*scaling,6))

# Does nothing!
hotfix('testing',
    'Char_BattleDroid.Mesh.Skel_BattleDroid:SkeletalMeshSocket_63',
    'RelativeLocation.Z',
    '-170')

###
### Generate the mod string
###

mod_str = """BL2
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Just makes a few balance adjustments to Saturn is all.
    # Shouldn't be such a pushover anymore.

    {mp:name}

    {mp:pool}

    {mp:pool_included}

    {mp:attributes}

    {mp:body_scale}

    {mp:turret_scale}

    {mp:arm_scale_0}

    {mp:arm_scale_1}

    {mp:arm_scale_2}

    {mp:arm_scale_3}

    {mp:collisioncube_scale_0}

    {mp:collisioncube_scale_1}

    {mp:testing}

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        mp=mp,
        )

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
