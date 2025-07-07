"""
Test cases for Day 3: Reverse String

Comprehensive test suite for string reversal problem with
edge cases, performance tests, and educational demonstrations.

Run with: python test.py
"""

import sys
from solution import (
    reverse_string,
    reverse_string_two_pointers,
    reverse_string_stack,
    reverse_string_recursive,
    reverse_only_letters,
    is_palindrome_using_two_pointers
)


class TestReverseString:
    """Test class for string reversal solutions."""
    
    def test_basic_cases(self):
        """Test basic functionality."""
        # Test case 1: Standard string
        s = ["h","e","l","l","o"]
        reverse_string(s)
        assert s == ["o","l","l","e","h"]
        
        # Test case 2: Mixed case
        s = ["H","a","n","n","a","h"]
        reverse_string(s)
        assert s == ["h","a","n","n","a","H"]
        
        # Test case 3: Single character
        s = ["A"]
        reverse_string(s)
        assert s == ["A"]
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Empty string
        s = []
        reverse_string(s)
        assert s == []
        
        # Two characters
        s = ["a","b"]
        reverse_string(s)
        assert s == ["b","a"]
        
        # Palindrome
        s = ["a","b","c","b","a"]
        reverse_string(s)
        assert s == ["a","b","c","b","a"]
        
        # All same characters
        s = ["x","x","x","x"]
        reverse_string(s)
        assert s == ["x","x","x","x"]
    
    def test_special_characters(self):
        """Test with special characters and numbers."""
        # Numbers
        s = ["1","2","3","4","5"]
        reverse_string(s)
        assert s == ["5","4","3","2","1"]
        
        # Special characters
        s = ["!","@","#","$","%"]
        reverse_string(s)
        assert s == ["%","$","#","@","!"]
        
        # Mixed alphanumeric
        s = ["a","1","b","2","c"]
        reverse_string(s)
        assert s == ["c","2","b","1","a"]
    
    def test_all_methods_consistency(self):
        """Test that all reversal methods produce the same result."""
        test_cases = [
            ["h","e","l","l","o"],
            ["A"],
            [],
            ["a","b"],
            ["1","2","3","4","5"],
            ["!","@","#"],
        ]
        
        for original in test_cases:
            # Test all methods
            s1 = original[:]
            reverse_string_two_pointers(s1)
            
            s2 = original[:]
            reverse_string_stack(s2)
            
            s3 = original[:]
            reverse_string_recursive(s3)
            
            s4 = original[:]
            reverse_string(s4)
            
            # All should be equal
            assert s1 == s2 == s3 == s4, \
                f"Methods disagree on {original}"
    
    def test_in_place_modification(self):
        """Test that reversal happens in-place."""
        s = ["a","b","c","d","e"]
        original_id = id(s)
        reverse_string(s)
        
        # Should be the same object
        assert id(s) == original_id
        assert s == ["e","d","c","b","a"]
    
    def test_bonus_functions(self):
        """Test bonus functionality."""
        # Test reverse only letters
        s = list("a-bC-dEf-ghIj")
        reverse_only_letters(s)
        assert ''.join(s) == "j-Ih-gfE-dCba"
        
        # Test palindrome detection
        assert is_palindrome_using_two_pointers(["a","b","a"]) == True
        assert is_palindrome_using_two_pointers(["a","b","c"]) == False
        assert is_palindrome_using_two_pointers([]) == True
        assert is_palindrome_using_two_pointers(["x"]) == True


def visual_test():
    """Visual demonstration of the reversal process."""
    print("\n" + "="*60)
    print("VISUAL REVERSAL DEMONSTRATION")
    print("="*60)
    
    test_strings = [
        ["h","e","l","l","o"],
        ["a","b","c"],
        ["A"],
        ["x","y"],
    ]
    
    for s in test_strings:
        print(f"\nReversing: {s}")
        print("-" * 30)
        
        if not s:
            print("Empty string - nothing to reverse")
            continue
        
        if len(s) == 1:
            print("Single character - already 'reversed'")
            continue
        
        # Show step by step
        work_copy = s[:]
        left, right = 0, len(work_copy) - 1
        step = 1
        
        print(f"Initial:  {work_copy}")
        
        while left < right:
            print(f"Step {step}: Swap positions {left} and {right}")
            print(f"         Swap '{work_copy[left]}' and '{work_copy[right]}'")
            work_copy[left], work_copy[right] = work_copy[right], work_copy[left]
            print(f"         Result: {work_copy}")
            
            left += 1
            right -= 1
            step += 1
        
        print(f"Final:    {work_copy}")


