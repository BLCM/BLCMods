### azakhi's Borderlands: The Pre Sequel mods

# Item Drop Rates
Affects ratio of rarities of (probably) all items. Does not affect quantity.

The changed variable is `ValueFormula->Multiplier->BaseValueConstant` of related Weight_X_XXXX objects.

Ratio Calculation (It is my guess):  
Numbers corresponds to amount of that rarity you will probably see in a pool of items with an amount of total of all rarities. E.g. let the values for White, Green and Blue rarity be only possible rarities and their values be 100, 10 and 1. This means for every 111 items you get probably 100 of them will be White, 10 will be Green and 1 will be Blue.

Changes:  

| Rarity | Old Value | New Value |
| --- | --- | --- |
| Weight_1_Common | 100 | 100 |
| Weight_2_Uncommon | 10 | 20 |
| Weight_3_Uncommoner | 5 | 12 |
| Weight_4_Rare | 1 | 3.5 |
| Weight_5_VeryRare | 0.1 | 0.6 |
| Weight_6_Legendary | 0.01 | 0.12 |

# Item of the Day Rates
Affects ratio of rarities of item of the day items in shops. Probably also affect some of the chests

The related item pools are modified. In those pools there is a record for each sub item category, the ratios of those categories are defined in `Probability` properties, initialized using Weight_X_XXXX values and scaled by `BaseValueScaleConstant` property.

Changes:  

| Rarity | Old Value | New Value |
| --- | --- | --- |
| Weight_2_Uncommon | 1 | 1 |
| Weight_4_Rare | 1 | 1 |
| Weight_5_VeryRare | 2.5 | 5 |
| Weight_6_Legendary | 3 | 15 |

# Moonstone Drop Rates
Increases drop rates of moonstones and moonstone cluster.

The changed variable is `ConstantValue`

Changes:  

|  | Old Value | New Value |
| --- | --- | --- |
| Moonstone | 0.05 | 0.12 |
| Moonstone Cluster | 0.025 | 0.06 |
