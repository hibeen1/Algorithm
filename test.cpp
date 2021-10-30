#include <iostream>
#include <sstream>
#include <algorithm>
#include <queue>
#include <utility>
#include <array>

using namespace std;

int binary_search_recursive(vector<int> arr, int target, int start, int end);

int binary_search_iteratable(vector<int> arr, int target, int start, int end);


int main()
{
    
    int arr2[10] = {3, 7, 10, 33, 44, 23, 12, 24, 76, 11};
    vector<int> arr;
    arr.push_back(3);
    arr.push_back(7);
    arr.push_back(32);
    arr.push_back(34);
    arr.push_back(11);
    arr.push_back(1);
    arr.push_back(56);
    arr.push_back(98);
    arr.push_back(22);
    arr.push_back(12);
    arr.push_back(100);

    sort(arr.begin(), arr.end());

    for (int i = 0; i < 10; i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl;
    int target = 33;
    int n = binary_search_iteratable(arr, target, 0, 9);
    if (n != -1) {
        cout << n+1 << "번 째 있지용?" << endl;
    }
    else {
        cout << "찾는 숫자가 없어용..." << endl;
    }
}



int binary_search_recursive(vector<int> arr, int target, int start, int end)
{

    if (start > end)
    {
        return -1;
    }
    int mid = (start + end) / 2;
    if (arr[mid] == target)
    {
        return mid;
    }
    else if (arr[mid] > target)
    {
        return binary_search_recursive(arr, target, start, mid - 1);
    }
    else
    {
        return binary_search_recursive(arr, target, mid + 1, end);
    }
}

int binary_search_iteratable(vector<int> arr, int target, int start, int end)
{
    int mid;
    while (start <= end)
    {
        mid = (start + end) / 2;
        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] > target)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
    return -1;
}