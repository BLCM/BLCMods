===================================================================================================================
replace the Kitten

The L.O.V.E

braek the Dahlminator

Shoots hurt shots

6 shots burst

shots fast as you can pull the triger

++damage

-Projectiles Per Shot

--fire rate

+mag size

+accuracy 

created by ozay (or oz yohay)
===================================================================================================================
##skin##

set GD_Iris_Weapons.ManufacturerMaterials.Mat_Vladof_3_Kitten Material MaterialInstanceConstant 'Iris_GunMaterials.Materials.AssaultRifle.Mati_TorgueUnique_BoomPuppy'

##name##



set GD_Iris_Weapons.Name.Title.Title_Unique_Kitten PartName L.O.V.E

set GD_Iris_Weapons.Name.Title.Title_Unique_Kitten:AttributePresentationDefinition_8 NoConstraintText L.O.V.E can hurts.

##stats##




set GD_Iris_Weapons.AssaultRifles.AR_Barrel_Vladof_Kitten WeaponAttributeEffects ((AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponDamage',ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=10.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponClipSize',ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=3.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponProjectilesPerShot',ModifierType=MT_PreAdd,BaseModifierValue=(BaseValueConstant=0.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponFireInterval',ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=-3.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponSpread',ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=-1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponProjectileSpeedMultiplier',ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponShotCost',ModifierType=MT_PostAdd,BaseModifierValue=(BaseValueConstant=0.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponPerShotAccuracyImpulse',ModifierType=MT_Scale,BaseModifierValue=(BaseValueConstant=-3.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponAutomaticBurstCount',ModifierType=MT_PreAdd,BaseModifierValue=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)))



set GD_Iris_Weapons.AssaultRifles.AR_Barrel_Vladof_Kitten ZoomWeaponAttributeEffects ((AttributeToModify=AttributeDefinition'D_Attributes.Weapon.WeaponAutomaticBurstCount',ModifierType=MT_PreAdd,BaseModifierValue=(BaseValueConstant=6.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000))


##Shots##



set GD_Iris_Weapons.AssaultRifles.AR_Barrel_Vladof_Kitten CustomFiringModeDefinition FiringModeDefinition 'GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator'

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator FireType EWWFT_Bullet

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator PartSysTemplate ParticleSystem 'FX_WEP_Grenades.Particles.Part_TransfusionOrb_Trail'

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator Lifetime 5.000000

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator OnAnyImpact ()

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator bSuppressImpactEffects True

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator FiringPatternLines ()

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator Speed 1000.000000

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator NumRicochets 0

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator bPenetratePawn True


#Bullet#

set GD_Weap_Pistol.FiringModes.Bullet_Pistol_Spiker_Homing_Dahlminator OnAnyImpact (Behavior_SpawnProjectile'GD_Weap_SniperRifles.FiringModes.Bullet_Sniper_ChereAmie:Behavior_SpawnProjectile_2')

##parts##


set GD_Iris_Weapons.AssaultRifles.AR_Barrel_Vladof_Kitten GestaltModeSkeletalMeshName AR_Barrel_Torgue

==================================================================================================================
