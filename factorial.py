"""Module for estimation of factorial (Homework #1)
    """

from nose.tools import assert_equal
from nose.tools import assert_raises
import time


def factorial_recursive(n):
    """ Calculates n! using recursion. n must be a
    non-negative integer
    """
    if (type(n) != int) or n < 0:
        raise ValueError('This function is only defined for'
                         ' non-negative integers')
    elif n == 0:
        return 1
    else:
        again = factorial_recursive(n-1)
        return n * again


def factorial(n):
    """ Calculates n! using loops n must be a
    non-negative integer
    """
    result = n
    if type(n) != int or n < 0:
        raise ValueError('This function is only defined for'
                         ' non-negative integers')
    elif n == 0:
        return 1
    while n > 1:
        result *= (n-1)
        n -= 1
    return result


def time_function(n, func2time):
    """Computation time test for any function 'func2time'
    that takes one positional argument 'n'. Used here for
    factorial and factorial_recursive
    """
    tStart = time.time()
    func2time(n)
    elapsed = time.time() - tStart
    return elapsed


def time_test(n):
    """Times the factorial and factorial_recursive functions
    for n and returns times in that order
    """
    a = time_function(n, factorial_recursive)
    b = time_function(n, factorial)
    return a, b


def test_factorial():
    """Tests factorial and factorial_recursive to ensure
    that they give the same output given legal input and
    raise ValueError for negative numbers, floats, and strings
    """
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(99), factorial(99))
    assert_raises(ValueError, factorial, -1)
    assert_raises(ValueError, factorial_recursive, -1)
    assert_raises(ValueError, factorial_recursive, 3.14159)
    assert_raises(ValueError, factorial, 3.14159)
    assert_raises(ValueError, factorial_recursive, 'string')
    assert_raises(ValueError, factorial, 'string')


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below
    nconditions = int(raw_input("Please enter number of conditions: "))
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
