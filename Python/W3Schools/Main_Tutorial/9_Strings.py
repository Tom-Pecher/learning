
# PYTHON: W3Schools - Main Tutorial
# Section 9: Strings

# NOTATION
    # Strings in python are surrounded by either single quotation marks, or double quotation marks:
print("1.", "hello", 'hello')

    # The same is true for multiline strings:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,"""
b = '''sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print("2.", a, b)


# STRINGS AS COLLECTIONS
    # Strings in python are arrays of bytes so they can be indexed:
a = "Hello, World!"
print("3.", a[1])

    # And iterated through:
for x in "banana":
  print("4.", x)

    # This includes slicing:
a = "Hello, World!"
print("5.", a[:5])
print("6.", a[2:])
print("7.", a[-5:-2])

    # The built-in function len() returns a string's length:
a = "Hello, World!"
print("8.", len(a))

    # We can also check if a certain substring appears in a larger string:
txt = "The best things in life are free!"
print("9.", "free" in txt)

    # Concatenation between two strings is also possible using the + operator:
a = "Hello, World!"
print("10.", a + '?!')


# FORMAT STRINGS
    # string.format(values)
        # input type: any
        # output type: string
    # creates a new string with variables inserted at placeholder positions (an other formatting):
quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print("11.", my_order.format(quantity, item_no, price))

    # We can assign the exact positions of certain items by specifying their index in each placeholder:
quantity = 3
item_no = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print("12.", my_order.format(quantity, item_no, price))


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
