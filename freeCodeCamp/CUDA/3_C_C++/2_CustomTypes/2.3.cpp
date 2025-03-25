
// C++ Mini Tutorial
// Section 2.3: Custom Types

#include <iostream>

using namespace std;

typedef struct {
    float x;
    float y;
} Point;

int main() {
    Point p1 = {1.5, 2.5};
    cout << "Size of Point: " << sizeof(Point) << endl;
}
