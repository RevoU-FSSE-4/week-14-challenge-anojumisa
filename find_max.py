# find_max.py

def find_max(numbers: list) -> int:
    """
    This function takes a list of numbers and returns the largest number in the list.

    Args:
    - numbers (list): A list of numbers.

    Returns:
    - int: The largest number in the list.

    Examples:
    - find_max([1, 2, 3, 4, 5]) should return 5
    - find_max([-1, -2, -3, -4, -5]) should return -1
    """
    # Implement your solution here
    if not numbers:
        raise ValueError("The list is empty.")
    
    max_number = numbers[0]
    
    for number in numbers:
        if number > max_number:
            max_number = number
    
    return max_number

print(find_max([-1, -2, -3, -4, -5]))
# You can test your function with print statements below
# Example:
# print(find_max([1, 2, 3, 4, 5]))  # Expected output: 5
# print(find_max([-1, -2, -3, -4, -5]))  # Expected output: -1
