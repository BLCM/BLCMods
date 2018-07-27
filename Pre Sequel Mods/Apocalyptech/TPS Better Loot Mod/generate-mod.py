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

# Python script to generate my TPS Better Loot Mod.  All the drop
# weights and stuff can be controlled by all the variables at the
# top of the file.  Generates a human-readable multiline file which
# must be converted using conv_to_mod.py in order to be loaded by
# Borderlands / FilterTool.

import sys
import math

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

###
### Output variables
###

mod_name = 'TPS Better Loot Mod'
mod_version = '1.1.0'
input_filename = 'input-file-mod.txt'
output_filename = '{}.blcm'.format(mod_name)

###
### Variables which control drop rates and stuff like that
###

class Config(object):
    """
    Base class which allows us to use constants as format strings
    """

    def set_balanced_pct_reports(self, basename, weights, fixedlen=False):
        """
        Given a list of numerical `weights`, sets some attributes in our
        object based on `basename` which describe the percent chances
        of drops.  Var names will be `basename_pct_idx`, where `idx`
        relates to the position of the weight in question in `weights`.
        If `fixedlen` is true, the percentages will be stored as
        right-aligned strings, otherwise it should be numbers.
        """
        total = sum(weights)
        for (idx, weight) in enumerate(weights):
            varname = '{}_pct_{}'.format(basename, idx)
            pct = weight/total*100
            if pct >= 1:
                pct = round(pct)
            elif pct != 0:
                pct = round(pct, 2)
                if str(pct) == '1.0':
                    pct = 1
            if fixedlen:
                if pct == 0 or pct >= 1:
                    setattr(self, varname, '{:4d}'.format(round(pct)))
                else:
                    setattr(self, varname, '{:4.2f}'.format(pct))
            else:
                setattr(self, varname, pct)

    def set_badass_qty_reports(self, basename, quantities):
        """
        This is only really used when reporting likely numbers of drops from
        the various badass enemy definitions.  Will always set fixed-width
        strings.  Will set the vars `badass_basename_idx`.
        """
        for (idx, quantity) in enumerate(quantities):
            varname = 'badass_{}_{}'.format(basename, idx)
            if int(quantity) == quantity:
                setattr(self, varname, '{:4d}'.format(int(quantity)))
            elif round(quantity,1) == quantity:
                setattr(self, varname, '{:4.1f}'.format(quantity))
            else:
                setattr(self, varname, '{:4.2f}'.format(quantity))

    def __format__(self, formatstr):
        """
        A bit of magic so that we can use our values in format strings
        """
        attr = getattr(self, formatstr)
        if type(attr) == str:
            return attr
        elif type(attr) == int or type(attr) == float:
            return str(attr)
        else:
            return attr()

class ConfigBase(Config):
    """
    Class to hold all our weights, and other vars which alter the probabilities of
    various things dropping.  Derive from this class to actually define the
    values.
    """

    # 2x chance of both kinds of moonstone
    moonstone_drop = 0.1          # Stock: 0.050000
    moonstone_cluster_drop = 0.05 # Stock: 0.025000

    # Gun Type drop weights.  Note that because these values are going into
    # our hotfix object, these variables *cannot* be successfully overridden
    # in an extending class.  These probabilities aren't actually too much
    # different than the stock ones.
    drop_prob_pistol = 100
    drop_prob_ar = 100
    drop_prob_smg = 100
    drop_prob_shotgun = 100
    drop_prob_sniper = 80
    drop_prob_launcher = 40
    drop_prob_laser = 80

    def full_profile_name(self):
        if self.profile_name_orig:
            return '{} Quality (formerly "{}")'.format(self.profile_name, self.profile_name_orig)
        else:
            return '{} Quality'.format(self.profile_name)

###
### Config classes which define the actual contstants that we use
### for things like drop weights, etc.
###

