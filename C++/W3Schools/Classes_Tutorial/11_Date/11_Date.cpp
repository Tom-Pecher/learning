
// C++: W3Schools - Classes Tutorial
// Section 11: Date

#include <iostream>
#include <ctime>
using namespace std;

// BASICS
int main() {
  // Timestamps represent moments in time as single numbers: 
  time_t timestamp;           // Initialize timestamp
  time(&timestamp);           // Get the timestamp for the current date and time
  cout << "1. " << ctime(&timestamp) << '\n';  // Display the date and time represented by the timestamp

  // Datetime structures represent all components of a date as separate numbers:
  struct tm datetime;
  datetime.tm_year = 2023 - 1900; // Number of years since 1900
  datetime.tm_mon = 12 - 1; // Number of months since January
  datetime.tm_mday = 17;
  datetime.tm_hour = 0; datetime.tm_min = 0; datetime.tm_sec = 0;
  datetime.tm_isdst = -1;
  mktime(&datetime);

  string weekdays[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

  cout << "2. " << "The date is on a " << weekdays[datetime.tm_wday] << '\n';

  return 0;
}
