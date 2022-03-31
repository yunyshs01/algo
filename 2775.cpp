#include<iostream>

int arr[15][15];
using namespace std;
int main(){
    int t;
    cin>>t;

    for (int j=1;j<15;j++){
        arr[0][j] = j;  //0층 j호에는 j명이 살고 있음
    }

    for (int i=1;i<15;i++){     //1 층부터는 아래층과 관련이 있음
        for(int j=1;j<15;j++){  
            arr[i][j] = arr[i][j-1] + arr[i-1][j];  //i층 j호에는 i층 j-1호의 인원과 i-1층 j호의 인원을 합한 만큼 살고 있음
        }
    }

    while(t--){
        int k, n;
        cin>>k>>n;
        cout<<arr[k][n]<<endl;
    }

}