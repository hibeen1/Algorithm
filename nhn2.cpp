#include <iostream>
#include <sstream>
#include <algorithm>
#include <queue>

using namespace std;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int temp = 0;

bool bfs(int x, int y, int size, int **matrix)
{
    queue<pair<int, int> > q;

    if (matrix[x][y] == 0)
    {
        return false;
    }
    if (matrix[x][y] == 1)
    {
        matrix[x][y] = 0;
        temp += 1;
        q.push(make_pair(x, y));
        while (!q.empty())
        {
            x = q.front().first;
            y = q.front().second;
            q.pop();
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= size || ny < 0 || ny >= size)
                {
                    continue;
                }
                if (matrix[nx][ny] == 0)
                {
                    continue;
                }
                if (matrix[nx][ny] == 1)
                {
                    matrix[nx][ny] = 0;
                    q.push(make_pair(nx, ny));
                    temp += 1;
                }
            }
        }
    }
    return true;
}

void solution(int sizeOfMatrix, int **matrix)
{
    int result = 0;
    vector<int> arr;

    for (int i = 0; i < sizeOfMatrix; i++)
    {
        for (int j = 0; j < sizeOfMatrix; j++)
        {
            if (bfs(i, j, sizeOfMatrix, matrix) == true)
            {
                arr.push_back(temp);
                result += 1;
                temp = 0;
            }
        }
    }
    sort(arr.begin(), arr.end());
    cout << result << endl;
    for (int i = 0; i < result; i++)
    {
        cout << arr[i] << ' ';
    }
}

struct input_data
{
    int sizeOfMatrix;
    int **matrix;
};

void process_stdin(struct input_data &inputData)
{
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.sizeOfMatrix;
    ;

    inputData.matrix = new int *[inputData.sizeOfMatrix];
    for (int i = 0; i < inputData.sizeOfMatrix; i++)
    {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        inputData.matrix[i] = new int[inputData.sizeOfMatrix];
        for (int j = 0; j < inputData.sizeOfMatrix; j++)
        {
            iss >> inputData.matrix[i][j];
        }
    }
}

int main()
{
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.sizeOfMatrix, inputData.matrix);
    return 0;
}

// 6
// 0 1 1 0 0 0
// 0 1 1 0 1 1
// 0 0 0 0 1 1
// 0 0 0 0 1 1
// 1 1 0 0 1 0
// 1 1 1 0 0 0

// 3
// 4 5 7

// 4
// 0 0 0 0
// 0 0 0 0
// 0 0 0 0
// 0 0 0 0

// 0
