#include <iostream>
using namespace std;

int main()
{
    int n, arr[100], a[100], temp, key, j;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        a[i] = arr[i];
    }

    // Bubble Sort
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    cout << "\nBubble Sort: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Insertion Sort
    for (int i = 1; i < n; i++)
    {
        key = a[i];
        j = i - 1;

        while (j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }

    cout << "\nInsertion Sort: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}