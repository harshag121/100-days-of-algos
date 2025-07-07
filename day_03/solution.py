"""
Day 3: Reverse String
Topic: String Basics
Difficulty: Easy

Problem: Reverse a string in-place using O(1) extra memory.

Author: 100 Days DSA Course
Date: Day 3
"""

def reverse_string_two_pointers(s):
    """
    Optimal solution using two pointers technique.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        s (List[str]): List of characters to reverse in-place
        
    Example:
        >>> s = ["h","e","l","l","o"]
        >>> reverse_string_two_pointers(s)
        >>> s
        ['o', 'l', 'l', 'e', 'h']
    """
    # Handle edge cases
    if not s or len(s) <= 1:
        return
    
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    # Swap characters from outside in
    while left < right:
        # Swap characters at left and right positions
        s[left], s[right] = s[right], s[left]
        
        # Move pointers toward center
        left += 1
        right -= 1


def reverse_string_stack(s):
    """
    Educational approach using stack (not optimal for this problem).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    This approach demonstrates stack usage but violates the O(1) space requirement.
    """
    if not s:
        return
    
    # Push all characters onto stack
    stack = []
    for char in s:
        stack.append(char)
    
    # Pop characters back into original array
    for i in range(len(s)):
        s[i] = stack.pop()


def reverse_string_recursive(s, left=0, right=None):
    """
    Recursive approach to string reversal.
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    
    Args:
        s (List[str]): List of characters to reverse
        left (int): Left pointer (default: 0)
        right (int): Right pointer (default: len(s)-1)
    """
    if right is None:
        right = len(s) - 1
    
    # Base case: pointers have met or crossed
    if left >= right:
        return
    
    # Swap characters at current positions
    s[left], s[right] = s[right], s[left]
    
    # Recursively process inner substring
    reverse_string_recursive(s, left + 1, right - 1)


def reverse_string_pythonic(s):
    """
    Pythonic approach using slicing (creates new list, then copies back).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Note: This approach is not truly in-place as it creates a new list.
    """
    if not s:
        return
    
    # Create reversed copy and assign back
    reversed_chars = s[::-1]
    for i in range(len(s)):
        s[i] = reversed_chars[i]


def reverse_string(s):
    """
    Main solution function - reverses string in-place.
    
    This is the preferred implementation using two pointers
    for optimal time and space complexity.
    
    Args:
        s (List[str]): List of characters to reverse (modified in-place)
        
    Returns:
        None (modifies s in-place)
        
    Example:
        >>> s = ["h","e","l","l","o"]
        >>> reverse_string(s)
        >>> s
        ['o', 'l', 'l', 'e', 'h']
    """
    # Input validation and edge cases
    if not s or len(s) <= 1:
        return
    
    # Two pointers approach
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers
        left += 1
        right -= 1


