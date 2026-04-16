#include<bits/stdc++.h>
using namespace std;
char a[1001];
string s;
bool check[1001];
void ketqua (){
     for(int i=1;i<=s.size();i++){
        cout << a[i];
     }
     cout <<" ";
}
void quaylui (int i){
     for(int j=0;j<s.size();j++){
        if(!check[j]){
            a[i]=s[j];
            check[j]=true;
        if(i==s.size()){
           ketqua();
        } else {
            quaylui(i+1);     
           }
           check[j]=false;
        }
     }
}
int main(){
    int t; cin >> t;
    while(t--){
    cin >> s;
    for(auto &c : s) c=toupper(c);
    fill(check,check + s.size(),false);
    quaylui(1);
    cout <<'\n'; 
    }  
    return 0;
}