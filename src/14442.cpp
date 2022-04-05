//20220405
//14442.cpp


#include<iostream>
#include<queue>
#include<memory.h>
using namespace std;

int arr[1001][1001];
int visit[1001][1001];

struct dat
{
    int y;
    int x;
    int b;
    int t;
};

int dy[] = {-1,0,1,0};
int dx[] = {0,1,0,-1};


int main(){
    
    int n, m, k;
    memset(visit,-1,sizeof(visit));
    scanf("%d %d %d",&n,&m,&k);
    for(int i=0;i<n;i++){
        char str[1002];
        scanf(" %s",str);
        for (int j=0;j<m;j++){
            arr[i][j] = str[j] - '0';
        }    
    }
    
    queue<dat> q;
    q.push({0,0,0,1});
    visit[0][0] = 0;
    int ans = -1;
    while(!q.empty()){
        dat now = q.front();
        q.pop();

        if (now.y == n-1 && now.x == m-1){
            ans = now.t;
            break;
        }
        
        for(int d=0;d<4;d++){
            int ny = now.y + dy[d];
            int nx = now.x + dx[d];
            if (ny>=n || ny<0 || nx<0 || nx >=m)continue;
            if (arr[ny][nx] == 1 && now.b<k && (visit[ny][nx] == -1 || visit[ny][nx] > now.b+1) ){
                visit[ny][nx] = now.b+1;
                q.push({ny,nx,now.b+1,now.t+1});

            }
            else if (arr[ny][nx] == 0 && (visit[ny][nx] == -1 || visit[ny][nx] > now.b)){
                visit[ny][nx] = now.b;
                q.push({ny,nx,now.b,now.t+1});
            }
        }
    }
    printf("%d\n", ans);
}