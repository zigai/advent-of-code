import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Scanner;

public class main_00 {
    public static ArrayList<String> read_file(String filename) {
        ArrayList<String> lines = new ArrayList<String>();
        try {
            File file = new File(filename);
            Scanner file_reader = new Scanner(file);
            while (file_reader.hasNextLine()) {
                String data = file_reader.nextLine();
                lines.add(data);
            }
            file_reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return lines;
    }

    public static long part_1(ArrayList<String> data) {

    }

    public static void part_2(ArrayList<String> data) {

    }

    public static void main(String[] args){
        ArrayList<String> data = read_file("./input");
        part_1(data);
        part_2(data);
    }
}
