package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsArray;
import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.BorderlandsStruct;
import blcmm.data.lib.DataManager;
import blcmm.data.lib.DataManager.Dump;
import blcmm.model.assist.BLCharacter;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PCommand;
import java.util.HashSet;
import java.util.function.Consumer;

/*
  We use various classes to look through dumps to work out what to lock, this
   class is a collection of them all
*/
public class DumpProcessors {
    /*
      Each "ClassModBalanceDefinition" contains a list of "ClassModDefinition"s
       but no "Manufacturer"
      Instead, each "ClassModDefinition" has a "ManufacturerOverride" and a
       "RequiredPlayerClass" field
      To lock them we simply change the "RequiredPlayerClass" if needed
    
      Another method would be to remove incorrect "ClassModDefinition"s from the
       "ClassModBalanceDefinition", however this will delete items if you load
       the wrong character
    */
    public static class ClassModDefinition implements Consumer<Dump> {
        private PCategory classMods;
        private String manuClass;
        private String limitChar;
        private HashSet<String> blackList;
        public ClassModDefinition(PCategory root, Manufacturer manu, BLCharacter blChar) {
            classMods = new PCategory("Class Mods");
            root.addChild(classMods);
            manuClass = manu.getClas();
            limitChar = "set %s RequiredPlayerClass GD_PlayerClassId."
                    + blChar.getCharacterClass();
            
            blackList = new HashSet<String>();
            blackList.add("ClassModDefinition'WillowGame.Default__ClassModDefinition'");
            blackList.add("CrossDLCClassModDefinition'WillowGame.Default__CrossDLCClassModDefinition'");
        }
        
        public void accept(Dump itemDump) {
            if (blackList.contains(itemDump.getFullyQuantizedName())) {
                return;
            }
            
            BorderlandsObject item = BorderlandsObject.parseObject(
                itemDump,
                "ManufacturerOverride"
            );
            if (!item.getStringField("ManufacturerOverride").contains(manuClass)) {
                classMods.addChild(new PCommand(String.format(
                    limitChar, item.getFullyQuantizedName()
                )));
            }
        }
    }
    
    /*
      Most "InventoryBalanceDefinition"s have a "Manufacturers" field, in which
       you can find "Manufacturer" and (nested a bit) "MinGameStage" fields
      We check if ther manufacturer is incorrect, and if so set the min game
       stage to 500, so even with level uncapper mods, it's pretty much
       unreachable, and thus will never spawn that type of item
    */
    public static class InventoryBalanceDefinition implements Consumer<Dump> {
        private PCategory guns;
        private PCategory shields;
        private PCategory grenades;
        private PCategory relics;
        
