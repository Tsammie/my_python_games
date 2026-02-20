text = input("Please input text only : ")
is_palindrome = text == text[::-1]
print(f'It is {is_palindrome} that {text} is a palindrome.')