"""
Test cases for Day 1: Two Sum Problem

This file contains comprehensive test cases to verify the correctness
of the Two Sum implementation and handle various edge cases.

Run with: python test.py
Or with pytest: pytest test.py -v
"""

import sys
import pytest
from solution import two_sum, two_sum_brute_force, two_sum_hash_map, two_sum_with_edge_cases


class TestTwoSum:
    """Test class for Two Sum problem solutions."""
    
    def test_basic_cases(self):
        """Test basic functionality with standard inputs."""
        # Test case 1: Standard positive numbers
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]
        
        # Test case 2: Different order
        assert two_sum([3, 2, 4], 6) == [1, 2]
        
        # Test case 3: Duplicate numbers
        assert two_sum([3, 3], 6) == [0, 1]
        
        # Test case 4: Solution at the end
        assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Empty array
        assert two_sum([], 0) == []
        
        # Single element
        assert two_sum([1], 1) == []
        
        # No solution exists (this shouldn't happen per problem constraints)
        # But testing for robustness
        assert two_sum([1, 2, 3], 10) == []
        
        # Minimum valid input
        assert two_sum([1, 2], 3) == [0, 1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        # Both negative
        assert two_sum([-1, -2, -3, -4], -6) == [1, 3]
        
        # Mixed positive and negative
        assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
        
        # Negative target
        assert two_sum([1, -1, 0], -1) == [1, 2]
    
    def test_zero_cases(self):
        """Test cases involving zero."""
        # Zero in array
        assert two_sum([0, 4, 3, 0], 0) == [0, 3]
        
        # Target is zero
        assert two_sum([-1, 0, 1], 0) == [0, 2]
        
        # All zeros
        assert two_sum([0, 0, 0], 0) == [0, 1]
    
    def test_large_numbers(self):
        """Test with large numbers."""
        # Large positive numbers
        assert two_sum([1000000, 2000000, 3000000], 3000000) == [0, 1]
        
        # Large negative numbers
        assert two_sum([-1000000, -2000000], -3000000) == [0, 1]
    
    def test_duplicate_elements(self):
        """Test arrays with duplicate elements."""
        # Multiple duplicates
        assert two_sum([1, 1, 1, 1], 2) == [0, 1]
        
        # Some duplicates
        assert two_sum([1, 2, 1, 3], 2) == [0, 2]
    
    def test_all_solution_methods(self):
        """Test that all solution methods give same results."""
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([-1, -2, -3], -5),
            ([0, 4, 3, 0], 0)
        ]
        
        for nums, target in test_cases:
            result_optimal = two_sum(nums, target)
            result_brute = two_sum_brute_force(nums, target)
            result_hashmap = two_sum_hash_map(nums, target)
            
            # All methods should give the same result
            assert result_optimal == result_brute == result_hashmap, \
                f"Results differ for nums={nums}, target={target}"


class TestErrorHandling:
    """Test error handling and invalid inputs."""
    
    def test_invalid_inputs(self):
        """Test handling of invalid inputs."""
        with pytest.raises(ValueError):
            two_sum_with_edge_cases("not a list", 5)
        
        with pytest.raises(ValueError):
            two_sum_with_edge_cases([1, 2, 3], "not a number")
        
        with pytest.raises(ValueError):
            two_sum_with_edge_cases(None, 5)


def performance_test():
    """Manual performance test (not run with pytest)."""
    import time
    
    print("\n" + "="*50)
    print("PERFORMANCE COMPARISON")
    print("="*50)
    
    # Create a large test case
    size = 10000
    nums = list(range(size))
    target = size * 2 - 3  # Second to last + last element
    
    # Test brute force approach
    start_time = time.time()
    result_brute = two_sum_brute_force(nums, target)
    brute_time = time.time() - start_time
    
    # Test hash map approach
    start_time = time.time()
    result_hash = two_sum_hash_map(nums, target)
    hash_time = time.time() - start_time
    
    print(f"Array size: {size:,} elements")
    print(f"Brute force time: {brute_time:.4f} seconds")
    print(f"Hash map time: {hash_time:.4f} seconds")
    print(f"Speedup: {brute_time/hash_time:.1f}x")
    print(f"Results match: {result_brute == result_hash}")
    
    # Memory usage comparison
    import tracemalloc
    
    # Measure hash map memory
    tracemalloc.start()
    two_sum_hash_map(nums, target)
    hash_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    # Measure brute force memory
    tracemalloc.start()
    two_sum_brute_force(nums, target)
    brute_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    print(f"\nMemory Usage:")
    print(f"Brute force: {brute_memory / 1024:.1f} KB")
    print(f"Hash map: {hash_memory / 1024:.1f} KB")
    print(f"Memory overhead: {hash_memory / brute_memory:.1f}x")


def visual_test():
    """Visual test with step-by-step execution."""
    print("\n" + "="*50)
    print("VISUAL STEP-BY-STEP EXECUTION")
    print("="*50)
    
    nums = [2, 7, 11, 15]
    target = 9
    
    print(f"Finding two numbers in {nums} that sum to {target}:")
    print()
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        print(f"Step {i+1}: num = {num}, complement = {target} - {num} = {complement}")
        
        if complement in seen:
            print(f"✅ Found! {complement} is at index {seen[complement]}")
            print(f"   Answer: [{seen[complement]}, {i}]")
            print(f"   Verification: {nums[seen[complement]]} + {nums[i]} = {nums[seen[complement]] + nums[i]}")
            break
        else:
            print(f"   {complement} not seen yet, storing {num} at index {i}")
            seen[num] = i
            print(f"   seen = {seen}")
        print()


def run_all_tests():
    """Run all tests and demonstrations."""
    print("🧪 RUNNING TWO SUM TESTS")
    print("="*50)
    
    # Run pytest tests
    pytest.main([__file__, "-v"])
    
    # Run performance test
    performance_test()
    
    # Run visual test
    visual_test()
    
    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    run_all_tests()
