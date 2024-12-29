
// JAVASCRIPT: W3Schools - Main Tutorial
// Section 35: Date Objects

// JavaScript Date Objects let us work with dates:
const d = new Date(2018, 11, 24, 10, 33, 30, 0);
// new Date(year,month,day,hours,minutes,seconds,ms)

// New Date() creates a new date object with the current date and time:
new Date();

// We can also parse strings:
new Date("2022-03-25");

// Specifying a month higher than 11, will not result in an error but add the overflow to the next year.

// To display a date, we can use the following methods:
// Covert to string:
d.toString();

// toDateString() returns the date portion of a Date object in a human-readable string format.
d.toDateString();

// toTimeString() returns the time portion of a Date object in a human-readable string format.
d.toTimeString();

// toISOString() returns the date as a string, using the ISO standard.
d.toISOString();

// toUTCString() converts a date to a UTC string (a date display standard).
d.toUTCString();
