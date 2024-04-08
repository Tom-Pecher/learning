
# PYTHON: W3Schools - Tutorial
# Section 9: Strings

# NOTATION
    # Strings in python are surrounded by either single quotation marks, or double quotation marks:
print("hello", 'hello')

    # The same is true for multiline strings:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,"""
b = '''sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a, b)

# STRINGS AS COLLECTIONS
    # Strings in python are arrays of bytes so they can be indexed:
a = "Hello, World!"
print(a[1])

    # And iterated through:
for x in "banana":
  print(x)

    # This includes slicing:
a = "Hello, World!"
print(a[:5])
print(a[2:])
print(a[-5:-2])

    # The built-in function len() returns a string's length:
a = "Hello, World!"
print(len(a))

    # We can also check if a certain substring appears in a larger string:
txt = "The best things in life are free!"
print("free" in txt)

    # Concatenation between two strings is also possible using the + operator:
a = "Hello, World!"
print(a + '?!')

# FORMAT STRINGS
    # string.format(values)
        # input type: any
        # output type: string
    # creates a new string with variables inserted at placeholder positions (an other formatting):
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

    # We can assign the exact positions of certain items by specifying their index in each placeholder:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# ESCAPE CHARACTERS
    # For an added level of customization and special cases, we can use escape characters:
# \' 	Single Quote 	
# \" 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value
