# 12) Display Fibonacci series up to 10 terms.

first_term = 0
second_term = 1

next_term = first_term + second_term

print("Fibonacci series up to 10 terms:", first_term, second_term, end = " ")

for i in range(2, 10):
    print(next_term, end = " ")
    first_term = second_term
    second_term = next_term
    next_term = first_term + second_term