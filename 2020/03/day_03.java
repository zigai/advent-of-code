import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Scanner;

public class main_03 {
    public static LinkedList<String> read_file(String filename) {
        LinkedList<String> listOfFiles = new LinkedList<String>();
        try {
            File file = new File(filename);
            Scanner file_reader = new Scanner(file);
            while (file_reader.hasNextLine()) {
                String data = file_reader.nextLine();
                listOfFiles.add(data);
            }
            file_reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return listOfFiles;
    }

    public static long solve(int horizontal_step, int vertical_step) {
        LinkedList<String> data = read_file("./input.txt");
        int num_of_lines = data.size();
        int len_of_line = data.get(0).length();
        int horizontal_pos = 0;
        int tree_count = 0;

        for (int i = 0; i< num_of_lines; i+=vertical_step) {
            if (horizontal_pos > len_of_line - 1) {
                horizontal_pos = horizontal_pos - len_of_line;
            }
            if (i + (vertical_step - 1) < num_of_lines){
                char y = data.get(i).charAt(horizontal_pos);
                if (y == '#') {
                    tree_count++;
                }
            }
            horizontal_pos += horizontal_step;
        }
        return tree_count;
    }

    public static void solve_part_2(){
        long a, b, c, d, e;
        a = solve(1,1);
        b = solve(3,1);
        c = solve(5,1);
        d = solve(7,1);
        e = solve(1,2);
        long result = a*b*c*d*e;
        System.out.println("Part 2: " + result);
    }

    public static void main(String[] args){
        long part_1 = solve(3, 1);
        System.out.println("Part 1: " + part_1);
        solve_part_2();
    }
}
