#include<bits/stdc++.h>
using namespace std;
int n,k;
vector<string> ten;
vector<string> chon;
void dulieuvao (){
    cin >> n >> k;
    ten.resize(n);
    chon.resize(k+1);
    vector<string> a;
    a.resize(n);
    for(int i=0;i<n;i++){
        cin >> a[i];
        for(auto &c : a[i]){
            c=toupper(c);
        }
    }
    sort(a.begin(),a.end());
    a.erase(unique(a.begin(),a.end()),a.end());
    ten=a;
}
void ketqua (){
    for(int i=1;i<=k;i++){
        cout <<chon[i]<<" ";
    }
    cout <<'\n';
}
void quaylui (int i,int c){
    for(int j=c ; j <= ten.size()-k+i-1 ;j++){
        chon[i]=ten[j];
        if(i==k){
            ketqua();
        } else {
            quaylui(i+1,j+1);
        }
    }
}
int main(){
    dulieuvao();
    quaylui(1,0);
}