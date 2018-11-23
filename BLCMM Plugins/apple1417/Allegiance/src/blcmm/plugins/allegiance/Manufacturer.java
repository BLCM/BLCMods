package blcmm.plugins.allegiance;

// Who would've guessed this might be important to an allegiance generator
public enum Manufacturer {
    BANDIT("Bandit/Scav", "GD_Manufacturers.Manufacturers.Bandit"),
    DAHL("Dahl", "GD_Manufacturers.Manufacturers.Dahl"),
    HYPERION("Hyperion", "GD_Manufacturers.Manufacturers.Hyperion"),
    JAKOBS("Jakobs", "GD_Manufacturers.Manufacturers.Jakobs"),
    MALIWAN("Maliwan", "GD_Manufacturers.Manufacturers.Maliwan"),
    TEDIORE("Tediore", "GD_Manufacturers.Manufacturers.Tediore"),
    TORGUE("Torgue", "GD_Manufacturers.Manufacturers.Torgue"),
    VLADOF("Vladof", "GD_Manufacturers.Manufacturers.Vladof"),
    ANSHIN("Anshin", "GD_Manufacturers.Manufacturers.Anshin"),
    ERIDIAN("Eridian", "GD_Manufacturers.Artifacts."),
    MOXXI("Moxxi", "GD_Manufacturers.Manufacturers.Moxxi"),
    STOCK("Stock", "GD_Manufacturers.Manufacturers.Stock"),
    PANGOLIN("Pangolin", "GD_Manufacturers.Manufacturers.Pangolin");
    
    
    private String name;
    private String clas;
    private Manufacturer(String name, String clas) {
        this.name = name;
        this.clas = clas;
    }
    
    public static Manufacturer fromInt(int i) {
        return values()[i];
    }
    
    public String toString() {
        return name;
    }

    public String getClas() {
        return clas;
    }
}
