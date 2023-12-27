Vacuum Combustion
=============

This mod change the incendiary status type to slag from ignite to bypass the vacuum restriction, allowing burn status effects.

Burning status effects not applying in vacuum is hard coded in the game engine, it checks if it the dot use the Ignite status effect type somehow.

If you need to use a
* StatusEffectExpressionEvaluator 
* OzBehavior_ForceSpreadStatusEffect
* Behavior_StatusEffectSwitch
* Functions with Python using the status effect type as an argument

For an incendiary effect in your mod, it will needs to use STATUS_EFFECT_Amp instead of STATUS_EFFECT_Ignite.

Changelog
=========

**v1.0** -
 * Uploaded
