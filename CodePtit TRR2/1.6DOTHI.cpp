#include<bits/stdc++.h>
using namespace std;

void fileinout(){
    freopen("DT.INP", "r", stdin);
    freopen("DT.OUT", "w", stdout);
}

int main(){
    fileinout();
    int t;
    cin >> t;
    int n,m;
    cin >> n >> m;
    vector<vector<int>> a(n,vector<int>(n,0));
    for (int i=0;i<m;i++){
        int x,y;
        cin >> x >> y;
        a[x-1][y-1] = 1;
        a[y-1][x-1] = 1;
    }
    
    if(t == 1){
        vector<int> deg;
        for (int i=0; i<n;i++){
            int dem = 0;
            for (int j=0;j<n;j++){
                if (a[i][j]==1){
                    dem+=1;
                }
            }
            deg.push_back(dem);
        }
        for (int i=0; i<n; i++){
            cout << deg[i] <<" ";
        }
    } else {
        vector<pair<int,int>> canh;
        for (int i=0; i<n;i++){
            for (int j=i+1;j<n;j++){
                if (a[i][j] == 1){
                    canh.push_back({i,j});
                }
            }
        }
        int arc[101][101] = {0};
        for (int i=0;i<m;i++){
            int u = canh[i].first;
            int v = canh[i].second;
            arc[u][i] = 1;
            arc[v][i] = 1;
        }
        cout << n << " " << m << endl;
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                cout << arc[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}