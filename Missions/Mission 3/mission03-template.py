#
# CS1010S --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))


# Your answer here: n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation: The function add1 will be repeated 3^3 = 27 times, so the final answer is 6 + 1*27 = 33.

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation: The function is composed, but no value is entered to the equation, so the function does not return a value.

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: The function sq(1) will be repeated 3^3 = 27 times, so the final answer is (1^2)^27 = 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: The function sq(2) will be repeated 3^3 = 27 times, so the final answer is 2^27. However, the number is too large, and I do not have the patience to wait for it to finish running.


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    if t == 1:
        return 1
    else:
        def f(x):
            if x == 1:
                return 1/2
            else:
                return x**2
        def op(x, y):
            return int(x + 2*y)
    n  = t+1
    return combine(f, op, n)

print(smiley_sum(4))

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        if x == 0 or x == 1:
            return x
        else:
            return f(x-1) + f(x-2)
    def op(x, y):
        return y
    return combine(f, op, n+1)

# Your answer here: Yes
