
#include <iostream>
#include <cstring>
using namespace std;

struct Student {
    int rollNo;
    char name[50];
    float cgpa;
};

int main() {
    Student s[15], temp;

    // Input student details
    for (int i = 0; i < 15; i++) {
        cout << "\nEnter details of Student " << i + 1 << endl;

        cout << "Enter Roll No: ";
        cin >> s[i].rollNo;

        cout << "Enter Name: ";
        cin >> s[i].name;

        cout << "Enter CGPA: ";
        cin >> s[i].cgpa;
    }

    // Display original roll call list
    cout << "\n--- Original Roll Call List ---\n";
    for (int i = 0; i < 15; i++) {
        cout << s[i].rollNo << "\t"
             << s[i].name << "\t"
             << s[i].cgpa << endl;
    }

    // Bubble Sort by Roll Number
    for (int i = 0; i < 14; i++) {
        for (int j = 0; j < 14 - i; j++) {
            if (s[j].rollNo > s[j + 1].rollNo) {
                temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
        }
    }

    // Display sorted roll call list
    cout << "\n--- Sorted Roll Call List ---\n";
    for (int i = 0; i < 15; i++) {
        cout << s[i].rollNo << "\t"
             << s[i].name << "\t"
             << s[i].cgpa << endl;
    }

    return 0;
}
