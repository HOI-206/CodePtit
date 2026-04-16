#include<bits/stdc++.h>
using namespace std;
int n;
vector<int> a;
void dulieuvao (){
    cin >> n;
    a.resize(n);
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
}
void ketqua(vector < int > chon){
    cout <<"[";
    for(int i=0;i<chon.size()-1;i++){
        cout << chon[i] <<" ";
    }
    cout<<chon[chon.size()-1]<<"]";
    cout <<'\n';
}
void quaylui (vector < int> v){
    ketqua(v);
    if(v.size()==1) return ;
    vector<int> tong ;
    tong.resize(v.size()-1);
    for(int i=0;i<v.size()-1;i++){
        tong[i]=v[i]+v[i+1];
    }
    quaylui(tong);
}
int main(){
    int t;cin >> t;
    while(t--){
    dulieuvao();
    quaylui(a);
    }   
}
/*main()
 └── quaylui(a = [1,2,3,4,5])
        ├─ in [1,2,3,4,5]
        ├─ tạo tong = [3,5,7,9]
        └── quaylui([3,5,7,9])
               ├─ in [3,5,7,9]
               ├─ tạo tong = [8,12,16]
               └── quaylui([8,12,16])
                        ...
*/