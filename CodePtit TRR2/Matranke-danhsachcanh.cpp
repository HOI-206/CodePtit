#include<bits/stdc++.h>
using namespace std;

void fileinout(){
	freopen("DT.INP", "r", stdin);
	freopen("DT.OUT", "w", stdout);
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	//fileinout();

	int t;
	cin >> t;
	int n;
	cin >> n;
	vector<vector<int>> a(n,vector<int>(n,0));
	for(int i = 0;i < n;i++){
		for(int j = 0;j < n;j++){
			int x ;
			cin >> x;
			a[i][j] = x;
		}
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
			cout << x << " ";
		}
	} else if ( t == 2){
		int dem = 0;
		vector<int>c;
		for(int i = 0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if (a[i][j] == 1){
					dem+=1;
					c.push_back(i+1);
					c.push_back(j+1);
				} 
			}
		}
		cout << n << " " << dem <<'\n';
		for (int i = 0;i<c.size();i+=2){
			cout << c[i] << " " << c[i+1] << '\n';
		}
	}
	return 0;
}