class ConfigExcellent(ConfigBase):
    """
    This is our default config, which I personally find quite pleasant.
    Many folks will consider this a bit too OP/Extreme.
    """

    profile_name = 'Excellent'
    profile_name_orig = 'Lootsplosion'
    profile_desc = 'Original "Lootsplosion" presets.  This is the version I prefer.'

    # Custom weapon drop scaling
    weapon_base_common = 8
    weapon_base_uncommon = 85
    weapon_base_rare = 65
    weapon_base_veryrare = 50
    weapon_base_glitch = 8
    weapon_base_legendary = 2

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 8
    weapon_clap_base_uncommon = 85
    weapon_clap_base_rare = 65
    weapon_clap_base_veryrare = 50
    weapon_clap_base_glitch = 16
    weapon_clap_base_legendary = 3

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Custom COM drop scaling (identical to weapons, apart from buffing
    # legendary rates a bit)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = 5

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Drop rates for "regular" treasure chests
    treasure_base_common = 0
    treasure_base_uncommon = 0
    treasure_base_rare = 30
    treasure_base_veryrare = 60
    treasure_base_glitch = 10
    treasure_base_legendary = 4

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 0
    epic_base_rare = 0
    epic_base_veryrare = 1.4
    epic_base_glitch = .6
    epic_base_legendary = 0.2
    epic_base_legendary_dbl = 0.4

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 0
    epic_glitch_base_rare = 0
    epic_glitch_base_veryrare = 0.9
    epic_glitch_base_glitch = 1.1
    epic_glitch_base_legendary_dbl = 0.5

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.4
    badass_pool_glitch = 0.3
    badass_pool_epicchest = 0.1

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.2
    badass_pool_clap_glitch = 0.5
    badass_pool_clap_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 1
    super_badass_pool_glitch = 1
    super_badass_pool_legendary = 1
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0.5
    ultimate_badass_pool_glitch_1 = 1
    ultimate_badass_pool_glitch_2 = 0.5
    ultimate_badass_pool_legendary_1 = 1
    ultimate_badass_pool_legendary_2 = 0.5
    ultimate_badass_pool_legendary_3 = 0.25
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 0.5
    ultimate_badass_pool_epicchest_3 = 0.5

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 1
    ultimate_badass_pool_clap_veryrare_2 = 0.2
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0.8

class ConfigVeryGood(ConfigBase):
    """
    Alternate config for inbetween the former Lootsplosion and Reasonable
    presets.
    """

    profile_name = 'Very Good'
    profile_name_orig = None
    profile_desc = 'Inbetween the former "Lootsplosion" and "Reasonable" presets.'

    # Custom weapon drop scaling
    weapon_base_common = 15
    weapon_base_uncommon = 35
    weapon_base_rare = 25
    weapon_base_veryrare = 10
    weapon_base_glitch = 3
    weapon_base_legendary = .5

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 15
    weapon_clap_base_uncommon = 35
    weapon_clap_base_rare = 25
    weapon_clap_base_veryrare = 10
    weapon_clap_base_glitch = 6
    weapon_clap_base_legendary = .5

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Custom COM drop scaling (identical to weapons, apart from buffing
    # legendary rates a bit)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = .8

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Drop rates for "regular" treasure chests
    treasure_base_common = 20
    treasure_base_uncommon = 40
    treasure_base_rare = 25
    treasure_base_veryrare = 7
    treasure_base_glitch = 7
    treasure_base_legendary = 1

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 15
    epic_base_rare = 45
    epic_base_veryrare = 23
    epic_base_glitch = 15
    epic_base_legendary = 1.8
    epic_base_legendary_dbl = 3.6

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 15
    epic_glitch_base_rare = 45
    epic_glitch_base_veryrare = 23
    epic_glitch_base_glitch = 35
    epic_glitch_base_legendary_dbl = 3.6

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.3
    badass_pool_glitch = 0.22
    badass_pool_epicchest = 0.1

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.15
    badass_pool_clap_glitch = 0.33
    badass_pool_clap_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = .8
    super_badass_pool_glitch = .6
    super_badass_pool_legendary = .1
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0.2
    ultimate_badass_pool_glitch_1 = 1
    ultimate_badass_pool_glitch_2 = 0
    ultimate_badass_pool_legendary_1 = 0.5
    ultimate_badass_pool_legendary_2 = 0.5
    ultimate_badass_pool_legendary_3 = 0
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 0.5
    ultimate_badass_pool_epicchest_3 = 0

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 0.7
    ultimate_badass_pool_clap_veryrare_2 = 0.1
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0.4

class ConfigGood(ConfigBase):
    """
    Alternate config which has slightly-more-reasonable drop rates for stuff
    like legendaries.  Unsurprisingly, most folks find my default values a
    bit excessive.
    """

    profile_name = 'Good'
    profile_name_orig = 'Reasonable'
    profile_desc = 'Original "Reasonable" presets.  Attempts to be somewhat restrained.'

    # Weapon drops
    weapon_base_common = 32.75
    weapon_base_uncommon = 35
    weapon_base_rare = 25
    weapon_base_veryrare = 5
    weapon_base_glitch = 2
    weapon_base_legendary = 0.25

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 32.75
    weapon_clap_base_uncommon = 35
    weapon_clap_base_rare = 25
    weapon_clap_base_veryrare = 4
    weapon_clap_base_glitch = 4
    weapon_clap_base_legendary = 0.25

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Class mods (identical to weapons)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = weapon_base_legendary

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Drop rates for "regular" treasure chests
    treasure_base_common = 32.5
    treasure_base_uncommon = 40
    treasure_base_rare = 20
    treasure_base_veryrare = 5
    treasure_base_glitch = 3
    treasure_base_legendary = 0.5

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 25
    epic_base_rare = 49
    epic_base_veryrare = 20
    epic_base_glitch = 5
    epic_base_legendary = 1
    epic_base_legendary_dbl = 2

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 25
    epic_glitch_base_rare = 49
    epic_glitch_base_veryrare = 10
    epic_glitch_base_glitch = 15
    epic_glitch_base_legendary_dbl = 2

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.2
    badass_pool_glitch = 0.15
    badass_pool_epicchest = 0.1

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.1
    badass_pool_clap_glitch = 0.25
    badass_pool_clap_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 0.4
    super_badass_pool_glitch = 0.15
    super_badass_pool_legendary = .03
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0
    ultimate_badass_pool_glitch_1 = 0.4
    ultimate_badass_pool_glitch_2 = 0
    ultimate_badass_pool_legendary_1 = 0.08
    ultimate_badass_pool_legendary_2 = 0
    ultimate_badass_pool_legendary_3 = 0
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 1
    ultimate_badass_pool_epicchest_3 = 1

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 0.4
    ultimate_badass_pool_clap_veryrare_2 = 0
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0

class ConfigImproved(ConfigBase):
    """
    Alternate config which has improved drop rates for stuff like legendaries.
    Quite anemic to my mind, still, but better than stock.
    """

    profile_name = 'Improved'
    profile_name_orig = None
    profile_desc = 'For anyone who thought that "Reasonable" was still OP but doesn\'t want to go all the way to Stock'

    # Weapon drops
    weapon_base_common = 40
    weapon_base_uncommon = 40
    weapon_base_rare = 5
    weapon_base_veryrare = .5
    weapon_base_glitch = .5
    weapon_base_legendary = 0.1

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 40
    weapon_clap_base_uncommon = 40
    weapon_clap_base_rare = 5
    weapon_clap_base_veryrare = .5
    weapon_clap_base_glitch = 2
    weapon_clap_base_legendary = 0.1

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Class mods (identical to weapons)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = weapon_base_legendary

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Drop rates for "regular" treasure chests
    treasure_base_common = 40
    treasure_base_uncommon = 45
    treasure_base_rare = 10
    treasure_base_veryrare = 2
    treasure_base_glitch = 2
    treasure_base_legendary = 0.15

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 37
    epic_base_rare = 45
    epic_base_veryrare = 10
    epic_base_glitch = 4
    epic_base_legendary = 0.6
    epic_base_legendary_dbl = 1.2

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 37
    epic_glitch_base_rare = 45
    epic_glitch_base_veryrare = 10
    epic_glitch_base_glitch = 12
    epic_glitch_base_legendary_dbl = 1.2

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.2
    badass_pool_glitch = 0.1
    badass_pool_epicchest = 0.05

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.2
    badass_pool_clap_glitch = 0.3
    badass_pool_clap_epicchest = 0.05

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 0.2
    super_badass_pool_glitch = 0.15
    super_badass_pool_legendary = 0.03
    super_badass_pool_epicchest = 0.8

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 0.8
    ultimate_badass_pool_veryrare_2 = 0
    ultimate_badass_pool_glitch_1 = 0.4
    ultimate_badass_pool_glitch_2 = 0
    ultimate_badass_pool_legendary_1 = 0.07
    ultimate_badass_pool_legendary_2 = 0
    ultimate_badass_pool_legendary_3 = 0
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 0.5
    ultimate_badass_pool_epicchest_3 = 0

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 0.8
    ultimate_badass_pool_clap_veryrare_2 = 0
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0.1

class ConfigStock(ConfigBase):
    """
    Alternate config which has roughly stock drop rates for stuff
    like legendaries.  This isn't *actually* stock, and pretends to
    be using a Vault Hunter's Relic, but it probably won't feel too
    off for most players (though of course much of the rest of the
    mod will still be buffing stuff up).
    """

    profile_name = 'Stock-ish'
    profile_name_orig = None
    profile_desc = 'This is not *actually* stock values, but it\'s somewhat close.  Not recommended, but You Do You(tm).'

    # Weapon drops
    weapon_base_common = 75
    weapon_base_uncommon = 10
    weapon_base_rare = 1
    weapon_base_veryrare = .1
    weapon_base_glitch = .1
    weapon_base_legendary = 0.03

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 75
    weapon_clap_base_uncommon = 10
    weapon_clap_base_rare = 1
    weapon_clap_base_veryrare = .1
    weapon_clap_base_glitch = .5
    weapon_clap_base_legendary = 0.03

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Class mods (identical to weapons)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = weapon_base_legendary

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Drop rates for "regular" treasure chests
    treasure_base_common = 5
    treasure_base_uncommon = 6.6
    treasure_base_rare = .35
    treasure_base_veryrare = .05
    treasure_base_glitch = .05
    treasure_base_legendary = 0

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 10
    epic_base_rare = 1
    epic_base_veryrare = .25
    epic_base_glitch = .25
    epic_base_legendary = 0.03
    epic_base_legendary_dbl = 0.06

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 10
    epic_glitch_base_rare = 1
    epic_glitch_base_veryrare = .25
    epic_glitch_base_glitch = 1
    epic_glitch_base_legendary_dbl = 0.06

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.1
    badass_pool_glitch = 0.05
    badass_pool_epicchest = 0

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.1
    badass_pool_clap_glitch = 0.1
    badass_pool_clap_epicchest = 0

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 0.5
    super_badass_pool_veryrare = 0.1
    super_badass_pool_glitch = 0.1
    super_badass_pool_legendary = 0.03
    super_badass_pool_epicchest = 0.5

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 0.5
    ultimate_badass_pool_veryrare_2 = 0
    ultimate_badass_pool_glitch_1 = 0.4
    ultimate_badass_pool_glitch_2 = 0
    ultimate_badass_pool_legendary_1 = 0.06
    ultimate_badass_pool_legendary_2 = 0
    ultimate_badass_pool_legendary_3 = 0
    ultimate_badass_pool_epicchest_1 = 0.5
    ultimate_badass_pool_epicchest_2 = 0.05
    ultimate_badass_pool_epicchest_3 = 0

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 0.5
    ultimate_badass_pool_clap_veryrare_2 = 0
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0

# The profiles we'll generate
profiles = [
    ConfigExcellent(),
    ConfigVeryGood(),
    ConfigGood(),
    ConfigImproved(),
    ConfigStock(),
    ]

class QtyExcellent(Config):
    """
    Excellent drop quantities - bosses will drop as many items as they
    have unique items in their pools.  Formerly this was the "Lootsplosion"
    defaults.
    """

    qty_index = 'excellent'
    qty_label = 'Excellent Drop Quantities (formerly "Lootsplosion")'

    quantity_default_two = 2
    quantity_default_three = 3

    quantity_swagman = 3

    # Note that the Sentinel's drops in the raid version drop twice,
    # which is why we're setting 2 rather than 4 here.
    quantity_sentinel_raid = 2

class QtyImproved(Config):
    """
    Improved drop quantities - bosses with more than one unique item will
    spawn more than one, though not necessarily as many as there are items
    in the pool.
    """

    qty_index = 'improved'
    qty_label = 'Improved Drop Quantities'

    quantity_default_two = 2
    quantity_default_three = 2

    quantity_swagman = 2

    # Note that the Sentinel's drops in the raid version drop twice,
    # which is why we're setting 2 rather than 4 here.
    quantity_sentinel_raid = 1

class QtyStock(Config):
    """
    Stock drop quantities - bosses will only ever drop a single item from
    their unique drop pools.  (This is the same as the game's stock drop
    quantities.
    """

    qty_index = 'stock'
    qty_label = 'Stock Drop Quantities (just one per boss)'

    quantity_default_two = 1
    quantity_default_three = 1

    quantity_swagman = 1

    # Note that the Sentinel's drops in the raid version drop twice,
    # which is why we're setting 2 rather than 4 here.
    quantity_sentinel_raid = 1

###
### Hotfixes; these are handled a little differently than everything
### else.
###

# Remove bias for dropping Pistols in the main game.  Also buffs drop rates
# for snipers, lasers, and launchers, though it does not bring them up to the
# level of pistols/ARs/SMGs/shotguns.  This could be done with a `set`
# statement, but this is more concise.  We don't need to touch the Claptastic
# Voyage pool GD_Ma_ItemPools.WeaponPools.Pool_Weapons_All_Glitch_Marigold
# beacuse that pool already has equal weights for all weapon types.
for (number, rarity) in [
        ('01', 'Common'),
        ('02', 'Uncommon'),
        ('04', 'Rare'),
        ('05', 'VeryRare'),
        ('06', 'Legendary'),
        ]:
    for (idx, (guntype, gunprob)) in enumerate([
            ('Pistol', ConfigBase.drop_prob_pistol),
            ('AR', ConfigBase.drop_prob_ar),
            ('SMG', ConfigBase.drop_prob_smg),
            ('Shotgun', ConfigBase.drop_prob_shotgun),
            ('Sniper', ConfigBase.drop_prob_sniper),
            ('Launcher', ConfigBase.drop_prob_launcher),
            ('Laser', ConfigBase.drop_prob_laser),
            ]):
        mp.register_str('normalize_weapon_types_{}_{}'.format(rarity, guntype),
            'level None set GD_Itempools.WeaponPools.Pool_Weapons_All_{}_{} BalancedItems[{}].Probability.BaseValueConstant {}'.format(
                number,
                rarity,
                idx,
                gunprob))

# Generate statements to ensure that all legendary/unique items will spawn with
# Lunshine (at least, if world Luneshine drops are enabled).
weapons = [
    # Some of these are commented because they have custom Luneshine attachments
    # already, or are glitch guns.  Wanted it to be clear that they were omitted
    # on purpose, which is why they're here but commented.
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom',
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBreaker',
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Torgue_5_KerBoom',
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Jakobs_3_Wallop',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_IceScream',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_Ricochet',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_ZX1',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Old_Hyperion_5_Excalibastard',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Dahl_3_Firestarta',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_VibraPulse',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Egun',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_SavorySideSaber',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_Thingy',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Cryophobia',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
    'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Tediore_3_Rocketeer',
    'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Zim',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_88Fragnum',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Globber',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Smasher',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_CyberColt',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF',
    #'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MareksMouth',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Old_Hyperion_BlackSnake',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Moonface',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_TooScoops',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Torguemada',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Wombat',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma',
    #'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Razorback',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine',
    'GD_Cypressure_Weapons.A_Weapons_Unique.AR_Bandit_3_BossNova',
    'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan',
    'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Torgue_3_Landscaper2',
    'GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker',
    'GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_FusionBeam',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_Thunderfire',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker',
    'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Jakobs_5_LuckCannon',
    'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander',
    'GD_Ma_Weapons.A_Weapons_Legendary.RL_Tediore_5_KanedasLaser',
    'GD_Ma_Weapons.A_Weapons_Legendary.SG_Jakobs_5_Flayer',
    'GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode',
    'GD_Ma_Weapons.A_Weapons_Legendary.Sniper_Old_Hyperion_5_OmniCannon',
    #'GD_Ma_Weapons.A_Weapons_Unique.Laser_Dahl_6_Glitch_HeartfullSplodger',
    'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Enlightenment',
    'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Minac',
    'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper',
    'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot',
    #'GD_Ma_Weapons.A_Weapons_Unique.SMG_Bandit_6_Glitch_CutieKiller',
    #'GD_Petunia_Weapons.AssaultRifles.AR_Bandit_3_CryBaby',
    'GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace',
    'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr',
    'GD_Petunia_Weapons.SMGs.SMG_Tediore_3_Boxxy',
    'GD_Petunia_Weapons.Shotguns.SG_Tediore_3_PartyLine',
    'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett',
    'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
    'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Fridgia',
    'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Frostfire',
    'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
    ]
data = Data('TPS')
guaranteed_luneshine_statements = []
for weapon_name in weapons:
    weapon_struct = data.get_struct_by_full_object(weapon_name)
    runtime_parts = Data.get_struct_attr_obj(weapon_struct, 'RuntimePartListCollection')
    if runtime_parts:
        part_struct = data.get_struct_by_full_object(runtime_parts)
        acc2_parts = part_struct['Accessory2PartData']['WeightedParts']
        if 'Launchers' in weapon_name or 'KanedasLaser' in weapon_name:
            proper_num = 8
        else:
            proper_num = 9
        do_full_create = False
        if len(acc2_parts) == proper_num:
            found_none = False
            found_disabled = False
            for idx, part in enumerate(acc2_parts):
                if part['Part'] == "WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_None'":
                    none_idx = idx
                    found_none = True
                if part['bDisabled'] == 'True':
                    found_disabled = True

            if found_disabled:
                do_full_create = True
            elif found_none:
                guaranteed_luneshine_statements.append(
                    'level None set {} Accessory2PartData.WeightedParts[{}].bDisabled True'.format(
                        runtime_parts, none_idx))
            else:
                raise Exception('{}: No "None" attachment found'.format(weapon_name))
        else:
            do_full_create = True

        # At this point, we could take any `runtime_parts` object with `do_full_create`
        # set to `True`, and set its entire `Accessory2PartData` array to allow
        # luneshine.  This is handled by the Luneshine On Uniques mod, rather
        # than here, because the items created with luneshine would be
        # sanity-checked if the mods aren't loaded and sanity checks aren't
        # disabled, which I don't want to do in this mod.

guaranteed_luneshine = "\n\n".join(['{}{}'.format(' '*(4*5), s) for s in guaranteed_luneshine_statements])

# Fix some container drop pools which reference an item (Pool_BuffDrinks_Euphoria)
# which doesn't actually exist, causing that loot possibility to never actually
# get chosen.  We'll replace with Pool_BuffDrinks_HealingRegen.  Most of these could
# happen via a regular `set` statement, but this lets us be much more concise.
for (idx, (classname, propname, loot_idx, attachment_idx)) in enumerate([
        ('GD_Balance_Treasure.ChestGrades.ObjectGrade_DahlEpic', 'DefaultLoot', 4, 11),
        ('GD_Itempools.ListDefs.EpicChestRedLoot', 'LootData', 4, 11),
        ('GD_Ma_ItemPools.ListDefs.EpicChestRedLoot_Marigold', 'LootData', 4, 11),
        ('GD_Itempools.ListDefs.EpicChestHyperionLoot', 'LootData', 3, 11),
        ('GD_Ma_ItemPools.ListDefs.EpicChestHyperionLoot_Marigold', 'LootData', 3, 11),
        ('GD_Meteorites.Balance.ObjectGrade_Meteorite_LootPile_Chest', 'DefaultLoot', 4, 11),
        ]):
    mp.register_str('euphoria_fix_{}'.format(idx),
        'level None set {} {}[{}].ItemAttachments[{}].ItemPool GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingRegen'.format(
            classname,
            propname,
            loot_idx,
            attachment_idx,
            ))

# Improve Nel's loot
for idx in [15, 16, 17, 18, 19, 20, 21]:
    mp.register_str('nel_drops_{}'.format(idx),
        """level Deadsurface_P set GD_Nel.Population.PawnBalance_Nel DefaultItemPoolList[{}].ItemPool ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear'""".format(idx))

# For the record, the Empyrean Sentinel drops from the various Behavior_SpawnItems_* found
# under GD_FinalBossCorkBig.IOs.IO_LootSpew:BehaviorProviderDefinition_0.  "85" is
# money+moonstone, which I'm ignoring here, but it otherwise drops thusly:
# 
# Non-Raid Drops:
# 
# 2x 81 - GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear
# 1x 84 - GD_Itempools.Runnables.Pool_FinalBoss
#         GD_Itempools.Runnables.Pool_ColZarpedon
#         GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear
# 1x 86 - GD_Itempools.Runnables.Pool_FinalBoss
#         GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear 
#         (+customizations)
# 1x 87 - GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear
# 
# Raid Drops:
# 
# 2x 82 - GD_Itempools.Runnables.Pool_FinalBossRaid
#         (+customizations)
# 1x 83 - GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear
# 1x 88 - GD_Itempools.Runnables.Pool_FinalBossRaid
#         GD_Itempools.Runnables.Pool_ColZarpedon
#         GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear
# 1x 89 - GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear

# Tweaks to EOS/SH4D0W-TP End-DLC Loot Shower.  There's a bunch of spawners at
# GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_*
# which fall into a few categories, which are identical save for the velocities +
# angles which the loot comes out of:
# 
#   144, 148, 150, 154, 156, 158, 160: Money + Moonstones
#   145, 147, 149, 151, 155, 157, 159, 161: One GunsAndGear Drop, 30% chance of purple,
#       40% chance of blue, and 40% chance of green
#   152: One Purple, Two Blues (seemingly only used outside System Shutdown (while farming))
#   153: Legendary (only used during System Shutdown)
#   146: Legendary (only used outside System Shutdown (while farming))
#
# Those pools (at least the main gear pools) can be called more than once, and the actual
# quantity seems to be a bit random (and possibly depends on whether you're in System Shutdown
# or not).  The in-mission drops, based on a small sample size, seem to be reasonably
# consistent, with about 1-3 drops per pool.  Outside of the mission it seems to be a bit more
# volatile (though that could be due to a small sample size), more like 0-4 per pool.  Apart
# from the legendary pools and "152", which only have one drop, as noted above.  Anyway, we're
# getting rid of greens, adding glitches, and adding a bit more money + moonstone.
#
# We're leaving 152 alone, doesn't seem worth the hotfix.  :)

# First up, more money+moonstone:
for num in [144, 148, 150, 154, 156, 158, 160]:
    mp.register_str('eos_drop_{}'.format(num),
        """level Ma_FinalBoss_P set GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            ( 
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster', 
                PoolProbability=( 
                    BaseValueConstant=0.500000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(num))

# Next: improved general gear drops (though we're acutally going to tweak the
# probabilities a bit here, with a net result of a bit less loot)
for num in [145, 147, 149, 151, 155, 157, 159, 161]:
    mp.register_str('eos_drop_{}'.format(num),
        """level Ma_FinalBoss_P set GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare', 
                PoolProbability=( 
                    BaseValueConstant=0.300000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare', 
                PoolProbability=( 
                    BaseValueConstant=0.400000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Ma_ItemPools.WeaponPools.Pool_Weapons_All_Glitch_Marigold', 
                PoolProbability=( 
                    BaseValueConstant=0.200000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(num))

# Change the legendary drops to use our main legendary drop pool rather than
# the "weighted" Marigold one.
for num in [153, 146]:
    mp.register_str('eos_drop_{}'.format(num),
        """level Ma_FinalBoss_P set GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(num))

# Altering probabilities in the mutator arena chests (in the Cortex).  There's
# a set of fun little AttributeInitializationDefinition objects which base
# their weights on the difficulty selected by the user.  The stock percentages
# end up looking like this (in percentages, assuming you have a pool with all
# four probabilities - uncommon, rare, veryrare, legendary):
#
#   Torment level 1: 84, 14, 2, 0.09
#   Torment level 2: 77, 19, 4, 0.1
#   Torment level 3: 65, 27, 8, 0.33
#   Torment level 4: 55, 33, 12, 0.55
#   Torment level 5: 37, 43, 20, 1
#   Torment level 6: 19, 51, 28, 2
#   Torment level 7: 0.15, 53, 44, 4
#   Torment level 8: 0.14, 42, 52, 5
#   Torment level 9: 0.13, 33, 61, 6
#
# We're changing that to look like this instead, using a gaussian function as
# our guide (with some custom tweaks to make the more common rarities fall
# off a little faster than they otherwise would):
#
#   Torment level 1: 79, 19, 2, 0.07
#   Torment level 2: 71, 25, 4, 0.2
#   Torment level 3: 61, 32, 7, 0.54
#   Torment level 4: 33, 50, 15, 2
#   Torment level 5: 23, 51, 23, 4
#   Torment level 6: 17, 37, 36, 10
#   Torment level 7: 0.0, 33, 48, 18
#   Torment level 8: 0.0, 23, 49, 28
#   Torment level 9: 0.0, 15, 47, 38

# All these curve + step parameters I'd just played around with until they
# felt more-or-less "right"
def gauss_at(x):
    peak = 50
    center = 50
    std_dev = 25
    exp = -((x-center)**2)/(2*(std_dev**2))
    return peak*(math.e**exp)
start = 75
interval = 24
step = -10
uncommons = []
rares = []
veryrares = []
legendaries = []
for count in range(9):
    if count >= 6:
        uncommons.append(0)
    elif count >= 3:
        uncommons.append(gauss_at(start)/2)
    else:
        uncommons.append(gauss_at(start))

    if count >= 5:
        rares.append(gauss_at(start+(interval*1))*2/3)
    else:
        rares.append(gauss_at(start+(interval*1)))

    veryrares.append(gauss_at(start+(interval*2)))
    legendaries.append(gauss_at(start+(interval*3)))
    start += step

# Now actually set up those hotfixes
for (label, objname, levels) in [
        ('uncommon', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_2_Uncommon', uncommons),
        ('rare', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_3_Rare', rares),
        ('veryrare', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_4_VeryRare', veryrares),
        ('legendary', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_5_Legendary', legendaries),
        ]:
    for idx, weight in enumerate(levels):
        mp.register_str('mutator_weight_{}_{}'.format(label, idx),
            """level Ma_SubBoss_P set {} ConditionalInitialization.ConditionalExpressionList[{}].BaseValueIfTrue
            (
                BaseValueConstant={},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
            """.format(objname, idx, round(weight, 6)))

# Now some hotfixes to improve the actual mutator loot pools themselves
def mutator_pool(label, obj_name, contents):
    items = []
    for (pool, weight, scale) in contents:
        if weight == 2:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_2_Uncommon'
        elif weight == 3:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_3_Rare'
        elif weight == 4:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_4_VeryRare'
        elif weight == 5:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_5_Legendary'
        else:
            raise Exception('Unknown weight: {}'.format(weight))
        if not scale:
            scale = '1.000000'
        items.append("""( 
                ItmPoolDefinition=ItemPoolDefinition'{}', 
                InvBalanceDefinition=None, 
                Probability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=AttributeInitializationDefinition'{}', 
                    BaseValueScaleConstant={} 
                ), 
                bDropOnDeath=True 
            )""".format(pool, idef, scale))

    mp.register_str('mutator_{}'.format(label),
        """level Ma_SubBoss_P set {} BalancedItems
        (
            {}
        )
        """.format(obj_name, ','.join(items)))

mutator_pool('common_coms', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_ClassMods', [
    ('GD_Itempools.ClassModPools.Pool_ClassMod_02_Uncommon', 2, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare', 3, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare', 4, None),
    ])
mutator_pool('common_grenades', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_GrenadeMods', [
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_02_Uncommon', 2, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare', 3, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare', 4, None),
    ])
mutator_pool('common_ozkits', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_MoonItems', [
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_02_Uncommon', 2, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_04_Rare', 3, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_05_VeryRare', 4, None),
    ])
mutator_pool('common_shields', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Shields', [
    ('GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon', 2, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', 3, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', 4, None),
    ])
mutator_pool('common_launchers', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Weapons_Launchers', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', 4, None),
    ])
mutator_pool('common_longguns', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Weapons_LongGuns', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', 4, None),
    ])
mutator_pool('common_pistols', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Weapons_Pistols', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', 4, None),
    ])
mutator_pool('red_coms', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_ClassMods', [
    ('GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare', 3, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare', 4, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary', 5, None),
    ])
mutator_pool('red_grenades', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_GrenadeMods', [
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare', 3, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare', 4, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary', 5, None),
    ])
mutator_pool('red_ozkits', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_MoonItems', [
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_04_Rare', 3, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_05_VeryRare', 4, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_06_Legendary', 5, None),
    ])
mutator_pool('red_shields', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Shields', [
    ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', 3, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', 4, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', 5, None),
    ])
mutator_pool('red_launchers', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Launchers', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Launchers_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', 5, None),
    ])
mutator_pool('red_launchers_glitch', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Launchers_PlusGitch', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Launchers_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', 5, None),
    ])
mutator_pool('red_longguns', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_LongGuns', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_AssaultRifles_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Shotguns_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_SMG_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Sniper_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_06_Legendary', 5, None),
    ])
mutator_pool('red_longguns_glitch', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_LongGuns_PlusGlitch', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_AssaultRifles_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Shotguns_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_SMG_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Sniper_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_06_Legendary', 5, None),
    ])
mutator_pool('red_pistols', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Pistols', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Pistols_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', 5, None),
    ])
mutator_pool('red_pistols_glitch', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Pistols_PlusGlitch', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Pistols_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', 5, None),
    ])

# Improve Flameknuckle's Holodome Onslaught drops
for num in [17, 18, 19, 20]:
    mp.register_str('flameknuckle_holodome_drop_{}'.format(num),
        """level Eridian_Slaughter_P set GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlSergeantFlameKnuckle DefaultItemPoolList[{}].ItemPool ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare'""".format(num))

# Legendary Pool management
unique_hotfixes = []
uniqueglitch_hotfixes = []
for (guntype, legendaries, uniques, uniqueglitches) in [
        (
            'AssaultRifles',
            [
                # Regular Legendaries
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Torgue_5_KerBoom',
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier',
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom',
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBreaker',
                'GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade',
            ],
            [
                # Uniques
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Jakobs_3_Wallop',
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail',
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_IceScream',
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful',
                'GD_Cypressure_Weapons.A_Weapons_Unique.AR_Bandit_3_BossNova',
                'GD_Petunia_Weapons.AssaultRifles.AR_Bandit_3_CryBaby',
            ],
            [
                # Unique Glitches
            ],
        ),
        (
            'Launchers',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Cryophobia',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_Thingy',
                'GD_Ma_Weapons.A_Weapons_Legendary.RL_Tediore_5_KanedasLaser',
                'GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Tediore_3_Rocketeer',
                'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
            ],
            [
                # Unique Glitches
            ],
        ),
        (
            'Pistols',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Zim',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_88Fragnum',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
                'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Jakobs_5_LuckCannon',
                'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Globber',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Smasher',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_CyberColt',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe',
                'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper',
                'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot',
                'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr',
            ],
            [
                # Unique Glitches
            ],
        ),
        (
            'Shotguns',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
                'GD_Ma_Weapons.A_Weapons_Legendary.SG_Jakobs_5_Flayer',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Moonface',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_TooScoops',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Torguemada',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Wombat',
                'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan',
                'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Torgue_3_Landscaper2',
                'GD_Petunia_Weapons.Shotguns.SG_Tediore_3_PartyLine',
            ],
            [
                # Unique Glitches
            ],
        ),
        (
            'SMG',
            [
                # Regular Legendaries
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF',
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent',
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
                'GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode',
            ],
            [
                # Uniques
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MareksMouth',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Old_Hyperion_BlackSnake',
                'GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker',
                'GD_Petunia_Weapons.SMGs.SMG_Tediore_3_Boxxy',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Fridgia',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Frostfire',
            ],
            [
                # Unique Glitches
                'GD_Ma_Weapons.A_Weapons_Unique.SMG_Bandit_6_Glitch_CutieKiller',
            ],
        ),
        (
            'SniperRifles',
            [
                # Regular Legendaries
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
                'GD_Ma_Weapons.A_Weapons_Legendary.Sniper_Old_Hyperion_5_OmniCannon',
            ],
            [
                # Uniques
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Razorback',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine',
                'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
            ],
            [
                # Unique Glitches
            ],
        ),
        (
            'Lasers',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_ZX1',
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla',
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_Ricochet',
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Old_Hyperion_5_Excalibastard',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_FusionBeam',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_Thunderfire',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Dahl_3_Firestarta',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_VibraPulse',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Egun',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_SavorySideSaber',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen',
                'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Enlightenment',
                'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Minac',
            ],
            [
                # Unique Glitches
                'GD_Ma_Weapons.A_Weapons_Unique.Laser_Dahl_6_Glitch_HeartfullSplodger',
            ],
        ),
        ]:

    # First set up a hotfix for the base pool initialization
    initial_pool = []
    for legendary in legendaries:
        initial_pool.append((legendary, 1, 'WeaponBalanceDefinition'))
    for i in range(len(uniques) + len(uniqueglitches)):
        initial_pool.append((None, 0))
    mp.register_str('weapon_pool_clear_{}'.format(guntype.lower()),
        'level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems {}'.format(
            guntype,
            mp.get_balanced_items(initial_pool),
            ))  

    # Hotfixes to add uniques
    for (idx, unique) in enumerate(uniques):
        unique_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + idx,
                unique
                ))

    # Hotfixes to add unique glitches
    for (idx, uniqueglitch) in enumerate(uniqueglitches):
        uniqueglitch_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + idx,
                uniqueglitch
                ))

