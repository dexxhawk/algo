#include <iostream>
#include <string>
#include <sstream>

using namespace std;


struct Node {
    int key;
    Node* left;
    Node* right;
};

class Tree {
    private:
    Node* root;
    bool flag = false;

    Node* add(Node* node, int n) {
        if (!node) {
            return new Node{n, nullptr, nullptr};
        }
        if (n == node->key){
            flag = true;
            return node;
        } else if (n < node->key) {
            node->left = add(node->left, n);
        } else if (n > node->key){
            node->right = add(node->right, n);
        }
        return node;
    }


    void search(Node* node, int n) {
        if (!node){
            return;
        }
        if (n == node->key){
            flag = true;
            return;
        } else if (n < node->key) {
            search(node->left, n);
        } else if (n > node->key) {
            search(node->right, n);
        }
        return;
    }

    void print(Node* node, string& res, int lvl) {
        if (!node) return;

        print(node->left, res, lvl + 1);
        if (node->left) res += "\n";

        res += string(lvl, '.');
        res += to_string(node->key);

        if (node->right) res += "\n";
        print(node->right, res, lvl + 1);
    }

    public:
    Tree() : root(nullptr){}


    string add(int n){
        flag = false;
        root = add(root, n);
        return flag ? "ALREADY" : "DONE";
    }

    string search(int n){
        flag = false;
        search(root, n);
        return flag ? "YES" : "NO";
    }

    string tostring(){
        string res;
        print(root, res, 0);
        return res;
    }
};


int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    Tree tree;

    string line;
    getline(cin, line);
    while(!line.empty()) {
        stringstream ss(line);

        string cmd;
        int n;
        ss >> cmd >> n;
        if (cmd == "PRINTTREE") {
            cout << tree.tostring() << endl;
        } else if (cmd == "ADD") {
            cout << tree.add(n) << endl;
        } else {
            cout << tree.search(n) << endl;
        }
        getline(cin, line);
    }

    return 0;
}