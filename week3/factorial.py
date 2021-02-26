# factorial.py

def factorial(x):
    """Computes x! for any nonnegative integer x"""
    xfact = 1
    while x != 0:
        xfact *= x
        x -= 1
    return xfact

print(factorial(5))
print(factorial(-1))