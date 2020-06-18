# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1

    if n == 0:
        print(0)
    if n > 0:
        print(fibonacci_1)
    if n > 1:
        print(fibonacci_2)
    index = 0
    while index < n - 2:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
        index += 1
        print(fibonacci_2)


print(fibonacci(5))

# TODO: HW: Rewrite code, which will return only needed element of Fib sequence

def fibonacci_1(n):
    fibonacci_1 = 1
    fibonacci_2 = 1

    if n == 0:
        return(0)
    elif n == 1:
         return(1)
    else:
        fibr_number = 1
        index = 0
        while index < n - 2:
            fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
            fibr_number = fibonacci_2
            index += 1
    return(fibr_number)

print(fibonacci_1(5))

# Use of recursion

def fibonacci_2(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    return(fibonacci_2(n-1) + fibonacci_2(n-2))

print(fibonacci_2(5))
