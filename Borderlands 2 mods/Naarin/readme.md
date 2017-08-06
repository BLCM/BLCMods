Readme
=============

**Experience Multiplier**

You can choose between 2x 4x 8x 16x and 512x.

    set globals BaseEnemyExperienceFormula (BaseValueScaleConstant=2)

**Gearbox Software Hot Fixes**

All the hotfixes released to date (present in the UCP more or less).

**Golden Chest Needs Eridium**

**It costs 10 Eridium to open.**

    set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Golden:BehaviorProviderDefinition_1.Behavior_SetUsabilityCost_10 CostAmount 10

**Golden Chest is Free**

**Free.**

**Simulate More Vault Hunters**

**Needs to be _exec_ while in-game.** You can use it with FilterTool to check/uncheck.

    set Engine.GameInfo EffectiveNumPlayers 2
