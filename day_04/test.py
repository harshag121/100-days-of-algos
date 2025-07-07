"""
Test cases for Day 4: Valid Palindrome

Comprehensive test suite for palindrome validation with
two-pointer technique and character filtering.

Run with: python test.py
"""

import sys
from solution import (
    is_palindrome,
    is_palindrome_clean_string,
    is_palindrome_two_pointers,
    is_valid_palindrome_ii
)


class TestValidPalindrome:
    """Test class for valid palindrome solutions."""
    
    def test_basic_cases(self):
        """Test basic palindrome functionality."""
        # Standard palindromes
        assert is_palindrome("A man, a plan, a canal: Panama") == True
        assert is_palindrome("Madam") == True
        assert is_palindrome("racecar") == True
        
        # Non-palindromes
        assert is_palindrome("race a car") == False
        assert is_palindrome("hello") == False
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Empty and single character
        assert is_palindrome("") == True
        assert is_palindrome("a") == True
        assert is_palindrome("A") == True
        
        # Only punctuation
        assert is_palindrome(".,!@#") == True
        assert is_palindrome(" ") == True
        
        # Mixed case
        assert is_palindrome("Aa") == True
        assert is_palindrome("Ab") == False
    
    def test_numeric_palindromes(self):
        """Test palindromes with numbers."""
        assert is_palindrome("12321") == True
        assert is_palindrome("1a2a1") == True
        assert is_palindrome("12345") == False
        assert is_palindrome("A1B2b1a") == True
    
    def test_complex_cases(self):
        """Test complex real-world palindromes."""
        complex_cases = [
            ("Was it a car or a cat I saw?", True),
            ("No 'x' in Nixon", True),
            ("Mr. Owl ate my metal worm", True),
            ("Madam, I'm Adam", True),
            ("Never odd or even", True),
            ("Do geese see God?", True),
        ]
        
        for text, expected in complex_cases:
            assert is_palindrome(text) == expected
    
    def test_method_consistency(self):
        """Test that all methods produce same results."""
        test_cases = [
            "A man, a plan, a canal: Panama",
            "race a car",
            "Madam",
            "12321",
            "",
            "a",
            ".,!",
        ]
        
        for test_case in test_cases:
            result1 = is_palindrome_clean_string(test_case)
            result2 = is_palindrome_two_pointers(test_case)
            result3 = is_palindrome(test_case)
            
            assert result1 == result2 == result3, \
                f"Methods disagree on '{test_case}'"
    
    def test_case_insensitive(self):
        """Test case insensitive comparison."""
        assert is_palindrome("AaA") == True
        assert is_palindrome("AbA") == False
        assert is_palindrome("RaceCar") == True
        assert is_palindrome("MaDaM") == True
    
    def test_bonus_palindrome_ii(self):
        """Test palindrome with one deletion allowed."""
        assert is_valid_palindrome_ii("aba") == True
        assert is_valid_palindrome_ii("abca") == True  # Delete 'c'
        assert is_valid_palindrome_ii("abc") == False
        assert is_valid_palindrome_ii("raceacar") == True  # Delete middle 'e'


def visual_test():
    """Visual demonstration of palindrome checking."""
    print("\n" + "="*60)
    print("VISUAL PALINDROME CHECKING")
    print("="*60)
    
    examples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Madam, I'm Adam"
    ]
    
    for example in examples:
        print(f"\nChecking: '{example}'")
        print("-" * 40)
        
        # Show cleaned version
        cleaned = ''.join(c.lower() for c in example if c.isalnum())
        print(f"Cleaned: '{cleaned}'")
        
        # Show two-pointer process
        left, right = 0, len(example) - 1
        comparisons = []
        
        while left < right:
            # Skip non-alphanumeric
            while left < right and not example[left].isalnum():
                left += 1
            while left < right and not example[right].isalnum():
                right -= 1
            
            if left < right:
                char_left = example[left].lower()
                char_right = example[right].lower()
                comparisons.append(f"'{char_left}' vs '{char_right}'")
                
                if char_left != char_right:
                    comparisons.append("❌ MISMATCH")
                    break
                
                left += 1
                right -= 1
        
        print("Comparisons:", " → ".join(comparisons))
        result = is_palindrome(example)
        print(f"Result: {'✅ Palindrome' if result else '❌ Not palindrome'}")


