
// C: W3Schools - Main Tutorial
// Section 17: Strings

#include <stdio.h>
#include <string.h> // Include string functions

// Unlike many other programming languages, there is no explicit string type in C.
int main() {

    // BASICS
    // Instead, we must create an array of characters to store a string:
    char greetings[] = "Hello World!";  // Defining a string this way puts a null character (\0) at the end of the string.
    printf("%s", greetings);

    // Again, we can access the elements of the array using the index number:
    greetings[0] = 'J';
    printf("%s", greetings);

    // ESCAPE CHARACTERS
    // \' 	' 	Single quote
    // \" 	" 	Double quote
    // \\ 	\ 	Backslash
    // \n 	    New Line 	
    // \t 	    Tab 	
    // \0 	    Null

    // STRING FUNCTIONS
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // The function strlen() returns the length of the string:
    printf("%lu\n", strlen(alphabet));

    // The function strcat() concatenates two strings:
    char str1[20] = "Hello ";
    char str2[] = "World!";
    strcat(str1, str2);

    // The function strcpy() copies one string to another:
    strcpy(str2, str1);

    // The function strcmp() compares two strings:
    strcmp(str1, str2);

    return 0;
}
