#include <iostream>
#include <cstdlib>
#include <cstring>
#include <chrono>
using namespace std;
using namespace std::chrono;
 
struct Student {
    int id;
    char name[50];
    float cgpa;
};
 
Student* studentArr = nullptr;
int count = 0;      // number of students currently stored
int capacity = 0;    // allocated capacity
 
// ---------- Dynamic memory management ----------
void initDatabase(int initialCapacity) {
    studentArr = (Student*) malloc(initialCapacity * sizeof(Student));
    capacity = initialCapacity;
    count = 0;
}
 
void expandIfNeeded() {
    if (count >= capacity) {
        capacity *= 2;
        Student* temp = (Student*) realloc(studentArr, capacity * sizeof(Student));
        if (temp == nullptr) {
            cout << "Memory reallocation failed!\n";
            exit(1);
        }
        studentArr = temp;
        cout << "[Database expanded to capacity " << capacity << "]\n";
    }
}
 
void addStudent(int id, const char* name, float cgpa) {
    expandIfNeeded();
    studentArr[count].id = id;
    strcpy(studentArr[count].name, name);
    studentArr[count].cgpa = cgpa;
    count++;
}
 
void displayAll() {
    cout << "\n----- Student Database -----\n";
    cout << "ID\tName\t\tCGPA\n";
    for (int i = 0; i < count; i++) {
        cout << studentArr[i].id << "\t" << studentArr[i].name
             << "\t\t" << studentArr[i].cgpa << "\n";
    }
    cout << "-----------------------------\n";
}
 
// ---------- Searching ----------
int linearSearchById(int key) {
    for (int i = 0; i < count; i++) {
        if (studentArr[i].id == key) return i;
    }
    return -1;
}
 
// Requires the array to already be sorted by ID
int binarySearchById(int key) {
    int low = 0, high = count - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (studentArr[mid].id == key) return mid;
        else if (studentArr[mid].id < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
 
// ---------- Sorting ----------
void bubbleSortByName() {
    for (int i = 0; i < count - 1; i++)
        for (int j = 0; j < count - i - 1; j++)
            if (strcmp(studentArr[j].name, studentArr[j + 1].name) > 0)
                swap(studentArr[j], studentArr[j + 1]);
}
 
void selectionSortByCgpaAsc() {
    for (int i = 0; i < count - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < count; j++)
            if (studentArr[j].cgpa < studentArr[minIdx].cgpa)
                minIdx = j;
        swap(studentArr[i], studentArr[minIdx]);
    }
}
 
void insertionSortById() {
    for (int i = 1; i < count; i++) {
        Student key = studentArr[i];
        int j = i - 1;
        while (j >= 0 && studentArr[j].id > key.id) {
            studentArr[j + 1] = studentArr[j];
            j--;
        }
        studentArr[j + 1] = key;
    }
}
 
// ---------- Performance comparison ----------
void compareSearchPerformance(int key) {
    auto t1 = high_resolution_clock::now();
    int r1 = linearSearchById(key);
    auto t2 = high_resolution_clock::now();
    double linearTime = duration_cast<duration<double, micro>>(t2 - t1).count();
 
    insertionSortById();   // sort by ID so binary search is valid
 
    auto t3 = high_resolution_clock::now();
    int r2 = binarySearchById(key);
    auto t4 = high_resolution_clock::now();
    double binaryTime = duration_cast<duration<double, micro>>(t4 - t3).count();
 
    cout << "\n----- Search Performance Comparison (key = " << key << ") -----\n";
    cout << "Linear Search : index = " << r1 << ", time = " << linearTime << " microseconds\n";
    cout << "Binary Search : index = " << r2 << ", time = " << binaryTime << " microseconds (after sorting by ID)\n";
}
 
int main() {
    initDatabase(2);   // start small deliberately to demonstrate realloc growth
 
    addStudent(103, "Yogesh", 9.10f);
    addStudent(101, "Amit", 8.75f);
    addStudent(105, "Priya", 9.40f);
    addStudent(102, "Sneha", 8.20f);
    addStudent(104, "Rahul", 7.95f);
 
    displayAll();
 
    cout << "\n-- Sorted by Name (Bubble Sort) --";
    bubbleSortByName();
    displayAll();
 
    cout << "\n-- Sorted by CGPA Ascending (Selection Sort) --";
    selectionSortByCgpaAsc();
    displayAll();
 
    compareSearchPerformance(104);
 
    free(studentArr);
    return 0;
}
 
