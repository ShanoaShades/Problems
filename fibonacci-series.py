# The function that will add Fibonacci's numbers depending of the user's number.
def fibonacci(amount, list):
    i = 2

    while i < amount:
        next_fibo = list[i-1] + list[i-2]
        list.append(next_fibo)
        i += 1
    return list

# Variables and starting list
amount_text = input("How many numbers of the Fibonacci series do you wanna see ? ")

amount = int(amount_text)
fibo = [0, 1]
fibo_list = fibonacci(amount, fibo)

# A little test to check if the user wrote numbers under 2
if amount <= 0:
  print("(｡•́︿•̀｡)")
elif amount == 1:
  fibo.pop()
  print(fibo)
else:     
  print(fibo_list)