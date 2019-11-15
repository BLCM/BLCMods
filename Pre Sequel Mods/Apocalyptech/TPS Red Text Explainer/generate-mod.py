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

import sys

try:
    from modprocessor import ModProcessor
    mp = ModProcessor()
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink modprocessor.py')
    print('from Apocalyptech\'s BL2 mods directory, so it exists here as well.')
    print('Sorry for the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

try:
    from ftexplorer.data import Data
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink the')
    print('"ftexplorer" and "resources" dirs from my ft-explorer project so')
    print('they exist here as well.  Sorry for the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

# Control Vars
mod_name = 'TPS Red Text Explainer'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)
explanation_color = '#5ff5ff'
data = Data('TPS')
DESC = 'Description'
NOC = 'NoConstraintText'
valid_attrs = { DESC, NOC }
ON_CARD = 'All effects listed.'

# Item lists
mod_items = [
    ('ARs', NOC, [
        ('KerBoom',
            'gd_cork_weap_assaultrifle.Name.Title_Torgue.Title_Legendary_KerBoom:AttributePresentationDefinition_8',
            'Releases a child grenade on impact.',
            ),
        ('Shredifier',
            'gd_cork_weap_assaultrifle.Name.Title_Vladof.Title_Legendary_Shredifier:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Major Tom',
            'gd_cork_weap_assaultrifle.Name.Title_Dahl.Title_Legendary_MajorTom:AttributePresentationDefinition_8',
            '5-shot burst, 3 bullets at a time for the price of 2.',
            ),
        ('Hammer Buster II',
            'gd_cork_weap_assaultrifle.Name.Title_Jakobs.Title_Legendary_HammerBreaker:AttributePresentationDefinition_8',
            'Penetrating rounds.',
            ),
        ('Fusillade',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_AR_Bandit_5_Fusillade:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Wallop',
            'gd_cork_weap_assaultrifle.Name.Title_Jakobs.Title_Unique_Wallop:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Hail',
            'gd_cork_weap_assaultrifle.Name.Title.Title_Unique_Hail:AttributePresentationDefinition_8',
            'Projectiles fly in arc, split in two after awhile.  Player is healed 3% of damage dealt.',
            ),
        ('Ice Scream',
            'gd_cork_weap_assaultrifle.Name.Title.Title_Unique_IceScream:AttributePresentationDefinition_8',
            'No movement loss while aiming down sights.',
            ),
        ("Ol' Painful",
            'gd_cork_weap_assaultrifle.Name.Title_Vladof.Title_Unique_OldPainful:AttributePresentationDefinition_8',
            'Fires laser bolts instead of bullets.',
            ),
        ('Boss Nova',
            'GD_Cypressure_Weapons.Name.Title.Title__Unique_BossNova:AttributePresentationDefinition_8',
            'High projectile speed.  On surface hit, projectiles explode in small nova.',
            ),
        ('Cry Baby',
            'GD_Petunia_Weapons.ManufacturerMaterials.AssaultRifle.Mat_Bandit_3_CryBaby:AttributePresentationDefinition_8',
            'If "Wiggly," slow shots will oscillate up and down.  Otherwise, just slow bullets.',
            )
        ]),
    ('Rocket Launchers', NOC, [
        ('Badaboom',
            'GD_Cork_Weap_Launchers.Name.Title_Legendary_Badaboom:AttributePresentationDefinition_8',
            'Fires six rockets for the cost of one.',
            ),
        ('Cryophobia',
            'GD_Cork_Weap_Launchers.Name.Title_Legendary_Cryophobia:AttributePresentationDefinition_8',
            'Projectiles explode multiple times mid-flight.',
            ),
        ('Nukem',
            'GD_Cork_Weap_Launchers.Name.Title_Torgue.Title_Legendary_Nukem:AttributePresentationDefinition_8',
            'Rockets fly in arc and explode in mushroom cloud.',
            ),
        ('Mongol',
            'GD_Cork_Weap_Launchers.Name.Title_Vladof.Title_Legendary_Mongol:AttributePresentationDefinition_8',
            'Large main rocket occasionally releases smaller rockets along path.  Consumes 2 ammo.',
            ),
        ('Thingy',
            'GD_Cork_Weap_Launchers.Name.Title_Legendary_Thingy:AttributePresentationDefinition_8',
            'On impact, splits into three homing corrosive grenades.',
            ),
        ("Kaneda's Laser",
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Launcher_Tediore_5_KanedasLaser:AttributePresentationDefinition_8',
            'Fires a fast-travelling laser which can score crits.',
            ),
        ('Berrigan',
            'GD_Petunia_Weapons.Name.Title.Title__Unique_Menace:AttributePresentationDefinition_8',
            'Fires six total rockets in three bursts with single trigger pull, consumes only 1 rocket.',
            ),
        ('Volt Thrower',
            'GD_Cork_Weap_Launchers.Name.Title.Title__Unique_Rocketeer:AttributePresentationDefinition_8',
            'Increased rocket speed, decreased explosion radius.',
            ),
        ('Creamer',
            'GD_Cork_Weap_Launchers.Name.Title__Unique_Creamer:AttributePresentationDefinition_8',
            'Rocket splits into two after a set distance.  Player is healed 2% of damage.',
            ),
        ]),
    ('Pistols', NOC, [
        ('Zim',
            'GD_Cork_Weap_Pistol.Name.Title_Bandit.Title_Legendary_Zim:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Shooterang',
            'GD_Cork_Weap_Pistol.Name.Title_Tediore.Title_Legendary_Shooterang:AttributePresentationDefinition_8',
            'Flies around like a boomerang, bouncing off surfaces and firing continuously.',
            ),
        ('Blowfly',
            'GD_Cork_Weap_Pistol.Name.Title_Dahl.Title_Legendary_Blowfly:AttributePresentationDefinition_8',
            'Projectiles split in two after awhile and orbit each other.  Splash on impact.  7-round burst when zoomed.',
            ),
        ('88 Fragnum',
            'GD_Cork_Weap_Pistol.Name.Title_Torgue.Title_Legendary_88Fragnum:AttributePresentationDefinition_8',
            'Fires 5 bullets at once in accelerating spread, at cost of 3 ammo.',
            ),
        ('Maggie',
            'GD_Cork_Weap_Pistol.Name.Title_Jakobs.Title_Legendary_Maggie:AttributePresentationDefinition_8',
            '6 projectiles for the cost of 1.',
            ),
        ("Logan's Gun",
            'GD_Weap_Pistol.Name.Title_Hyperion.Title_Legendary_LogansGun:AttributePresentationDefinition_8',
            'Rounds explode once on contact then continue until they hit a surface, when they explode again.',
            ),
        ('Luck Cannon',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Pistol_Jakobs_5_LuckCannon:AttributePresentationDefinition_8',
            'Shots have a chance to deal 400% explosive damage.',
            ),
        ('Proletarian Revolution',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Pistol_Vladof_5_Expander:AttributePresentationDefinition_8',
            'Magazine size increases while the gun is not fired.',
            ),
        ("Gwen's Other Head",
            'GD_Cork_Weap_Pistol.Name.Title.Title__Unique_GwensOtherHead:AttributePresentationDefinition_8',
            'Fires second round at an angle to the left, 6-round burst when zoomed.',
            ),
        ('Fibber (remove global red text)',
            'GD_Cork_Weap_Pistol.Name.Title_Hyperion.Title__Unique_Fibber:AttributePresentationDefinition_8',
            '',
            '',
            0,
            ),
        ('Fibber #1',
            'GD_Cork_Weap_Pistol.Barrel.Pistol_Barrel_Bandit_Fibber_1:AttributePresentationDefinition_1',
            'Low-velocity shotgun.',
            '<font color="#DC4646">Would I lie to you?</font>',
            20,
            ),
        ('Fibber #2',
            'GD_Cork_Weap_Pistol.Barrel.Pistol_Barrel_Bandit_Fibber_2:AttributePresentationDefinition_1',
            'Full-speed ricochet on impact or wall hit.',
            '<font color="#DC4646">Would I lie to you?</font>',
            20,
            ),
        ('Fibber #3',
            'GD_Cork_Weap_Pistol.Barrel.Pistol_Barrel_Bandit_Fibber_3:AttributePresentationDefinition_1',
            'Arcing projectiles with 700% crit bonus.',
            '<font color="#DC4646">Would I lie to you?</font>',
            20,
            ),
        ('Globber',
            'GD_Cork_Weap_Pistol.Name.Title.Title__Unique_Globber:AttributePresentationDefinition_8',
            'Projectiles travel in low arc and can bounce twice.',
            ),
        ('Lady Fist',
            'GD_Cork_Weap_Pistol.Name.Title_Hyperion.Title__Unique_LadyFist:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Smasher',
            'GD_Cork_Weap_Pistol.Name.Title_Jakobs.Title_Unique_Smasher:AttributePresentationDefinition_8',
            'Fires 7 bullets in horizontal spread, at cost of 3 ammo.',
            ),
        ('Cyber Eagle',
            'GD_Cork_Weap_Pistol.Name.Title.Title__Unique_CyberColt:AttributePresentationDefinition_8',
            'Shoots bolts of electricity.',
            ),
        ('Party Popper',
            'GD_Ma_Weapons.Name.Title.Title__Unique_Bandit_Pistol_3_PartyPopper:AttributePresentationDefinition_8',
            '7 projectiles at cost of 1 ammo, bullets vanish after a very short distance and release confetti.',
            ),
        ('Hard Reboot',
            'GD_Ma_Weapons.Name.Title.Title__Unique_Maliwan_Pistol_3_HardReboot:AttributePresentationDefinition_8',
            'Wide-radius shock effect on impact.',
            ),
        ('T4s-R',
            'GD_Petunia_Weapons.Name.Title.Title__Unique_T4sr:AttributePresentationDefinition_8',
            'Fires lasers instead of bullets.',
            ),
        ('Probe',
            'GD_Cork_Weap_Pistol.Name.Title.Title__Unique_Moxxis_Probe:AttributePresentationDefinition_8',
            'Heals player at 5% of damage dealt.',
            ),
        ]),
    ('Shotguns', NOC, [
        ("Sledge's Shotty",
            'GD_Weap_Shotgun.Name.Title_Bandit.Title_Legendary_Shotgun:AttributePresentationDefinition_8',
            'Two-shot burst, +1 projectile count.',
            ),
        ('Flakker',
            'GD_Cork_Weap_Shotgun.Name.Title_Torgue.Title_Legendary_Flakker:AttributePresentationDefinition_8',
            'Extremely large spread, rounds detonate after reaching a certain distance.',
            ),
        ('Striker',
            'GD_Cork_Weap_Shotgun.Name.Title_Jakobs.Title_Legendary_Striker:AttributePresentationDefinition_8',
            '50% additive crit bonus and a 15% multiplicative crit bonus.',
            ),
        ('Viral Marketer',
            'GD_Cork_Weap_Shotgun.Name.Title_Hyperion.Title_Legendary_ConferenceCall:AttributePresentationDefinition_8',
            'Fires 5 projectiles per shot. Each projectile generates additional projectiles upon impact or after sufficient distance.',
            ),
        ('Flayer',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_SG_Jakobs_5_Flayer:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Boganella',
            'GD_Cork_Weap_Shotgun.Name.Title__Unique_Boganella:AttributePresentationDefinition_8',
            'Unique voice module',
            ),
        ('Moonface',
            'GD_Cork_Weap_Shotgun.Name.Title.Title__Unique_Moonface:AttributePresentationDefinition_8',
            'Fires in oscillating smiley-face pattern, pellets deal 50% explosive splash on impact.',
            ),
        ('Boomacorn',
            'GD_Cork_Weap_Shotgun.Name.Titles.Title__Unique_Boomacorn:AttributePresentationDefinition_8',
            'Shoots spread of 5 random-elemental projectiles',
            ),
        ('Too Scoops',
            'GD_Cork_Weap_Shotgun.Name.Titles.Title__Unique_TooScoops:AttributePresentationDefinition_8',
            'Fires 2 cryo-element spheres which explode after a certain time.  Higher elemental chance than listed.',
            ),
        ('Bullpup',
            'GD_Cork_Weap_Shotgun.Name.Titles.Title__Unique_Bullpup:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Octo',
            'GD_Cork_Weap_Shotgun.Name.Title.Title__Unique_Octo:AttributePresentationDefinition_8',
            'Fires 10 slow-moving, oscillating pellets in 3x3 grid',
            ),
        ("Jack-o'-Cannon",
            'GD_Cork_Weap_Shotgun.Name.Titles.Title__Unique_JackOCannon:AttributePresentationDefinition_8',
            "Launches flaming jack-o'-lanterns which bounce.  No movement penalty when aiming.",
            ),
        ('Torguemada',
            'GD_Cork_Weap_Shotgun.Name.Titles.Title__Unique_Torgemada:AttributePresentationDefinition_8',
            'Fires 3 explosive projectiles in fixed triangular spread, which also produce smaller, delayed explosions.',
            ),
        ('Wombat',
            'GD_Cork_Weap_Shotgun.Name.Title.Title__Unique_Wombat:AttributePresentationDefinition_8',
            'Fires 5 sticky grenade-like projectiles which explode after 6 seconds or contact with enemy.',
            ),
        ('Company Man',
            'GD_Cypressure_Weapons.Name.Title.Title__Unique_CompanyMan:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Moonscaper',
            'GD_Cypressure_Weapons.Name.Title.Title__Unique_Landscaper2:AttributePresentationDefinition_8',
            'Fires 5 grenades in a square.  If hit on ground, they will rise and then explode.',
            ),
        ('Party Line',
            'GD_Petunia_Weapons.Name.Title.Title__Unique_PartyLine:AttributePresentationDefinition_8',
            'Projectiles explode like fireworks, as does the gun when reloaded.',
            ),
        ('Heart Breaker',
            'GD_Cork_Weap_Shotgun.Name.Title_Hyperion.Title__Unique_HeartBreaker:AttributePresentationDefinition_8',
            'Shoots in heart pattern, restores 2% damage dealt as health.',
            ),
        ]),
    ('SMGs', NOC, [
        ('IVF',
            'GD_Cork_Weap_SMG.Name.Title_Legendary_IVF:AttributePresentationDefinition_8',
            'When reloaded, explodes and spawns 2 smaller guns which deal increased damage and also explode.',
            ),
        ('HellFire',
            'GD_Cork_Weap_SMG.Name.Title_Maliwan.Title_Legendary_HellFire:AttributePresentationDefinition_8',
            '50% elemental splash damage',
            ),
        ('Torrent',
            'GD_Cork_Weap_SMG.Name.Title.Title_Legendary_Dahl_Torrent:AttributePresentationDefinition_8',
            'No movement penalty while aiming, 5-round burst without delay.',
            ),
        ('Fatale',
            'GD_Cork_Weap_SMG.Name.Title_Hyperion.Title_Legendary_Bitch:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Cheat Code',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_SMG_Hyperion_5_CheatCode:AttributePresentationDefinition_8',
            'When in FFYL, has a chance to not consume ammo.',
            ),
        ("Marek's Mouth",
            'GD_Cork_Weap_SMG.Name.Title.Title__Unique_MareksMouth:AttributePresentationDefinition_8',
            'Bullets have a chance to apply an extra random elemental effect.',
            ),
        ('Meat Grinder',
            'GD_Cork_Weap_SMG.Name.Title_Bandit.Title__Unique_MeatGrinder:AttributePresentationDefinition_8',
            'Fires three bullets.',
            ),
        ('Bad Touch',
            'GD_Cork_Weap_SMG.Name.Title_Maliwan.Title__Unique_BadTouch:AttributePresentationDefinition_8',
            'Heals player at 2% of damage done.',
            ),
        ('Good Touch',
            'GD_Cork_Weap_SMG.Name.Title_Maliwan.Title__Unique_GoodTouch:AttributePresentationDefinition_8',
            'Heals player at 2.5% of damage done.',
            ),
        ('Black Snake',
            'GD_Cork_Weap_SMG.Name.Title.Title__Unique_BlackSnake:AttributePresentationDefinition_8',
            '2 bullets per shot in horizontal pattern.',
            ),
        ('Fast Talker',
            'GD_Cypressure_Weapons.Name.Title.Title__Unique_FastTalker:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Boxxy Gunn',
            'GD_Petunia_Weapons.Name.Title.Title__Unique_Boxxy:AttributePresentationDefinition_8',
            'Bullets ricochet twice.  May explode when reloaded, most likely when magazine is fuller.',
            ),
        ('Fridgia',
            'GD_Weap_SMG.Name.Title.Title__Unique_Fridgia:AttributePresentationDefinition_8',
            '2 bullets for the price of 1, fires in the shape of a horse',
            ),
        ('Frostfire',
            'GD_Weap_SMG.Name.Title.Title__Unique_Frostfire:AttributePresentationDefinition_8',
            'Fires 2 projectiles, one cryo and the other incendiary.  May apply cryo to player.',
            ),
        ('Cutie Killer',
            'GD_Ma_Weapons.Name.Title.Title__Unique_SMG_Bandit_6_Glitch_CutieKiller:AttributePresentationDefinition_8',
            'Unique voice module',
            ),
        ]),
    ('Snipers', NOC, [
        ('Pitchfork',
            'GD_Cork_Weap_SniperRifles.Name.Title_Dahl.Title_Legendary_Pitchfork:AttributePresentationDefinition_8',
            'Fires 5 shots in horizontal line.',
            ),
        ('Magma',
            'GD_Cork_Weap_SniperRifles.Name.Title_Maliwan.Title_Legendary_Magma:AttributePresentationDefinition_8',
            'Elemental damage can spread to other enemies in vicinity.',
            ),
        ('Skullmasher',
            'GD_Cork_Weap_SniperRifles.Name.Title_Legendary_Skullmasher:AttributePresentationDefinition_8',
            '6 bullets for the price of 1.',
            ),
        ('Longnail',
            'GD_Cork_Weap_SniperRifles.Name.Title_Vladof.Title_Legendary_Longnail:AttributePresentationDefinition_8',
            'Shots bypass shields.',
            ),
        ('Invader',
            'GD_Cork_Weap_SniperRifles.Name.Title_Hyperion.Title_Legendary_Invader:AttributePresentationDefinition_8',
            '5-round burst when scoped.',
            ),
        ('Omni-Cannon',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Sniper_Hyperion_5_OmniCannon:AttributePresentationDefinition_8',
            'Deals unlisted explosive damage.',
            ),
        ('Wet Week',
            'GD_Cork_Weap_SniperRifles.Name.Title_Dahl.Title__Unique_WetWeek:AttributePresentationDefinition_8',
            'Slow projectile speed.',
            ),
        ('Razorback',
            'GD_Cork_Weap_SniperRifles.Name.Title_Jakobs.Title_Jakobs_Razorback:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Chere-amie',
            'GD_Cork_Weap_SniperRifles.Name.Title_Maliwan.Title__Unique_Chere-amie:AttributePresentationDefinition_8',
            'Transfusion effect, and player is healed 2% of damage while weilding.',
            # BLCMM doesn't write files in latin1/iso-8859-1, so for now we have to avoid "special" chars.  When
            # BLCMM gets fixed, I can get rid of this override...
            'Je suis enchante. Ou est la bibliotheque?',
            ),
        ('Machine',
            'GD_Cork_Weap_SniperRifles.Name.Title_Vladof.Title_Unique_TheMachine:AttributePresentationDefinition_8',
            'Damage and fire rate increase the longer the trigger is held.',
            ),
        ('Plunkett',
            'GD_Petunia_Weapons.Name.Title.Title__Unique_Plunkett:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ("Fremington's Edge",
            'GD_Weap_SniperRifles.Name.Title.Title__Unique_FremingtonsEdge:AttributePresentationDefinition_8',
            'Extremely high zoom factor.',
            ),
        ]),
    ('Lasers', NOC, [
        ('ZX-1',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_ZX1:AttributePresentationDefinition_8',
            'After a target is hit, subsequent shots will corkscrew towards that target.',
            ),
        ('Min Min Lighter',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Legendary_Tesla:AttributePresentationDefinition_8',
            'Shoots slow, bouncy lightning balls with a large AOE.',
            None,
            None,
            DESC,
            ),
        ("Cat o' Nine Tails",
            'GD_Cork_Weap_Lasers.Name.Title.Title__Legendary_Ricochet:AttributePresentationDefinition_8',
            'Beam ricochets and splits into 3-8 beams.',
            ),
        ('Excalibastard',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Legendary_Excalibastard:AttributePresentationDefinition_8',
            'Crits have a 100% freeze.  Meleeing frozen enemies generates a cryo singularity.',
            ),
        ('Longest Yard',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Laser_Hyperion_5_LongestYard:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Absolute Zero',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Laser_Maliwan_5_FusionBeam:AttributePresentationDefinition_8',
            ON_CARD,
            None,
            None,
            DESC,
            ),
        ('Thunderfire',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Laser_Maliwan_5_Thunderfire:AttributePresentationDefinition_8',
            'Beam emits small incendiary nova on hitting enemy or object.',
            ),
        ('Laser Disker',
            'GD_Ma_Weapons.Name.Title.Title__Legendary_Laser_Tediore_5_LaserDisker:AttributePresentationDefinition_8',
            'Fires blue disk in a straight trajectory.  Deals more damage to airborne enemies.',
            ),
        ('Firestarta',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_Firestarta:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Mining Laser',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_Mining:AttributePresentationDefinition_8',
            'Fires 3 railgun-like projectiles in a tight triangle.',
            ),
        ('Freezeasy',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_Freezeasy:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Vibra-Pulse',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_Vibrapulse:AttributePresentationDefinition_8',
            'Has a chance to chain lightning to nearby targets.  Heals for 2.5% of damage dealt.',
            ),
        ('E-GUN',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_EGun:AttributePresentationDefinition_8',
            'No movement penalty while aiming.  Effective against flesh, weak against armor/shields.',
            ),
        ("Ol' Rosie",
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_Rosie:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ('Bright Spadroon',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Unique_SavorySideSaber:AttributePresentationDefinition_8',
            'Extremely short range, lasers shoot to left of crosshair.',
            ),
        ('Vandergraffen',
            'GD_Cork_Weap_Lasers.Name.Title.Title__Deadlift:AttributePresentationDefinition_8',
            ON_CARD,
            ),
        ("Tannis' Laser of Enlightenment",
            'GD_Ma_Weapons.Name.Title.Title__Unique_Maliwan_Laser_3_Enlightenment:AttributePresentationDefinition_8',
            'Short-range flamethrower.',
            ),
        ("MINAC's Atonement",
            'GD_Ma_Weapons.Name.Title.Title__Unique_Maliwan_Laser_3_Minac:AttributePresentationDefinition_8',
            'Randomly selects corrosive, incendiary, or shock for each shot.',
            ),
        ('Heartfull Splodger',
            'GD_Ma_Weapons.Name.Title.Title__Unique_Maliwan_Laser_6_Glitch_HeartfullSplodger:AttributePresentationDefinition_8',
            'Unique voice module.',
            # For some reason our data dump doesn't seem to have the full value in here?  Weird.
            "\\#Splodger'''s ^ere -!",
            ),
        ]),
    ('Grenade Mods', DESC, [
        # NOTE: Monster Trap does not have red text (and you wouldn't want it outside that mission anyway)
        ('Bonus Package',
            'GD_Cork_GrenadeMods.Payload.Payload_BonusPackage:AttributePresentationDefinition_4',
            'When child grenades explode, they release an additional child.',
            ),
        ('Bouncing Bazza',
            'GD_GrenadeMods.Payload.Payload_BouncingBonny:AttributePresentationDefinition_4',
            'Disperses child grenades as it bounces.',
            ),
        ('Fire Bee',
            'GD_GrenadeMods.Title.Title_ExterminatorIncendiary:AttributePresentationDefinition_0',
            'Spits fire in circular motion and shoots small incendiary missiles.',
            ),
        ('Four Seasons',
            'GD_GrenadeMods.Payload.Payload_FourSeasons:AttributePresentationDefinition_0',
            'Creates a random AOE: Shock, Incendiary, Corrosive, or Cryo.',
            ),
        ('Leech',
            'GD_GrenadeMods.Payload.Payload_Leech:AttributePresentationDefinition_4',
            'Decreased blast radius, transfusion effect when dealing damage.',
            ),
        ('Meganade',
            'GD_Ma_GrenadeMods.Delivery.Delivery_Meganade:AttributePresentationDefinition_0',
            'Creates three singularity pulls',
            ),
        ('Nasty Surprise',
            'GD_GrenadeMods.Delivery.Delivery_NastySurprise:AttributePresentationDefinition_4',
            'Longbow delivery, will drop four child grenades enroute or at final destination.',
            ),
        ('Pandemic',
            'GD_GrenadeMods.Title.Title_ExterminatorCorrosive:AttributePresentationDefinition_0',
            'Launches 3 corrosive-DOT homing grenades on explosion.',
            ),
        ('Quasar',
            'GD_Cork_GrenadeMods.Payload.Payload_Quasar:AttributePresentationDefinition_4',
            'Largest singularity grenade, constant shock DOTs.',
            # Have to do an override here thanks to some deficiencies in FT/BLCMM Explorer's data introspection
            'E = mc^(OMG)/wtf',
            ),
        ('Rolling Thunder',
            'GD_GrenadeMods.Delivery.Delivery_RollingThunder:AttributePresentationDefinition_4',
            'Low arc, detonates on each bounce, will eventually explode as a MIRV.',
            ),
        ('Storm Front',
            'GD_GrenadeMods.Title.Title_ExterminatorShock:AttributePresentationDefinition_0',
            'Launches sticky child tesla grenades.',
            ),
        ('Baby Boomer',
            'GD_GrenadeMods.Delivery.Delivery_BabyBoomer:AttributePresentationDefinition_4',
            'Rubberized, spawns child grenades with each bounce',
            ),
        ('Data Scrubber',
            'GD_Ma_GrenadeMods.Delivery.Delivery_DataScrubber:AttributePresentationDefinition_1',
            'Slow travel time, regenerates grenade ammo.',
            ),
        ('Kiss of Death',
            'GD_Cork_GrenadeMods.Payload.Payload_KissOfDeath:AttributePresentationDefinition_4',
            'Grenade homes in and sticks to enemies, dealing DOTs.  Upon explosion, sounds out healing orbs.',
            ),
        ('Snowball',
            'GD_GrenadeMods.Delivery.Delivery_Snowball:AttributePresentationDefinition_4',
            'Fast projectile speed with very little arc.',
            ),
        ('Contraband Sky Rocket',
            'GD_GrenadeMods.Delivery.Delivery_SkyRocket:AttributePresentationDefinition_0',
            'Flies upwards and releases a large burst of fireworks, increased damage.',
            ),
        ]),
    ('Shields', DESC, [
        ('Kala',
            'GD_Shields.Titles.Title_Absorption04_AbsorptionShieldLegendaryShock:AttributePresentationDefinition_0',
            'Shock damage recharges the shield.',
            ),
        ('Sham',
            'GD_Shields.Titles.Title_Absorption04_AbsorptionShieldLegendaryNormal:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Prismatic Bulwark',
            'GD_Shields.Titles.Title_Absorption04_PrismaticBulwark:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Whisky Tango Foxtrot',
            'GD_Shields.Titles.Title_Booster04_BoosterShieldLegendary:AttributePresentationDefinition_0',
            'IED Boosters spawn 3 volleys of shock grenades, can self damage.',
            ),
        ('Reogenator',
            'GD_Shields.Titles.Title_Chimera04_ChimeraShieldLegendary:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Rerouter',
            'GD_Ma_Shields.Titles.Title_Impact_05_Rerouter:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Fabled Tortoise',
            'GD_Shields.Titles.Title_Juggernaut04_JuggernautLegendary:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Black Hole',
            'GD_Shields.Titles.Title_ShockNova02_Singularity:AttributePresentationDefinition_0',
            'Shock nova blast also has a singularity effect.',
            ),
        ('Deadly Bloom',
            'GD_Shields.Titles.Title_ExplosiveNova02_DeadlyBloom:AttributePresentationDefinition_1',
            ON_CARD,
            # Bah, more working around deficiencies in my data processing
            'What do you mean, theoretically?',
            ),
        ('Supernova',
            'GD_Shields.Titles.Title_FireNova03_Supernova:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Bigg Thumppr',
            'GD_Shields.Titles.Title_Roid02_RoidShieldLegendary:AttributePresentationDefinition_0',
            'On recharge, will damage player if roid effect has been used while down.',
            ),
        ('Shooting Star',
            'GD_Shields.Titles.Title_Roid06_ShootingStar:AttributePresentationDefinition_0',
            'While depleted, a "shooting star" is procced which deals extra explosive damage.',
            ),
        ('Avalanche',
            'GD_Shields.Titles.Title_Roid07_Avalanche:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ("Flyin' Maiden",
            'GD_Shields.Titles.Title_CorrosiveSpike02_Legendary:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Cradle',
            'GD_Shields.Titles.Title_Standard05_Legendary:AttributePresentationDefinition_1',
            'Discarded shield releases an explosive nova.',
            ),
        ('Asteroid Belt',
            'GD_Shields.Titles.Title_Booster01_BoosterShieldAsteroidBelt:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Slammer',
            'GD_Shields.Titles.Title_Booster01_BoosterShieldMoxxisSlammer:AttributePresentationDefinition_0',
            'Boosters also restore 25% shields.',
            ),
        ('Haymaker',
            'GD_Shields.Titles.Title_Chimera02_Haymaker:AttributePresentationDefinition_1',
            ON_CARD,
            ),
        ('M0RQ',
            'GD_Ma_Shields.Titles.Title_Chimera_05_M0RQ:AttributePresentationDefinition_1',
            'Unique voice module.',
            ),
        ('Shield of Ages',
            'GD_Ma_Shields.Titles.Title_Juggernaut_03_ShieldOfAges:AttributePresentationDefinition_1',
            ON_CARD,
            ),
        ('Sunshine',
            'GD_Shields.Titles.Title_LaserNova01_Sunshine:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Rapid Release',
            'GD_Cork_Shields.Titles.Title_RapidRelease:AttributePresentationDefinition_0',
            ON_CARD,
            ),
        ('Naught',
            'GD_Ma_Shields.Titles.Title_Naught:AttributePresentationDefinition_0',
            ON_CARD,
            # Have to work around deficiencies in my data library once again
            '5+7+1=Zero',
            ),
        ]),
]

# Construct the mod
lines = []
lines.append('TPS')
lines.append('#<{}>'.format(mod_name))
lines.append('')
lines.append('    # {} v{}'.format(mod_name, mod_version))
lines.append('    # by Apocalyptech')
lines.append('    # Licensed under Public Domain / CC0 1.0 Universal')
lines.append('    # Inspired by Ezeith\'s BL2 mod "Red text explainer"')
lines.append('    #')
lines.append('    # All weapons, grenades, and shields with red text will include text describing')
lines.append('    # the extra effects.  A lot of shields already have all their effects listed on the')
lines.append('    # card, so those will show up as "{}"'.format(ON_CARD))
lines.append('    #')
lines.append('    # Class Mods and Oz Kits have been left alone, since all those list their effects')
lines.append('    # right on the card.')
lines.append('    #')
lines.append('    # Effect descriptions were largely taken from the Fandom wiki, so take them with a')
lines.append('    # grain of salt, and let me know if anything\'s wrong!')
lines.append('')

for (top_cat, attr_name, items) in sorted(mod_items):
    if attr_name not in valid_attrs:
        raise Exception('Invalid attribute specified: {}'.format(attr_name))
    lines.append('#<{}>'.format(top_cat))
    lines.append('')
    for item in sorted(items):
        if len(item) == 6:
            (item_name, obj_name, extra_text, override_text, priority, override_attr) = item
        elif len(item) == 5:
            (item_name, obj_name, extra_text, override_text, priority) = item
            override_attr = attr_name
        elif len(item) == 4:
            (item_name, obj_name, extra_text, override_text) = item
            override_attr = attr_name
            priority = None
        elif len(item) == 3:
            (item_name, obj_name, extra_text) = item
            override_attr = attr_name
            override_text = None
            priority = None
        else:
            raise Exception('Need at least three items: {}'.format(item))
        lines.append('#<{}>'.format(item_name))
        lines.append('')
        if priority is not None:
            lines.append('set {} BasePriority {}'.format(obj_name, priority))
            lines.append('')
        if override_text is None:
            item_struct = data.get_struct_by_full_object(obj_name)
            red_text = item_struct[override_attr]
        else:
            red_text = override_text
        if red_text != '' and extra_text != '':
            lines.append('set {} {} {} <font color="{}">[{}]</font>'.format(
                obj_name,
                override_attr, 
                red_text.replace('(', '[').replace(')', ']'),
                explanation_color,
                extra_text.replace('(', '[').replace(')', ']'),
                ))
            lines.append('')
        lines.append('#</{}>'.format(item_name))
        lines.append('')
    lines.append('#</{}>'.format(top_cat))
    lines.append('')

lines.append('#</{}>'.format(mod_name))
lines.append('')

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
