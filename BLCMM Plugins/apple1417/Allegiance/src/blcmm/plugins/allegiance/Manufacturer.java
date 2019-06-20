package blcmm.plugins.allegiance;

// Who would've guessed this might be important to an allegiance generator

import blcmm.data.lib.DataManager;

public enum Manufacturer {
    BANDIT("Bandit", "GD_Manufacturers.Manufacturers.Bandit",
        "GD_Artifacts.A_Item.A_AllegianceA"),
    DAHL("Dahl", "GD_Manufacturers.Manufacturers.Dahl",
        "GD_Artifacts.A_Item.A_AllegianceB"),
    HYPERION("Hyperion", "GD_Manufacturers.Manufacturers.Hyperion",
        "GD_Artifacts.A_Item.A_AllegianceC"),
    JAKOBS("Jakobs", "GD_Manufacturers.Manufacturers.Jakobs",
        "GD_Artifacts.A_Item.A_AllegianceD"),
    MALIWAN("Maliwan", "GD_Manufacturers.Manufacturers.Maliwan",
        "GD_Artifacts.A_Item.A_AllegianceE"),
    TEDIORE("Tediore", "GD_Manufacturers.Manufacturers.Tediore",
        "GD_Artifacts.A_Item.A_AllegianceF"),
    TORGUE("Torgue", "GD_Manufacturers.Manufacturers.Torgue",
        "GD_Artifacts.A_Item.A_AllegianceG"),
    VLADOF("Vladof", "GD_Manufacturers.Manufacturers.Vladof",
        "GD_Artifacts.A_Item.A_AllegianceH"),
    ANSHIN("Anshin", "GD_Manufacturers.Manufacturers.Anshin", ""),
    ERIDIAN("Eridian", "GD_Manufacturers.Artifacts.", ""),
    MOXXI("Moxxi", "GD_Manufacturers.Manufacturers.Moxxi", ""),
    PANGOLIN("Pangolin", "GD_Manufacturers.Manufacturers.Pangolin", "");
    
    
    private String name;
    private String clas;
    private String relic;
    private Manufacturer(String name, String clas, String relic) {
        this.name = name;
        this.clas = clas;
        this.relic = relic;
    }
    
    public static Manufacturer fromInt(int i) {
        return values()[i];
    }
    
    public String toString() {
        if (name.equals("Bandit") && !DataManager.getBL2()) {
            return "Scav";
        }
        return name;
    }
    public String getBaseName() {
        return name;
    }

    public String getClas() {
        return clas;
    }
    
    public String getRelic() {
        return relic;
    }
}
