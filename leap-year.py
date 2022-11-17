year_text = input("Which year do you want to check ?")
year = int(year_text)

# This fonction will check if the year can be divided by 4.
# If the remainder is equal to 0, it's a leap year.
def leap_year(y): 
     if y%4 == 0:
         return "is a leap year."
     else:
         return "isn't a leap year."

result = leap_year(year)
print(year, result)