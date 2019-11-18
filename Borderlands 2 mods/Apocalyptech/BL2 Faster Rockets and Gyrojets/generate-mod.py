#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2019, CJ Kucera
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

# Python script to generate my BL2 Faster Gyrojets mod

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

mod_name = 'BL2 Faster Rockets and Gyrojets'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

# Main scaling for Gyrojets
jet_scale = 3

# Main scaling for Rockets
rocket_scale_usual = 3
rocket_scale_etech = 2
rocket_scale_vladof = 1.4

# Overrides for some specific gear -- these are all pretty arbitrary, honestly.
ar_scale_boompuppy = 2
rocket_scale_norfleet = 1.7
rocket_scale_hive = 1.7
rocket_scale_pyrophobia = 1.7
rocket_scale_nukem = 1.7
rocket_scale_mongol = 1.7
rocket_scale_12pounder = 1.5
rocket_scale_tunguska = 1.7
shotgun_scale_swordsplosion = 1.7
shotgun_scale_carnage = 1.7
# UCP does a 3x buff to Pocket Rocket speed, so what the hell, we'll do that too.
# This actually matches our default scale now, but I'll keep it overridden in case
# I ever walk back the main value
pistol_scale_pocketrocket = 3

(TYPE_PROJ, TYPE_FM) = range(2)

modifications = [
    ('ARs', TYPE_PROJ, jet_scale, [
        ('Standard Barrels', [
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Dahl_Grenade', 2300),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_Bandit', 2700),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_KerBlaster', 3600),
            # Eh, leave KerBlaster grenades alone
            #('GD_Weap_AssaultRifle.Projectiles.Projectile_KerBlaster_Grenade', 260),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_Torgue', 3400),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_Vladof', 5000),
            ('GD_Weap_AssaultRifle.FiringModes.Bullets_Assault_Torgue_GyroJet', 1000, jet_scale, TYPE_FM),
            # I feel like these are already fast enough
            #('GD_Weap_AssaultRifle.Projectiles.Projectile_Jakobs_Cannonball', 7000),
            ]),
        ('Boom Puppy', [
            ('GD_Iris_Weapons.Projectiles.Projectile_Grenade_BoomPuppy', 2300, ar_scale_boompuppy),
            ]),
        ('Seeker', [
            ('GD_Aster_RaidWeapons.AssaultRifles.Projectile_Seeker_Homing', 2000),
            ]),
        ]),
    ('Pistols', TYPE_FM, jet_scale, [
        ('Standard Barrels', [
            ('GD_Weap_Pistol.FiringModes.Bullets_Pistol_Torgue_GyroJet', 800),
            ]),
        ('Pocket Rocket (identical to UCP buff)', [
            ('GD_Iris_Weapons.FiringModes.Bullets_Pistol_Torgue_PocketRocket', 700, pistol_scale_pocketrocket),
            ]),
        # People probably don't want Harold projectiles sped up...
        #('Unkempt Harold', [
        #    ('GD_Weap_Pistol.FiringModes.Bullets_Pistol_Torgue_Calla', 700),
        #    ('GD_Weap_Pistol.FiringModes.Bullets_Pistol_Torgue_CallaChild', 700),
        #    ]),
        ]),
    ('Rockets', TYPE_PROJ, rocket_scale_usual, [
        ('Standard Barrels', [
            # "Vanilla" rocket types
            # This one is actually only used in some level-specific kismet events
            #('GD_Weap_Launchers.Projectiles.Projectile_Rocket', 2700),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Bandit', 3000),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Maliwan', 3000),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Tediore', 3300),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Torgue', 2600),
            # Vladof rockets are already quite zippy, don't scale 'em as much
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Vladof', 5200, rocket_scale_vladof),
            ('GD_Weap_Launchers.Projectiles.Projectile_TedioreReloadLauncher', 800),
            ]),
        ('E-Tech Barrels', [
            ('GD_Weap_Launchers.Projectiles.Projectile_Alien_Bandit_Child', 80, rocket_scale_etech),
            ('GD_Weap_Launchers.Projectiles.Projectile_Alien_Bandit_Plasma', 1800, rocket_scale_etech),
            ('GD_Weap_Launchers.Projectiles.Projectile_Alien_Maliwan_BFG', 2000, rocket_scale_etech),
            ]),
        ('12 Pounder', [
            ('GD_Orchid_BossWeapons.Projectiles.Projectile_12Pounder', 7000, rocket_scale_12pounder),
            ]),
        ('Ahab', [
            ('GD_Orchid_RaidWeapons.RPG.Ahab.Orchid_Seraph_Ahab_Projectile', 2000),
            ]),
        ('Badaboom', [
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Bandit_BadaBoom', 2100),
            ]),
        ('Bunny', [
            ('GD_Weap_Launchers.Projectiles.Projectile_TedioreReloadLauncher_Bunny', 800),
            ]),
        # People probably wouldn't want Creamer sped up...
        #('Creamer', [
        #    ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Creamer', 2500),
        #    ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Creamer_Child', 2600),
        #    ]),
        ('Hive', [
            # I suspect people probably don't want the base hive projectile sped up too much
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Maliwan_Hive', 1500, rocket_scale_hive),
            # Will speed up the Hive's children, though.
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Maliwan_Hive_Child', 600),
            ]),
        ('Mongol', [
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Vladof_Mongol', 1200, rocket_scale_mongol),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Vladof_Mongol_Child', 2300),
            ]),
        ('Norfleet', [
            ('GD_Weap_Launchers.Projectiles.Projectile_Alien_Maliwan_Norfleet', 1500, rocket_scale_norfleet),
            ]),
        ('Nukem', [
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Torgue_Nukem', 2100, rocket_scale_nukem),
            ]),
        ('Pyrophobia', [
            # Probably don't want full scaling on Pyrophobia, either
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Maliwan_Pyrophobia', 2100, rocket_scale_pyrophobia),
            ]),
        ('Tunguska', [
            ('GD_Gladiolus_Weapons.Projectiles.Projectile_Rocket_Torgue_Tunguska', 5000, rocket_scale_tunguska),
            # Tunguska child shouldn't be touched at all; reduces the effectiveness.
            #('GD_Gladiolus_Weapons.Projectiles.Projectile_Rocket_Torgue_Tunguska_Ball', 800, rocket_scale_tunguska),
            ]),
        ]),
    ('Shotguns', TYPE_FM, jet_scale, [
        ('Standard Barrels', [
            ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_GyroJet', 600),
            ]),
        ('Carnage', [
            ('GD_Lobelia_Weapons.Projectiles.Projectile_Rocket_Torgue_Carnage', 4000, shotgun_scale_carnage, TYPE_PROJ),
            ]),
        ('Landscaper', [
            ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Landscaper', 260),
            ]),
        ('Swordsplosion', [
            ('GD_Aster_Weapons.FiringModes.Bullet_Shotgun_Swordsplosion', 2800, shotgun_scale_swordsplosion),
            ]),
        ('Unicornsplosion', [
            ('GD_Anemone_Weapons.Projectiles.Projectile_Swordsplosion', 600, shotgun_scale_swordsplosion, TYPE_PROJ),
            ('GD_Anemone_Weapons.Projectiles.Projectile_Swordsplosion_Child', 600, shotgun_scale_swordsplosion, TYPE_PROJ),
            ]),
        # Flakker isn't really gyrojets anyway, eh?  This first one might
        # take its speed from a projectile rather than a firingmode, too.
        #('Flakker', [
        #    ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker', 250),
        #    ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker_Child', 1500),
        #    ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker_Child_2', 3000),
        #    ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker_Child_3', 4500),
        #    ]),
        ]),
    ]

