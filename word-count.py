# Function that will count the number of white spaces. 
# We'll count white spaces and deduce the number of words. 

def word_count(text):
    count = 0
    for char in text:
        if char == " ":
            count = count + 1
 #  We count + 1 for the last word of the text. 
    return count + 1

check = False

while check == False:
    words_text = input("Tell me about you with 50 words max. ")
    words = str(words_text)    
    check_words = word_count(words)

    if check_words > 50:
        print(check_words, " words. A way too much... Let's redo it.")
    elif check_words == 1:
        print(check_words, " word. Well... Thanks for your word.")
        check = True
    else:
        print(check_words, " words. Thanks for your text ! :D")
        check = True