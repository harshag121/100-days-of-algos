"""
Test cases for Day 2: Array Rotation

This file contains comprehensive test cases for the array rotation problem,
including edge cases and performance comparisons.

Run with: python test.py
"""

import sys
from solution import (
    rotate, 
    rotate_with_extra_space, 
    rotate_cyclic_replacement, 
    rotate_reverse_method,
    rotate_left
)


class TestArrayRotation:
    """Test class for Array Rotation problem solutions."""
    
    def test_basic_cases(self):
        """Test basic functionality."""
        # Test case 1: Standard case
        nums = [1,2,3,4,5,6,7]
        rotate(nums, 3)
        assert nums == [5,6,7,1,2,3,4]
        
        # Test case 2: Negative numbers
        nums = [-1,-100,3,99]
        rotate(nums, 2)
        assert nums == [3,99,-1,-100]
        
        # Test case 3: Single element
        nums = [1]
        rotate(nums, 1)
        assert nums == [1]
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # k = 0 (no rotation)
        nums = [1,2,3,4,5]
        rotate(nums, 0)
        assert nums == [1,2,3,4,5]
        
        # k > array length
        nums = [1,2,3]
        rotate(nums, 4)  # k=4, n=3, so k%n=1
        assert nums == [3,1,2]
        
        # k = array length (full rotation)
        nums = [1,2,3,4]
        rotate(nums, 4)
        assert nums == [1,2,3,4]
        
        # Two elements
        nums = [1,2]
        rotate(nums, 1)
        assert nums == [2,1]
        
        # Empty array (edge case, though not in constraints)
        nums = []
        rotate(nums, 3)
        assert nums == []
    
    def test_large_k_values(self):
        """Test with k values much larger than array length."""
        nums = [1,2,3,4,5]
        rotate(nums, 13)  # 13 % 5 = 3
        assert nums == [3,4,5,1,2]
        
        nums = [1,2,3]
        rotate(nums, 100)  # 100 % 3 = 1
        assert nums == [3,1,2]
    
    def test_all_methods_consistency(self):
        """Test that all rotation methods produce the same result."""
        test_cases = [
            ([1,2,3,4,5,6,7], 3),
            ([-1,-100,3,99], 2),
            ([1], 1),
            ([1,2,3,4,5], 7),
            ([10,20,30,40], 0),
        ]
        
        for original_nums, k in test_cases:
            # Test all methods
            nums1 = original_nums[:]
            rotate_with_extra_space(nums1, k)
            
            nums2 = original_nums[:]
            rotate_cyclic_replacement(nums2, k)
            
            nums3 = original_nums[:]
            rotate_reverse_method(nums3, k)
            
            nums4 = original_nums[:]
            rotate(nums4, k)
            
            # All should be equal
            assert nums1 == nums2 == nums3 == nums4, \
                f"Methods disagree on {original_nums} with k={k}"
    
    def test_left_rotation(self):
        """Test left rotation functionality."""
        nums = [1,2,3,4,5,6,7]
        rotate_left(nums, 3)
        # Left rotation by 3 should give [4,5,6,7,1,2,3]
        assert nums == [4,5,6,7,1,2,3]
    
    def test_in_place_modification(self):
        """Test that the array is modified in-place."""
        nums = [1,2,3,4,5]
        original_id = id(nums)
        rotate(nums, 2)
        
        # Should be the same object (in-place modification)
        assert id(nums) == original_id
        assert nums == [4,5,1,2,3]


