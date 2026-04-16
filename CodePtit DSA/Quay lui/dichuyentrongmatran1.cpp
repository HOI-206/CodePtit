#include<bits/stdc++.h>
using namespace std;
long long hoanvi (int n,int k){
    long long res=1;
    for(int i=1;i<=k;i++){
        res =res*(n-k+i)/i;
    }
    return res;
}
int main(){
    int t;
    cin >> t;
    while(t--){
    int n,m;
    cin >> n >> m;
    vector<vector<int>> a(n,vector<int>(m));
    for(int i =0;i<n;i++){
        for(int j=0;j<m;j++){
            cin >> a[i][j];
        }
    }
    cout << hoanvi(n+m-2,m-1) <<'\n';    
    }
    return 0;  
}