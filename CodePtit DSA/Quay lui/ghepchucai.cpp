#include<bits/stdc++.h>
using namespace std;
char a;
vector<int> b;
vector<bool> ktra (8,false);
vector<string> res;
int asize;
void dlv(){
    cin >> a;
    asize = a-'A'+1;
    b.resize(asize);
}
bool nguyenam (char c){
    return c=='A' || c=='E';
}
bool test (string s){
    for(int i=1;i<s.size()-1;i++){
        if(!nguyenam(s[i-1]) && nguyenam(s[i]) && !nguyenam(s[i+1])) return false;
    }
    return true;
}
void kqua (){
    if(asize > 8 || asize < 1) return ;
    string s="";
    for(int i=0;i<asize;i++) s+= char('A' + b[i]);
    if(test(s)){
       res.push_back(s);
    }
}
void in (){
    sort(res.begin(),res.end());
    for(auto x : res ) cout << x <<'\n';
}
void quaylui (int i){
     for(int j=0;j<asize;j++){
        if(!ktra[j]){
            b[i]=j;
            ktra[j]=true;
            if(i==asize-1){
               kqua();
            }else {
               quaylui(i+1);
        }
            ktra[j]=false;
        }   
    }
}
int  main(){
     dlv();
     quaylui(0);
     in();
}