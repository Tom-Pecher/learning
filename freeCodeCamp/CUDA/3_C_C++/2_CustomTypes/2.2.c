
// C Mini Tutorial
// Section 2: Custom Types

#include <stdio.h>

typedef struct {
    float x;
    float y;
} Point;

int main() {
    Point p1 = {1.5, 2.5};
    printf("Size of Point: %zu\n", sizeof(Point));
}
