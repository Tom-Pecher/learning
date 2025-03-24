
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 18: Inheritance

class Animal {
  String color;

  // Shorthand constructor:
  Animal(this.color);

  void eat() {
    print('Eat');
  }
}

// Dog class is inheriting from Animal class. Dog is a subclass of Animal:
class Dog extends
    Animal { 
  String breed;

  // Shorthand constructor:
  Dog(String color, this.breed) : super(color);

  void bark() {
    print('Bark');
  }
}

main() {
  var dog = Dog('Black', 'Labrador');
  print(dog.color);
  print(dog.breed);
  dog.eat();
  dog.bark();
}
