#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

vector<string> read_file(string filepath)
{
    string line;
    vector<string> lines;
    ifstream input_file(filepath);

    if (!input_file)
    {
        cout<<"Error opening output file"<< endl;
    }

    while (getline(input_file, line))
    {
        lines.push_back(line);
    }
    return lines;
}

bool is_ok(long long line, vector<long long> last_five){
    for (int i = 0; i < last_five.size(); i++) {
        for (int j = 0; j < last_five.size(); j++) {
            if (last_five[i] == last_five[j]){
                continue;
            }
            if (last_five[i] + last_five[j] == line){
                return true;
            }
        }
    }
    return false;
}

long long solve_part_1(vector<string> data){
    long long current_line;
    vector<long long> five_array;
    five_array.reserve(25);

    for (int i = 0; i < 25; i++){
        five_array.emplace_back(stoll(data[i]));
    }
    for (int  i = 25; i < data.size(); i++){
        current_line = stoll(data[i]);
        if (!is_ok(current_line, five_array)){
            return current_line;
        }
        five_array.erase(five_array.begin());
        five_array.emplace_back(current_line);
    }
    return 0;
}

long long solve_part_2(vector<string> data, long long m){
    long long result = 0;
    vector<long long> nums;

    for (int i =0; i < data.size();i++){
        nums.clear();
        result = 0;
        for (int j = i; j < data.size(); ++j) {
            long long n = stoll(data[j]);
            result += n;
            nums.emplace_back(n);
            if (result == m){
                sort(nums.begin(), nums.end());
                return nums[0] + nums[nums.size() - 1];;
            }
        }
    }
    return -1;
}

int main() {
    vector<string> data = read_file("D:/0. Projects/advent-of-code-2020/09/input");
    long long part1 = solve_part_1(data);
    cout << "Part 1: "<< part1 << endl;
    long long part2 = solve_part_2(data, part1);
    cout << "Part 2: "<< part2 << endl;
    return 0;
}