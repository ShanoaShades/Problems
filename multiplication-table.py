# The function will take a number and multiply it with the variable of a loop.
def multiplication_table(num):
    i = 0

    while i <= 10:
        print(i, "X", num, "= ", i*num)
        i += 1

# We ask the user to type a number.
print("Multiplication table 0 -> 10")
number_text = input("Write  a number : ")
number = int(number_text)

multiplication_table(number)

