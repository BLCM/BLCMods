package blcmm.plugins.allegiance;

import blcmm.plugins.BLCMMModelPlugin;
import blcmm.plugins.pseudo_model.PCategory;
import javax.swing.JPanel;
import javax.swing.JProgressBar;

// Not much going on here, just overwriting the required stuff
public class Allegiance extends BLCMMModelPlugin {
    AllegiancePanel panel;
    public Allegiance() {
        super(true, true, "apple1417", "0.1");
    }

    @Override
    public String getName() {
        return "Allegiance Forcer";
    }

    @Override
    public JPanel getGUI() {
        panel = new AllegiancePanel();
        return panel;
    }

    @Override
    public String[] getRequiredDataClasses() {
        return new String[] {
            "InventoryBalanceDefinition",
            "ManufacturerDefinition",
            "PlayerClassIdentifierDefinition"
        };
    }

    @Override
    public PCategory getOutputModel() {
        return panel.generate();
    }

    @Override
    public JProgressBar getProgressBar() {
        return null;
    }
}
