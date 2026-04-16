#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    cin.ignore();
    stack<int> d;
    string kqua = "NONE";
    for(int i = 0; i < n; i++) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        string word;
        ss >> word;
        if(word == "PUSH") {
            int x;
            ss >> x;
            d.push(x);
        } 
        else if(word == "POP") {
            if(!d.empty()) d.pop();
        }
        else if(word == "PRINT") {
            if(d.size() == 0){
                cout << kqua <<'\n';
            } else {
            stack<int> st = d;
            vector<int> tmp;
            while(!st.empty()){
                tmp.push_back(st.top());
                st.pop();
            }
            reverse(tmp.begin(), tmp.end());
            cout << tmp.back() <<'\n';    
            } 
        }
    }
    return 0;
}
