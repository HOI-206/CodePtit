#include<bits/stdc++.h>
using namespace std;
int main(){
	FILE* fin = fopen("DT.INP","r");
	FILE* fout = fopen("DT.OUT","w");
	
	int t;
	fscanf(fin,"%d", &t);
	int n,m;
	fscanf(fin,"%d %d", &n ,&m);
	vector<vector<int>> a(n,vector<int>(n,0));
	vector<int> b;
	for (int i=0;i<m;i++){
		int x,y;
		fscanf(fin,"%d %d", &x, &y);
		a[x-1][y-1] = 1;
		a[y-1][x-1] = 1;
	}
	
	if (t == 1){
		vector<int>c;
		for(int i = 0;i<n;i++){
			int dem = 0;
			for(int j=0;j<n;j++){
				if (a[i][j] == 1){
					dem+=1;
				} 
			}
			c.push_back(dem);
		}
		for (auto x : c){
			fprintf(fout,"%d ",x);
		}
	} else if ( t == 2){
		fprintf(fout,"%d\n", n);
		for(int i = 0;i<n;i++){
			int dem = 0;
			vector<int>c;
			for(int j=0;j<n;j++){
				if (a[i][j] == 1){
					c.push_back(j+1);
					dem += 1;
				} 
			}
			fprintf(fout,"%d", dem);
			for(auto x : c){
				fprintf(fout," %d",x);
			}
			fprintf(fout,"\n");
			c.clear();	
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
