#include <fstream>
#include <iostream>
#include <map>
#include <set>
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

void solve_part_1()
{
    vector<string> data = read_file("D:/0. Projects/advent-of-code-2020/06/input");
    data.push_back("");
    int sum = 0;
    set<char> answ;
    for (string line : data)
    {
        if (line == "")
        {
            sum += answ.size();
            answ.clear();
            continue;
        }
        for (int i = 0; i < line.size(); ++i)
        {
            answ.emplace(line[i]);
        }
    }

    cout << "Part 1: " << sum << endl;
}

void solve_part_2()
{
    vector<string> data = read_file("D:/0. Projects/advent-of-code-2020/06/input");
    data.push_back("");
    int sum = 0;
    int group_size = 0;
    map<char, int> count;

    for (string line : data)
    {
        if (line == "")
        {
            for (auto el : count)
            {
                if (el.second == group_size)
                {
                    sum++;
                }
            }
            count.clear();
            group_size = 0;
            continue;
        }

        for (char ch : line)
        {
            count[ch]++;
        }
        group_size++;
    }

    cout << "Part 2: " << sum << endl;
}

int main()
{
    solve_part_1();
    solve_part_2();

    return 0;
}
