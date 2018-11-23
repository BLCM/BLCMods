package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsArray;
import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.BorderlandsStruct;
import blcmm.data.lib.DataManager.Dump;
import blcmm.model.assist.BLCharacter;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PCommand;
import java.util.function.Consumer;
import java.util.HashSet;

// This class looks over each item and locks it if necessary
public class InventoryDumpProcessor implements Consumer<Dump> {
    private String limitChar;
    private String manuClass;
    private PCategory root;
    private HashSet<String> modified;
    public InventoryDumpProcessor( BLCharacter blChar, Manufacturer manu,
            PCategory root) {
        limitChar = "set %s RequiredPlayerClass GD_PlayerClassId."
                + blChar.getCharacterClass();
        manuClass = manu.getClas();
        this.root = root;
        modified = new HashSet<String>();
    }
    
    public void accept(Dump dump) {
        BorderlandsObject item = BorderlandsObject.parseObject(
            dump,
            "Manufacturers",
            "InventoryDefinition"
        );
        
        /*
          Don't think there's anything with multiple manufacturers but let's be
           safe
        */
        boolean useableItem  = true;
        BorderlandsArray<BorderlandsStruct> manus = item.getArrayField("Manufacturers");
        if (manus != null) {
            for (int i = 0; i < manus.size(); i++) {
                String manu = manus.get(i).getString("Manufacturer");
                if (!manu.contains(manuClass)) {
                    useableItem = false;
                }
            }
            if (!useableItem) {
                String invDef = item.getField("InventoryDefinition").toString();
                // More exceptions to come...
                if (!modified.contains(invDef)
                    && !invDef.startsWith("MissionItemDefinition")
                    && !invDef.equals("None")) {
                    modified.add(invDef);
                    root.addChild(new PCommand(String.format(limitChar, invDef)));
                }
            }
        }
    }
}
