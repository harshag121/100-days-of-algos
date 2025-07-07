"""
Day 4: Valid Palindrome
Topic: Two Pointers
Difficulty: Easy

Problem: Check if a string is a valid palindrome after cleaning.

Author: 100 Days DSA Course
Date: Day 4
"""

def is_palindrome_clean_string(s):
    """
    Approach 1: Clean string first, then check.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        s (str): Input string
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome_clean_string("A man, a plan, a canal: Panama")
        True
    """
    # Clean the string: keep only alphanumeric, convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointers(s):
    """
    Approach 2: Two pointers without extra space.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    This is the optimal approach.
    """
    if not s:
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def is_palindrome(s):
    """
    Main solution function - check if string is a valid palindrome.
    
    A valid palindrome reads the same forward and backward after
    removing non-alphanumeric characters and ignoring case.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if valid palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
    """
    if not s:
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer to next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move right pointer to previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters in case-insensitive manner
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers inward
        left += 1
        right -= 1
    
    return True


def is_palindrome_verbose(s):
    """
    Educational version with detailed steps for learning.
    """
    print(f"Checking if '{s}' is a palindrome...")
    
    if not s:
        print("Empty string is considered a palindrome")
        return True
    
    left, right = 0, len(s) - 1
    comparisons = 0
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            print(f"Skipping non-alphanumeric '{s[left]}' at position {left}")
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            print(f"Skipping non-alphanumeric '{s[right]}' at position {right}")
            right -= 1
        
        if left < right:
            char_left = s[left].lower()
            char_right = s[right].lower()
            comparisons += 1
            
            print(f"Comparing '{s[left]}'({char_left}) at pos {left} with '{s[right]}'({char_right}) at pos {right}")
            
            if char_left != char_right:
                print(f"Mismatch found! Not a palindrome.")
                return False
            
            print(f"Match! Moving inward...")
            left += 1
            right -= 1
    
    print(f"All {comparisons} comparisons matched. It's a palindrome!")
    return True


def is_valid_palindrome_ii(s):
    """
    Bonus: Valid Palindrome II - allow one character deletion.
    
    Returns True if string can be palindrome after deleting at most one character.
    """
    def is_palindrome_range(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try deleting left character or right character
            return (is_palindrome_range(left + 1, right) or 
                    is_palindrome_range(left, right - 1))
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (input, expected, description)
        ("A man, a plan, a canal: Panama", True, "Classic palindrome"),
        ("race a car", False, "Not a palindrome"),
        (" ", True, "Empty after cleaning"),
        ("a", True, "Single character"),
        ("Madam", True, "Simple palindrome"),
        ("No 'x' in Nixon", True, "Complex valid palindrome"),
        ("Mr. Owl ate my metal worm", True, "Long palindrome"),
        ("Was it a car or a cat I saw?", True, "Question palindrome"),
        ("", True, "Empty string"),
        ("12321", True, "Numeric palindrome"),
        ("A1B2b1a", True, "Mixed alphanumeric"),
        (".,", True, "Only punctuation"),
    ]
    
    print("Testing Valid Palindrome Solutions...")
    print("=" * 60)
    
    for i, (s, expected, description) in enumerate(test_cases, 1):
        # Test main solution
        result = is_palindrome(s)
        
        print(f"Test Case {i}: {description}")
        print(f"  Input: '{s}'")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {'✅ PASS' if result == expected else '❌ FAIL'}")
        print()
    
    # Demonstrate step-by-step process
    print("Step-by-Step Demonstration:")
    print("=" * 60)
    demo_string = "A man, a plan, a canal: Panama"
    is_palindrome_verbose(demo_string)
    
    # Test all methods give same result
    print("\nMethod Comparison:")
    print("=" * 60)
    
    test_inputs = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Madam",
        "12321"
    ]
    
    for test_input in test_inputs:
        result1 = is_palindrome_clean_string(test_input)
        result2 = is_palindrome_two_pointers(test_input)
        result3 = is_palindrome(test_input)
        
        print(f"Input: '{test_input}'")
        print(f"  Clean String: {result1}")
        print(f"  Two Pointers: {result2}")
        print(f"  Main Solution: {result3}")
        print(f"  All match: {result1 == result2 == result3}")
        print()
    
    # Test bonus function
    print("Bonus: Valid Palindrome II (allow one deletion):")
    print("=" * 60)
    
    palindrome_ii_tests = [
        ("aba", True),
        ("abca", True),  # Delete 'c'
        ("abc", False),
        ("raceacar", True),  # Delete 'e'
        ("abcddcba", True),  # Already palindrome
    ]
    
    for test_input, expected in palindrome_ii_tests:
        result = is_valid_palindrome_ii(test_input)
        status = "✅" if result == expected else "❌"
        print(f"  '{test_input}' → {result} {status}")
    
    # Performance test
    print("\nPerformance Test:")
    print("=" * 60)
    
    import time
    
    # Large palindrome test
    large_palindrome = "a" * 50000 + "b" + "a" * 50000
    
    # Test clean string method
    start = time.time()
    result1 = is_palindrome_clean_string(large_palindrome)
    time1 = time.time() - start
    
    # Test two pointers method
    start = time.time()
    result2 = is_palindrome_two_pointers(large_palindrome)
    time2 = time.time() - start
    
    print(f"String length: {len(large_palindrome):,} characters")
    print(f"Clean string method: {time1:.4f} seconds (O(n) space)")
    print(f"Two pointers method: {time2:.4f} seconds (O(1) space)")
    print(f"Both methods agree: {result1 == result2}")
    print(f"Space efficiency: Two pointers saves memory for large inputs")
