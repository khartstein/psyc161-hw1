"""Module for estimation of factorial (Homework #1)
    """

from nose.tools import assert_equal
import time

def factorial_recursive(n):
    if type(n) != int:
        print 'This function is only defined for non-negative integers'
        return None
    elif n < 0:
        print 'This function is only defined for non-negative integers'
        return None
    elif n == 0:
        return 1
    else:
        again = factorial_recursive(n-1)
        # crashes here when n is set to (super) large numbers
        output = n * again
        return output

def factorial(n):
    result = n
    if type(n) != int:
        print 'This function is only defined for non-negative integers'
        return None
    elif n < 0:
        print 'This function is only defined for non-negative integers'
        return None
    elif n == 0:
        return 1
    while n > 1:
        result = result*(n-1)
        n = n-1
    return result


def timeRecursive(n):
    tStart = time.clock()
    factorial_recursive(n)
    elapsed = time.clock() - tStart
    return elapsed

def timeNonRecursive(n):
    tStart = time.clock()
    factorial(n)
    elapsed = time.clock() - tStart
    return elapsed

def timeTest(n):
    a = timeRecursive(n)
    b = timeNonRecursive(n)
    print 'For calculating the factorial of %(a)s, the time ratio (recursive:non-recursive) is %(ratio)s.' %{'a':n,'ratio': a/b}

def test_factorial():
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(99),factorial(99))
    assert_equal(factorial_recursive(-1), None)
    assert_equal(factorial_recursive(3.14159), None)
    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(int(nconditions))
    print("Number of possible trial orders: " + str(norders))

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below
    
    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))