#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    long substringSize = s.size();
    long reps = n / substringSize;

    int count = 0;
    for (int i = 0; i < substringSize; i++) {
        if (s[i] == 'a') count++;
    }

    long res = count * reps;

    int end = n % substringSize; 
    for (int i = 0; i < end; i++) {
        if (s[i] == 'a') res++;
    }

    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
