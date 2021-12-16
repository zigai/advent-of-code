package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    public static ArrayList<String> read_file(String filename) {
        ArrayList<String> listOfFiles = new ArrayList<String>();
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

    static boolean is_valid_part_1(String p){
        ArrayList<String> solution_1 = new ArrayList<String>(Arrays.asList("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"));
        ArrayList<String> solution_2 = new ArrayList<String>(Arrays.asList("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"));
        Collections.sort(solution_1);
        Collections.sort(solution_2);
        List<String> items = Arrays.asList(p.split(" "));

        if (items.size() > 6 && items.size() < 9){
            ArrayList<String> pass_items = new ArrayList<String>();

            for (int j = 0; j < items.size(); j++){
                pass_items.add(items.get(j).toString().split(":")[0]);
            }
            Collections.sort(pass_items);
            if (pass_items.equals(solution_1) || pass_items.equals(solution_2)){
                return true;
            }
        }
        return false;
    }

    static boolean is_valid_part_2(String p){
        List<String> items = Arrays.asList(p.split(" "));
        for (String item : items){
            List<String> key_value = Arrays.asList(item.split(":"));
            String type = key_value.get(0);
            String value = key_value.get(1);

            if (type.equals("byr")){
                int v = Integer.parseInt(value);
                if (v < 1920 || v > 2002){ return false; }
            }
            else if (type.equals("iyr")){
                int v = Integer.parseInt(value);
                if (v < 2010 || v > 2020){ return false; }
            }

            else if (type.equals("eyr")){
                int v = Integer.parseInt(value);
                if (v < 2020 || v > 2030){ return false; }
            }

            else if (type.equals("hgt")){
                StringBuilder m = new StringBuilder();
                m.append(value.charAt(value.length()-2)).append(value.charAt(value.length()-1));
                String height = value.substring(0, value.length()-2);

                if (m.toString().equals("cm")){
                    int v = Integer.parseInt(height);
                    if (v < 150 || v > 193){ return false; }
                }

                else if (m.toString().equals("in")){
                    int v = Integer.parseInt(height);
                    if (v < 59 || v > 76){ return false; }
                }

                else { return false; }
            }

            else if (type.equals("hcl")){
                Pattern pattern = Pattern.compile("^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$");
                Matcher matcher = pattern.matcher(value);
                boolean match_found = matcher.find();
                if(!match_found){
                    return false;
                }
            }

            else if (type.equals("ecl")){
                List<String> colors = Arrays.asList("amb","blu","brn","gry","grn","hzl","oth");
                if (!colors.contains(value)){
                     return false;
                }
            }

            else if (type.equals("pid")){
                if (value.length() != 9){ return false;}
                try{
                    int tmp = Integer.parseInt(value);
                }
                catch (NumberFormatException e){ return false; }
            }
        }
        return true;
    }

    static ArrayList<String> prepare_data(){
        ArrayList<String> data = read_file("./input.txt");
        data.add(""); // Last newline isn't added when reading file
        int input_lines = data.size();
        StringBuilder passport = new StringBuilder();
        ArrayList<String> passports = new ArrayList<String>();

        for (String line : data){
            if (line == ""){
                passports.add(passport.toString());
                passport = new StringBuilder();
                continue;
            }
            passport.append(line).append(" ");
        }
        return passports;
    }

    static void part_1(){
        ArrayList<String> passports = prepare_data();
        int counter = 0;
        for (String pass : passports){
            if (is_valid_part_1(pass)){
                counter++;
            }
        }
        System.out.println("Part 1: " + counter);
    }

    static void part_2(){
        ArrayList<String> passports = prepare_data();
        int counter = 0;
        for (String pass : passports){
            if (is_valid_part_1(pass)){
                if (is_valid_part_2(pass)){
                    counter++;
                }
            }
        }
        System.out.println("Part 2: " + counter);
    }

    public static void main(String[] args) {
        part_1();
        part_2();
    }
}
