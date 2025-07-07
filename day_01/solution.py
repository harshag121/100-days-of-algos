"""
Day 1: Two Sum Problem
Topic: Array Basics
Difficulty: Easy

Problem: Given an array of integers and a target sum, return the indices of 
two numbers that add up to the target.

Author: 100 Days DSA Course
Date: Day 1
"""

def two_sum_brute_force(nums, target):
    """
    Brute force approach: Check all pairs of numbers.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
        
    Returns:
        List[int]: Indices of two numbers that sum to target
        
    Example:
        >>> two_sum_brute_force([2, 7, 11, 15], 9)
        [0, 1]
    """
    # Input validation
    if not nums or len(nums) < 2:
        return []
    
    # Check all possible pairs
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # No solution found (shouldn't happen per problem constraints)
    return []


def two_sum_hash_map(nums, target):
    """
    Optimized approach using hash map for O(1) lookups.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
        
    Returns:
        List[int]: Indices of two numbers that sum to target
        
    Example:
        >>> two_sum_hash_map([2, 7, 11, 15], 9)
        [0, 1]
    """
    # Input validation
    if not nums or len(nums) < 2:
        return []
    
    # Dictionary to store number -> index mapping
    num_to_index = {}
    
    # Single pass through the array
    for i, num in enumerate(nums):
        # Calculate what number we need to reach the target
        complement = target - num
        
        # Check if we've seen the complement before
        if complement in num_to_index:
            # Found the pair! Return indices
            return [num_to_index[complement], i]
        
        # Store current number and its index for future lookups
        num_to_index[num] = i
    
    # No solution found (shouldn't happen per problem constraints)
    return []


def two_sum_optimal(nums, target):
    """
    Most readable and efficient solution.
    This is the preferred implementation.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}  # Dictionary to store seen numbers and their indices
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in our seen dictionary, we found our answer
        if complement in seen:
            return [seen[complement], i]
        
        # Remember this number and its index
        seen[num] = i
    
    return []  # No solution found


def two_sum_with_edge_cases(nums, target):
    """
    Solution with comprehensive edge case handling.
    
    Handles:
    - Empty arrays
    - Arrays with less than 2 elements
    - Invalid inputs
    - No solution scenarios
    """
    # Edge case: Invalid input
    if not isinstance(nums, list) or not isinstance(target, (int, float)):
        raise ValueError("Invalid input: nums must be a list, target must be a number")
    
    # Edge case: Not enough elements
    if len(nums) < 2:
        return []
    
    # Main algorithm
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    # Edge case: No solution found
    return []


# Main solution function (clean and production-ready)
def two_sum(nums, target):
    """
    Find two numbers in array that add up to target sum.
    
    This function uses the hash map approach for optimal O(n) time complexity.
    It handles edge cases gracefully and returns empty list if no solution exists.
    
    Args:
        nums (List[int]): List of integers
        target (int): Target sum to find
        
    Returns:
        List[int]: List containing two indices [i, j] where nums[i] + nums[j] = target
                  Returns empty list if no solution exists
                  
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]
    """
    if len(nums) < 2:
        return []
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (nums, target, expected_output)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 2], 3, [0, 1]),
        ([5, 75, 25], 100, [1, 2])
    ]
    
    print("Testing Two Sum Solutions...")
    print("=" * 50)
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        # Test the main solution
        result = two_sum(nums, target)
        
        print(f"Test Case {i}:")
        print(f"  Input: nums = {nums}, target = {target}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {'✅ PASS' if result == expected else '❌ FAIL'}")
        print()
    
    # Performance comparison
    print("Performance Comparison:")
    print("=" * 50)
    
    import time
    
    # Large test case
    large_nums = list(range(10000))
    large_target = 19999
    
    # Test brute force
    start = time.time()
    result_bf = two_sum_brute_force(large_nums, large_target)
    time_bf = time.time() - start
    
    # Test hash map
    start = time.time()
    result_hm = two_sum_hash_map(large_nums, large_target)
    time_hm = time.time() - start
    
    print(f"Brute Force: {time_bf:.6f} seconds")
    print(f"Hash Map: {time_hm:.6f} seconds")
    print(f"Speedup: {time_bf/time_hm:.2f}x faster with hash map")
    print(f"Both got same result: {result_bf == result_hm}")
