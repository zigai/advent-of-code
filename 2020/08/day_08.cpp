#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> read_file(string filepath)
{
    string line;
    vector<string> lines;
    ifstream input_file(filepath);

    if (!input_file)
    {
        cout << "Error opening output file" << endl;
    }

    while (getline(input_file, line))
    {
        lines.push_back(line);
    }
    return lines;
}

int part_1(vector<string> &data)
{
    int acc = 0;
    int i = 0;
    vector<int> executed_instructions;

    while (i < data.size())
    {
        if (find(executed_instructions.begin(), executed_instructions.end(), i) != executed_instructions.end())
        {
            return acc;
        }
        executed_instructions.push_back(i);
        string instruction = data[i].substr(0, data[i].find(" "));
        int value = stoi(data[i].substr(data[i].find(" "), data[i].length() - 1));
        if (instruction == "acc")
        {
            acc += value;
            i++;
        }
        else if (instruction == "jmp")
        {
            i += value;
        }
        else if (instruction == "nop")
        {
            i++;
        }
        else
        {
            cout << "ERROR READING INSTRUCTION!";
            break;
        }
    }
    return acc;
}

bool part_2_run(vector<string> &data, int &acc)
{
    int acc_tmp = 0;
    int i = 0;
    vector<int> executed_instructions;
    while (i < data.size())
    {
        if (find(executed_instructions.begin(), executed_instructions.end(), i) != executed_instructions.end())
        {
            return false;
        }
        executed_instructions.push_back(i);
        string instruction = data[i].substr(0, data[i].find(" "));
        int value = stoi(data[i].substr(data[i].find(" "), data[i].length() - 1));
        if (instruction == "acc")
        {
            acc_tmp += value;
            i++;
        }
        else if (instruction == "jmp")
        {
            i += value;
        }
        else if (instruction == "nop")
        {
            i++;
        }
        else
        {
            cout << "ERROR READING INSTRUCTION!";
            break;
        }
    }
    acc = acc_tmp;
    return true;
}

int part_2(vector<string> &data)
{
    int i = 0;
    int acc = 0;
    while (i < data.size())
    {
        string instruction = data[i].substr(0, data[i].find(" "));
        string value = data[i].substr(data[i].find(" "), data[i].length() - 1);
        vector<string> data_copy = data;
        if (instruction == "nop")
        {
            string new_instruction = "jmp " + value;
            data_copy[i] = new_instruction;
        }
        else if (instruction == "jmp")
        {
            string new_instruction = "nop " + value;
            data_copy[i] = new_instruction;
        }
        if (part_2_run(data_copy, acc))
        {
            return acc;
        }
        i++;
    }
    return NULL;
}

int main()
{
    vector<string> data = read_file("D:/0. Projects/advent-of-code-2020/08/input");
    int part1 = part_1(data);
    int part2 = part_2(data);
    cout << "Part 1: " << part1 << "\nPart 2: " << part2 << endl;

    return 0;
}