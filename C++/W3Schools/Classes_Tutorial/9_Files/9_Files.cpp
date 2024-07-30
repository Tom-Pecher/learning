
// C++: W3Schools - Classes Tutorial
// Section 9: Files

#include <iostream>
#include <fstream>
using namespace std;

// To manipulate files in C++, we must include the file stream library:
int main() {
  // WRITING
    // Create and open a text file
  ofstream MyFile("test_file_1.txt");
    // Write to the file
  MyFile << "Files can be tricky, but it is fun enough!";
    // Close the file
  MyFile.close();


  // READING
    // Create a text string, which is used to output the text file
  string myText;
    // Read from the text file
  ifstream MyReadFile("test_file_1.txt");
    // Use a while loop together with the getline() function to read the file line by line
  while (getline (MyReadFile, myText)) {
    // Output the text from the file
    cout << "1. " << myText << '\n';
  }
    // Close the file
  MyReadFile.close();
}
