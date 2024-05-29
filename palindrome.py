# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    This function checks if the given string `s` is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    - s (str): The input string.
    
    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    
    Examples:
    - is_palindrome("A man, a plan, a canal, Panama") should return True
    - is_palindrome("racecar") should return True
    - is_palindrome("hello") should return False
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not (s[left].isalpha() or s[left].isdigit()):
            left += 1
        while left < right and not (s[right].isalpha() or s[right].isdigit()):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("A man, a plan, a canal, Panama"))

# You can test your function with print statements below
# Example:
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
# print(is_palindrome("racecar"))  # Expected output: True
# print(is_palindrome("hello"))  # Expected output: False