def performance_test():
    """Performance comparison of different approaches."""
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    
    import time
    import tracemalloc
    
    # Create test cases of different sizes
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"\nString length: {size:,} characters")
        print("-" * 30)
        
        # Create palindrome test string
        half = "a" * (size // 2)
        middle = "b" if size % 2 else ""
        test_string = half + middle + half[::-1]
        
        methods = [
            ("Clean String", is_palindrome_clean_string),
            ("Two Pointers", is_palindrome_two_pointers),
        ]
        
        for name, method in methods:
            # Measure time
            start_time = time.time()
            result = method(test_string)
            end_time = time.time()
            
            # Measure memory
            tracemalloc.start()
            method(test_string)
            _, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            space_complexity = "O(n)" if "Clean" in name else "O(1)"
            print(f"{name:15}: {end_time - start_time:.4f}s, "
                  f"{peak_memory/1024:.1f} KB ({space_complexity})")


def educational_demo():
    """Educational demonstration of two-pointer technique."""
    print("\n" + "="*60)
    print("EDUCATIONAL: TWO-POINTER PALINDROME TECHNIQUE")
    print("="*60)
    
    print("The two-pointer technique for palindromes:")
    print("1. Place pointers at both ends")
    print("2. Skip non-alphanumeric characters")
    print("3. Compare characters (case-insensitive)")
    print("4. Move pointers inward")
    print("5. Continue until pointers meet or mismatch found")
    print()
    
    example = "A man, a plan, a canal: Panama"
    print(f"Example: '{example}'")
    print()
    
    # Show character positions
    print("Position mapping:")
    valid_chars = []
    for i, char in enumerate(example):
        if char.isalnum():
            valid_chars.append((i, char.lower()))
            print(f"  Position {i:2}: '{char}' → '{char.lower()}'")
    
    print(f"\nValid characters: {[char for _, char in valid_chars]}")
    print("This reads the same forwards and backwards!")
    
    print("\nKey advantages of two-pointer approach:")
    print("• No extra space needed (O(1) vs O(n))")
    print("• Single pass through string")
    print("• Early termination on mismatch")
    print("• Handles filtering on-the-fly")


def correctness_test():
    """Comprehensive correctness testing."""
    print("\n" + "="*60)
    print("CORRECTNESS TESTING")
    print("="*60)
    
    test_cases = [
        # (input, expected, description)
        ("A man, a plan, a canal: Panama", True, "Classic palindrome"),
        ("race a car", False, "Common non-palindrome"),
        ("", True, "Empty string"),
        ("a", True, "Single character"),
        ("Aa", True, "Case insensitive"),
        ("Ab", False, "Different characters"),
        ("12321", True, "Numeric palindrome"),
        ("Was it a car or a cat I saw?", True, "Complex palindrome"),
        ("No 'x' in Nixon", True, "Tricky palindrome"),
        (".,!@#", True, "Only punctuation"),
        ("A1B2b1a", True, "Mixed alphanumeric"),
        ("Madam, I'm Adam", True, "Famous palindrome"),
    ]
    
    for i, (text, expected, description) in enumerate(test_cases, 1):
        result = is_palindrome(text)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i:2}: {description}")
        print(f"        Input: '{text}'")
        print(f"        Expected: {expected}")
        print(f"        Got: {result}")
        print(f"        Status: {status}")
        print()


def run_all_tests():
    """Run all tests and demonstrations."""
    print("🔄 TESTING VALID PALINDROME")
    print("="*60)
    
    # Create test instance and run tests
    test_instance = TestValidPalindrome()
    
    try:
        print("Running basic tests...")
        test_instance.test_basic_cases()
        print("✅ Basic tests passed")
        
        print("Running edge case tests...")
        test_instance.test_edge_cases()
        print("✅ Edge case tests passed")
        
        print("Running numeric tests...")
        test_instance.test_numeric_palindromes()
        print("✅ Numeric palindrome tests passed")
        
        print("Running complex case tests...")
        test_instance.test_complex_cases()
        print("✅ Complex case tests passed")
        
        print("Running method consistency tests...")
        test_instance.test_method_consistency()
        print("✅ All methods produce consistent results")
        
        print("Running case insensitive tests...")
        test_instance.test_case_insensitive()
        print("✅ Case insensitive tests passed")
        
        print("Running bonus palindrome II tests...")
        test_instance.test_bonus_palindrome_ii()
        print("✅ Palindrome II tests passed")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return
    
    # Run demonstrations
    visual_test()
    performance_test()
    educational_demo()
    correctness_test()
    
    print("\n🎉 All tests completed successfully!")
    print("\n🎯 Key takeaway: Two pointers + character filtering = powerful pattern!")
    print("   This technique appears in many string processing problems.")


if __name__ == "__main__":
    run_all_tests()