def performance_test():
    """Performance comparison of different methods."""
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    
    import time
    import tracemalloc
    
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"\nString length: {size:,} characters")
        print("-" * 30)
        
        # Create test data
        test_chars = [chr(ord('a') + (i % 26)) for i in range(size)]
        
        methods = [
            ("Two Pointers (Optimal)", reverse_string_two_pointers),
            ("Stack Method", reverse_string_stack),
            ("Recursive", reverse_string_recursive),
        ]
        
        for name, method in methods:
            # Test time
            chars = test_chars[:]
            start_time = time.time()
            method(chars)
            end_time = time.time()
            
            # Test memory
            tracemalloc.start()
            chars = test_chars[:]
            method(chars)
            _, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            space_complexity = "O(1)" if "Two Pointers" in name else "O(n)"
            print(f"{name:20}: {end_time - start_time:.4f}s, "
                  f"{peak_memory/1024:.1f} KB ({space_complexity})")


def correctness_test():
    """Comprehensive correctness testing."""
    print("\n" + "="*60)
    print("CORRECTNESS TESTING")
    print("="*60)
    
    test_cases = [
        # (input, expected, description)
        (["h","e","l","l","o"], ["o","l","l","e","h"], "Standard case"),
        (["H","a","n","n","a","h"], ["h","a","n","n","a","H"], "Mixed case"),
        (["A"], ["A"], "Single character"),
        ([], [], "Empty string"),
        (["a","b"], ["b","a"], "Two characters"),
        (["1","2","3","4","5"], ["5","4","3","2","1"], "Numbers"),
        (["!","@","#","$"], ["$","#","@","!"], "Special chars"),
        (["a","b","c","b","a"], ["a","b","c","b","a"], "Palindrome"),
        (["x","x","x"], ["x","x","x"], "All same"),
        (["a","1","B","2","c"], ["c","2","B","1","a"], "Mixed alphanumeric"),
    ]
    
    for i, (original, expected, description) in enumerate(test_cases, 1):
        s = original[:]
        reverse_string(s)
        
        status = "✅ PASS" if s == expected else "❌ FAIL"
        print(f"Test {i:2}: {description}")
        print(f"        Input: {original}")
        print(f"        Expected: {expected}")
        print(f"        Got: {s}")
        print(f"        Status: {status}")
        print()


def educational_demo():
    """Educational demonstration of two-pointer technique."""
    print("\n" + "="*60)
    print("EDUCATIONAL DEMO: TWO-POINTER TECHNIQUE")
    print("="*60)
    
    print("The two-pointer technique is fundamental in many algorithms:")
    print()
    
    # Demo 1: Basic reversal
    print("1. String Reversal:")
    s = ["a","b","c","d","e"]
    print(f"   Original: {s}")
    print("   Two pointers start at ends and move toward center")
    
    left, right = 0, len(s) - 1
    while left < right:
        print(f"   Swap s[{left}]='{s[left]}' with s[{right}]='{s[right]}'")
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    print(f"   Result: {s}")
    print()
    
    # Demo 2: Palindrome check
    print("2. Palindrome Check (bonus):")
    test_palindromes = [
        ["r","a","c","e","c","a","r"],
        ["h","e","l","l","o"],
    ]
    
    for chars in test_palindromes:
        is_pal = is_palindrome_using_two_pointers(chars)
        print(f"   {chars} → {'Palindrome' if is_pal else 'Not palindrome'}")
    
    print()
    print("Key insights:")
    print("• Two pointers eliminate need for extra space")
    print("• Works for many symmetric operations")
    print("• Time complexity: O(n), Space complexity: O(1)")
    print("• Pattern appears in many problems!")


def run_all_tests():
    """Run all tests and demonstrations."""
    print("📝 TESTING STRING REVERSAL")
    print("="*60)
    
    # Create test instance and run tests
    test_instance = TestReverseString()
    
    try:
        print("Running basic tests...")
        test_instance.test_basic_cases()
        print("✅ Basic tests passed")
        
        print("Running edge case tests...")
        test_instance.test_edge_cases()
        print("✅ Edge case tests passed")
        
        print("Running special character tests...")
        test_instance.test_special_characters()
        print("✅ Special character tests passed")
        
        print("Running method consistency tests...")
        test_instance.test_all_methods_consistency()
        print("✅ All methods produce consistent results")
        
        print("Running in-place modification tests...")
        test_instance.test_in_place_modification()
        print("✅ In-place modification confirmed")
        
        print("Running bonus function tests...")
        test_instance.test_bonus_functions()
        print("✅ Bonus functions work correctly")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return
    
    # Run demonstrations
    visual_test()
    performance_test()
    correctness_test()
    educational_demo()
    
    print("\n🎉 All tests completed successfully!")
    print("\n🎯 Key takeaway: Master the two-pointer technique!")
    print("   It's one of the most important patterns in DSA.")


if __name__ == "__main__":
    run_all_tests()
