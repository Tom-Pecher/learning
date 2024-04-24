
# PYTHON: W3Schools - Tutorial
# Section 6: Data Types

# CATEGORIES
    # Text Type: 	    str
    # Numeric Types: 	int, float, complex
    # Sequence Types: 	list, tuple, range
    # Mapping Type: 	dict
    # Set Types: 	    set, frozenset
    # Boolean Type: 	bool
    # Binary Types: 	bytes, bytearray, memoryview
    # None Type: 	    NoneType


# GETTING TYPE
    # type(value)
        # input type: any
        # output type: str
    # displays an object's type as a string
x = 5
print("1.", type(x))


# ASSIGNMENT
x = "Hello World" 	                            # str 	       - text
x = 20 	                                        # int 	       - integers
x = 20.5 	                                    # float 	   - real numbers
x = 1j 	                                        # complex 	   - complex numbers
x = ["apple", "banana", "cherry"] 	            # list 	       - mutable, ordered collection of nonunique elements (NOTE: ordered = indexable)
x = ("apple", "banana", "cherry") 	            # tuple 	   - immutable, ordered collection of nonunique elements
x = range(6) 	                                # range 	   - built-in generator for integer arithmetic progressions
x = {"name" : "John", "age" : 36} 	            # dict 	       - mutable, ordered mapping collection of unique elements
x = {"apple", "banana", "cherry"} 	            # set 	       - mutable, unordered collection of unique elements
x = frozenset({"apple", "banana", "cherry"}) 	# frozenset    - immutable, unordered collection of unique elements
x = True 	                                    # bool 	       - true or false
x = b"Hello" 	                                # bytes 	   - immutable bytes object
x = bytearray(5) 	                            # bytearray    - mutable array of bytes
x = memoryview(bytes(5)) 	                    # memoryview   - mutable memoryview object
x = None 	                                    # NoneType     - null


# SETTING TYPES
x = str("Hello World") 	                        # str 	
x = int(20) 	                                # int 	
x = float(20.5) 	                            # float 	
x = complex(1j) 	                            # complex 	
x = list(("apple", "banana", "cherry")) 	    # list 	
x = tuple(("apple", "banana", "cherry")) 	    # tuple 	
x = range(6) 	                                # range 	
x = dict(name="John", age=36) 	                # dict 	
x = set(("apple", "banana", "cherry")) 	        # set 	
x = frozenset(("apple", "banana", "cherry")) 	# frozenset 	
x = bool(5) 	                                # bool 	
x = bytes(5) 	                                # bytes 	
x = bytearray(5) 	                            # bytearray 	
x = memoryview(bytes(5))                        # memoryview
