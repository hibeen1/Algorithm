
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int> > monsters) {
    int answer = 0;

    for (int i = 0; i < 100 - n; i++){
        for (int j = 0; j < 100 - n; j++){
            int cnt = 0;
            for (int k = 0;  k < monsters.size(); k++){
                if (monsters[k][0] <= i+n+1 && monsters[k][1] <= j+n+1){
                    cnt ++;
                }
            }
            if (answer < cnt){
                answer = cnt;
            }
        }
    }
    return answer;
}

int main(){
    
}