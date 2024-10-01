
// C++: W3Schools - Classes Tutorial
// Section 6: Encapsulation

#include <iostream>
using namespace std;

// BASICS
// Encapsulation the bundling of data, along with the methods that operate on that data, into a single unit:
class Employee {
  private:
    // Private attribute
    int salary;

  public:
    // Setter
    void setSalary(int s) {
      salary = s;
    }
    // Getter
    int getSalary() {
      return salary;
    }
};

int main() {
  Employee myObj;
  myObj.setSalary(50000);
  cout << "1. " << myObj.getSalary() << '\n';
  return 0;
}