def visual_test():
    """Visual demonstration of the rotation process."""
    print("\n" + "="*60)
    print("VISUAL ROTATION DEMONSTRATION")
    print("="*60)
    
    # Test case 1
    print("Example 1: Rotate [1,2,3,4,5,6,7] right by 3 steps")
    print("-" * 50)
    
    nums = [1,2,3,4,5,6,7]
    n = len(nums)
    k = 3
    
    print(f"Original array: {nums}")
    print(f"We want to rotate right by {k} steps")
    print()
    
    # Show the reverse method step by step
    def reverse_range(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Step 1
    print("Step 1: Reverse the entire array")
    reverse_range(nums, 0, n - 1)
    print(f"Result: {nums}")
    print()
    
    # Step 2
    print(f"Step 2: Reverse the first {k} elements")
    reverse_range(nums, 0, k - 1)
    print(f"Result: {nums}")
    print()
    
    # Step 3
    print(f"Step 3: Reverse the remaining {n-k} elements")
    reverse_range(nums, k, n - 1)
    print(f"Final result: {nums}")
    print()
    
    # Test case 2
    print("Example 2: Rotate [-1,-100,3,99] right by 2 steps")
    print("-" * 50)
    
    nums = [-1,-100,3,99]
    print(f"Original: {nums}")
    rotate(nums, 2)
    print(f"After rotation: {nums}")


def performance_test():
    """Performance comparison of different methods."""
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    
    import time
    import tracemalloc
    
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"\nArray size: {size:,} elements")
        print("-" * 30)
        
        # Create test data
        test_array = list(range(size))
        k = size // 2
        
        methods = [
            ("Extra Space", rotate_with_extra_space),
            ("Cyclic", rotate_cyclic_replacement),
            ("Reverse (Optimal)", rotate_reverse_method)
        ]
        
        for name, method in methods:
            # Test time
            nums = test_array[:]
            start_time = time.time()
            method(nums, k)
            end_time = time.time()
            
            # Test memory
            tracemalloc.start()
            nums = test_array[:]
            method(nums, k)
            _, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            print(f"{name:15}: {end_time - start_time:.4f}s, {peak_memory/1024:.1f} KB")


def correctness_test():
    """Comprehensive correctness testing."""
    print("\n" + "="*60)
    print("CORRECTNESS TESTING")
    print("="*60)
    
    test_cases = [
        # (original_array, k, expected_result, description)
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4], "Standard case"),
        ([-1,-100,3,99], 2, [3,99,-1,-100], "Negative numbers"),
        ([1], 1, [1], "Single element"),
        ([1,2], 3, [2,1], "k > length"),
        ([1,2,3,4,5], 0, [1,2,3,4,5], "No rotation"),
        ([1,2,3], 6, [1,2,3], "k = 2*length"),
        ([5,7,7,8,8,10], 3, [8,8,10,5,7,7], "Duplicates"),
    ]
    
    for i, (original, k, expected, description) in enumerate(test_cases, 1):
        nums = original[:]
        rotate(nums, k)
        
        status = "✅ PASS" if nums == expected else "❌ FAIL"
        print(f"Test {i}: {description}")
        print(f"  Input: {original}, k={k}")
        print(f"  Expected: {expected}")
        print(f"  Got: {nums}")
        print(f"  Status: {status}")
        print()


def run_all_tests():
    """Run all tests and demonstrations."""
    print("🔄 TESTING ARRAY ROTATION")
    print("="*60)
    
    # Create test instance and run basic tests
    test_instance = TestArrayRotation()
    
    try:
        print("Running basic tests...")
        test_instance.test_basic_cases()
        print("✅ Basic tests passed")
        
        print("Running edge case tests...")
        test_instance.test_edge_cases()
        print("✅ Edge case tests passed")
        
        print("Running method consistency tests...")
        test_instance.test_all_methods_consistency()
        print("✅ All methods produce consistent results")
        
        print("Running in-place modification tests...")
        test_instance.test_in_place_modification()
        print("✅ In-place modification confirmed")
        
        print("Running left rotation tests...")
        test_instance.test_left_rotation()
        print("✅ Left rotation works correctly")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return
    
    # Run demonstrations
    visual_test()
    performance_test()
    correctness_test()
    
    print("\n🎉 All tests completed successfully!")


if __name__ == "__main__":
    run_all_tests()
