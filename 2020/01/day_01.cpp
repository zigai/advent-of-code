#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int day_1_part_1(vector<int> &lines)
{
    int length = lines.size();
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            if (i == j) { continue; }
            if (lines[i] + lines[j] == 2020)
            {
                int solution = lines[i] * lines[j];
                cout << "Solution 1: " << solution<< endl;
                return solution;
            }
        }
    }
    return 0;
}

int day_1_part_2(vector<int> &lines)
{
    int length = lines.size();
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            if (lines[i] + lines[j] < 2020)
            {
                for (int k = 0; k < length; k++)
                {
                    if (i == j || j == k || i == k){ continue; }
                    if (lines[i] + lines[j] + lines[k] == 2020)
                    {
                        int solution = lines[i] * lines[j] * lines[k];
                        cout << "Solution 2: " << solution<< endl;
                        return solution;
                    }
                }
            }
        }
    }
    return 0;
}

int main()
{
    string line;
    vector<int> lines;
    ifstream input_file("D:/0. Projects/advent-of-code-2020/1/input.txt");

    if (!input_file)
    {
        cout<<"Error opening output file"<< endl;
    }

    while (getline(input_file, line))
    {
       lines.push_back(stoi(line));
    }

    day_1_part_1(lines);
    day_1_part_2(lines);

    return 0;
}
