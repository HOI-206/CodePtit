#include<bits/stdc++.h>
using namespace std;
vector<int> a;
vector<bool> check(1e6, true);
void ktra (int n){
     check[0]=check[1]=false;
     for(int i=2;i<=sqrt(n);i++){
        if(check[i]){
            for(int j=i*i;j<=n;j+=i){
                check[j]=false;
            }
        }
     }
     for(int i=2;i<=n;i++){
        if(check[i]){
            a.push_back(i);
        }
     }
}
int main(){
    ktra(1e6);
    for(auto x : a){
        cout << x << " ";
    }
}