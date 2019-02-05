#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);
#define DFS_BLACK 1
#define UNVISITED 0

void dfs(vector<vector<long> > &AdjList, long u, long &nodes, vector<long> &dfs_num) {          // DFS for normal usage: as graph traversal algorithm
                                    // this vertex is visited
  dfs_num[u] = DFS_BLACK;      // important step: we mark this vertex as visited
  nodes++;
  for (long j = 0; j < (long)AdjList[u].size(); j++) {
    long v = AdjList[u][j];                      // v is a (neighbor, weight) pair
    if (dfs_num[v] == UNVISITED)         // important check to avoid cycle
      dfs(AdjList, v, nodes, dfs_num);      // recursively visits unvisited neighbors v of vertex u
} }
// Complete the roadsAndLibraries function below.
long roadsAndLibraries(long n, long c_lib, long c_road, vector<vector<long>> cities) {

        if (c_lib <= c_road) {
            long res =  n * c_lib;
            return res;
        }
        vector<vector<long> > AdjList(n);
        for (long i = 0; i < cities.size(); i++) {
            AdjList[cities[i][0] - 1].push_back(cities[i][1] - 1);
            AdjList[cities[i][1] - 1].push_back(cities[i][0] - 1);
        }

        vector<long> dfs_num;
        dfs_num.assign(n, UNVISITED);
        long total_cost = 0;
        for (long i = 0; i  < n; i++) {
            if (dfs_num[i] == UNVISITED) {
                long nodes = 0;
                dfs(AdjList, i, nodes, dfs_num);
                total_cost += c_lib + ((nodes-1) * 1LL * min(c_lib, c_road));
            }
        }
        return total_cost;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    long q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (long q_itr = 0; q_itr < q; q_itr++) {
        string nmC_libC_road_temp;
        getline(cin, nmC_libC_road_temp);

        vector<string> nmC_libC_road = split_string(nmC_libC_road_temp);

        long n = stoi(nmC_libC_road[0]);

        long m = stoi(nmC_libC_road[1]);

        long c_lib = stoi(nmC_libC_road[2]);

        long c_road = stoi(nmC_libC_road[3]);

        vector<vector<long>> cities(m);
        for (long i = 0; i < m; i++) {
            cities[i].resize(2);

            for (long j = 0; j < 2; j++) {
                cin >> cities[i][j];
            }

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        long result = roadsAndLibraries(n, c_lib, c_road, cities);

        fout << result << "\n";
    }

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
