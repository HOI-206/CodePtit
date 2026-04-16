#include<bits/stdc++.h> 
using namespace std;
int n,k,x[100];
void ketqua (){
    for(int i=1;i<=k;i++){
        cout << x[i] <<" ";
    }
    cout <<"\n";
}
void tohopquaylui (int i){
    for(int j=x[i-1]+1;j<=n-k+i;j++){
        x[i]=j;
        if(i==k){
            ketqua();
        }
        else {
            tohopquaylui(i+1);
        }
    }
}
int main(){
    cin >> n >> k;
    x[0]=0;
    tohopquaylui(1);
}