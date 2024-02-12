
def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input")
    return user_input

while(True):
    word = get_input("input any word you think is a palindrome", str)

    if word == word[::-1]:
        print(f"your word: {word}, is a palindrome")
    
    elif word != word[::-1]:
        print(f"your word: {word}, is NOT a palindrome")

    print(word)
    print(word[::-1])