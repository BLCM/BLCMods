package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsArray;
import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.BorderlandsStruct;
import blcmm.data.lib.DataManager;
import blcmm.data.lib.DataManager.Dump;
import blcmm.model.HotfixType;
import blcmm.plugins.BLCMMPlugin;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PCommand;
import blcmm.plugins.pseudo_model.PHotfix;
import java.util.HashSet;
import java.util.function.Consumer;
import javax.swing.JProgressBar;
import plugins.pseudo_model.ApplyablePModel;

/*
  We use various classes to look through dumps to work out what to lock, this
   class is a collection of them all
*/
public class DumpProcessors {
    /*
      Each item pool either refrences another item pool or specific items
      As we're processing all anyway of them we skip the item pool references,
       and just look at the item ones
      If the item is from an unsuitable manufacturer we then replace it with
       money
      This makes it so that you don't get more items than you would normally,
       and so that you still have a decent source of income
      If the item has multiple manufacturers (e.g. mirvs, bandit and torgue)
       then we allow the full item but remove the incorrect manufacturer
      In this case whenever you would've gotten a mirv you're guarenteed to get
       one in the correct brand
    */
    public static class ItemPoolDefinition implements Consumer<Dump> {
        private PCategory guns;
        private PCategory shields;
        private PCategory grenades;
        private PCategory classMods;
        private PCategory relics;
        private PCategory misc;
        
        private JProgressBar bar;
        private String manuClass;
        private String manuName;
        private String manuRelic;
        private boolean applyModel;
        
        private ApplyablePModel currentModel;
        private boolean isBL2;
        private HashSet<String> blacklist;
        
