#include <bits/stdc++.h>

using namespace std;

// Complete the makeAnagram function below.
int makeAnagram(string a, string b) {
    int lettersA [30] = {0};
    int lettersB [30] = {0};

    for (int i = 0; i < a.size(); i++) {
        lettersA[a[i] - 'a'] += 1;
    }

    for (int i = 0; i < b.size(); i++) {
        lettersB[b[i] - 'a'] += 1;
    }

    int diffs = 0;

    for (int i = 0; i < 30; i++) {
        diffs += abs(lettersA[i] - lettersB[i]);
    }

    return diffs;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
