#include <iostream>
#include <sstream>
//
#include <algorithm>
//

using namespace std;

//
int temp = 0;

bool dfs(int x, int y, int size, int **matrix)
{
    if (x < 0 || x >= size || y < 0 || y >= size)
        return false;
    if (matrix[x][y] == 1)
    {
        matrix[x][y] = 0;
        temp += 1;
        dfs(x - 1, y, size, matrix);
        dfs(x + 1, y, size, matrix);
        dfs(x, y - 1, size, matrix);
        dfs(x, y + 1, size, matrix);
        return true;
    }
    return false;
}
//

void solution(int sizeOfMatrix, int **matrix)
{
    //
    int result = 0;
    int arr[1000];

    for (int i = 0; i < sizeOfMatrix; i++)
    {
        for (int j = 0; j < sizeOfMatrix; j++)
        {
            if (dfs(i, j, sizeOfMatrix, matrix) == true)
            {
                result += 1;
                arr[result - 1] = temp;
                temp = 0;
            }
        }
    }

    sort(arr, arr + result);
    cout << result << endl;
    for (int i = 0; i < result; i++)
        cout << arr[i] << ' ';
    //
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