        private HashSet<String> modified;
        public ItemPoolDefinition(
            PCategory root,
            JProgressBar bar,
            Manufacturer manu,
            boolean allowRelic,
            boolean applyModel
        ) {
            
            this.bar = bar;
            manuClass = manu.getClas();
            manuName = manu.getBaseName();
            manuRelic = allowRelic ? manu.getRelic() : "  placeholder  ";
            this.applyModel = applyModel;
            isBL2 = DataManager.getBL2();
            modified = new HashSet<String>();

            if (applyModel) {
                currentModel = new ApplyablePModel(
                    BLCMMPlugin.getCurrentlyOpenedBLCMMModel()
                );
            }
            
            guns = new PCategory("Guns");
            shields = new PCategory("Shields");
            grenades = new PCategory("Grenade Mods");
            classMods = new PCategory("Class Mods");
            relics = new PCategory(isBL2 ? "Relics" : "Oz Kits");
            PCategory moxxtails = new PCategory("Moxxtails");
            misc = new PCategory("Unknown Category");
            
            root.addChild(guns);
            root.addChild(shields);
            root.addChild(grenades);
            root.addChild(classMods);
            if (manu != Manufacturer.ERIDIAN) {
                root.addChild(relics);
            }
            if (!isBL2 && manu != Manufacturer.MOXXI) {
                root.addChild(moxxtails);
            }
            root.addChild(misc);
            
            // Without this you can just buy free money from vendors
            misc.addChild(new PCommand(
                "UsableItemDefinition'GD_Currency.A_Item.Currency_Big'",
                "MonetaryValue",
                "(BaseValueConstant=100000000.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)"
            ));
            
            /*
              Some of these are things that just don't get filtered elsewhere,
               others are things that error when you try change them
            */
            blacklist = new HashSet<String>();
            if (isBL2) {
                blacklist.add("CrossDLCItemPoolDefinition'GD_Aster_EridiumSlotMachine.Pools.Weapon_Pool_Pearl_Launcher'");
                blacklist.add("CrossDLCItemPoolDefinition'GD_Aster_EridiumSlotMachine.Pools.Weapon_Pool_Pearl_Long'");
                blacklist.add("CrossDLCItemPoolDefinition'GD_Aster_EridiumSlotMachine.Pools.Weapon_Pool_Pearl_Pistol'");
                blacklist.add("ItemPoolDefinition'GD_Allium_GrandmaData.LootPool.Pool_Grandma'");
                blacklist.add("ItemPoolDefinition'GD_Allium_GrandmaData.WeaponPools.Pool_Torgue_Launchers_05_VeryRare'");
                blacklist.add("ItemPoolDefinition'GD_AngelBoss.LootPools.Pool_Bitch'");
                blacklist.add("ItemPoolDefinition'GD_Aster_AmuletDoNothingData.BalanceDefs.IP_MysteryAmulet'");
                blacklist.add("ItemPoolDefinition'GD_Aster_RolandNPC.Weapon.Pool_AsterRoland_AssaultRifles'");
                blacklist.add("ItemPoolDefinition'GD_BoomBoom.WeaponPools.Pool_Weapons_Shotguns_BoomBoom'");
                blacklist.add("ItemPoolDefinition'GD_HarkGutter.WeaponPools.Weapons_PistolsHark'");
                blacklist.add("ItemPoolDefinition'GD_ItemPools_Shop.HealthShop.HealthShop_InstaHealth_1'");
                blacklist.add("ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_StorageDeckUpgrades'");
                blacklist.add("ItemPoolDefinition'GD_Jack.WeaponPools.Pool_Weapons_AssaultRifles_01_JackBots_Common'");
                blacklist.add("ItemPoolDefinition'GD_JacksBodyDouble.WeaponPools.Pool_Weapons_HyperionSMG_02_Uncommon'");
                blacklist.add("ItemPoolDefinition'GD_JohnMamaril.WeaponPools.JohnMamarilAssaultUse'");
                blacklist.add("ItemPoolDefinition'GD_JohnMamaril.WeaponPools.JohnMamarilVeryRarePistolUse'");
                blacklist.add("ItemPoolDefinition'GD_Knight_Paladin.Shields.Pool_Shields_Standard_EnemyPaladin_Use'");
                blacklist.add("ItemPoolDefinition'GD_MarshallFriedman.WeaponPools.Weapons_SniperRifles_Marshall'");
                blacklist.add("ItemPoolDefinition'GD_MordecaiNPC.WeaponPools.Pool_Weapons_SniperRifles_Mordecai'");
                blacklist.add("ItemPoolDefinition'GD_Sage_Hammerlock.WeaponPools.Pool_Weapons_SniperRifles_Hammerlock'");
                blacklist.add("ItemPoolDefinition'GD_Spider_ClaptrapWand_Proto.Shields.Pool_Shields_Standard_EnemySpider_Use'");
                blacklist.add("ItemPoolDefinition'GD_WizardShared.Shields.Pool_Shields_Standard_EnemyWizard_Use'");
                blacklist.add("ItemPoolDefinition'GD_Z2_OverlookedData.ItemPool.IP_MO_Overlooked_Meds'");
                // These pools will delete items if I edit them
                blacklist.add("CrossDLCItemPoolDefinition'GD_Lobelia_Itempools.WeaponPools.Pool_Lobelia_Pearlescent_Weapons_All'");
                blacklist.add("ItemPoolDefinition'GD_Aster_ItemPools.GrenadeModPools.Pool_SpellGrenade_0_All'");
                blacklist.add("CrossDLCItemPoolDefinition'GD_Gladiolus_Itempools.Raid.Pool_Iris_Raid1_PinkWeapons_Revised'");
                blacklist.add("CrossDLCItemPoolDefinition'GD_Gladiolus_Itempools.Raid.Pool_Orchid_Raid1_PinkWeapons_Revised'");
                blacklist.add("CrossDLCItemPoolDefinition'GD_Gladiolus_Itempools.Raid.Pool_Orchid_Raid3_PinkWeapons_Revised'");
                blacklist.add("CrossDLCItemPoolDefinition'GD_Gladiolus_Itempools.Raid.Pool_Sage_Raid1_PinkWeapons_Revised'");
            } else {
                blacklist.add("ItemPoolDefinition'Evyn_Test.WeaponPools.Pool_Weapons_Pistols_Ice'");
                blacklist.add("ItemPoolDefinition'Evyn_Test.WeaponPools.Pool_Weapons_SMG_Ice'");
                blacklist.add("ItemPoolDefinition'GD_Co_EasterEggs.Excalibastard.ItemPool_Excalibastard'");
                blacklist.add("ItemPoolDefinition'GD_DahlShared.WeaponPools.Pool_Dahl_Shotguns_SMGS_NoScheduling'");
                blacklist.add("ItemPoolDefinition'GD_ItemPools_Shop.HealthShop.HealthShop_InstaHealth_1'");
                blacklist.add("ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_StorageDeckUpgrades'");
                blacklist.add("ItemPoolDefinition'GD_Ma_AdPopup.Pool_Grenades_AdPopup'");
                blacklist.add("ItemPoolDefinition'GD_Ma_AdPopup.Pool_Health_AdPopup'");
                blacklist.add("ItemPoolDefinition'GD_Ma_AdPopup.Pool_HyperionWeapons_AdPopup'");
                blacklist.add("ItemPoolDefinition'GD_Ma_ItemPools.WeaponPools.Pool_Weapons_All_Glitch_Grinder_Marigold'");
                blacklist.add("ItemPoolDefinition'GD_Ma_SH4D0W-TP.ItemPool.ItemPool_ShadowTrapBlaster'");
                blacklist.add("ItemPoolDefinition'GD_Ma_ShadowClone.ItemPool.ItemPool_ShadowCloneBlaster'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_AmmoPickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_DamagePickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_DefensePickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_ElementalPickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_HealthPickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_MeleePickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_OxygenPickup'");
                blacklist.add("ItemPoolDefinition'GD_Moxxtails.ItemPools.ItemPool_SpeedPickup'");
                blacklist.add("ItemPoolDefinition'GD_Prototype_Dummy.ItemPools.MiniTurret_Weapon'");
                blacklist.add("ItemPoolDefinition'GD_SpacemanDeadlift.WeaponPools.Pool_Weapons_Deadlift_Shocklaser'");
                
                blacklist.add("ItemPoolDefinition'GD_Ma_ItemPools.Cypress.CypressGunsAndGear_All'");
                blacklist.add("ItemPoolDefinition'GD_Pet_ItemPools.Pool_AllPetuniaGear'");
            }
        }
        
