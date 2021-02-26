# myscript.py

def double(thing):
    """Doubles the thing"""

    return thing + thing

def factorial(x):
    """Computes x! for any nonnegative integer x"""
    if not isinstance(x, int):
        raise TypeError("x should be of type int")
    if x < 0:
        raise ValueError("x should be nonnegative")
        
    xfact = 1
    while x != 0: 	# True
        xfact *= x 	# xfact = xfact * x = 1 * 5 = 5
        x -= 1 		# x = x - 1 = 5 - 1 = 4
    return xfact

if __name__ == '__main__':
	try:
		print(int(double(2)))
		print(int(double([1, 2])))
		print(int(double("foo")))
	except TypeError:
		print("The type wasn't right")
	print("Some other line")