#include<bits/stdc++.h>
using namespace std;
int n,k;
vector<int> dv;
int dem =0;
void dulieuvao (){
    cin >> n >> k;
    dv.resize(n);
    for(int i=0;i<n;i++){
        cin >> dv[i];
    }
}
void ketqua (int sum,vector<int> tohop){
     if(sum==k){
        dem++;
        cout <<"[";
        for(int i=0;i<tohop.size()-1;i++){
           cout << tohop[i] << " ";
        }
        cout << tohop[tohop.size()-1];
        cout <<"]";
     }
}
void quaylui (int i,int sum,vector<int> &tohop){
    //chon phan tu thu i
    if(i==n){
        ketqua(sum,tohop);
        return;
    }
    tohop.push_back(dv[i]);
    quaylui(i+1,sum+dv[i],tohop);
    tohop.pop_back();
    //khong chon phan tu thu i
    quaylui(i+1,sum,tohop);
}
int main(){
    int t;
    cin >> t;
    while(t--){
        dem=0;
        dulieuvao();
        vector<int> tohop;
        quaylui(0,0,tohop);
        if(dem == 0) cout <<-1;
        cout <<'\n';
    }
}