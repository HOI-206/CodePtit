#include<bits/stdc++.h>
using namespace std;
void fileinout(){
    freopen("DT.INT", "r", stdin);
    freopen("DT.OUT", "w", stdout);
}
void matrixmaker(vector<vector<int>> &a,int m){
    for (int i = 0; i < m; i++){
            int x,y;
            cin >> x >> y;
            a[x-1][y-1] = 1;
            a[y-1][x-1] = 1;
    }
}
string ktradeg(vector<vector<int>> a, int n){
    vector<int> deg;
    for (int i = 0;i<n;i++){
        int dem = 0;
        for (int j = 0 ;j < n ;j++){
            if (a[i][j]==1){
                dem+=1;
            }
        }
        deg.push_back(dem);
    }
    vector<int> odd;
    int dem = 0;
    for (int i = 0;i < n;i++){
        if (deg[i]%2!=0){
            odd.push_back(i+1);
            dem++;
        }
    }
    if (dem == 0){
        return "a";
    } else if (dem == 2){
        return "c";
    } else {
        return "b";
    }
}
void dfs(int u, vector<vector<int>> &a, vector<int> &visited, int n){
    visited[u] = 1;
    for (int v = 0; v < n; v++){
        if (a[u][v] == 1 && visited[v] == 0){
            dfs(v, a, visited, n);
        }
    }
}
bool lienThong(vector<vector<int>> &a, int n){
    vector<int> visited(n, 0);
    int start = -1;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (a[i][j] == 1){
                start = i;
                break;
            }
        }
        if (start != -1) break;
    }
    if (start == -1) return true;
    dfs(start, a, visited, n);
    for (int i = 0; i < n; i++){
        int deg = 0;
        for (int j = 0; j < n; j++){
            if (a[i][j] == 1){
                deg++;
            }
        }
        if (deg > 0 && visited[i] == 0){
            return false;
        }
    }
    return true;
}

void euler(vector<vector<int>> &a,vector<int> &path ,int n , int u){
    for (int v = 0;v < n;v++){
        if (a[u][v] == 1){
            a[u][v] = 0;
            a[v][u] = 0;
            euler(a,path,n,v);
        }
    }
    path.push_back(u);
}

int main(){
//    fileinout();
    int t;
    cin >> t;
    if (t==1){
        int n,m;
        cin >> n >> m;
        vector<vector<int>> a(n,vector<int>(n,0));
        matrixmaker(a,m);
        if (!lienThong(a,n)){
            cout << 0;
        } else {
            string res = ktradeg(a,n);
            if (res == "a"){
                cout << 1;
            } else if (res == "b"){
                cout << 0;
            } else {
                cout << 2;
            }
        }

    } else if (t == 2){
        int n,m,u;
        cin >> n >> m >> u;
        vector<vector<int>> a(n,vector<int>(n,0));
        matrixmaker(a,m);
        vector<int> path;
        int start = u-1;
        string res = ktradeg(a,n);
        if (res == "c"){
            for (int i = 0; i < n; i++){
                int deg = 0;
                for (int j = 0; j < n; j++){
                    if (a[i][j] == 1) deg++;
                }
                if (deg % 2 != 0){
                    start = i;
                    break;
                }
            }
        }
        euler(a,path,n,start);
        reverse(path.begin(),path.end());
        for (auto x : path){
            cout << x+1 << " ";
        }
    }
    return 0;
}