#include<bits/stdc++.h>
using namespace std;
int n,k;
vector<string> ten(n);
vector<string> chon;
void dulieuvao (){
     cin >>n>> k;
     ten.resize(n);
     chon.resize(k);
     for(auto &a : ten){
        cin >> a;
        for(auto &c : a) c=toupper(c);
     }
     sort(ten.begin(),ten.end());
     ten.erase(unique(ten.begin(),ten.end()),ten.end());
}
void ketqua(){
    for(int i=0;i<k;i++){
        cout << chon[i] <<" ";
    }
    cout <<'\n';
}
void quaylui (int i,int c){
     for(int j = c;j<=ten.size()-k+i;j++){
        chon[i]=ten[j];
        if(i==k-1){
            ketqua();
        } else {
            quaylui(i+1,j+1);
        }
     }
}
int main(){
    dulieuvao();
    quaylui(0,0);
}