mp.register_str('legendary_unique_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in unique_hotfixes]
    ))

mp.register_str('legendary_uniqueglitch_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in uniqueglitch_hotfixes]
    ))


# Legendary shield/grenade pool configuration.  Doing this a bit differently since there's
# not nearly as many shields/grenades to handle as weapons.

items = {
    'shield': {
        'GD_Itempools.ShieldPools.Pool_Shields_Booster_06_Legendary': [
            ('asteroidbelt', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_AsteroidBelt', 1),
            ('slammer', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_MoxxisSlammer', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Chimera_06_Legendary': [
            ('haymaker', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_Haymaker', 1),
            ('m0rq', 2, 'GD_Ma_Shields.A_Item_Legendary.ItemGrade_Gear_Shield_Chimera_05_M0RQ', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Juggernaut_06_Legendary': [
            ('shieldofages', 1, 'GD_Ma_Shields.A_Item_Unique.ItemGrade_Gear_Shield_Juggernaut_03_ShieldOfAges', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_06_Legendary': [
            ('sunshine', 3, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Starburst', 1),
            ('rapidrelease', 4, 'GD_Cork_Shields.A_Item_Custom.ItemGrade_Shield_RapidRelease', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Standard_06_Legendary': [
            ('naught', 1, 'GD_Ma_Shields.A_Item_Unique.ItemGrade_Gear_Shield_Naught', 1),
            ],
        },
    'grenade': {
        'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary': [
            ('baby_boomer', 11, 'GD_GrenadeMods.A_Item_Custom.GM_BabyBoomer', 1),
            ('data_scrubber', 12, 'GD_Ma_GrenadeMods.A_Item_Unique.GM_DataScrubber', 1),
            ('kiss_of_death', 13, 'GD_Cork_GrenadeMods.A_Item_Custom.GM_KissOfDeath', 1),
            ('snowball', 14, 'GD_GrenadeMods.A_Item_Custom.GM_Snowball', 1),
            ('sky_rocket', 15, 'GD_GrenadeMods.A_Item_Custom.GM_SkyRocket', 0.05),
            ],
        },
    'ozkit': {
        'GD_Itempools.MoonItemPools.Pool_MoonItem_06_Legendary': [
            ('cathartic', 5, 'GD_MoonItems.A_Item_Unique.A_Poopdeck', 1),
            ('freedom', 6, 'GD_MoonItems.A_Item_Unique.A_Freedom', 1),
            ('invigoration', 7, 'GD_MoonItems.A_Item_Unique.A_Invigoration', 1),
            ('systems_purge', 8, 'GD_MoonItems.A_Item_Unique.A_SystemsPurge', 1),
            ('perdy_lights', 9, 'GD_Pet_MoonItems.A_Item_Unique.A_AntiAir_PerdyLights', 1),
            ],
        },
    }
for (itemtype, itemdict) in items.items():
    for (pool, itemlist) in itemdict.items():
        for (label, index, itemname, scale) in itemlist:
            mp.set_bi_item_pool('{}_{}'.format(itemtype, label),
                pool,
                index,
                itemname,
                invbalance='InventoryBalanceDefinition',
                scale=scale,
                )

###
### Generate our quality category strings
###

qualities = {}
for profile in profiles:

    profile.set_balanced_pct_reports('drop_weapon', [
            profile.weapon_base_common,
            profile.weapon_base_uncommon,
            profile.weapon_base_rare,
            profile.weapon_base_veryrare,
            profile.weapon_base_glitch,
            profile.weapon_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('drop_weapon_clap', [
            profile.weapon_clap_base_common,
            profile.weapon_clap_base_uncommon,
            profile.weapon_clap_base_rare,
            profile.weapon_clap_base_veryrare,
            profile.weapon_clap_base_glitch,
            profile.weapon_clap_base_legendary,
            ], fixedlen=True)
    # We're assuming that all items have the same percentages, which is NOT
    # actually true - COM legendaries are *slightly* more likely than
    # legendaries from the other item types.  At some point in the future
    # perhaps we'll make a note of that and fix up the displays.
    profile.set_balanced_pct_reports('drop_items', [
            profile.grenade_base_common,
            profile.grenade_base_uncommon,
            profile.grenade_base_rare,
            profile.grenade_base_veryrare,
            profile.grenade_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('treasure_weapon', [
            profile.treasure_base_common,
            profile.treasure_base_uncommon,
            profile.treasure_base_rare,
            profile.treasure_base_veryrare,
            profile.treasure_base_glitch,
            profile.treasure_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('treasure_items', [
            profile.treasure_base_common,
            profile.treasure_base_uncommon,
            profile.treasure_base_rare,
            profile.treasure_base_veryrare,
            profile.treasure_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_weapon', [
            profile.epic_base_uncommon,
            profile.epic_base_rare,
            profile.epic_base_veryrare,
            profile.epic_base_glitch,
            profile.epic_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_glitch_weapon', [
            profile.epic_glitch_base_uncommon,
            profile.epic_glitch_base_rare,
            profile.epic_glitch_base_veryrare,
            profile.epic_glitch_base_glitch,
            profile.epic_glitch_base_legendary_dbl,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_items', [
            profile.epic_base_uncommon,
            profile.epic_base_rare,
            profile.epic_base_veryrare,
            profile.epic_base_legendary,
            ], fixedlen=True)
    profile.set_badass_qty_reports('regular', [
            profile.badass_pool_veryrare,
            profile.badass_pool_glitch,
            profile.badass_pool_epicchest,
            ])
    profile.set_badass_qty_reports('regular_clap', [
            profile.badass_pool_clap_veryrare,
            profile.badass_pool_clap_glitch,
            profile.badass_pool_clap_epicchest,
            ])
    profile.set_badass_qty_reports('super', [
            profile.super_badass_pool_rare,
            profile.super_badass_pool_veryrare,
            profile.super_badass_pool_glitch,
            profile.super_badass_pool_legendary,
            profile.super_badass_pool_epicchest,
            ])
    profile.set_badass_qty_reports('ultimate', [
            profile.ultimate_badass_pool_veryrare_1 + profile.ultimate_badass_pool_veryrare_2,
            profile.ultimate_badass_pool_glitch_1 + profile.ultimate_badass_pool_glitch_2,
            profile.ultimate_badass_pool_legendary_1 + profile.ultimate_badass_pool_legendary_2 + profile.ultimate_badass_pool_legendary_3,
            profile.ultimate_badass_pool_epicchest_1 + profile.ultimate_badass_pool_epicchest_2 + profile.ultimate_badass_pool_epicchest_3,
            ])
    profile.set_badass_qty_reports('ultimate_clap', [
            profile.ultimate_badass_pool_clap_veryrare_1 + profile.ultimate_badass_pool_clap_veryrare_2,
            profile.ultimate_badass_pool_clap_glitch_1 + profile.ultimate_badass_pool_clap_glitch_2,
            profile.ultimate_badass_pool_legendary_1 + profile.ultimate_badass_pool_legendary_2 + profile.ultimate_badass_pool_legendary_3,
            profile.ultimate_badass_pool_epicchest_1 + profile.ultimate_badass_pool_epicchest_2 + profile.ultimate_badass_pool_epicchest_3,
            ])

    with open('input-file-quality.txt') as df:
        qualities[profile.profile_name] = df.read().format(
                config=profile,
                mp=mp,
                )

###
### Generate our drop quantity category strings
###
boss_quantities = {}
for qty in [QtyExcellent(), QtyImproved(), QtyStock()]:
    with open('input-file-quantity.txt') as df:
        boss_quantities[qty.qty_index] = df.read().format(
                config=qty,
                mp=mp,
                )

###
### Generate our boss unique drop strings
###

boss_drops = {}
for (label, key, unique_pct, rare_pct, holodome_pct) in [
        ('Guaranteed', 'guaranteed', 1, 1, .2),
        ('Very Improved', 'veryimproved', .5, .75, .15),
        ('Improved', 'improved', .33, .60, 0.1),
        ('Slightly Improved', 'slight', .22, .45, .085),
        ('Stock', 'stock', .1, .33, .066),
        ]:

    with open('input-file-droprate.txt', 'r') as df:
        boss_drops[key] = df.read().format(
                section_label='{} ({}% Uniques, {}% Rares, {}% Holodome Uniques)'.format(
                    label, round(unique_pct*100), round(rare_pct*100), round(holodome_pct*100)),
                unique_pct=unique_pct,
                rare_pct=rare_pct,
                holodome_pct=holodome_pct,
                )

###
### Read in our early game unlocks
###

with open('input-file-earlyunlock.txt') as df:
    early_game_unlocks = df.read()

###
### Everything below this point is constructing the actual patch file
###

# Write out the file
with open(input_filename, 'r') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        mp=mp,
        base=ConfigBase(),
        drop_quality_excellent=qualities['Excellent'],
        drop_quality_verygood=qualities['Very Good'],
        drop_quality_good=qualities['Good'],
        drop_quality_improved=qualities['Improved'],
        drop_quality_stock=qualities['Stock-ish'],
        boss_drops_guaranteed=boss_drops['guaranteed'],
        boss_drops_veryimproved=boss_drops['veryimproved'],
        boss_drops_improved=boss_drops['improved'],
        boss_drops_slightimproved=boss_drops['slight'],
        boss_drops_stock=boss_drops['stock'],
        boss_quantity_excellent=boss_quantities['excellent'],
        boss_quantity_improved=boss_quantities['improved'],
        boss_quantity_stock=boss_quantities['stock'],
        early_game_unlocks=early_game_unlocks,
        guaranteed_luneshine=guaranteed_luneshine,
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod to: {}'.format(output_filename))
