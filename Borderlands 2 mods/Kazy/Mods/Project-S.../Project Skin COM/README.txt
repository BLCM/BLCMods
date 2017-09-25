//created by Kazy
//credit goes to shadowevil1996 for fine-tuning some portions of the code


This overhaul allows you to turn the Customization Skin of your choice into a Class Mod. This includes the following features:
• The ability for the skin to be equipped, rather than consumed
• The ability to run effects and skill boosts on the skin
• The ability to change the appearance of the skin to that of a class mod
• The ability to give the skin a manufacturer
• The ability to give the skin a Damage Type Icon (seen on weapons and Krieg's Torch class mod)
• The ability to change the skin's rarity
• The ability to place the skin in a lootpool
• The ability to have the skindrop with a level requirewment
• The ability to have the skin drop with a class requirement
• Sound effects and display information displaying as a COM rather than a skin

Note: This file MUST be run prior to entering a session, or you risk losing the item due to the Sanity Check (Not that this is a surprise)

TABLE OF CONTENTS
[EXM] - Example Piece
- This section has an example piece of what the finished product should appear as. Copy it into its own text file to ensure it does not mess with the Class Mod you are designing. This section's example is the following:
    - Legendary Survivor Class Mod for Zer0 the Assassin. It replaces the Bloody Eye Fanboat Skin from Hammerlock's Hunt DLC.

[BSE] - Base Components
- This section has lines commonly modified on Class Mods, such as UI information, Skills that are boosted, and rarity. These lines can be freely modified.

[S2C] - Skin to COM Specifics [Do NOT Modify]
- This section contains the neccessary parts to create a Class Mod out of a Customization Skin. Do NOT Modify these lines.

[CHR] - Character-Specific Modifications
- This section contains character-specific lines geared toward building a Class Mod based upon the character. These lines must be included, but only the one for the character the Class Mod is for.

[MFT] - Manufacturer-Specific Modifications
- This section contains manufacturer-specific lines geared toward building a Class Mod based upon a manufacturer. These lines must be included, but only the one for the manufacturer the Class Mod is for.

[DTI] Damage Type Icon
- This section holds the Damage Type Icon, as seen on elemental weapons and COMs. Use the one you want to display on the Item Card.

[LOT] Droppable Location Lootpool
- This section houses the code needed for the Class Mod to be added to a lootpool. The lootpool you wish to add it to depends on how you would like this item to be obtainable, otherwise it will use its default location.
Note: You must ADD the Class Mod into the pool, and not simply just replace the pool, at risk of losing drop locations.

[CUS] - Customization Skin List
- This section holds all the Customization Skins, allowing for freedom of choice as to which Skin you would like to replace. This section holds the following:
    [SKC] Character Skins [Base Game]
    [SKR] Runner Skins
    [SKT] Bandit Technical Skins
    [SKF] Fanboat Skins (Requires Hammerlock's Hunt DLC)
    [SKH] Hovercraft Skins (Requires Scarlett's Booty DLC)
    [BDL] - Balance Definitions
- This section houses the Balance Definitions (BalanceDefs), allowing for freedom of choice as to which Skin you would like to replace. This section holds the following:
    [BDC] Character Skins [Base Game]
    [BDR] Runner Skins
    [BDT] Bandit Technical Skins
    [BDF] Fanboat Skins (Requires Hammerlock's Hunt DLC)
    [BDH] Hovercraft Skins (Requires Scarlett's Booty DLC)
    [API] - Attribute Presentations
- This section houses the Attribute Presentations, allowing for freedom of choice as to which Skin you would like to replace. This section holds the following:
    [APC] Character Skins [Base Game]
    [APR] Runner Skins
    [APT] Bandit Technical Skins
    [APF] Fanboat Skins (Requires Hammerlock's Hunt DLC)
    [APH] Hovercraft Skins (Requires Scarlett's Booty DLC)

In order to effectively use this file, you must replace the following items:
    [SKN]
    [BAL]
    [ATP]
If the two lines above are replaced with an Item and a Balance Definition with the "Replace All" tool, your Customization Skin should now be a clean-slate for a Class Mod. From here, just add the required Character, Manufacturer, and Base Traits to finalize the Class Mod.
