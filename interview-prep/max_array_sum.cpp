#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int memo[100005][2];

int maxSubsetSumDP(int k, vector<int> &arr, bool last) {
    if (k == arr.size()) return 0;
    if (memo[k][last] != -1) return memo[k][last];
    
    int nonPicked = maxSubsetSumDP(k + 1, arr, false);
    if (last) {
        return memo[k][last] = nonPicked;
    } else {
        return memo[k][last] = max(arr[k] + maxSubsetSumDP(k + 1, arr, true),
                    nonPicked);
    }
}

// Complete the maxSubsetSum function below.
int maxSubsetSum(vector<int> arr) {
    memset(memo, -1, sizeof(memo));
    return maxSubsetSumDP(0, arr, false);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int res = maxSubsetSum(arr);

    fout << res << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
