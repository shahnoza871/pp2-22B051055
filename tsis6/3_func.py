# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
string = input('Enter text: ')
def is_palindrome(string):
    temp = list(string)
    temp.reverse()
    return True if "".join(temp) == string else False
print(is_palindrome(string))