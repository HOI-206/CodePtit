#include<bits/stdc++.h>
using namespace std ;
int n;
int hang[100];
bool cot[100];
bool xuoi[200];
bool nguoc[200];
int dem =0;
void ketqua (){
   /*   for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(hang[i]==j) cout <<"Q ";
            else cout <<". ";
        }
        cout <<'\n';
     }
     cout <<"_______________\n";*/
     dem++;
}
void quaylui (int i){
    for(int j=1;j<=n;j++){
        if(cot[j]== true && xuoi[i-j+n]== true && nguoc[i+j-1]== true){
            cot[j]=xuoi[i-j+n]=nguoc[i+j-1]=false;
            hang[i]=j;
            if(i==n){
                ketqua();
            } else {
                quaylui(i+1); 
            }
            //backtrack
            cot[j]=xuoi[i-j+n]=nguoc[i+j-1]=true;
        }
    }
}
int main(){
    int t;
    cin >> t;
    while(t--){
    dem=0;
    cin >> n;
    fill(cot,cot+200,true);
    fill(xuoi,xuoi+200,true);
    fill(nguoc,nguoc+200,true);
    quaylui(1);
    cout << dem <<'\n';
    }
    return 0;
}