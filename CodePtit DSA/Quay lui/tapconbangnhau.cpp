#include<bits/stdc++.h>
using namespace std;
int n;
vector<int> a;
vector<int> cur;
int tongnua;
bool check = false;
void dlv (){
    cin >> n;
    check=false;
    int tong=0;
    a.resize(n);
    cur.clear();
    for(auto &x : a) {cin >> x; tong+=x;}
    if(tong % 2 == 0){
       tongnua = tong / 2;
    } else {
       cout << "NO" <<'\n';
       exit(0);
    }
}
void kqua (){
    cout <<"YES"<<'\n';  
    check = true;
}
void quaylui (int i,int sum){
    if(check) return;
    if(sum > tongnua){
        return ;
    }
    if(sum == tongnua ){
        kqua();
        return ;
    }
    if(i==n) return ;
    cur.push_back(a[i]);
    quaylui(i+1,sum+a[i]);
    cur.pop_back();  
    quaylui(i+1,sum);
}
int main(){
    int t;cin >> t;
    while(t--){
    dlv();
    quaylui(0,0);
    if(!check) cout <<"NO"<<'\n';    
    }
    return 0;
}