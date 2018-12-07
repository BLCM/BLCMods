package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.BorderlandsStruct;
import blcmm.data.lib.DataManager;
import blcmm.model.HotfixType;
import javax.swing.JRadioButton;
import javax.swing.ButtonModel;
import java.util.HashMap;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PCommand;
import blcmm.plugins.pseudo_model.PHotfix;
import javax.swing.JProgressBar;
import javax.swing.event.ChangeEvent;

/*
  So while netbeans may have let me import the default project all nicely, it's
   form creator sucks and won't let me properly edit the auto-generated one
  Because of that, and because its code is messy, I wrap it in this class
*/
public class AllegiancePanel extends AllegiancePanelGenerated {
    private HashMap<ButtonModel, Manufacturer> manuMap;
    private boolean isBL2;
    private JProgressBar bar;
    public AllegiancePanel() {
        super();
        
        isBL2 = DataManager.getBL2();
        eridianButton.setEnabled(isBL2);
        relicCheckBox.setEnabled(isBL2);
        moxxiButton.setEnabled(!isBL2);
        
        bar = new JProgressBar();
        bar.setValue(0);
        
        eridianButton.addChangeListener((ChangeEvent e) -> {
            if (eridianButton.isSelected()) {
                relicCheckBox.setSelected(false);
                relicCheckBox.setEnabled(false);
            } else {
                relicCheckBox.setEnabled(true);
            }
        });
        
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
    
    public JProgressBar getProgressBar() {
        return bar;
    }
    
    public PCategory generate() {
        bar.setMaximum(
            DataManager.getGetAll("ItemPoolDefinition").size()
            + DataManager.getGetAll("ClassModDefinition").size()
            + 12
        );
        
        Manufacturer manu = manuMap.get(manuButtonGroup.getSelection());
        
        PCategory root = new PCategory(String.format(
            "%s Allegiance",
            manu.toString()
        ));
        
        DataManager.streamAllDumpsOfClassAndSubclasses(
            "ItemPoolDefinition",
            new DumpProcessors.ItemPoolDefinition(
                root,
                bar,
                manu,
                relicCheckBox.isSelected(),
                applyModel.isSelected()
            )
        );

        DataManager.streamAllDumpsOfClassAndSubclasses(
            "ClassModDefinition",
            new DumpProcessors.ClassModDefinition(
                (PCategory) root.getChildren().get(3),
                bar,
                manu
            )
        );
        
        if (!isBL2 && manu != Manufacturer.MOXXI) {
            PCategory moxxtails = (PCategory) root.getChildren().get(5);
            
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
            
            for (String moxx : moxxtailClasses) {
                bar.setValue(bar.getValue() + 1);
                
                moxxtails.addChild(new PHotfix(
                    moxx,
                    "Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage",
                    "500",
                    HotfixType.LEVEL,
                    "Spaceport_P",
                    "DisableMoxxtails"
                ));
            }
        }
        
        float moneyMultiplier = (float) moneySpinner.getValue();
        if (moneyMultiplier != 1f) {
            PCategory money = new PCategory(String.format(
                "%s Money Drops (x%.1f)",
                moneyMultiplier > 1 ? "Increase" : "Decrease",
                moneyMultiplier
            ));
            root.addChild(money);
            
            String[] moneyTypes = new String[] {
                "UsableItemDefinition'GD_Currency.A_Item.Currency'",
                "UsableItemDefinition'GD_Currency.A_Item.Currency_Big'",
                "UsableItemDefinition'GD_Currency.A_Item.Currency_Crystal'",
                "UsableItemDefinition'GD_Skeleton_Crystal.A_Item.Currency_CrystalBones'"
            };

            for (int i = 0; i < moneyTypes.length; i++) {
                bar.setValue(bar.getValue() + 1);
                if (!isBL2 && i <= 3) {
                    break;
                }
                
                BorderlandsStruct itemAttributes =
                    (BorderlandsStruct) BorderlandsObject.parseObject(
                        DataManager.getDump(moneyTypes[i]),
                        "AttributeSlotEffects"
                    ).getArrayField("AttributeSlotEffects").get(0);
                
                float base = itemAttributes
                    .getStruct("BaseModifierValue")
                    .getFloat("BaseValueScaleConstant")
                    * moneyMultiplier;
                
                float grade = itemAttributes
                    .getStruct("PerGradeUpgrade")
                    .getFloat("BaseValueScaleConstant")
                    * moneyMultiplier;
                
                money.addChild(new PHotfix(
                    moneyTypes[i],
                    "AttributeSlotEffects[0].BaseModifierValue.BaseValueScaleConstant",
                    String.format("%.6f", base),
                    HotfixType.LEVEL,
                    "",
                    "IncreaseMoneyValue"
                ));
                money.addChild(new PHotfix(
                    moneyTypes[i],
                    "AttributeSlotEffects[0].PerGradeUpgrade.BaseValueScaleConstant",
                    String.format("%.6f", grade),
                    HotfixType.LEVEL,
                    "",
                    "IncreaseMoneyValue"
                ));
            }
        }
        return root;
    }
}
