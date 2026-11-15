
#include <iostream>
using namespace std;

int main()
{
    int n, arr[100], key, found = 0;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "Enter element to search: ";
    cin >> key;

    // Linear Search
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            cout << "Element found at position " << i + 1 << endl;
            found = 1;
            break;
        }
    }

    if (found == 0)
    {
        cout << "Element not found!" << endl;
    }

    return 0;
}
