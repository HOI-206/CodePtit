#include<bits/stdc++.h>
using namespace std;
char n;
int k;
vector<int> a;
vector<string> res;
int nsize;
void dlv(){
    cin >> n;
    cin >> k;
    nsize = n-'A'+1;
    a.resize(k);
    for(int i=0;i<k;i++) a.push_back(i);
}
void kqua (){
    string s="";
    for(int i=0;i<k;i++) s+=char('A' +a[i]);
    res.push_back(s);
}
void in (){
    sort(res.begin(),res.end());
    for(auto x : res)  cout << x <<'\n';
}
void quaylui (int i ,int l){
    for(int j=l;j<nsize;j++){
        a[i]=j;
        if(i==k-1) kqua();
        else quaylui(i+1,j);
    }
}
int main(){
    dlv();
    quaylui(0,0);
    in();
}