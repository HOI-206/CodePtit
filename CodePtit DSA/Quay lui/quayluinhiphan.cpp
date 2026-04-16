#include<bits/stdc++.h>
using namespace std;
int n,x[20];
void ketqua (){
    for (int i=1;i<=n;i++){
        cout <<x[i];
    }
    cout <<'\n';
}
void quaylui (int i){
    for(int j = 0;j<=1;j++){
        x[i]=j;
        if(i==n){
            ketqua ();
        } else {
            quaylui(i+1);
        }
    }
}
int main(){
    cin >> n;
    quaylui(1);
}