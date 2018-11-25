package blcmm.plugins.allegiance;

/**
 * A main class that simply lets a dialog pop up with the plugin that you made.
 *
 * @author LightChaosman
 */
public class Test {

    /**
     * @param args the command line arguments
     * @throws java.lang.Exception
     */
    public static void main(String[] args) throws Exception {
        //Set the look and feel to match that of BLCMM.
        //The colors won't match, but the shapes will.
        //If the GUI looks good in this project, it will also look good when run trough BLCMM
        for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
            if ("Nimbus".equals(info.getName())) {
                javax.swing.UIManager.setLookAndFeel(info.getClassName());
                break;
            }
        }

        blcmm.plugins.BLCMMPlugin plugin = new Allegiance();
        javax.swing.JFrame frame = new javax.swing.JFrame();
        frame.setTitle(plugin.getName());
        frame.getContentPane().add(plugin.getGUI());
        frame.pack();
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
    }

}
