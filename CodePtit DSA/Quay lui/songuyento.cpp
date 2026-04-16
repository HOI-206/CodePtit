#include<bits/stdc++.h>
using namespace std;
/*------------danh sach snt--------------------*/
int a = 1e6;
vector<int> snt ;
vector<bool> check(a,true);
void build (){
    check[0] = check [1] = false;
    for(int i=2;i<=sqrt(a) ; i++){
        if(check[i]){
            for(int j=i*i ; j<=a ;j+=i){
                check[j]= false;
            }
        }
    }
    for(int i=2;i<a;i++){
        if(check[i]) snt.push_back(i);
    }
}
/*---------------------------------------------*/
int n,p,s; // nhập n: số snt ,p :snt gốc , s :tổng
vector<int> selectt; //mảng chọn
vector<string> res; //mảng để sắp xếp
int dem=0; // đếm số mảng
int located; // vị trí của p trong mảng snt lớn
int vitris; // vị trí của s trong mảng snt lớn
void dlv (){
    cin >> n >> p >> s;
    selectt.clear();
    res.clear();
    dem=0;
    auto it =find(snt.begin(),snt.end(),p);
    located = it - snt.begin();
    vitris = upper_bound(snt.begin(),snt.end(),s) - snt.begin();
/*
    for(int i = 0;i<snt.size();i++){
        if(snt[i] > s){
            vitris=i;
            break;
        }
    }
*/
}
void kqua (){
    dem++;
    string k="";
    for(int i =0 ;i <selectt.size();i++) k+=to_string(selectt[i]) + " ";
    k.pop_back();
    res.push_back(k);
}
void in (){
    sort (res.begin(),res.end());
    for(int i=0;i<dem;i++) cout << res[i] <<'\n';
}
void quaylui (int pos ,int count ,int sum){
    if(count == 0){
        if(sum == s){
            kqua();
        }
        return;
       }
    for(int j = pos ; j < vitris ;j++){
       if(sum + snt[j] > s ) break;
       selectt.push_back(snt[j]);
       quaylui (j+1,count - 1, sum+snt[j]);
       selectt.pop_back();
    }
}
int main(){
build();
int t;
cin >> t;
while(t--){
    dlv ();
    quaylui(located+1,n,0);
    cout << dem <<'\n';
    in();
}
return 0;
}