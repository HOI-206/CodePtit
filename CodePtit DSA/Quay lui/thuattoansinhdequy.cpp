#include<bits/stdc++.h>
using namespace std;

int a[100],b[100],n;

void in(){
	for(int i=1;i<=n;i++)cout<<a[i]<<" ";
	cout<<endl;
}
int test(){
	for(int i=1;i<=n;i++)if(a[i]!=b[i])return 0;
	return 1;
}

void run(int i){
	for(int j=0;j<=1;j++){
		a[i]=j;
		b[n-i+1]=j;
		if(i==n){
			if(test())in();
		}
		else run(i+1);
	}

	
}

int main(){
	cin>>n;
	run(1);
}
