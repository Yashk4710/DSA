
#include <iostream>
using namespace std;

int cqueue[5];
int front = -1, rear = -1, n = 5;

void insertCQ(int val)
{
    if ((front == 0 && rear == n - 1) || (front == rear + 1))
    {
        cout << "Queue Overflow\n";
        return;
    }

    if (front == -1)
    {
        front = 0;
        rear = 0;
    }
    else
    {
        if (rear == n - 1)
            rear = 0;
        else
            rear = rear + 1;
    }

    cqueue[rear] = val;
}

void deleteCQ()
{
    if (front == -1)
    {
        cout << "Queue Underflow\n";
        return;
    }

    cout << "Element deleted from queue is: "
         << cqueue[front] << endl;

    if (front == rear)
    {
        front = -1;
        rear = -1;
    }
    else
    {
        if (front == n - 1)
            front = 0;
        else
            front = front + 1;
    }
}

void displayCQ()
{
    if (front == -1)
    {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Queue elements are:\n";

    int f = front;

    while (true)
    {
        cout << cqueue[f] << " ";

        if (f == rear)
            break;

        f = (f + 1) % n;
    }

    cout << endl;
}

int main()
{
    int ch, val;

    do
    {
        cout << "\n1) Insert (Enqueue)\n";
        cout << "2) Delete (Dequeue)\n";
        cout << "3) Display\n";
        cout << "4) Exit\n";

        cout << "Enter choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            cout << "Enter value for insertion: ";
            cin >> val;
            insertCQ(val);
            break;

        case 2:
            deleteCQ();
            break;

        case 3:
            displayCQ();
            break;

        case 4:
            cout << "Exit\n";
            break;

        default:
            cout << "Incorrect choice!\n";
        }

    } while (ch != 4);

    return 0;
}
