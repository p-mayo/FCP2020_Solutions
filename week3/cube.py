# cube.py

def cube(x):
    """Returns the cube of x"""
    return x**3  # <--- This obviously doesn't work correctly
    #return x*x*x

def test_square():
    assert cube(0) == 0
    assert cube(2) == 8
    assert cube(-2) == -8