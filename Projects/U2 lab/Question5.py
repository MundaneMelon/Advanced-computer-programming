def is_palindrome(string1):
    if string1.lower() == string1[::-1].lower():
        return True
    return False