        public void accept(Dump itemDump) {
            bar.setValue(bar.getValue() + 1);
            
            String itemName = itemDump.getFullyQuantizedName();
            if (modified.contains(itemName)
                || blacklist.contains(itemName)
                || itemName.contains("EnemyUse")) {
                
                return;
            }
            
            BorderlandsObject currentObject = BorderlandsObject.parseObject(
                itemDump,
                "BalancedItems"
            );
            if (applyModel) {
                currentModel.applyTo(currentObject);
            }
            BorderlandsArray allItems = currentObject
                .getArrayField("BalancedItems");
            
            if (allItems == null) {
                return;
            }
            
            boolean changed = false;
            for (int i = 0; i < allItems.size(); i++) {
                BorderlandsStruct item = (BorderlandsStruct) allItems.get(i);
                String invDef = item.getString("InvBalanceDefinition");
                
                if (invDef == null
                    || invDef.equals("None")
                    || invDef.contains(manuRelic)
                    || invDef.contains("EnemyUse") // Shield Boosters
                    || invDef.contains("CustomItemPools") // Skins
                    || invDef.contains("GD_CustomItems") // SDUs
                    || invDef.contains("SeraphCrystal")
                    || invDef.contains("ShieldChargerPickup")
                    || invDef.contains("TorgueToken")
                ) {

                    continue;
                }

                String dump = DataManager.getDump(invDef);
                if (dump == null) {
                    continue;
                }

                BorderlandsObject manuObject = BorderlandsObject.parseObject(
                    dump,
                    "Manufacturers",
                    "InventoryDefinition",
                    "RuntimePartListCollection"
                );
                if (applyModel) {
                    currentModel.applyTo(manuObject);
                }

                BorderlandsArray allManus = manuObject
                    .getArrayField("Manufacturers");
                
                if (allManus != null) {
                    // Items with multiple manufacturers have a different method
                    if (allManus.size() > 1) {
                        multiManu(invDef);
                        continue;
                    }

                    String manu = ((BorderlandsStruct) allManus.get(0))
                        .getString("Manufacturer");

                    // We need to allow money as well as stuff like ammo
                    if (manu.contains(manuClass)
                        || manu.contains("GD_Currency.Manufacturers.Cash_Manufacturer")
                        || manu.contains("GD_Manufacturers.Manufacturers.Stock")) {

                        continue;
                    }
                } else {
                    // As a backup we can try check the weapon name
                    if (!invDef.startsWith("WeaponBalanceDefinition")) {
                        continue;
                    }
                    
                    BorderlandsObject partList = BorderlandsObject.parseObject(
                        DataManager.getDump(
                            manuObject.getStringField("RuntimePartListCollection")
                        ),
                        "AssociatedWeaponType"
                    );
                    if (applyModel) {
                        currentModel.applyTo(partList);
                    }

                    String type = partList.getStringField("AssociatedWeaponType")
                            .toLowerCase();
                    if (type.contains(manuName.toLowerCase())) {
                        continue;
                    }
                }

                changed = true;
                modified.add(itemName);
                item.set("InvBalanceDefinition", "InventoryBalanceDefinition'GD_ItemGrades.Currency.ItemGrade_Currency_Money_Big'");
            }
            
            if (changed) {
                saveAndSortCommand(new PCommand(
                    itemName,
                    "BalancedItems",
                    allItems.toString()
                ));
            }
        }
        
