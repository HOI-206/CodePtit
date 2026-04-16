#include<bits/stdc++.h>
using namespace std;
int n;
vector<int> a;
vector<bool> ktra ;
void dlv (){
    cin >> n;
    a.assign(n,0);
    ktra.assign(n,false);// vừa reset kích thước vừa reset số liệu.
    fill(ktra.begin(),ktra.end(),false);
}
void kqua (){
    bool ok = true;
    for(int i=0;i<n-1;i++){
        if( abs(a[i] - a[i+1]) == 1) {
            ok=false;
            break;
        }
    }
    if(ok) {
        for(auto x : a) cout <<x;
    }
    cout <<'\n';
}
void quaylui (int i){
    for(int j=0;j<n;j++){
        if(!ktra[j]){
           a[i]= j+1;
           ktra[j]=true;
           if(i==n-1){
            kqua();
           } else {
            quaylui(i+1);
           }
           ktra[j]= false;
        } 
    }
}
int main(){
    int t;
    cin >> t;
    while(t--){
    dlv();
    quaylui(0);
    }
    return 0;
}