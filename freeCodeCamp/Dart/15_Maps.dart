
// DART: freeCodeCamp - https://www.youtube.com/watch?v=Ej_Pcr4uC2Q
// Section 15: Maps

main() {
  // A map is a collection of key-value pairs:
  Map<String, int> myMap = {
    'first': 1,
    'second': 2,
    'third': 3,
  };
  print(myMap);

  // Add a key-value pair to a map:
  myMap['fourth'] = 4;

  // Remove a key-value pair from a map:
  myMap.remove('fourth');

  // Check if a map contains a key:
  print(myMap.containsKey('first'));

  // Check if a map contains a value:
  print(myMap.containsValue(3));

  // Get the length of a map:
  print(myMap.length);

  // Clear a map:
  myMap.clear();
}