        private void multiManu(String clas) {
            if (modified.contains(clas)) {
                return;
            }
            
            BorderlandsObject currentObject = BorderlandsObject.parseObject(
                DataManager.getDump(clas),
                "Manufacturers"
            );
            if (applyModel) {
                currentModel.applyTo(currentObject);
            }
            BorderlandsArray allManus = currentObject
                .getArrayField("Manufacturers");
            
            for (int i = 0; i < allManus.size(); i++) {
                String manu = ((BorderlandsStruct) allManus.get(i)).getString("Manufacturer");
                if (!(manu.contains(manuClass)
                    || manu.contains("GD_Currency.Manufacturers.Cash_Manufacturer")
                    || manu.contains("GD_Manufacturers.Manufacturers.Stock"))) {
                    
                    modified.add(clas);
                    saveAndSortCommand(new PHotfix(
                        currentObject.getFullyQuantizedName(),
                        String.format(
                            "Manufacturers[%d].Grades[0].GameStageRequirement.MinGameStage",
                            i
                        ),
                        "500",
                        HotfixType.LEVEL,
                        "",
                        "LimitTo" + manuName
                    ));
                }
            }
        }
        
        private void saveAndSortCommand(PCommand command) {
            String name = command.getObject().toLowerCase();
            if (name.contains("weapon")) {
                guns.addChild(command);
            } else if (name.contains("shield")) {
                shields.addChild(command);
            } else if (name.contains("grenade")) {
                grenades.addChild(command);
            } else if (name.contains("classmod")) {
                classMods.addChild(command);
            } else if (name.contains("artifact") || name.contains("moonitem")) {
                relics.addChild(command);
            } else {
                misc.addChild(command);
            }
        }
    }
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
        private JProgressBar bar;
        private String manuClass;
        private HashSet<String> blackList;
        public ClassModDefinition(
            PCategory classMods,
            JProgressBar bar,
            Manufacturer manu
        ) {
            this.classMods = classMods;
            this.bar = bar;
            manuClass = manu.getClas();
            
            blackList = new HashSet<String>();
            blackList.add("ClassModDefinition'WillowGame.Default__ClassModDefinition'");
            blackList.add("CrossDLCClassModDefinition'WillowGame.Default__CrossDLCClassModDefinition'");
        }
        
        public void accept(Dump itemDump) {
            bar.setValue(bar.getValue() + 1);
            
            if (blackList.contains(itemDump.getFullyQuantizedName())) {
                return;
            }
            
            BorderlandsObject item = BorderlandsObject.parseObject(
                itemDump,
                "ManufacturerOverride"
            );
            if (!item.getStringField("ManufacturerOverride").contains(manuClass)) {
                classMods.addChild(new PCommand(String.format(
                    "set %s RequiredPlayerClass GD_PlayerClassId.FakeChar",
                    item.getFullyQuantizedName()
                )));
            }
        }
    }
}
