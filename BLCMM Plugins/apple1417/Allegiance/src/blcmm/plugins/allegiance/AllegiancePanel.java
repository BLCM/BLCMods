package blcmm.plugins.allegiance;

import blcmm.data.lib.DataManager;
import javax.swing.JRadioButton;
import javax.swing.ButtonModel;
import javax.swing.DefaultComboBoxModel;
import java.util.HashMap;
import java.util.EnumSet;
import blcmm.model.assist.BLCharacter;
import blcmm.plugins.pseudo_model.PCategory;

/*
  So while netbeans may have let me import the default project all nicely, it's
   form creator sucks and won't let me properly edit the auto-generated one
  Because of that, and because its code is messy, I wrap it in this class
*/
public class AllegiancePanel extends AllegiancePanelGenerated {
    
    private boolean isBL2 = DataManager.getBL2();
    private HashMap<ButtonModel, Manufacturer> manuMap;
    
    public AllegiancePanel() {
        super();
        
        // We have to change some stuff based on what game it is
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
            JRadioButton10,
            moxxiButton,
            jRadioButton12,
            jRadioButton13
        };

        // Swing is awkward and won't return the enum directly so I need this
        manuMap = new HashMap<ButtonModel, Manufacturer>();
        for (int i = 0; i < manuButtons.length; i++) {
            manuMap.put(manuButtons[i].getModel(), Manufacturer.fromInt(i));
        }
    }
    
    public PCategory generate() {
        if (buttonGroup.getSelection() == null) {return null;}
        BLCharacter blChar = BLCharacter.values()[
                charComboBox.getSelectedIndex()+ (isBL2 ? 0 : 6)];
        Manufacturer manu = manuMap.get(buttonGroup.getSelection());
        
        PCategory root = new PCategory(String.format(
            "%s Allegiance (to %s)",
            manu.toString(),
            blChar.getCharacterName()
        ));
        
        InventoryDumpProcessor processor = new InventoryDumpProcessor(
            blChar, manu, root
        );

        DataManager.streamAllDumpsOfClassAndSubclasses("InventoryBalanceDefinition",
                processor);
        
        return root;
    }
}
