#include <bits/stdc++.h>

using namespace std;

// Complete the abbreviation function below.


int memo[1001][1001];

bool abb(string a, string b, int aIdx, int bIdx) {
    if (memo[aIdx][bIdx] != -1) return memo[aIdx][bIdx];

    if (aIdx == a.size() && bIdx != b.size()) return memo[aIdx][bIdx] = false;
    
    if (bIdx == b.size()) {
        for (int i = aIdx; i < a.size(); i++) {
            if (toupper(a[i]) == a[i]) return memo[aIdx][bIdx] =  false;
        }
        return memo[aIdx][bIdx] = true;
    }


    if (b[bIdx] == a[aIdx]) return memo[aIdx][bIdx] = abb(a, b, aIdx + 1, bIdx + 1);
    else if (b[bIdx] == toupper(a[aIdx])) {
        bool isTrue = abb(a, b, aIdx + 1, bIdx + 1);
        if (isTrue) return memo[aIdx][bIdx] = true;
        return memo[aIdx][bIdx] =  abb(a, b, aIdx + 1, bIdx);
    } else if (a[aIdx] != toupper(a[aIdx])) {
        return memo[aIdx][bIdx] = abb(a, b, aIdx + 1, bIdx);
    }

    return memo[aIdx][bIdx] = false;
}


string abbreviation(string a, string b) {
    memset(memo, -1, sizeof(memo));
    return abb(a, b, 0, 0) ? "YES" : "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string a;
        getline(cin, a);

        string b;
        getline(cin, b);

        string result = abbreviation(a, b);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
