#include <iostream>
// #include <stack>

using namespace std;

int n;
int graph[1000][1000];
int temp = 0;

bool dfs(int x, int y){
    if (x<0 || x>=n || y<0 || y>=n){
        return false;
    }
    if(graph[x][y] == 1){
        graph[x][y] = 0;
        temp += 1;
        dfs(x-1, y);
        dfs(x+1, y);
        dfs(x, y-1);
        dfs(x, y+1);
        return true;
    }
    return false;
}

int main(){
    cin >> n;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            scanf("%1d", &graph[i][j]);
        }
    }

    // stack<int> Stack;
    int result = 0;
    int arr[result];
    int k = 0;
    for (int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if (dfs(i, j) == true){
                result += 1;
                arr[k] = temp;
                k++;
                // Stack.push(temp);
                temp = 0;
            }
        }
    }
    // printf("");
    cout << result << '\n';
    // printf("");
    sort(arr, arr + result);
    for(int i=0; i<result; i++){
        cout << arr[i] << ' ';
    }
    // while(!Stack.empty()){
    //     cout << Stack.top() << ' ';
    //     Stack.pop();
    // }
}