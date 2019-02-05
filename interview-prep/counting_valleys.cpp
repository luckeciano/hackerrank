#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    int level = 0;
    int valley = 0;
    for (int i = 0; i < n; i++) {
        int prevLevel = level;
        if (s[i] == 'D') level--;
        else level++;

        if (level == -1 && prevLevel == 0) valley++;
    }

    return valley;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
