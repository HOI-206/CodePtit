#include<stdio.h>
int main(){
    FILE *fin = fopen("DT.INP","r");
    FILE *fout = fopen("DT.OUT","w");
    
    int t, n;
    fscanf(fin,"%d",&t);
    fscanf(fin,"%d",&n);
    int a[105][105];

    for (int i = 0; i<n; i++){
        for (int j= 0 ; j<n;j++){
            fscanf(fin,"%d",&a[i][j]);
        }
    }

    int deg[105];
    for(int i = 0;i<n;i++){
        deg[i] = 0;
        for (int j = 0;j < n;j++){
            deg[i] += a[i][j];
        }
    }

    int u[10000],v[10000];
    int m = 0;
    for (int i = 0;i<n;i++){
        for (int j = i+1;j<n;j++){
            if (a[i][j] == 1){
                u[m] = i+1;
                v[m] = j+1;
                m++;
            }
        }
    }

    if (t == 1){
        for (int i = 0;i<n;i++){
            fprintf(fout,"%d \n", deg[i]);
        }
    } else {
        fprintf(fout,"%d %d\n", n , m);
        for (int i = 0 ;i < m;i++){
            fprintf(fout,"%d %d\n", u[i],v[i]);
        }
    }

    fclose(fin);
    fclose(fout);

    return 0;

}