#include<bits/stdc++.h>
using namespace std;
int n;
vector<int> so;
vector<int> chon;
vector<string> sapxepchuoi;
void dlv(){
    cin >> n;
    so.resize(n);
    for(auto &c : so)  cin >> c;
}
void taochuoi (){
    string s="";
    for(int i=0;i<chon.size();i++) s+=to_string(chon[i]) + " ";
    sapxepchuoi.push_back(s);
}
void kqua (){
    sort(sapxepchuoi.begin(),sapxepchuoi.end());
    for(auto c : sapxepchuoi) cout << c <<'\n';
}
void quaylui (int i){
    for(int j=i;j<n;j++){
        if(chon.empty() || so[j] > chon.back()){
            chon.push_back(so[j]);
            if(chon.size() >= 2){
                taochuoi();
            } 
            quaylui (j+1);     
            chon.pop_back();
        } 
    }
}
int main(){
    dlv();
    quaylui(0);
    kqua();
}