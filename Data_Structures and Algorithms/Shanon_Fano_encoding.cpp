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

// struct Node* create_node(string s,int x,struct Node* left,struct Node* right){
//     struct Node* a = new struct Node;
//     a->left = left;
//     a->right = right;
//     a->s = s;
//     a->x = x;
//     return a;
// }

bool cmp(Tuple x,Tuple y){
    return x.second < y.second;
}

int array_half(vector<Tuple>& v,int l,int r){
    int sum = 0;
    for(int i = l;i < r+1;i++){
        sum += v[i].second;
    }
    int half = 0;
    for(int i = l;i < r+1;i++){
        half += v[i].second;
        if((half <= sum/2) && (half + v[i+1].second > sum/2)){
            return i;
        }
    }
}

int summer(vector<Tuple>& v,int l,int r){
    int sum = 0;
    for(int i = l;i < r+1;i++){
        sum += v[i].second;
    }
    return sum;
}

string construct_string(vector<Tuple>& v,int l,int r){
    string s = "";
    for(int i = l;i < r+1;i++){
        s += v[i].first;
    }
    return s;
}

struct Node* Shanon_fano_tree_constructor(vector<Tuple>& v,int l,int r){
    struct Node* Root = new struct Node;
    //cout << "HI" << endl;
    //cout << array_half(v,l,r) << endl;
    if(l == r){
        Root->s = v[l].first;
        Root->x =  v[l].second;
        Root->left = NULL;
        Root->right = NULL;
        //cout << Root->x << endl;
        return Root;
    }
    else{
        Root->s = construct_string(v,l,r);
        Root->x = summer(v,l,r);
        //cout << l << " " << r << endl;
        Root->left = Shanon_fano_tree_constructor(v,l,array_half(v,l,r));
        //cout << l << " " << r << endl;
        Root->right = Shanon_fano_tree_constructor(v,array_half(v,l,r)+1,r);
        //cout << Root->x << endl;
        return Root;
    }
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

void bfs(struct Node* Root){
    vector<struct Node*> Queue;
    Queue.push_back(Root);
    while(Queue.size() > 0){
        if(Queue[0]->left){
            Queue.push_back(Queue[0]->left);
            Queue.push_back(Queue[0]->right);
        }
        cout << Queue[0]->s << "(" << Queue[0]->x << ")" << " ";
        Queue.erase(Queue.begin());
    }
    cout << endl;
}

int main(){
    map<char,int> m;
    map<string,string> Encoded;
    string s;
    Tuple a;
    vector<Tuple> A;
    vector<struct Node*> B;
    int n,x;
    cin >> n >> s;
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
        cout << A[i].first << " " << A[i].second << endl;
    }
    struct Node* Root;
    Root = Shanon_fano_tree_constructor(A,0,x-1);
    //cout << Root->x << endl;
    string Coded = "";
    string c;
    dfs(Encoded,Root,Coded);
    x = s.size();
    Coded.erase();
    for(auto i : Encoded){
        cout << i.first << i.second << endl;
    }
    bfs(Root);
    for(int i = 0;i < x;i++){
        c = s[i];
        Coded += Encoded[c];
    }
    cout << Coded;
}