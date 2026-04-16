#include<bits/stdc++.h>
using namespace std;
int main(){
    FILE *fin = fopen("DT.INP","r");
    FILE *fout = fopen("DT.OUT","w");
    
    int t,n,m,x,y;
    fscanf(fin,"%d",&t);
    fscanf(fin,"%d %d",&n,&m);
    vector<int> a;
    for (int i =0;i<m;i++){
    	fscanf(fin,"%d %d",&x ,&y);
    	a.push_back(x);
    	a.push_back(y);
	}
	
	vector<vector<int>> b(n,vector<int>(n,0));
	for (int i = 0 ; i < a.size()-1 ;i+=2){
		b[a[i]-1][a[i+1]-1]  = 1;
		b[a[i+1]-1][a[i]-1]  = 1;
	}
	if (t == 1){
		vector<int> dem;
	    for (int i = 0; i < n ; i++){
	    	int cnt = 0;
	        for (int j = 0; j < n ; j++){
	        	if (b[i][j] == 1){
	        		cnt++;
					}
				}
	        dem.push_back(cnt);
	        }
	    for (auto x : dem){
	    	fprintf(fout,"%d ",x);
		}
		fprintf(fout,"\n");
	} else if (t == 2){
		fprintf(fout,"%d\n", n);
		for (int i = 0; i < n ; i++){
	        for (int j = 0; j < n ; j++){
	        	fprintf(fout,"%d ",b[i][j]);
	        }
	        fprintf(fout,"\n");
		}
	}
	return 0;
}
