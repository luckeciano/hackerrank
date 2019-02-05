#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

void swap (vector<int> &q, int a, int b) {
    int aux = q[a];
    q[a] = q[b];
    q[b] = aux;
}

int bribe(int num, vector<int> &q, vector<int> &numBribes) {
    int idx = 0;
    for (int i = num - 1; i < q.size(); i++) {
        if (q[i] == num) {
            idx = i;
            break;
        }
    }

    int bribes = 0;
    for (int i = idx; i > num - 1; i--) {
        swap(q, i, i - 1);
        numBribes[q[i] - 1]++;
        if (numBribes[q[i] - 1] > 2) return -1;
        bribes++;
    }
    return bribes;
}

// Complete the minimumBribes function below.
void minimumBribes(vector<int> q) {
    vector<int> numBribes (q.size(), 0);
    int totalBribes = 0;
    for (int i = 0; i < q.size(); i++) {
        if (q[i] == i + 1) continue;
        int res = bribe(i + 1, q, numBribes);
        if (res == -1) {
            cout << "Too chaotic" << endl;
            return;
        }

        

        totalBribes += res;
    }

    cout << totalBribes << endl;
}

int main()
{
    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string q_temp_temp;
        getline(cin, q_temp_temp);

        vector<string> q_temp = split_string(q_temp_temp);

        vector<int> q(n);

        for (int i = 0; i < n; i++) {
            int q_item = stoi(q_temp[i]);

            q[i] = q_item;
        }

        minimumBribes(q);
    }

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
