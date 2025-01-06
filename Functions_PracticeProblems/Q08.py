# 8) Generate a Python list of all the even numbers between 4 to 30.

def even_num(start, end):

    print(f"All the even numbers between {start} to {end} is: ", end = "")
    for i in range(start, end + 1):
        if(i % 2 == 0):
            print(i, end = " ")

start = 4
end = 30

even_num(start, end)