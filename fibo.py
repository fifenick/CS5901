#!/uer/bin/env python
import sys

def fibonacci(n):
    """ write a Fibonacci series up to n """
    a,b, = 0,1
    while b < n:
        print(b)
        a,b = b, a+b

def fibonacci2(n):
    """ write a Fibonacci series up to n """
    a,b, = 0,1
    results = []
    while b < n:
        results.append(b)
        a,b = b, a+b
    return results

if __name__ == "__main__":
    if len(sys.argv[1]) > 0:
        print (fibonacci2(int(sys.argv[1])))