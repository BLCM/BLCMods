package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsArray;
import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.BorderlandsStruct;
import blcmm.data.lib.DataManager;
import blcmm.model.HotfixType;
import blcmm.model.assist.BLCharacter;
import javax.swing.JRadioButton;
import javax.swing.ButtonModel;
import java.util.HashMap;
import java.util.EnumSet;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PCommand;
import blcmm.plugins.pseudo_model.PHotfix;
import javax.swing.DefaultComboBoxModel;
import javax.swing.event.ChangeEvent;

/*
  So while netbeans may have let me import the default project all nicely, it's
   form creator sucks and won't let me properly edit the auto-generated one
  Because of that, and because its code is messy, I wrap it in this class
*/
public class AllegiancePanel extends AllegiancePanelGenerated {
    
    private HashMap<ButtonModel, Manufacturer> manuMap;
    private boolean isBL2;
    public AllegiancePanel() {
        super();
        
        isBL2 = DataManager.getBL2();
        eridianButton.setEnabled(isBL2);
        relicCheckBox.setEnabled(isBL2);
        moxxiButton.setEnabled(!isBL2);
        
        eridianButton.addChangeListener((ChangeEvent e) -> {
            if (eridianButton.isSelected()) {
                relicCheckBox.setSelected(false);
                relicCheckBox.setEnabled(false);
            } else {
                relicCheckBox.setEnabled(true);
            }
        });
        
        EnumSet<BLCharacter> characters = isBL2 ? BLCharacter.BL2Chars
                                                : BLCharacter.TPSChars;
        DefaultComboBoxModel<String> model = new DefaultComboBoxModel<String>();
        for (BLCharacter blChar : characters) {
            model.addElement(blChar.getCharacterName());
        }
        charComboBox.setModel(model);

        
        JRadioButton[] manuButtons = new JRadioButton[] {
            jRadioButton1,
            jRadioButton2,
            jRadioButton3,
            jRadioButton4,
            jRadioButton5,
            jRadioButton6,
            jRadioButton7,
            jRadioButton8,
            jRadioButton9,
            eridianButton,
            moxxiButton,
            jRadioButton12
        };

        // Swing is awkward and won't return the enum directly so I need this
        manuMap = new HashMap<ButtonModel, Manufacturer>();
        for (int i = 0; i < manuButtons.length; i++) {
            manuMap.put(manuButtons[i].getModel(), Manufacturer.fromInt(i));
        }
    }
    
    public PCategory generate() {        
        Manufacturer manu = manuMap.get(manuButtonGroup.getSelection());
        BLCharacter blChar = BLCharacter.values()[
                charComboBox.getSelectedIndex() + (isBL2 ? 0 : 6)];
        
        PCategory root = new PCategory(String.format(
            "%s Allegiance (No %s)",
            manu.toString(),
            blChar.getCharacterName()
        ));
        
        
        DataManager.streamAllDumpsOfClassAndSubclasses(
                "InventoryBalanceDefinition",
                new DumpProcessors.InventoryBalanceDefinition(root, manu,
                    relicCheckBox.isSelected())
        );
        
        DataManager.streamAllDumpsOfClassAndSubclasses(
                "ClassModDefinition",
                new DumpProcessors.ClassModDefinition(root, manu, blChar)
        );

        if (!isBL2 && manu != Manufacturer.MOXXI) {
            PCategory moxxtails = new PCategory("Moxxtails");
            root.addChild(moxxtails);
            
            String[] moxxtailClasses = new String[] {
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_AmmoPickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_DamagePickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_DefensePickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_ElementalPickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_HealthPickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_MeleePickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_OxygenPickup'",
                "InventoryBalanceDefinition'GD_Moxxtails.Balance.ItemGrade_SpeedPickup'"
            };
            // All moxxtails have the same stats so we only need to do this once
            BorderlandsArray<BorderlandsStruct> modifiedMoxxtail =
                BorderlandsObject.parseObject(
                    DataManager.getDump(moxxtailClasses[0]),
                    "Manufacturers"
                ).getArrayField("Manufacturers");
            // This is kind of a mess but I didn't want to make extra vars
            ((BorderlandsStruct)modifiedMoxxtail
                .get(0)
                .getArray("Grades")
                .get(0))
                    .getStruct("GameStageRequirement")
                    .set("MinGameStage", 500);
            
            for (String moxxtail : moxxtailClasses) {
                moxxtails.addChild(new PHotfix(
                    moxxtail,
                    "Manufacturers",
                    modifiedMoxxtail.toString(),
                    HotfixType.LEVEL,
                    "Spaceport_P",
                    "DisableMoxxtails"
                ));
            }
        }
        
        float moneyMultiplier = (float) moneySpinner.getValue();
        if (moneyMultiplier != 1f) {
            PCategory money = new PCategory(String.format(
                "Increase Money Drops (x%.2f)",
                moneyMultiplier
            ));
            root.addChild(money);
            
            String[] moneyTypes = new String[] {
                "UsableItemDefinition'GD_Currency.A_Item.Currency'",
                "UsableItemDefinition'GD_Currency.A_Item.Currency_Big'",
                "UsableItemDefinition'GD_Currency.A_Item.Currency_Crystal'"
            };

            for (int i = 0; i < moneyTypes.length; i++) {
                BorderlandsStruct itemAttributes =
                    (BorderlandsStruct) BorderlandsObject.parseObject(
                        DataManager.getDump(moneyTypes[i]),
                        "AttributeSlotEffects"
                    ).getArrayField("AttributeSlotEffects").get(0);
                
                BorderlandsStruct modifierValue = itemAttributes
                    .getStruct("BaseModifierValue");
                modifierValue.set("BaseValueScaleConstant",
                    modifierValue.getFloat("BaseValueScaleConstant")
                    * moneyMultiplier);
                
                BorderlandsStruct gradeUpgrade = itemAttributes
                    .getStruct("PerGradeUpgrade");
                gradeUpgrade.set("BaseValueScaleConstant",
                    gradeUpgrade.getFloat("BaseValueScaleConstant")
                    * moneyMultiplier);
                
                money.addChild(new PCommand(String.format(
                    "set %s AttributeSlotEffects (%s)",
                     moneyTypes[i],
                     itemAttributes.toString()
                )));
            }
            
            // The crystal bones need a hotfix so we have to do this all again
            if (isBL2) {
                String moneyType = "UsableItemDefinition'GD_Skeleton_Crystal.A_Item.Currency_CrystalBones'";
                BorderlandsArray<BorderlandsStruct> itemAttributes =
                    BorderlandsObject.parseObject(
                        DataManager.getDump(moneyType),
                        "AttributeSlotEffects"
                    ).getArrayField("AttributeSlotEffects");
                
                BorderlandsStruct modifierValue = itemAttributes.get(0)
                    .getStruct("BaseModifierValue");
                modifierValue.set("BaseValueScaleConstant",
                    modifierValue.getFloat("BaseValueScaleConstant")
                    * moneyMultiplier);
                
                BorderlandsStruct gradeUpgrade = itemAttributes.get(0)
                    .getStruct("PerGradeUpgrade");
                gradeUpgrade.set("BaseValueScaleConstant",
                    gradeUpgrade.getFloat("BaseValueScaleConstant")
                    * moneyMultiplier);
                
                money.addChild(new PHotfix(
                    moneyType,
                    "AttributeSlotEffects",
                    itemAttributes.toString(),
                    HotfixType.LEVEL,
                    "",
                    "IncreaseCrystalBoneValue"
                ));
            }
        }
        return root;
    }
}
