#include <bits/stdc++.h>

using namespace std;


void inorder(int rootIdx, vector<vector<int>> &tree, vector<int> &res) {
    int root = rootIdx + 1;
    cout << root << endl;
    if (root == -1) return;
    inorder(tree[rootIdx][0] - 1, tree, res);
    res.push_back(root);
    inorder(tree[rootIdx][1] - 1, tree, res);
}

void swapTrees(vector<vector<int> > &tree, int rootIdx) {
    int aux = tree[rootIdx][0];
    tree[rootIdx][0] = tree[rootIdx][1];
    tree[rootIdx][1] = aux;
}

void swapSubtrees(int rootIdx, int K, vector<vector<int>> &tree, int h) {
    int root = rootIdx + 1;
    if (root == -1) return;
    if (h%K == 0) {
        swapTrees(tree, rootIdx);
    }
    swapSubtrees(tree[rootIdx][0] - 1, K, tree, h + 1);
    swapSubtrees(tree[rootIdx][1] - 1, K, tree, h + 1);
}


vector<int> swapSubtreesAndInorder(int rootIdx, int K, vector<vector<int>> &tree, int h) {
    swapSubtrees(rootIdx, K, tree, h);


    vector<int> res;
    inorder(0, tree, res);
    return res;
}
/*
 * Complete the swapNodes function below.
 */
vector<vector<int>> swapNodes(vector<vector<int>> indexes, vector<int> queries) {
    /*
     * Write your code here.
     */

    vector<vector<int>> res;
    for (int i = 0; i < queries.size(); i++) {
        int root = 0;
        int h = 1;
        res.push_back(swapSubtreesAndInorder(root, queries[i], indexes, h));
    }

    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> indexes(n);
    for (int indexes_row_itr = 0; indexes_row_itr < n; indexes_row_itr++) {
        indexes[indexes_row_itr].resize(2);

        for (int indexes_column_itr = 0; indexes_column_itr < 2; indexes_column_itr++) {
            cin >> indexes[indexes_row_itr][indexes_column_itr];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int queries_count;
    cin >> queries_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> queries(queries_count);

    for (int queries_itr = 0; queries_itr < queries_count; queries_itr++) {
        int queries_item;
        cin >> queries_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        queries[queries_itr] = queries_item;
    }

    vector<vector<int>> result = swapNodes(indexes, queries);

    for (int result_row_itr = 0; result_row_itr < result.size(); result_row_itr++) {
        for (int result_column_itr = 0; result_column_itr < result[result_row_itr].size(); result_column_itr++) {
            fout << result[result_row_itr][result_column_itr];

            if (result_column_itr != result[result_row_itr].size() - 1) {
                fout << " ";
            }
        }

        if (result_row_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}
