package blcmm.plugins.allegiance;

import blcmm.data.lib.DataManager;
import blcmm.model.HotfixType;
import blcmm.model.assist.BLCharacter;
import javax.swing.JRadioButton;
import javax.swing.ButtonModel;
import java.util.HashMap;
import java.util.EnumSet;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PHotfix;
import javax.swing.DefaultComboBoxModel;

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
        moxxiButton.setEnabled(!isBL2);
        EnumSet<BLCharacter> characters = isBL2 ? BLCharacter.BL2Chars
                                                : BLCharacter.TPSChars;
        DefaultComboBoxModel<String> model = new DefaultComboBoxModel<String>();
        for (BLCharacter blChar : characters) {
            model.addElement(blChar.getCharacterName());
        }
        charComboBox.setModel(model);

        JRadioButton[] manuButtons = {
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
        if (buttonGroup.getSelection() == null) {return null;}
        Manufacturer manu = manuMap.get(buttonGroup.getSelection());
        BLCharacter blChar = BLCharacter.values()[
                charComboBox.getSelectedIndex() + (isBL2 ? 0 : 6)];
        
        PCategory root = new PCategory(String.format(
            "%s Allegiance (No %s)",
            manu.toString(),
            blChar.getCharacterName()
        ));
        
        // This will deal with everything but class mods and moxxtails
        DataManager.streamAllDumpsOfClassAndSubclasses("InventoryBalanceDefinition",
                new InventoryDumpProcessor(manu, root));
        /*
          "ClassModBalanceDefinition"s don't include a manufacturer, instead they
           contain a list of "ClassModDefinition"s, which each contain a
           "ManufacturerOverride"
          Because of this different format they need their own dump processor
        */
        DataManager.streamAllDumpsOfClassAndSubclasses("ClassModBalanceDefinition",
                new ClassModDumpProcessor(manu, root, blChar));
        
        /*
          Moxxtails are a UsableItemDefinition so they won't be picked up by
           InventoryDumpProcessor, and they also need hotfixes, which it can't
           deal with, so we do them here instead
          There are also few enough that I can hardcode them
        */
        if (!DataManager.getBL2() && manu != Manufacturer.MOXXI) {
            String[] allMoxxtails = new String[] {
                "GD_Moxxtails.Balance.ItemGrade_AmmoPickup",
                "GD_Moxxtails.Balance.ItemGrade_DamagePickup",
                "GD_Moxxtails.Balance.ItemGrade_DefensePickup",
                "GD_Moxxtails.Balance.ItemGrade_ElementalPickup",
                "GD_Moxxtails.Balance.ItemGrade_HealthPickup",
                "GD_Moxxtails.Balance.ItemGrade_MeleePickup",
                "GD_Moxxtails.Balance.ItemGrade_OxygenPickup",
                "GD_Moxxtails.Balance.ItemGrade_SpeedPickup"
            };
            for (String moxxtail : allMoxxtails) {
             root.addChild(new PHotfix(
                     moxxtail,
                     "Manufacturers",
                     "(Manufacturer=ManufacturerDefinition'GD_Manufacturers.Manufacturers.Moxxi',Grades=((GradeModifiers=(ExpLevel=10,CustomInventoryDefinition=None),GameStageRequirement=(MinGameStage=81,MaxGameStage=100),MinSpawnProbabilityModifier=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),MaxSpawnProbabilityModifier=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000))))",
                     HotfixType.LEVEL,
                     "Spaceport_P",
                     "DisableMoxxtails"
             ));
            }
        }
        return root;
    }
}
