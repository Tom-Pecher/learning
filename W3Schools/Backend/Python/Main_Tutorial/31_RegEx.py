
# PYTHON: W3Schools - Main Tutorial
# Section 31: RegEx


# BASICS
    # We can manipulate RegEx using the re module:
import re

    # Here is how we might search if a piece of text starts and ends with certain characters using re.search():
txt = "The rain in Spain"
print("1.", re.search("^The.*Spain$", txt))

    # The function re.findall() returns a list of all occurances:
txt = "The rain in Spain"
print("2.", re.findall("ai", txt)) 

    # The re.search() function returns a Match object of the position of the first occurence:
txt = "The rain in Spain"
x = re.search("\s", txt) # NOTE: None will instead be returned if there is no Match.
print("3.", "The first white-space character is located in position:", x.start())
    # The Match object has some methods that can be called:
        # .span() returns a tuple containing the start-, and end positions of the match
        # .string returns the string passed into the function
        # .group() returns the part of the string where there was a match
print("4.", x.span())

    # The re.split() function splits the string at each match, where we can control the maximum number of splits:
txt = "The rain in Spain"
print("5.", re.split("\s", txt, 2))

    # The re.sub() function substitutes each occurence with a specified item up to a maximum number of substitutes:
txt = "The rain in Spain"
print("6.", re.sub("\s", "9", txt, 2)) 


# METHODS
    # findall 	        Returns a list containing all matches
    # search 	        Returns a Match object if there is a match anywhere in the string
    # split 	        Returns a list where the string has been split at each match
    # sub 	            Replaces one or many matches with a string


# SPECIAL CHARACTERS
    # [] 	        A set of characters 	                                                        "[a-m]" 	
    # \ 	        Signals a special sequence (can also be used to escape special characters) 	    "\d" 	
    # . 	        Any character (except newline character) 	                                    "he..o" 	
    # ^ 	        Starts with 	                                                                "^hello" 	
    # $ 	        Ends with 	                                                                    "planet$" 	
    # * 	        Zero or more occurrences 	                                                    "he.*o" 	
    # + 	        One or more occurrences 	                                                    "he.+o" 	
    # ? 	        Zero or one occurrences 	                                                    "he.?o" 	
    # {} 	        Exactly the specified number of occurrences 	                                "he.{2}o" 	
    # | 	        Either or 	                                                                    "falls|stays" 	
    # () 	        Capture and group


# SPECIAL SEQUENCES
    # \A 	        Returns a match if the specified characters are at the beginning of the string 	                                                            "\AThe" 	
    # \b 	        Returns a match where the specified characters are at the beginning or at the end of a word
    # (the "r" in the beginning is making sure that the string is being treated as a "raw string") 	                                                            r"\bain", r"ain\b" 	
    # \B 	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
    # (the "r" in the beginning is making sure that the string is being treated as a "raw string") 	                                                            r"\Bain", r"ain\B" 	
    # \d 	        Returns a match where the string contains digits (numbers from 0-9) 	                                                                    "\d" 	
    # \D 	        Returns a match where the string DOES NOT contain digits 	                                                                                "\D" 	
    # \s 	        Returns a match where the string contains a white space character 	                                                                        "\s" 	
    # \S 	        Returns a match where the string DOES NOT contain a white space character 	                                                                "\S" 	
    # \w 	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w" 	
    # \W 	        Returns a match where the string DOES NOT contain any word characters 	                                                                    "\W" 	
    # \Z 	        Returns a match if the specified characters are at the end of the string 	                                                                "Spain\Z"


# SETS
    # [arn] 	    Returns a match where one of the specified characters (a, r, or n) is present 	
    # [a-n] 	    Returns a match for any lower case character, alphabetically between a and n 	
    # [^arn] 	    Returns a match for any character EXCEPT a, r, and n 	
    # [0123] 	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
    # [0-9] 	    Returns a match for any digit between 0 and 9 	
    # [0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
    # [a-zA-Z] 	    Returns a match for any character alphabetically between a and z, lower case OR upper case 	
    # [+] 	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
