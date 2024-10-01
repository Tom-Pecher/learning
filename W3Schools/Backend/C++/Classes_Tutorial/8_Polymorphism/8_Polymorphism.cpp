
// C++: W3Schools - Classes Tutorial
// Section 8: Polymorphism

#include <iostream>
using namespace std;

// BASICS
// Polymorphism is where a method has different functionality based on the object that it is applied to:
class Animal {
  public:
    void animalSound() {
      cout << "1. " << "The animal makes a sound" << '\n';
    }
};

class Pig : public Animal {
  public:
    void animalSound() {
      cout << "2. " << "The pig says: wee wee" << '\n';
    }
};

class Dog : public Animal {
  public:
    void animalSound() {
      cout << "3. " << "The dog says: bow wow" << '\n';
    }
};

int main() {
  Animal myAnimal;
  Pig myPig;
  Dog myDog;

  myAnimal.animalSound();
  myPig.animalSound();
  myDog.animalSound();
  return 0;
} 
