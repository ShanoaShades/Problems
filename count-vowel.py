# This function will read each vowel one by one.
# For each vowel it will read all the text and compare.
# If a character of the text match with the vowel, count + 1.
def count_vowel(text):
  count = 0
  # The vowels could be in lowercase or uppercase.
  vowels = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
  for vowel in vowels:
    for char in text:
      # The "in" below is like == "If you find a char in vowel."
      if char in vowel:
        count += 1
  return count

# Now it's time to ask the user to write a message and count !
message_text = input("Write your message and let's count vowels ! ")
message = str(message_text)

result = count_vowel(message)
print(result)