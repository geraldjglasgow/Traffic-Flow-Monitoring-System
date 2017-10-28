import java.io.File;
import java.io.FileFilter;
public class ProcessData {

    String PATH = "/Users/SSLGhost/Desktop/Test5/";
    private void get_locations() {
        File file = new File(PATH);
        File[] files = file.listFiles(new FileFilter() {
            @Override
            public boolean accept(File f) {
                return f.isDirectory();
            }
        });
        System.out.println("Folders count: " + files.length);
    }


}
