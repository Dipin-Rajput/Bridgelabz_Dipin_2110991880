# 11) Print all prime numbers within a range.

num = int(input("Enter the range: "))
prime = list()

if(num <= 1):
    print("No, prime number in this range.")
else:
    for i in range(2, num + 1):
        for j in range(2, int(i/2) + 1):
            if(i % j == 0):
                break
        else:
            prime.append(i)

print("All prime numbers within give range are:", prime)
