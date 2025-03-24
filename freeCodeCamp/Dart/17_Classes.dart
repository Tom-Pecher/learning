
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 17: Classes

// A class is a blueprint for creating objects:
class Person {
  String name = '';
  int age = 0;

  // Constructor:
  Person(String name, [int age = 18]) { // This is called when an object is created.
    this.name = name;
    this.age = age;
  }

  // Named Constructor:
  Person.guest() {
    name = 'Guest';
    age = 24;
  }

  void showOutput() {
    print(name);
    print(age);
  }
}

main() {
  Person person1 = Person('Jack', 23);
  person1.showOutput();

  Person person2 = Person('Jill');
  person2.showOutput();

  Person person3 = Person.guest();
  person3.showOutput();
}
