
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 14: Sets

main() {
  // A set is a collection of unique items:
  Set<int> mySet = {1, 2, 3, 4, 5, 6, 7};
  mySet.add(7);
  mySet.add(7);
  mySet.add(7);
  print(mySet);

  // Add an item to a set:
  mySet.add(8);

  // Remove an item from a set:
  mySet.remove(8);

  // Check if a set contains an item:
  print(mySet.contains(4));

  // Check the length of a set:
  print(mySet.length);

  // Clear a set:
  mySet.clear();

  // Check if a set is empty:
  print(mySet.isEmpty);

  // If we do not assign the type of the set, Dart will assign it as a HashMap:
  var mySet2 = {};
  print(mySet2.runtimeType);

  var mySet3 = <int>{};
  print(mySet3.runtimeType);
}
