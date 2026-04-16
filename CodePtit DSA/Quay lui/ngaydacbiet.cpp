/*#include<bits/stdc++.h>
using namespace std;
string s = "22022022";
vector<char> ktu;
vector<char> chon(8);
vector<bool> check(8,true);
void dulieu (){
    for(auto c : s){
        ktu.push_back(c);
    }
}
void ketqua (){
    if(chon[4] != '2' || chon[2] == '2') return ;
    else {
        cout << chon[0]<<chon[1]<<"/"<< chon[2]<<chon[3]<<"/"<<chon[4]<<chon[5]<<chon[6]<<chon[7]<<'\n';
         }
}
void quaylui (int i){
    for(int j=0;j<ktu.size();j++){
        if(check[j]){
            chon[i]=ktu[j];
            check[j]=false;
            if(i==ktu.size()-1){
                ketqua();
            } else {
                quaylui(i+1);
                check[j]= true;
            }
        }    
    } 
}
int main(){
    dulieu();
    quaylui(0);
}
*/
#include<bits/stdc++.h>
using namespace std;
vector<string> t;
string s(8,0);
void giai (){
    int d=stoi(s.substr(0,2));
    int m=stoi(s.substr(2,2));
    int y=stoi(s.substr(4,4));
    if(d > 1 && d < 28 && m > 1 && m < 12 && y >=2000){
        string res=s;
        res.insert(2,"/");
        res.insert(5,"/");
        t.push_back(res);
    }
}
void quaylui (int i){
    for(auto x : {'0','2'}){
        s[i]=x;
        if(i==7){
            giai();
        }else{
            quaylui(i+1);
        }
    }
}
int main(){
    quaylui(0); 
    sort(t.begin(),t.end());
    for(auto c : t){
        cout <<c <<'\n';
    }
    return 0;
}