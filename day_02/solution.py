"""
Day 2: Array Rotation
Topic: Array Manipulation
Difficulty: Medium

Problem: Rotate an array to the right by k steps in-place with O(1) extra memory.

Author: 100 Days DSA Course
Date: Day 2
"""

def rotate_with_extra_space(nums, k):
    """
    Naive approach using extra space.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums (List[int]): Array to rotate (modified in-place)
        k (int): Number of steps to rotate right
        
    Example:
        >>> nums = [1,2,3,4,5,6,7]
        >>> rotate_with_extra_space(nums, 3)
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]
    """
    if not nums or k == 0:
        return
    
    n = len(nums)
    k = k % n  # Handle k > n
    
    if k == 0:
        return
    
    # Create a copy of the array
    temp = nums[:]
    
    # Place elements in their new positions
    for i in range(n):
        nums[(i + k) % n] = temp[i]


def rotate_cyclic_replacement(nums, k):
    """
    Cyclic replacement approach - move elements one by one.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    This method handles cases where gcd(n, k) > 1 by using multiple cycles.
    """
    if not nums or k == 0:
        return
    
    n = len(nums)
    k = k % n
    
    if k == 0:
        return
    
    def gcd(a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a
    
    # Number of cycles needed
    cycles = gcd(n, k)
    
    for start in range(cycles):
        current = start
        prev = nums[start]
        
        # Move elements in this cycle
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            
            # If we've completed the cycle
            if start == current:
                break


def rotate_reverse_method(nums, k):
    """
    Optimal approach using three reversals.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Algorithm:
    1. Reverse the entire array
    2. Reverse the first k elements
    3. Reverse the remaining n-k elements
    
    Example:
        nums = [1,2,3,4,5,6,7], k = 3
        Step 1: [7,6,5,4,3,2,1]  (reverse all)
        Step 2: [5,6,7,4,3,2,1]  (reverse first 3)
        Step 3: [5,6,7,1,2,3,4]  (reverse last 4)
    """
    if not nums or k == 0:
        return
    
    n = len(nums)
    k = k % n
    
    if k == 0:
        return
    
    def reverse(start, end):
        """Reverse array elements from start to end (inclusive)."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse the remaining elements
    reverse(k, n - 1)


def rotate(nums, k):
    """
    Main solution function - rotates array to the right by k steps.
    
    This is the preferred implementation using the reverse method
    for optimal time and space complexity.
    
    Args:
        nums (List[int]): Array to rotate (modified in-place)
        k (int): Number of positions to rotate right
        
    Returns:
        None (modifies nums in-place)
        
    Example:
        >>> nums = [1,2,3,4,5,6,7]
        >>> rotate(nums, 3)
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]
    """
    # Input validation
    if not nums or len(nums) <= 1 or k == 0:
        return
    
    n = len(nums)
    k = k % n  # Handle case where k > n
    
    if k == 0:  # No rotation needed after modulo
        return
    
    def reverse_range(start, end):
        """Helper function to reverse elements in range [start, end]."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Three-step reversal process
    reverse_range(0, n - 1)      # Reverse entire array
    reverse_range(0, k - 1)      # Reverse first k elements
    reverse_range(k, n - 1)      # Reverse remaining elements


def rotate_left(nums, k):
    """
    Bonus: Rotate array to the left by k steps.
    
    Left rotation by k is equivalent to right rotation by (n - k).
    """
    if not nums:
        return
    
    n = len(nums)
    k = k % n
    
    # Convert left rotation to right rotation
    rotate(nums, n - k)


def demonstrate_rotation_steps(nums, k):
    """
    Educational function to show step-by-step rotation process.
    """
    if not nums:
        return
    
    original = nums[:]
    n = len(nums)
    k = k % n
    
    print(f"Rotating {original} right by {k} steps:")
    print(f"Original array: {nums}")
    
    # Step 1: Reverse entire array
    def reverse_range(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse_range(0, n - 1)
    print(f"After reversing all: {nums}")
    
    # Step 2: Reverse first k elements
    reverse_range(0, k - 1)
    print(f"After reversing first {k}: {nums}")
    
    # Step 3: Reverse remaining elements
    reverse_range(k, n - 1)
    print(f"After reversing last {n-k}: {nums}")
    print(f"Final result: {nums}")


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (nums, k, expected_result)
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        ([1], 1, [1]),
        ([1,2], 1, [2,1]),
        ([1,2,3], 4, [3,1,2]),  # k > n case
        ([1,2,3,4,5], 0, [1,2,3,4,5]),  # k = 0 case
        ([1,2,3,4,5,6], 6, [1,2,3,4,5,6]),  # k = n case
    ]
    
    print("Testing Array Rotation Solutions...")
    print("=" * 60)
    
    for i, (nums_orig, k, expected) in enumerate(test_cases, 1):
        # Test main solution
        nums = nums_orig[:]
        rotate(nums, k)
        
        print(f"Test Case {i}:")
        print(f"  Original: {nums_orig}, k = {k}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {nums}")
        print(f"  Status:   {'✅ PASS' if nums == expected else '❌ FAIL'}")
        print()
    
    # Demonstrate the step-by-step process
    print("\nStep-by-Step Demonstration:")
    print("=" * 60)
    nums_demo = [1,2,3,4,5,6,7]
    demonstrate_rotation_steps(nums_demo, 3)
    
    # Test all methods give same result
    print("\nMethod Comparison:")
    print("=" * 60)
    
    test_nums = [1,2,3,4,5,6,7]
    k = 3
    
    # Test each method
    nums1 = test_nums[:]
    rotate_with_extra_space(nums1, k)
    
    nums2 = test_nums[:]
    rotate_cyclic_replacement(nums2, k)
    
    nums3 = test_nums[:]
    rotate_reverse_method(nums3, k)
    
    nums4 = test_nums[:]
    rotate(nums4, k)
    
    print(f"Original:           {test_nums}")
    print(f"Extra Space:        {nums1}")
    print(f"Cyclic Replacement: {nums2}")
    print(f"Reverse Method:     {nums3}")
    print(f"Main Solution:      {nums4}")
    print(f"All methods match:  {nums1 == nums2 == nums3 == nums4}")
    
    # Performance test
    print("\nPerformance Test:")
    print("=" * 60)
    
    import time
    
    # Large array test
    large_nums = list(range(100000))
    k = 50000
    
    # Test reverse method (optimal)
    test_array = large_nums[:]
    start = time.time()
    rotate_reverse_method(test_array, k)
    reverse_time = time.time() - start
    
    # Test extra space method
    test_array = large_nums[:]
    start = time.time()
    rotate_with_extra_space(test_array, k)
    extra_space_time = time.time() - start
    
    print(f"Array size: {len(large_nums):,} elements")
    print(f"Reverse method: {reverse_time:.4f} seconds")
    print(f"Extra space method: {extra_space_time:.4f} seconds")
    print(f"Memory efficiency: Reverse method uses O(1) space")
    print(f"Time difference: {abs(reverse_time - extra_space_time):.4f} seconds")
