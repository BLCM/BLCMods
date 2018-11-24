package blcmm.plugins.allegiance;

import blcmm.data.lib.BorderlandsArray;
import blcmm.data.lib.BorderlandsObject;
import blcmm.data.lib.DataManager;
import blcmm.data.lib.DataManager.Dump;
import blcmm.model.assist.BLCharacter;
import blcmm.plugins.pseudo_model.PCategory;
import blcmm.plugins.pseudo_model.PCommand;
import java.util.HashSet;
import java.util.function.Consumer;

// This class locks class mods, as they have a different format
public class ClassModDumpProcessor implements Consumer<Dump> {
    private String manuClass;
    private PCategory root;
    private String limitChar;
    private HashSet<String> modified;
    public ClassModDumpProcessor(Manufacturer manu, PCategory root, BLCharacter blChar) {
        manuClass = manu.getClas();
        this.root = root;
        limitChar = "set %s RequiredPlayerClass GD_PlayerClassId."
                + blChar.getCharacterClass();
        modified = new HashSet<String>();
    }
    
    public void accept(Dump dump) {
        BorderlandsArray<String> allMods = BorderlandsObject.parseObject(
            dump,
            "ClassModDefinitions"
        ).getArrayField("ClassModDefinitions");
        if (allMods == null) {
            return;
        }
        
        for (String modClass : allMods) {
            BorderlandsObject mod = BorderlandsObject.parseObject(
                DataManager.getDump(modClass),
                "ManufacturerOverride"
            );
            if (!mod.getStringField("ManufacturerOverride").contains(manuClass)
                 && !modified.contains(mod.getFullyQuantizedName())) {
                root.addChild(new PCommand(String.format(
                    limitChar, mod.getFullyQuantizedName()
                )));
                modified.add(mod.getFullyQuantizedName());
            }
        }
    }
}