def reverse_only_letters(s):
    """
    Bonus: Reverse only alphabetic characters, keeping others in place.
    
    Example:
        >>> s = list("a-bC-dEf-ghIj")
        >>> reverse_only_letters(s)
        >>> ''.join(s)
        'j-Ih-gfE-dCba'
    """
    if not s:
        return
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer to next letter
        while left < right and not s[left].isalpha():
            left += 1
        
        # Move right pointer to previous letter
        while left < right and not s[right].isalpha():
            right -= 1
        
        # Swap letters
        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def is_palindrome_using_two_pointers(s):
    """
    Bonus: Check if string is palindrome using two pointers.
    
    Args:
        s (List[str]): List of characters
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome_using_two_pointers(['a','b','a'])
        True
    """
    if not s:
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def demonstrate_reversal_steps(s):
    """
    Educational function to show step-by-step reversal process.
    """
    if not s:
        print("Empty string - nothing to reverse")
        return
    
    if len(s) == 1:
        print(f"Single character {s} - already 'reversed'")
        return
    
    original = s[:]
    print(f"Reversing: {original}")
    print(f"Steps:")
    
    left, right = 0, len(s) - 1
    step = 1
    
    while left < right:
        print(f"  Step {step}: Swap s[{left}]='{s[left]}' with s[{right}]='{s[right]}'")
        s[left], s[right] = s[right], s[left]
        print(f"           Result: {s}")
        
        left += 1
        right -= 1
        step += 1
    
    print(f"Final result: {s}")


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (input, expected_output, description)
        (["h","e","l","l","o"], ["o","l","l","e","h"], "Standard string"),
        (["H","a","n","n","a","h"], ["h","a","n","n","a","H"], "Mixed case"),
        (["A"], ["A"], "Single character"),
        ([], [], "Empty string"),
        (["a","b"], ["b","a"], "Two characters"),
        (["1","2","3","4","5"], ["5","4","3","2","1"], "Numbers"),
        (["!","@","#","$"], ["$","#","@","!"], "Special characters"),
        (["a","b","c","b","a"], ["a","b","c","b","a"], "Palindrome"),
    ]
    
    print("Testing String Reversal Solutions...")
    print("=" * 60)
    
    for i, (input_chars, expected, description) in enumerate(test_cases, 1):
        # Test main solution
        test_chars = input_chars[:]
        reverse_string(test_chars)
        
        print(f"Test Case {i}: {description}")
        print(f"  Input:    {input_chars}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {test_chars}")
        print(f"  Status:   {'✅ PASS' if test_chars == expected else '❌ FAIL'}")
        print()
    
    # Demonstrate step-by-step process
    print("Step-by-Step Demonstration:")
    print("=" * 60)
    
    demo_string = ["h","e","l","l","o"]
    demonstrate_reversal_steps(demo_string)
    
    # Test all methods give same result
    print("\nMethod Comparison:")
    print("=" * 60)
    
    test_input = ["a","b","c","d","e"]
    
    # Test each method
    test1 = test_input[:]
    reverse_string_two_pointers(test1)
    
    test2 = test_input[:]
    reverse_string_stack(test2)
    
    test3 = test_input[:]
    reverse_string_recursive(test3)
    
    test4 = test_input[:]
    reverse_string_pythonic(test4)
    
    test5 = test_input[:]
    reverse_string(test5)
    
    print(f"Original:           {test_input}")
    print(f"Two Pointers:       {test1}")
    print(f"Stack:              {test2}")
    print(f"Recursive:          {test3}")
    print(f"Pythonic:           {test4}")
    print(f"Main Solution:      {test5}")
    print(f"All methods match:  {test1 == test2 == test3 == test4 == test5}")
    
    # Test bonus functions
    print("\nBonus Functions:")
    print("=" * 60)
    
    # Test reverse only letters
    letters_test = list("a-bC-dEf-ghIj")
    print(f"Reverse only letters: {''.join(letters_test)}")
    reverse_only_letters(letters_test)
    print(f"Result: {''.join(letters_test)}")
    
    # Test palindrome check
    palindrome_tests = [
        (["a","b","a"], True),
        (["r","a","c","e","c","a","r"], True),
        (["h","e","l","l","o"], False),
        (["A"], True),
        ([], True),
    ]
    
    print("\nPalindrome Tests:")
    for chars, expected in palindrome_tests:
        result = is_palindrome_using_two_pointers(chars)
        status = "✅" if result == expected else "❌"
        print(f"  {chars} → {result} {status}")
    
    # Performance test
    print("\nPerformance Test:")
    print("=" * 60)
    
    import time
    
    # Large string test
    large_chars = [chr(ord('a') + (i % 26)) for i in range(100000)]
    
    # Test two pointers method
    test_chars = large_chars[:]
    start = time.time()
    reverse_string_two_pointers(test_chars)
    two_pointer_time = time.time() - start
    
    # Test stack method
    test_chars = large_chars[:]
    start = time.time()
    reverse_string_stack(test_chars)
    stack_time = time.time() - start
    
    print(f"String length: {len(large_chars):,} characters")
    print(f"Two pointers: {two_pointer_time:.4f} seconds (O(1) space)")
    print(f"Stack method: {stack_time:.4f} seconds (O(n) space)")
    print(f"Space efficiency: Two pointers uses no extra space")
    print(f"Time difference: {abs(two_pointer_time - stack_time):.4f} seconds")
