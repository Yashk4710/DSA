
#include <iostream>
using namespace std;

int main()
{
    int n, arr[100], key;
    int low, high, mid, found = 0;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements in sorted order:\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "Enter element to search: ";
    cin >> key;

    low = 0;
    high = n - 1;

    // Binary Search
    while (low <= high)
    {
        mid = (low + high) / 2;

        if (arr[mid] == key)
        {
            cout << "Element found at position " << mid + 1 << endl;
            found = 1;
            break;
        }
        else if (key < arr[mid])
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    if (found == 0)
    {
        cout << "Element not found!" << endl;
    }

    return 0;
}
