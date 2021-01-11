from functools import lru_cache
# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.
@lru_cache(maxsize=100)
def factorial(n):
    # Write code here
    if type(n) != int:
        raise TypeError('Value must be a positive number')
    if n < 1:
        raise ValueError('Number needs to be positive')

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# => 120