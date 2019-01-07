package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.BorderlandsStruct;
import blcmm.data.lib.DataManager;
import blcmm.model.HotfixType;
import blcmm.plugins.BLCMMPlugin;
import javax.swing.JCheckBox;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PHotfix;
import java.util.HashSet;
import javax.swing.JProgressBar;
import javax.swing.event.ChangeEvent;
import plugins.pseudo_model.ApplyablePModel;

/*
  So while netbeans may have let me import the default project all nicely, it's
   form creator sucks and won't let me properly edit the auto-generated one
  Because of that, and because its code is messy, I wrap it in this class
*/
public class AllegiancePanel extends AllegiancePanelGenerated {
    private boolean updateInProgress = false;
    private boolean isBL2;
    private JCheckBox[] manuCheckBoxes;
    
    private JProgressBar bar;
    private ApplyablePModel currentModel;
    
    public AllegiancePanel() {
        super();
        
        // Enable some stuff based on game
        isBL2 = DataManager.getBL2();
        eridianCheckBox.setEnabled(isBL2);
        relicCheckBox.setEnabled(isBL2);
        moxxiCheckBox.setEnabled(!isBL2);
        
        bar = new JProgressBar();
        bar.setValue(0);
        
        manuCheckBoxes = new JCheckBox[] {
            banditCheckBox,
            dahlCheckBox,
            hyperionCheckBox,
            jakobsCheckBox,
            maliwanCheckBox,
            tedioreCheckBox,
            torgueCheckBox,
            vladofCheckBox,
            anshinCheckBox,
            eridianCheckBox,
            moxxiCheckBox,
            pangolinCheckBox
        };
        
        // No point in letting you select this if relics are already allowed
        eridianCheckBox.addChangeListener((ChangeEvent e) -> {
            if (eridianCheckBox.isSelected()) {
                relicCheckBox.setSelected(false);
                relicCheckBox.setEnabled(false);
            } else {
                relicCheckBox.setEnabled(true);
            }
        });
        
        // Sync values
        moneySpinner.addChangeListener((ChangeEvent e) -> {
            if (!updateInProgress) {
                updateInProgress = true;
                
                float value = (float) moneySpinner.getValue();
                moneySlider.setValue((int) (Math.log10(value) * 50f));
                
                updateInProgress = false;
            }
        });
        moneySlider.addChangeListener((ChangeEvent e) -> {
            if (!updateInProgress) {
                updateInProgress = true;

                int value = moneySlider.getValue();
                moneySpinner.setValue(Math.round(Math.pow(10, value / 50f) * 10) / 10f);

                updateInProgress = false;
            }
        });
        
        convertSpinner.addChangeListener((ChangeEvent e) -> {
            if (!updateInProgress) {
                updateInProgress = true;

                convertSlider.setValue((int) convertSpinner.getValue());
                
                updateInProgress = false;
            }
        });
        convertSlider.addChangeListener((ChangeEvent e) -> {
            if (!updateInProgress) {
                updateInProgress = true;
                
                convertSpinner.setValue(convertSlider.getValue());
                
                updateInProgress = false;
            }
        });
    }
    
    public JProgressBar getProgressBar() {
        return bar;
    }
    
    public PCategory generate() {
        if (modelCheckBox.isSelected()) {
            currentModel = new ApplyablePModel(BLCMMPlugin.getCurrentlyOpenedBLCMMModel());
        } else {
            // This creates an empty model that won't change anything
            currentModel = new ApplyablePModel(new PCategory(""));
        }
        
        String allManuNames = "";
        HashSet<Manufacturer> selectedManus = new HashSet<Manufacturer>();
        for (int i = 0; i < manuCheckBoxes.length; i++) {
            if (manuCheckBoxes[i].isSelected()) {
                Manufacturer manu = Manufacturer.fromInt(i);
                allManuNames += ", " + manu.toString();
                selectedManus.add(manu);
            }
        }
        
        /*
          If (for some reason) you have all manufacturers selected then we don't
           actually have to generate anything (except maybe money)
        */
        if (selectedManus.size() >= 11) {
            return generateMoney();
        }
        
        // TODO: When it's available move this to the new size method
        bar.setMaximum(
            DataManager.getGetAll("ItemPoolDefinition").size()
            + DataManager.getGetAll("ClassModDefinition").size()
            + 12
        );
        
        PCategory root = new PCategory(String.format(
            "Allegiance Forcer (%s)",
            // Get rid of the inital ", "
            allManuNames.substring(2)
        ));
        
        DataManager.streamAllDumpsOfClassAndSubclasses(
            "ItemPoolDefinition",
            new DumpProcessors.ItemPoolDefinition(
                root,
                bar,
                currentModel,
                selectedManus,    
                relicCheckBox.isSelected(),
                (int) convertSpinner.getValue() / 100f
            )
        );

        DataManager.streamAllDumpsOfClassAndSubclasses(
            "ClassModDefinition",
            new DumpProcessors.ClassModDefinition(
                (PCategory) root.getChildren().get(3),
                bar,
                currentModel,
                selectedManus
            )
        );
        
        // Some small extra things that don't need a full dump
        if (!isBL2 && !selectedManus.contains(Manufacturer.MOXXI)) {
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
        
        PCategory money = generateMoney();
        if (money != null) {
            root.addChild(money);
        }
                
        return root;
    }
    
    // We want to call this from more than one spot so it's a function
    private PCategory generateMoney() {
        float moneyMultiplier = (float) moneySpinner.getValue();
        if (moneyMultiplier == 1f) {
            return null;
        }
        
        PCategory money = new PCategory(String.format(
            "%s Money Drops Value (x%.1f)",
            moneyMultiplier > 1 ? "Increase" : "Decrease",
            moneyMultiplier
        ));

        String[] moneyTypes = new String[] {
            "UsableItemDefinition'GD_Currency.A_Item.Currency'",
            "UsableItemDefinition'GD_Currency.A_Item.Currency_Big'",
            "UsableItemDefinition'GD_Currency.A_Item.Currency_Crystal'",
            "UsableItemDefinition'GD_Skeleton_Crystal.A_Item.Currency_CrystalBones'"
        };

        for (int i = 0; i < moneyTypes.length; i++) {
            bar.setValue(bar.getValue() + 1);
            if (!isBL2 && i >= 3) {
                break;
            }

            BorderlandsObject obj = BorderlandsObject.parseObject(
                DataManager.getDump(moneyTypes[i]),
                "AttributeSlotEffects"
            );
            currentModel.applyTo(obj);
            BorderlandsStruct itemAttributes = (BorderlandsStruct)
                    obj.getArrayField("AttributeSlotEffects").get(0);

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
        return money;
    }
}
