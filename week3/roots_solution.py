#!/usr/bin/env python
#
# Author: Oscar Benjamin
# Date: Feb 2021
# Description:
#   Command line script to find integer roots of polynomials with
#   integer coefficients.
# Author: Perla
# Date: Feb 2021
# Update: Added code for evaluate polynomials, etc


#-------------------------------------------------------------------#
#                                                                   #
#                   Command-line interface                          #
#                                                                   #
#-------------------------------------------------------------------#

PROGRAM_EXPLANATION = """
Usage:
$ python roots.py COEFF1 COEFF2 ...

Find integer roots of a polynomial with integer coefficients.

Example:

Find the roots of x^4 - 3x^3 - 75x^2 + 475x - 750.

$ python roots.py 1 -3 -75 475 -750
-10
3
5
"""


def main(*arguments):
    """Main entry point for the program"""
    if not arguments:
        print(PROGRAM_EXPLANATION)
        return

    poly = parse_coefficients(arguments)
    roots = integer_roots(poly)
    print_roots(roots)


def parse_coefficients(arguments):
    """Convert string arguments to integer

    >>> parse_coefficients(["2", "3"])
    [2, 3]
    """
    return [int(arg) for arg in arguments]


def print_roots(roots):
    """Print the roots one per line if there are any

    >>> print_roots([2, 3])
    2
    3
    """
    if roots:
        roots_str = [str(r) for r in roots]
        print('\n'.join(roots_str))


#-------------------------------------------------------------------#
#                                                                   #
#                      Polynomial functions                         #
#                                                                   #
#-------------------------------------------------------------------#


class BadPolynomialError(Exception):
    """Raised by polynomial routines when the polynomial is invalid.

    A valid polynomial is a list of coefficients like [1, 2, 1]

    The first (leading) coefficient must *not* be zero in a valid polynomial.
    """
    pass


def integer_roots(poly):
    """ Returns the integer roots of the polynomial p(x). 
        This works using the rational root theorem. 
        A simple observation is that given e.g. a polynomial 
        ax^3 + bx^2 + cx + d, then any integer root must satisfy 
        |x| <= |d|. So if for example d is 4 then the only possibilities
        for integer roots are {−4,−3,−2,−1,0,1,2,3,4}. Example:
    
    >>> integer_roots([1, -5, 6])
    [2, 3]

    """
    roots = []
    if not isinstance(poly, list):
        raise BadPolynomialError("Polynomial should be a list of coefficients")
    if poly != []:
        for coeff in poly:
            if not isinstance(coeff, int):
                raise BadPolynomialError("Polynomial should be a list of coefficients")
        d = abs(poly[-1])
        for i in range(-d, d+1):
            if is_root(poly, i):
                roots.append(i)
    return roots
    


def evaluate_polynomial(poly, xval):
    """ Calculates the value of the polynomial p(x) at x. 
        For example evaluate_polynomial([1, 2, 1], 3) calculates p(3) 
        where p(x) = x^2 + 2x + 1, p(x)=x 
    
    >>> evaluate_polynomial([1, 2, 1], 3)
    16
    """
    if not isinstance(poly, list):
        raise BadPolynomialError("Polynomial should be a list of coefficients")
    elif len(poly) == 0:
        return 0
    elif (poly == [0]):
        raise BadPolynomialError("Polynomial should be a list of coefficients")
    else:
        result = 0
        for coefficient in poly:
            if not isinstance(coefficient, int):
                raise BadPolynomialError("Polynomial should be a list of coefficients")
        poly.reverse()
        for power, coefficient in enumerate(poly):
            result += coefficient*pow(xval, power)
        poly.reverse()
        return result




def is_root(poly, xval):
    """ Returns True if x is a root of p(x) e.g.

    >>> is_root([1, 2, 1], 3)
    False
    """
    return evaluate_polynomial(poly, xval) == 0


#-------------------------------------------------------------------#
#                                                                   #
#                           Unit tests                              #
#                                                                   #
#-------------------------------------------------------------------#

#
# Run these tests with pytest:
#
#    $ pytest roots.py
#

def test_evaluate_polynomial():
    assert evaluate_polynomial([], 1) == 0
    assert evaluate_polynomial([1], 2) == 1
    assert evaluate_polynomial([1, 2], 3) == 5
    assert evaluate_polynomial([1, 2, 1], 4) == 25

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: evaluate_polynomial([0], 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial({}, 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial([[1]], 1))


def test_is_root():
    assert is_root([], 1) is True
    assert is_root([1], 1) is False
    assert is_root([1, 1], 1) is False
    assert is_root([1, 1], -1) is True
    assert is_root([1, -1], 1) is True
    assert is_root([1, -1], -1) is False
    assert is_root([1, -5, 6], 2) is True
    assert is_root([1, -5, 6], 3) is True
    assert is_root([1, -5, 6], 4) is False

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: is_root([0], 1))
    raises(BadPolynomialError, lambda: is_root({}, 1))
    raises(BadPolynomialError, lambda: is_root([[1]], 1))


def test_integer_roots():
    # In the case of the zero polynomial every value is a root but we return
    # the empty list because we can't list every possible value!
    assert integer_roots([]) == []
    assert integer_roots([1]) == []
    assert integer_roots([1, 1]) == [-1]
    assert integer_roots([2, 1]) == []
    assert integer_roots([1, -5, 6]) == [2, 3]
    assert integer_roots([1, 5, 6]) == [-3, -2]
    assert integer_roots([1, 2, 1]) == [-1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -3, -75, 475, -750]) == [-10, 3, 5]

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: integer_roots([0]))
    raises(BadPolynomialError, lambda: integer_roots({}))
    raises(BadPolynomialError, lambda: integer_roots([[1]]))


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    main(*arguments)
