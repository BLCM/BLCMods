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

# Python script to generate my TPS Faster Gyrojets mod

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

mod_name = 'TPS Faster Rockets and Gyrojets'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

# Main scaling for Gyrojets
jet_scale = 3

# Main scaling for Rockets
rocket_scale_usual = 3
rocket_scale_vladof = 1.4

# Overrides for some specific gear -- these are all pretty arbitrary, honestly.
ar_scale_boompuppy = 2
rocket_scale_cryophobia = 1.7
rocket_scale_nukem = 1.7
rocket_scale_mongol = 1.7
rocket_scale_volt_thrower = 1.5
shotgun_scale_jackocannon = 1.5
shotgun_scale_tooscoops = 1.5

(TYPE_PROJ, TYPE_FM) = range(2)

modifications = [
    ('ARs', TYPE_PROJ, jet_scale, [
        ('Standard Barrels', [
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Dahl_Grenade', 2300),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_Bandit', 2700),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_Torgue', 3400),
            ('GD_Weap_AssaultRifle.Projectiles.Projectile_Rocket_Vladof', 5000),
            ('GD_Weap_AssaultRifle.FiringModes.Bullets_Assault_Torgue_GyroJet', 1000, jet_scale, TYPE_FM),
            # I feel like these are already fast enough
            #('GD_Weap_AssaultRifle.Projectiles.Projectile_Jakobs_Cannonball', 7000),
            ]),
        ('KerBoom', [
            ('gd_cork_weap_assaultrifle.Projectiles.Projectile_Rocket_KerBoom', 3600),
            # Eh, leave KerBlaster grenades alone
            #('gd_cork_weap_assaultrifle.Projectiles.Projectile_KerBoom_Grenade', 260),
            ]),
        ]),
    ('Pistols', TYPE_FM, jet_scale, [
        ('Standard Barrels', [
            ('GD_Weap_Pistol.FiringModes.Bullets_Pistol_Torgue_GyroJet', 800),
            ]),
        ('88 Fragnum', [
            ('GD_Cork_Weap_Pistol.FiringModes.Bullets_Pistol_Torgue_88Fragnum', 700),
            ]),
        ]),
    ('Rockets', TYPE_PROJ, rocket_scale_usual, [
        ('Standard Barrels', [
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Bandit', 3000),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Maliwan', 3000),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Tediore', 3300),
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Torgue', 2600),
            # Vladof rockets are already quite zippy, don't scale 'em as much
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket_Vladof', 5200, rocket_scale_vladof),
            ('GD_Weap_Launchers.Projectiles.Projectile_TedioreReloadLauncher', 800),
            ]),
        ('Badaboom', [
            ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Bandit_BadaBoom', 2100),
            ]),
        ('Berrigan', [
            ('GD_Petunia_Weapons.Projectiles.Projectile_Menace', 2500),
            ]),
        ('Bunny (not actually in-game, but the variable still exists and is technically referenced by the Tediore RL BPD)', [
            ('GD_Weap_Launchers.Projectiles.Projectile_TedioreReloadLauncher_Bunny', 800),
            ]),
        ('Cryophobia', [
            # Probably don't want full scaling on Pyrophobia, either
            ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Maliwan_Cryophobia', 2100, rocket_scale_cryophobia),
            ]),
        ('Nukem', [
            ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Torgue_Nukem', 2100, rocket_scale_nukem),
            ]),
        ('Mongol', [
            ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Vladof_Mongol', 1200, rocket_scale_mongol),
            ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Vladof_Mongol_Child', 2300),
            ]),
        ('Thingy', [
            ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Bandit_Thingy', 2100),
            ]),
        ('Volt Thrower', [
            # Yep, it really does use this real-generic var which wasn't used for real weapons in BL2.
            ('GD_Weap_Launchers.Projectiles.Projectile_Rocket', 2700, rocket_scale_volt_thrower),
            ]),
        # People probably wouldn't want Creamer sped up...
        #('Creamer', [
        #    ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Creamer', 2500),
        #    ('GD_Cork_Weap_Launchers.Projectiles.Projectile_Rocket_Creamer_Child', 2600),
        #    ]),
        # Speeding up Kaneda's Laser would just be silly.
        #("Kaneda's Laser", [
        #    ('GD_Ma_Weapons.FiringModes.FM_Rocket_Tediore_KanedasLaser', 90000, rocket_scale_usual, TYPE_FM),
        #    ]),
        ]),
    ('Shotguns', TYPE_FM, jet_scale, [
        ('Standard Barrels', [
            ('GD_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_GyroJet', 600),
            ]),
        ("Jack-o'-Cannon", [
            ('GD_Cork_Weap_Shotgun.Projectiles.Projectile_JackOCannon', 2500, shotgun_scale_jackocannon, TYPE_PROJ),
            ]),
        ('Moonface', [
            ('GD_Cork_Weap_Shotgun.FiringModes.Bullet_Shotgun_Moonface', 3200),
            ]),
        ('Moonscaper', [
            ('GD_Cypressure_Weapons.FiringModes.Bullets_Shotgun_Torgue_Landscaper', 260),
            ]),
        ('Too Scoops', [
            ('GD_Cork_Weap_Shotgun.Projectiles.Projectile_TooScoops', 600, shotgun_scale_tooscoops, TYPE_PROJ),
            ]),
        ('Torguemada', [
            ('GD_Cork_Weap_Shotgun.FiringModes.Bullet_Shotgun_Torgemada', 600),
            # Not sure if we should do anything with the child...
            #('GD_Cork_Weap_Shotgun.FiringModes.Bullet_Shotgun_Torgemada_Child', 250),
            ]),
        ('Wombat', [
            ('GD_Cork_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Wombat', 260),
            ]),
        # Flakker isn't really gyrojets anyway, eh?  This first one might
        # take its speed from a projectile rather than a firingmode, too.
        #('Flakker', [
        #    ('GD_Cork_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker', 250),
        #    ('GD_Cork_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker_Child', 1500),
        #    ('GD_Cork_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker_Child_2', 3000),
        #    ('GD_Cork_Weap_Shotgun.FiringModes.Bullets_Shotgun_Torgue_Flakker_Child_3', 4500),
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

mod_str = f"""TPS
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Improves the speed of all gyrojet-based projectiles by {jet_scale}x, which also
    # affects other Torgue-barrel-provided projectiles on ARs, like grenades.
    # Rocket speeds are buffed by {rocket_scale_usual}x, though Vladof RLs only get a
    # much-smaller {rocket_scale_vladof}x.
    #
    # Many Unique/Legendary Torgues also get a buff, though those are generally more
    # slight.  Many have also been left alone, such as the Creamer, Flakker, etc.

    {mod_body}

#</{mod_name}>
"""

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
