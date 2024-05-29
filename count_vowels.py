# count_vowels.py

def count_vowels(s: str) -> int:
    """
    This function counts the number of vowels (a, e, i, o, u) in a given string `s`.

    Args:
    - s (str): The input string.

    Returns:
    - int: The number of vowels in the string.

    Examples:
    - count_vowels("hello world") should return 3
    - count_vowels("python") should return 1
    """
    # Implement your solution here
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("python"))
    

# You can test your function with print statements below
# Example:
# print(count_vowels("hello world"))  # Expected output: 3
# print(count_vowels("python"))  # Expected output: 1
