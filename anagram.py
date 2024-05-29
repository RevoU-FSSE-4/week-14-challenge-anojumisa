# anagram.py
import re 
from collections import Counter
def is_anagram(s1: str, s2: str) -> bool:
    """
    This function checks if the two given strings `s1` and `s2` are anagrams.
    
    Two strings are anagrams if they contain the same characters with the same frequencies,
    ignoring spaces and capitalization.
    
    Args:
    - s1 (str): The first input string.
    - s2 (str): The second input string.
    
    Returns:
    - bool: True if the strings are anagrams, False otherwise.
    
    Examples:
    - is_anagram("Listen", "Silent") should return True
    - is_anagram("hello", "billion") should return False
    """
    # Step 1: Clean the strings by removing non-alphanumeric characters and converting to lowercase
    # Step 2: Compare the character counts of both cleaned strings
    
    # Implement your solution here
    def clean_string(s: str) -> str:
        cleaned = ''
        for char in s:
            if char.isalnum():  
                cleaned += char.lower()  
        return cleaned

    def char_count(s: str) -> dict:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count

    cleaned_s1 = clean_string(s1)
    cleaned_s2 = clean_string(s2)
    
    return char_count(cleaned_s1) == char_count(cleaned_s2)

print(is_anagram("hello", "billion")) 
pass
# You can test your function with print statements below
# Example:
# print(is_anagram("Listen", "Silent"))  # Expected output: True
# print(is_anagram("hello", "billion"))  # Expected output: False
