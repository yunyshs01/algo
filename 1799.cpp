#include<iostream>

using namespace std;

int chess[10][10];
int n;

int dy[] = {-1,1,1,-1};
int dx[] = {1,1,-1,-1};

int dfs(int cdnum){
    int y = cdnum/n;
    int x = cdnum%n;

    


}


int  main(){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>chess[i][j];
        }
    }

}