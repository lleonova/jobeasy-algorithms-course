# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2

def fibonacci(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    return(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(9))

