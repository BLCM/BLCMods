# Deprecated - Gronp's "Faster Vehicle Animations" is better than this implementation,
# and they said I could use it. :)  Felt I should save this for posterity, though.

# Vehicle Animations
lines.append('#<Vehicle Animations>')
lines.append('')
lines.append('    # Vehicle Animations (such as characters entering, leaving, or changing seats)')
lines.append('    # are only getting a {vehicle_anim_speed_scale}x boost, since they look pretty weird if faster.'.format(
    vehicle_anim_speed_scale=vehicle_anim_speed_scale,
    ))
lines.append('')
animset_cache = {}
for (vehicle_name, vehicle_packages, characters) in [
        ('Bandit Technical',
            ['GD_BTech_Streaming'],
            [
                ('Assassin', 'Anim_Assassin.BanditTechnical_Assassin'),
                ('Mechromancer', 'Anim_Mechromancer.BanditTechnical_Mechromancer'),
                ('Mercenary', 'Anim_Merc.BanditTechnical_Merc'),
                ('Psycho', 'Anim_PsychoDLC.BanditTechnical_PsychoDLC'),
                ('Siren', 'Anim_Siren.BanditTechnical_Siren'),
                ('Soldier', 'Anim_Soldier.BanditTechnical_Soldier'),
            ]),
        ('Fan Boat',
            ['GD_Sage_ShockFanBoat', 'GD_Sage_CorrosiveFanBoat', 'GD_Sage_IncendiaryFanBoat'],
            [
                ('Assassin', 'Sage_Anim_Assassin.FanBoat_Assassin'),
                ('Mechromancer', 'Sage_Anim_Mecro.FanBoat_Mecro'),
                ('Mercenary', 'Sage_Anim_Merc.FanBoat_Merc'),
                ('Psycho', 'Anim_PsychoDLC.Fanboat_PsychoDLC'),
                ('Siren', 'Sage_Anim_Siren.FanBoat_Siren'),
                ('Soldier', 'Sage_Anim_Soldier.FanBoat_Soldier'),
            ]),
        ('Runner',
            ['GD_Runner_Streaming'],
            [
                ('Assassin', 'Anim_Assassin.LightRunner_Assassin'),
                ('Mechromancer', 'Anim_Mechromancer.LightRunner_Mechromancer'),
                ('Mercenary', 'Anim_Merc.LightRunner_Merc'),
                ('Psycho', 'Anim_PsychoDLC.LightRunner_PsychoDLC'),
                ('Siren', 'Anim_Siren.LightRunner_Siren'),
                ('Soldier', 'Anim_Soldier.LightRunner_Soldier'),
            ]),
        ('Skiff / Hovercraft',
            ['GD_Orchid_HarpoonHovercraft', 'GD_Orchid_RocketHovercraft', 'GD_Orchid_SawHovercraft'],
            [
                ('Assassin', 'Char_Orchid_Assassin.Orchid_Anim_Assassin'),
                ('Mechromancer', 'Char_Orchid_Mecro.Orchid_Anim_Mecro'),
                ('Mercenary', 'Char_Orchid_Merc.Orchid_Anim_Merc'),
                ('Psycho', 'Anim_PsychoDLC.Hovercraft_PsychoDLC'),
                ('Siren', 'Char_Orchid_Siren.Orchid_Anim_Siren'),
                ('Soldier', 'Char_Orchid_Soldier.Orchid_Anim_Soldier'),
            ]),
        ]:
    lines.append('#<{}>'.format(vehicle_name))
    lines.append('')
    for (char_name, char_animset_name) in characters:
        lines.append('#<{}>'.format(char_name))
        lines.append('')
        for vehicle_package in vehicle_packages:
            if char_animset_name not in animset_cache:
                sequences = []
                char_animset = data.get_struct_by_full_object(char_animset_name)
                for sequence in char_animset['Sequences']:
                    sequences.append(Data.get_attr_obj(sequence))
                animset_cache[char_animset_name] = sequences
            sequences = animset_cache[char_animset_name]
            for char_sequence in sequences:
                lines.append('demand {} set {} RateScale {}'.format(
                    vehicle_package,
                    char_sequence,
                    vehicle_anim_speed_scale,
                    ))
                lines.append('')
        lines.append('#</{}>'.format(char_name))
        lines.append('')
    lines.append('#</{}>'.format(vehicle_name))
    lines.append('')
lines.append('#</Vehicle Animations>')
lines.append('')
