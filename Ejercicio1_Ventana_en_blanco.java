import javax.swing.JFrame;
import javax.swing.WindowConstants;

public class Ejercicio1_Ventana_en_blanco extends JFrame {

    public Ejercicio1_Ventana_en_blanco() {
        setTitle("Juego de dados");            // corregido
        setSize(600, 500);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);           // centra la ventana en pantalla (opcional)
    }

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(() -> {
            Ejercicio1_Ventana_en_blanco ventana = new Ejercicio1_Ventana_en_blanco();
            ventana.setVisible(true);
        });
    }
}