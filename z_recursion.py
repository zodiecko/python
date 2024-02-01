from typing import Optional

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

#tail_recursion
def fibonacci_tail(n, previous: Optional[int] = 0, current: Optional[int] = 1):#n-ésimo, anterior ao inicial, número inicial# n-ésimo, n0 - 1, n0
    if n == 0:
        return previous
    elif n == 1:
        return current
    else:
        return fibonacci_tail(n - 1, current, previous + current)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def fatorial_tail(n, previous: Optional[int] = 1):
    if n == 0:
        return previous
    else:
        return fatorial_tail(n-1, n * previous)

print(fibonacci(0))

# 1, 1, 2, 3