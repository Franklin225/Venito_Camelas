import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.WindowConstants;
import javax.swing.ImageIcon;
import javax.swing.SwingUtilities;
import java.io.File;
import java.net.URL;

public class Ejercicio2_Ventana_con_dado extends JFrame {

    public Ejercicio2_Ventana_con_dado() {
        // Título
        setTitle("Juego de dados");

        // Tamaño y cierre
        setSize(600, 500);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        // Usamos layout null porque colocamos componentes con setBounds(...)
        getContentPane().setLayout(null);

        // Crear etiqueta para mostrar la imagen del dado
        JLabel lbldado1 = new JLabel();

        // Ruta como recurso en classpath (recomendada si pones la carpeta imagenes dentro de src)
        String recursoClasspath = "/imágenes a usar/Clase#1/5.jpg";
        ImageIcon imgDado = null;

        // Intentar cargar desde recursos (classpath)
        URL imgURL = getClass().getResource(recursoClasspath);
        if (imgURL != null) {
            imgDado = new ImageIcon(imgURL);
        } else {
            // Si no está como recurso, intentar ruta relativa en el sistema de archivos
            File f = new File("imagenes/4.jpg");
            if (f.exists()) {
                imgDado = new ImageIcon(f.getPath());
            }
        }

        // Si se cargó la imagen correctamente, ponerla y usar sus dimensiones.
        if (imgDado != null && imgDado.getIconWidth() > 0) {
            lbldado1.setIcon(imgDado);
            lbldado1.setBounds(10, 10, imgDado.getIconWidth(), imgDado.getIconHeight());
        } else {
            // Si no se encontró la imagen, mostrar un texto informativo
            lbldado1.setText("Imagen no encontrada: imagenes/4.jpg");
            lbldado1.setBounds(10, 10, 400, 30);
        }

        getContentPane().add(lbldado1);

        // Centrar ventana en pantalla
        setLocationRelativeTo(null);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Ejercicio2_Ventana_con_dado ventana = new Ejercicio2_Ventana_con_dado();
            ventana.setVisible(true);
        });
    }
}
