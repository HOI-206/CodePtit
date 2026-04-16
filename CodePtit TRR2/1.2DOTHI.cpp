#include<bits/stdc++.h>
using namespace std;
int main(){
    FILE *fin = fopen("DT.INP","r");
    FILE *fout  = fopen("DT.OUT","w");

    int t,n;
    fscanf(fin,"%d", &t);
    fscanf(fin,"%d",&n);
    map<int,int> c;
    vector<vector<int>> a(n, vector<int>(n));
    for(int i = 0;i <n;i++){
        for (int j = 0;j<n;j++){
            fscanf(fin,"%d", &a[i][j]);
            if (a[i][j] == 1){
                c[i+1]+=1;
            }
        }
    }
    if (t == 1){
        for (int i=0;i<n;i++){
            fprintf(fout, "%d ", c[i+1]);
        }
    } else if (t == 2){
        fprintf(fout,"%d\n", n);
        for (int i = 0;i< n; i++){
            int dem = 0;
            vector<int> k;
            for (int j = 0 ;j < n; j++){
                if (a[i][j] == 1){
                    dem ++;
                    k.push_back(j+1);
                }
            }
            fprintf(fout, "%d", dem);
            for (auto x : k){
                fprintf(fout, " %d", x);
            }
            fprintf(fout,"\n");
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;

}