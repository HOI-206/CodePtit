#include<bits/stdc++.h>
using namespace std;
/*bool ktraso (string s){
	for(auto c : s){
		if(!isdigit(c)){
			return false;
		}
	}
	return true;
}*/
int main(){
    deque<int> q;
    string s;
    while( cin >> s){
    	if(s == "push"){
    		int x;
    		cin >> x;
    		q.push_back(x);
		}
		else if(s == "pop"){
			if(!q.empty()){
				
				q.pop_back();
			} 
		}
		else if(s == "show"){
			if(q.empty()) cout <<"empty"<<'\n';
		    else {
		    	for(auto c : q){
		    		cout << c <<" ";
				}
				cout <<'\n';
			}
		}
	}
	return 0;
}