        private String manuClass;
        private String manuRelic;
        private HashSet<String> blackList;
        public InventoryBalanceDefinition(PCategory root, Manufacturer manu,
                boolean allowRelic) {
            manuClass = manu.getClas(); 
            manuRelic = allowRelic ? manu.getRelic() : "  placeholder  "; 
            
            /*
              Unfortuantly "InventoryBalanceDefinition" is quite a general class
               so we get a lot of extra objects
              Some can be filtered out by type but we still need to keep a
               proper blacklist
            */
            blackList = new HashSet<String>();
            if (DataManager.getBL2()) {
                relics = new PCategory("Relics");
                blackList.add("InventoryBalanceDefinition'GD_BTech_Streaming.Weapon.ItemGrades.ItemGrade_FrontMachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_BanditTurret.Weapon.ItemGrade_BanditTurret'");
                blackList.add("InventoryBalanceDefinition'GD_BigLoaderTurret.Weapons.BigLoaderTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_BigLoaderTurret_Digi.Weapons.BigLoaderTurret_Digi_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_CannonTurret.Weapon.ItemGrade_CannonTurret'");
                blackList.add("InventoryBalanceDefinition'GD_ConstructorTurret.Weapons.ConstructorTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_FirstPlaceTechnical.Weapon.ItemGrades.ItemGrade_MachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_GyrocopterShared.Weapon.ItemGrade_GyrocopterGun'");
                blackList.add("InventoryBalanceDefinition'GD_HyperionBunkerBoss.Balance.Balance_BunkerBoss_Weapon'");
                blackList.add("InventoryBalanceDefinition'GD_Hyperion_AutoCannon.Weapons.AutoCannon_Weapon_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Hyperion_LargeTurret.Weapons.Hyperion_LargeTurret_Weapon_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Hyperion_TurretShared.Weapons.HyperionTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Hyperion_TurretSlag_Digi.Weapons.HyperionTurret_ItemGrade_Slag'");
                blackList.add("InventoryBalanceDefinition'GD_Hyperion_VOGTurret.Weapons.VOGTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Iris_MotorMamaTurret.FireRocket.ItemGrade_Iris_MotorMamaFireRocket'");
                blackList.add("InventoryBalanceDefinition'GD_Iris_MotorMamaTurret.SMGTurret.ItemGrade_Iris_MotorMamaSMGTurret'");
                blackList.add("InventoryBalanceDefinition'GD_Iris_MotorMamaTurret.ShockRocket.ItemGrade_Iris_MotorMamaShockRocket'");
                blackList.add("InventoryBalanceDefinition'GD_Iris_RocketTurret.Weapon.Drunken.ItemGrade_Iris_DrunkenRocketTurret'");
                blackList.add("InventoryBalanceDefinition'GD_Iris_RocketTurret.Weapon.Super.ItemGrade_Iris_SuperRocketTurret'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Gear.ItemGrade_Gear_GrenadeMODs_Stock'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Gear.ItemGrade_Gear_Shield_Stock'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_BoomBoom'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Shields_Enemy.ItemGrade_Gear_Shield_Enemy_Standard'");
                blackList.add("InventoryBalanceDefinition'GD_JackDeployableTurret.Weapons.JacksTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Knight_Paladin.Shields.ItemGrade_Gear_Shield_EnemyPaladin_Standard'");
                blackList.add("InventoryBalanceDefinition'GD_LoaderBUL.Weapon.Balance_LoaderBUL_Weapon'");
                blackList.add("InventoryBalanceDefinition'GD_LoaderHOT.Weapon.Balance_LoaderHOT'");
                blackList.add("InventoryBalanceDefinition'GD_LoaderION.Weapon.Balance_LoaderION'");
                blackList.add("InventoryBalanceDefinition'GD_Orchid_HarpoonHovercraft.Weapon.ItemGrades.ItemGrade_Harpoon'");
                blackList.add("InventoryBalanceDefinition'GD_Orchid_Hovercraft.Weapon.ItemGrades.ItemGrade_MachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_Orchid_Hovercraft.Weapon.ItemGrades.ItemGrade_MachineGun_AIOnly'");
                blackList.add("InventoryBalanceDefinition'GD_Orchid_RocketHovercraft.Weapon.ItemGrades.ItemGrade_DualRockets'");
                blackList.add("InventoryBalanceDefinition'GD_RolandDeployableTurret.Weapon.RolandTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Runner_Streaming.Weapon.ItemGrades.ItemGrade_FrontMachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_Runner_Streaming.Weapon.ItemGrades.ItemGrade_MachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_Runner_Streaming.Weapon.ItemGrades.ItemGrade_RocketLauncher'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_CorrosiveFanBoat.Weapons.ItemGrades.ItemGrade_CorrosiveSpew'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_FanBoat.Weapons.ItemGrades.ItemGrade_CorrosiveSpew_AIOnly'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_FanBoat.Weapons.ItemGrades.ItemGrade_FrontMachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_FanBoat.Weapons.ItemGrades.ItemGrade_MachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_FanBoat.Weapons.ItemGrades.ItemGrade_StickyShock_AIOnly'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_IncendiaryFanBoat.Weapons.ItemGrades.ItemGrade_Flamethrower'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_IncendiaryFanBoat.Weapons.ItemGrades.ItemGrade_IncendiaryMachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_Sage_ShockFanBoat.Weapons.ItemGrades.ItemGrade_StickyShock'");
                blackList.add("InventoryBalanceDefinition'GD_SpiderTank.Weapons.AutoCannon_TurretWeapon_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Spider_ClaptrapWand_Proto.Shields.ItemGrade_Gear_Shield_EnemySpider_Standard'");
                blackList.add("InventoryBalanceDefinition'GD_TurretShared.Weapon.ItemGrade_TurretShared_Weapon'");
                blackList.add("InventoryBalanceDefinition'GD_WizardShared.Shields.ItemGrade_Gear_Shield_EnemyWizard_Standard'");
                blackList.add("WeaponBalanceDefinition'GD_Iris_MotorMama.Weapons.LauncherCustom'");
                blackList.add("WeaponBalanceDefinition'GD_Lilac_SkillsBase.Buzzaxe.Buzzaxe'");
                blackList.add("WeaponBalanceDefinition'GD_Weap_Scorpio.A_Weapon.WeapBalance_Scorpio'");
            } else {
                relics = new PCategory("Oz Kits");
                blackList.add("InventoryBalanceDefinition'GD_CannonTurret.Weapon.ItemGrade_CannonTurret'");
                blackList.add("InventoryBalanceDefinition'GD_Co_StingRay_Streaming.Weapon.ItemGrades.ItemGrade_FlakBurst'");
                blackList.add("InventoryBalanceDefinition'GD_Co_StingRay_Streaming.Weapon.ItemGrades.ItemGrade_Laser'");
                blackList.add("InventoryBalanceDefinition'GD_Co_StingRay_Streaming.Weapon.ItemGrades.ItemGrade_Rocket'");
                blackList.add("InventoryBalanceDefinition'GD_Cork_Dahl_RocketTurret.Weapons.Dahl_RocketTurret_Weapon_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Cork_Dahl_TurretShared.Weapons.DahlTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Cork_Dahl_TurretShared.Weapons.DahlTurret_ItemGrade_Mkii'");
                blackList.add("InventoryBalanceDefinition'GD_Eridian_Turret.Weapons.Eridian_Turret_Weapon_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Eridian_Turret.Weapons.Eridian_Turret_Weapon_ItemGrade_Corr'");
                blackList.add("InventoryBalanceDefinition'GD_Eridian_Turret.Weapons.Eridian_Turret_Weapon_ItemGrade_Cryo'");
                blackList.add("InventoryBalanceDefinition'GD_Eridian_Turret.Weapons.Eridian_Turret_Weapon_ItemGrade_Fire'");
                blackList.add("InventoryBalanceDefinition'GD_Eridian_Turret.Weapons.Eridian_Turret_Weapon_ItemGrade_Shock'");
                blackList.add("InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Custom.GM_FusterCluck'");
                blackList.add("InventoryBalanceDefinition'GD_GyrocopterShared.Weapon.ItemGrade_GyrocopterGun'");
                blackList.add("InventoryBalanceDefinition'GD_Hyperion_TurretShared.Weapons.HyperionTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Gear.ItemGrade_Gear_Shield_Stock'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Phoenix'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Shields_Enemy.ItemGrade_Gear_Shield_Enemy_Standard'");
                blackList.add("InventoryBalanceDefinition'GD_ItemGrades.Weapons.ItemGrade_Weapon_BotGun'");
                blackList.add("InventoryBalanceDefinition'GD_JetFighterShared.Weapon.ItemGrade_JetFighterGun'");
                blackList.add("InventoryBalanceDefinition'GD_Ma_EosRocketTurret.Weapons.Ma_EosRocketTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Ma_HeliosTurret.Weapons.Ma_HeliosTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_Ma_VoltronTrapTurret.Weapons.Ma_VoltronTrapTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_MoonBuggy_Streaming.Weapon.ItemGrades.ItemGrade_FrontMachineGun'");
                blackList.add("InventoryBalanceDefinition'GD_MoonBuggy_Streaming.Weapon.ItemGrades.ItemGrade_LightLaser'");
                blackList.add("InventoryBalanceDefinition'GD_ProtoWarBot_BlastTurret.Weapons.ProtoWarBot_BlastTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_ProtoWarBot_MissionTurret.Weapons.ProtoWarBot_BlastTurret_Mission_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_ProtoWarBot_RocketTurret.Weapons.ProtoWarBot_RocketTurret_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_ScavTurret_Small.Weapons.ScavTurret_Small_ItemGrade'");
                blackList.add("InventoryBalanceDefinition'GD_ShockHive.Weapons.ItemGrade_ShockBeam'");
                blackList.add("InventoryBalanceDefinition'GD_TurboLaser.Weapon.ItemGrade_TurboLaser'");
                blackList.add("InventoryBalanceDefinition'GD_ZarpedonJetP1Boss.Balance.Balance_ZarpedonJetP1Boss_Weapon'");
                blackList.add("WeaponBalanceDefinition'GD_Cork_Weap_Lasers.A_Weapons_Enemy_DahlOnly.Laser_Dahl_HypBarrel'");
                blackList.add("WeaponBalanceDefinition'GD_DahlPowersuit_Knuckle.Weapons.Knuckle_Laser_Dahl'");
                blackList.add("WeaponBalanceDefinition'GD_DahlShared.WeaponBalance.Laser_Dahl_EnemyUse_DahlBarrel'");
                blackList.add("WeaponBalanceDefinition'GD_Enforcer_Skills.Weapon.Laser_VengenceCannon'");
                blackList.add("WeaponBalanceDefinition'GD_Ma_SH4D0W-TP.Weapon.WeaponBalance_DahlBlasterOnly'");
                blackList.add("WeaponBalanceDefinition'GD_Ma_ShadowClone.Weapon.WeaponBalance_ShadowCloneBlaster'");
                blackList.add("WeaponBalanceDefinition'GD_Prototype_BuzzAxe.A_Weapons.BalanceDef_FragTrap_BuzzAxe'");
                blackList.add("WeaponBalanceDefinition'GD_Prototype_Dummy.A_Weapons.WeapBalance_MinionTrapTurret'");
                blackList.add("WeaponBalanceDefinition'GD_Prototype_Stethoscope.A_Weapons.Laser_Stethoscope'");
            }
            
            guns = new PCategory("Guns");
            shields = new PCategory("Shields");
            grenades = new PCategory("Grenade Mods");
            root.addChild(guns);
            root.addChild(grenades);
            root.addChild(shields);
            if (manu != Manufacturer.ERIDIAN) {
                root.addChild(relics);
            }
        }
        
