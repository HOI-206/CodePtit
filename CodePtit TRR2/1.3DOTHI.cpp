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
    int n;
    cin >> n;
    int a[101][101];
    for (int i=0; i<n;i++){
        for (int j=0;j<n;j++){
            cin >> a[i][j];
        }
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
        int k = canh.size();
        int arc[101][101] = {0};
        for (int i=0;i<k;i++){
            int u = canh[i].first;
            int v = canh[i].second;
            arc[u][i] = 1;
            arc[v][i] = 1;
        }
        cout << n << " " << k << endl;
        for (int i=0;i<n;i++){
            for (int j=0;j<k;j++){
                cout << arc[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}