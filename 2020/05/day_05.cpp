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

void solve(vector<string> &data)
{
    int max_seat_id = 0;
    int min_seat_id = 1000;
    vector<int> seat_ids;
    seat_ids.reserve(900);

    for (string line : data)
    {
        int lower_bound = 0;
        int upper_bound = 127;
        for (int i = 0; i < 7; i++)
        {
            if (line[i] == 'F')
            {
                upper_bound = upper_bound - ((upper_bound - lower_bound) / 2) - 1;
            }
            else if (line[i] == 'B')
            {
                lower_bound = lower_bound + ((upper_bound - lower_bound) / 2) + 1;
            }
        }

        int row = upper_bound;
        lower_bound = 0;
        upper_bound = 7;

        for (int i = 7; i < 10; i++)
        {
            if (line[i] == 'L')
            {
                upper_bound = upper_bound - ((upper_bound - lower_bound) / 2) - 1;
            }
            else if (line[i] == 'R')
            {
                lower_bound = lower_bound + ((upper_bound - lower_bound) / 2) + 1;
            }
        }

        int col = upper_bound;
        int seat_id = row * 8 + col;
        seat_ids.push_back(seat_id);

        if (seat_id > max_seat_id)
        {
            max_seat_id = seat_id;
        }

        if (seat_id < min_seat_id)
        {
            min_seat_id = seat_id;
        }
    }
    cout << "Part 1: " << max_seat_id << endl;

    sort(seat_ids.begin(), seat_ids.end());
    for (int i = 1; i < seat_ids.size(); i++)
    {
        if (seat_ids[i] - seat_ids[i - 1] != 1)
        {
            cout << "Part 2: " << seat_ids[i] - 1 << endl;
        }
    }
}

int main()
{
    vector<string> data = read_file("C:\\Users\\ivazi\\CLionProjects\\untitled5\\input.txt");
    solve(data);

    return 0;
}