        public void accept(Dump itemDump) {
            String dumpName = itemDump.getFullyQuantizedName();
            if (blackList.contains(dumpName) || dumpName.contains(manuRelic)) {
                return;
            }
            
            BorderlandsObject item = BorderlandsObject.parseObject(
                itemDump,
                "Manufacturers",
                "InventoryDefinition"
            );
            
            // Some things we don't want to modify can be filtered by type
            String itemType = item.getField("InventoryDefinition").toString()
                    .split("'")[0];
            if (itemType.equals("None")
                || itemType.startsWith("ClassMod")
                || itemType.equals("MissionItemDefinition")
                || itemType.equals("UsableCustomizationItemDefinition")
                || itemType.equals("UsableItemDefinition")
                || itemType.equals("VehicleWeaponTypeDefinition")) {
                return;
            }
            
            BorderlandsArray<BorderlandsStruct> itemManus =
                item.getArrayField("Manufacturers");
            boolean modified = false;
            // Some items like standard grenades have more than one manufacturer
            for (BorderlandsStruct manu : itemManus) {
                /*
                  Money doesn't get a nice recognisable prefix so we have to include
                   its manufacturer here
                */
                String manuType = manu.getString("Manufacturer");
                if (!(manuType.contains(manuClass)
                    || manuType.contains("GD_Currency.Manufacturers.Cash_Manufacturer"))) {
                    modified = true;
                    BorderlandsArray<BorderlandsStruct> allGrades =
                            manu.getArray("Grades");
                    allGrades.get(0).getStruct("GameStageRequirement")
                            .set("MinGameStage", 500);
                    manu.set("Grades", allGrades);
                }
            }
            if (modified) {
                PCommand newCommand = new PCommand(String.format(
                    "set %s Manufacturers %s",
                    dumpName,
                    itemManus
                ));
                switch (itemType) {
                    case "WeaponTypeDefinition": guns.addChild(newCommand); break;
                    case "ShieldDefinition": shields.addChild(newCommand); break;
                    case "GrenadeModDefinition": grenades.addChild(newCommand); break;
                    case "ArtifactDefinition": relics.addChild(newCommand); break;
                }
            }
        }
    }
}