###
### Generate the mod body
###

lines = []
for (weap_type, default_type, default_scale, guntypes) in modifications:
    lines.append('#<{}>'.format(weap_type))
    lines.append('')
    for (cat_name, projectiles) in guntypes:
        lines.append('#<{}>'.format(cat_name))
        lines.append('')
        for proj in projectiles:
            if len(proj) == 4:
                (obj_name, vanilla_value, override_scale, override_type) = proj
            elif len(proj) == 3:
                (obj_name, vanilla_value, override_scale) = proj
                override_type = default_type
            else:
                (obj_name, vanilla_value) = proj
                override_scale = default_scale
                override_type = default_type
            if override_type == TYPE_PROJ:
                lines.append("""set {} SpeedFormula (
                        BaseValueConstant={:0.6f}, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1 
                    )
                    """.format(obj_name, vanilla_value*override_scale))
            elif override_type == TYPE_FM:
                lines.append('set {} Speed {:0.6f}'.format(obj_name, vanilla_value*override_scale))
                lines.append('')
            else:
                raise Exception('Unknown type: {}'.format(override_type))
        lines.append('#</{}>'.format(cat_name))
        lines.append('')
    lines.append('#</{}>'.format(weap_type))
    lines.append('')
mod_body = "\n".join(lines)

###
### Generate the mod string
###

mod_str = f"""BL2
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Improves the speed of all gyrojet-based projectiles by {jet_scale}x, which also
    # affects other Torgue-barrel-provided projectiles on ARs, like grenades.
    # Rocket speeds are buffed by {rocket_scale_usual}x, though Vladof RLs only get a
    # much-smaller {rocket_scale_vladof}x, and E-Techs only get {rocket_scale_etech}x.
    #
    # Many Unique/Legendary/Seraph/etc Torgues also get a buff, though those
    # are generally more slight.  Many have also been left alone, such as the
    # Unkempt Harold, Creamer, Flakker, etc.

    {mod_body}

#</{mod_name}>
"""

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
