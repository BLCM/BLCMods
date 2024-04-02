<BLCMM v="1">
#<!!!You opened a file saved with BLCMM in FilterTool. Please update to BLCMM to properly open this file!!!>
	<head>
		<type name="BL2" offline="false"/>
	</head>
	<body>
		<category name="Silent Morningstar Mod 1.3">
			<comment> _     ____  _     _     ____ </comment>
			<comment>/ \   /  _ \/ \   / \   /  _ \</comment>
			<comment>| |   | / \|| |   | |   | / \|</comment>
			<comment>| |_/\| \_/|| |_/\| |_/\| \_/|</comment>
			<comment>\____/\____/\____/\____/\____/</comment>
			<category name="Description">
				<comment>Silent Morningstar Mod 1.0 by Lollo</comment>
				<comment></comment>
				<comment>Allows for the choice of silencing the Morningstar voice (or don't, I'm not your boss).</comment>
				<comment>This was designed with Morningstar Crit-stacking in mind.</comment>
				<comment>No longer shall you have to mute dialog!</comment>
				<comment></comment>
				<comment>Thanks to FromDarkHell and Apocolytech for the help in polishing this mod.</comment>
				<comment></comment>
				<comment>Feel free to repurpose this mod but please DO NOT REHOST IT</comment>
				<comment>Thank you for using my mod :) </comment>
			</category>
			<category name="Silence Morning Star?" MUT="true">
				<category name="Yes">
					<code profiles="default">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_0 Event None</code>
					<code profiles="default">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_1 Event None</code>
					<code profiles="default">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_2 Event None</code>
					<code profiles="default">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_3 Event None</code>
				</category>
				<category name="No">
					<code profiles="">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_0 Event AkEvent 'Ake_VOCT_Contextual.Ak_Play_VOCT_GuiltGun_Weapon_Switch'</code>
					<code profiles="">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_1 Event AkEvent 'Ake_VOCT_Contextual.Ak_Play_VOCT_GuiltGun_Fire'</code>
					<code profiles="">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_2 Event AkEvent 'Ake_VOCT_Contextual.Ak_Play_VOCT_GuiltGun_Reload'</code>
					<code profiles="">set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_3 Event AkEvent 'Ake_VOCT_Contextual.Ak_Play_VOCT_GuiltGun_Killed_Enemy'</code>
				</category>
			</category>
		</category>
	</body>
</BLCMM>

#Commands:
set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_0 Event None
set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_1 Event None
set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_2 Event None
set GD_Weap_SniperRifles.Skills.Skill_Morningstar:BehaviorProviderDefinition_0.Behavior_PostAkEvent_3 Event None

