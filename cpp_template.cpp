#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;
vector<string> read_file(const string &path)
{
    ifstream file(path);
    if (!file)
    {
        cout << "Error opening output file" << endl;
    }

    string line;
    vector<string> lines;
    while (getline(file, line))
    {
        lines.push_back(line);
    }
    return lines;
}

auto part_1(vector<string> data)
{
}

auto part_2(vector<string> data)
{
}

int main()
{
    vector<string> data = read_file("./input");
    part_1(data);
    part_2(data);
    return 0;
}