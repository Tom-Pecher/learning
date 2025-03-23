
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 13: Lists

main() {
  // A list is an ordered collection of values:
  List<int> numbers = [1, 2, 3, 4, 5];  // Specifying the type of elements in the list is optional (in this case, int).
  print(numbers);

  // Obtain the length of a list using the length property:
  print(numbers.length);

  // One can access elements in a list using the index:
  print(numbers[0]);

  // One can add elements to a list using the add method:
  numbers.add(6);

  // One can remove elements from a list using the remove method:
  numbers.remove(6);

  // One can remove elements from a list at an index position using the removeAt method:
  numbers.removeAt(3);

  // One can remove the last element from a list using the removeLast method:
  numbers.removeLast();

  // One can remove all elements from a list using the clear method:
  numbers.clear();

  // When we assign one list to another, it is by reference and so we are referencing the same list in memory:
  List<String> chars = ["a", "b", "c"];
  List<String> chars2 = chars;

  chars2.add("d");
  print(chars);

  // To create a copy of a list, we can use the spread operator:
  List<String> chars3 = ["a", "b", "c"];
  List<String> chars4 = [...chars3];

  chars4.add("d");
  print(chars3);
}
