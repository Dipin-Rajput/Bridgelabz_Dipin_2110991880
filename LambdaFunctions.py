# Lambda function

# It is also known as anonymous function.

# x = Lambda(arguments: operations/expression) # There can be more than one arguments, but only one operation or expression.

def a(a, b, c):
    return a + b + c
c = a(1, 2, 3)
print(c)

# Converting above code into lambda function.

x = lambda a, b, c : a + b + c # we can also use return function but it is not required.
print(x(4, 5, 6))

# lambda inside the function

def x(a, c):
    return lambda b, d : a + b + c + d

c = x(10, 11)
print(c(22, 20))