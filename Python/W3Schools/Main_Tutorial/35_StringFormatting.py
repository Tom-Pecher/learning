
# PYTHON: W3Schools - Main Tutorial
# Section 35: String Formatting

# BASICS
    # A more flexible way of writing strings, f-strings allow us to format certain parts:
txt = f"The price is 49 dollars"
print("1.", txt)

    # We can use placeholders to insert variables into our strings:
price = 59
print("2.", f"The price is {price} dollars")

    # Formatting values without storing them is also possible:
print("3.", f"The price is {95:.2f} dollars")


# OPERATIONS
    # We can perform operations inside placeholders:
price = 59
tax = 0.25
print("4.", f"The price is {price + (price * tax)} dollars")

    # This includes ternary operators:
price = 49
print("5.", f"It is very {'Expensive' if price>50 else 'Cheap'}")

    # We can also call builtin or custom methods:
def myconverter(x):
  return x * 0.3048
print("6.", f"The plane is flying at a {myconverter(30000)} meter altitude")


# MODIFIERS
    #   :< 	    Left aligns the result (within the available space)
    #   :> 	    Right aligns the result (within the available space)
    #   :^ 	    Center aligns the result (within the available space)
    #   := 	    Places the sign to the left most position
    #   :+ 	    Use a plus sign to indicate if the result is positive or negative
    #   :- 	    Use a minus sign for negative values only
    #   :  	    Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
    #   :, 	    Use a comma as a thousand separator
    #   :_ 	    Use a underscore as a thousand separator
    #   :b 	    Binary format
    #   :c 	    Converts the value into the corresponding Unicode character
    #   :d 	    Decimal format
    #   :e 	    Scientific format, with a lower case e
    #   :E 	    Scientific format, with an upper case E
    #   :f 	    Fix point number format
    #   :F 	    Fix point number format, in uppercase format (show inf and nan as INF and NAN)
    #   :g 	    General format
    #   :G 	    General format (using a upper case E for scientific notations)
    #   :o 	    Octal format
    #   :x 	    Hex format, lower case
    #   :X 	    Hex format, upper case
    #   :n 	    Number format
    #   :% 	    Percentage format


# OLD FORMATTING
    # In older versions of Python, the only way to format strings was with the string.format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print("7.", myorder.format(quantity, itemno, price))

    # We can specify an order by index:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print("8.", txt.format(age, name))

    # Or with keyword arguments:
myorder = "I have a {carname}, it is a {model}."
print("9.", myorder.format(carname = "Ford", model = "Mustang"))
