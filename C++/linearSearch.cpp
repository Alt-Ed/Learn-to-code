#include <iostream>
using namespace std;

int linear_search(int key, int arr[], int n)
{
     for (int i = 0; i < n; i++)
     {
          if (arr[i] == key)
               return (i + 1);
     }

     return -1;
}

int main()
{
     // Enter Array Size and Elements
     int n;
     cin >> n;
     int arr[n];
     for (int i = 0; i < n; i++)
          cin >> arr[i];

     // Enter the element to be searched
     int key;
     cin >> key;

     int pos = linear_search(key, arr, n);
     if (pos > 0)
          cout << "Element found at position " << pos;
     else
          cout << "Element Not Found!";

     return 0;
}
/*
Linear search in C++
Input: Size of array , Array of integers and the value to be searched in the array
Output: Returns position of the element if it's present else '-1'
----------------------------------------
Sample Input 1:
5
4 6 23 12 3
23
Output:
Element found at position 3

Sample Input 2:
6
23 231 24 12 43 54
2
Output:
Element Not Found!
*/
