#include<iostream>
#include<vector>
#include<string>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<map>

using namespace std;

struct Tuple{
    int first;
    int second;
};

struct Node{
    string s;
    int x;
    struct Node* left;
    struct Node* right;
};

struct Node* create_node(string s,int x,struct Node* left,struct Node* right){
    struct Node* a = new struct Node;
    a->left = left;
    a->right = right;
    a->s = s;
    a->x = x;
    return a;
}

bool cmp(Tuple x,Tuple y){
    return x.second < y.second;
}

struct Node* huffman_tree_constructor(vector<struct Node*>& B){
    while(B.size() > 1){
        struct Node* p = create_node(B[0]->s + B[1]->s,B[0]->x + B[1]->x,B[0],B[1]);
        int q = B.size();
        int i = 1;
        while((B[i+1]->x < p->x) && (i < q-1)){
            B[i] = B[i+1];
            i++;
        }
        B[i] = p;
        B.erase(B.begin());
    }
    struct Node* Root = B[0];
    return Root;
}

void dfs(map<string,string>& m,struct Node* Head,string &s){
    if((Head->s).size() == 1){
        m[(Head->s)] = s;
    }
    else{
        s = s + "0";
        dfs(m,Head->left,s);
        s.erase(s.size()-1);
        s = s + "1";
        dfs(m,Head->right,s);
        s.erase(s.size()-1);
    }
}

int main(){
    map<char,int> m;
    map<string,string> Encoded;
    string s;
    Tuple a;
    vector<Tuple> A;
    vector<struct Node*> B;
    int x;
    cin >> s;
    int n = s.size();
    for(int i = 0;i < n;i++){
        m[s[i]] += 1;
    }
    x = 0;
    for(auto i : m){
        x++;
        a.first = i.first;
        a.second = i.second;
        A.push_back(a);
    }
    sort(A.begin(),A.end(),cmp);
    for(int i = 0;i < x;i++){
        B.push_back(create_node(A[i].first,A[i].second,NULL,NULL));
    }
    struct Node* Root = huffman_tree_constructor(B);
    string Coded = "";
    string c;
    dfs(Encoded,Root,Coded);
    for(auto i : Encoded){
        cout << i.first << " " << i.second << endl;
    }
    x = s.size();
    Coded.erase();
    for(int i = 0;i < x;i++){
        c = s[i];
        Coded += Encoded[c];
    }
    cout << Coded;
}