# Day 1: Two Sum Problem 🎯

**Topic**: Array Basics  
**Difficulty**: Easy  
**Time to Complete**: 45-60 minutes

## 📋 Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target. You can assume that each input has exactly one solution, and you cannot use the same element twice.

### Examples

**Example 1:**
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

**Example 2:**
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6
```

**Example 3:**
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: nums[0] + nums[1] = 3 + 3 = 6
```

## 📥 Input/Output Format

**Input:**
- `nums`: List of integers (1 ≤ nums.length ≤ 10⁴)
- `target`: Integer target sum

**Output:**
- List of two integers representing the indices

## 🔍 Constraints and Edge Cases

### Constraints:
- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists

### Edge Cases:
1. **Minimum array size**: `[1, 2]` with target `3`
2. **Negative numbers**: `[-1, -2, -3, -4]` with target `-6`
3. **Same elements**: `[3, 3]` with target `6`
4. **Large numbers**: Very large positive/negative integers
5. **Zero values**: `[0, 4, 3, 0]` with target `0`

## 💡 Solution Approach

### Method 1: Brute Force (Naive)
Check every pair of numbers to see if they sum to the target.

**Algorithm:**
1. Use nested loops to check all pairs
2. For each pair (i, j) where i < j, check if nums[i] + nums[j] == target
3. Return [i, j] when found

**Time Complexity**: O(n²)  
**Space Complexity**: O(1)

### Method 2: Hash Map (Optimal) ⭐
Use a hash map to store seen numbers and their indices.

**Algorithm:**
1. Create an empty hash map
2. For each number, calculate its complement (target - current number)
3. Check if complement exists in hash map
4. If yes, return indices; if no, store current number and index

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

## 🔧 Step-by-Step Solution Walkthrough

Let's trace through Example 1: `nums = [2, 7, 11, 15]`, `target = 9`

### Hash Map Approach:
```
Iteration 1: num = 2, index = 0
- complement = 9 - 2 = 7
- hash_map = {} (empty)
- 7 not in hash_map
- Store: hash_map = {2: 0}

Iteration 2: num = 7, index = 1
- complement = 9 - 7 = 2
- hash_map = {2: 0}
- 2 in hash_map! Found at index 0
- Return [0, 1]
```

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|----------------|------------------|------|------|
| Brute Force | O(n²) | O(1) | Simple, no extra space | Slow for large arrays |
| Hash Map | O(n) | O(n) | Fast, single pass | Uses extra memory |

## 🎨 Visual Representation

```
Array: [2, 7, 11, 15]  Target: 9
Index:  0  1   2   3

Hash Map Approach:
Step 1: Check 2 → Need 7 → Store {2: 0}
Step 2: Check 7 → Need 2 → Found! Return [0, 1]

    [2, 7, 11, 15]
     ↑  ↑
     0  1  ← These indices sum to target!
```

## 🚀 Optimization Tips

1. **Early Return**: Return immediately when solution is found
2. **Input Validation**: Check for valid input (array length ≥ 2)
3. **Memory vs Speed**: Choose hash map for speed, brute force for memory constraints
4. **Hash Collisions**: Python dictionaries handle this automatically

## 🔗 Related Problems

- **Three Sum**: Find three numbers that sum to target
- **Four Sum**: Find four numbers that sum to target
- **Two Sum II - Input Array Is Sorted**: Optimized for sorted arrays
- **Two Sum Less Than K**: Find pairs with sum less than K

## 💭 Follow-up Questions

1. What if the array is sorted? Can we optimize further?
2. What if we need to find all pairs that sum to target?
3. How would you handle duplicate elements?
4. What if we need to minimize space complexity?

## 🎯 Practice Challenges

### Challenge 1: Modify for Three Sum
Extend the solution to find three numbers that sum to the target.

### Challenge 2: Return All Pairs
Modify to return all possible pairs (handling duplicates).

### Challenge 3: Closest Sum
Find the pair whose sum is closest to the target.

## 📚 Key Takeaways

1. **Hash maps are powerful** for O(1) lookup operations
2. **Trade-offs exist** between time and space complexity
3. **Edge cases matter** - always consider boundary conditions
4. **Problem patterns** like "Two Sum" appear frequently in variations

---

**Next**: Proceed to [Day 2: Array Rotation](../day_02/) to learn about in-place array operations! 

**Previous**: Return to [Course Schedule](../course_schedule.md) for overview.

---
*💡 Remember: The key to mastering DSA is understanding the underlying patterns. Two Sum introduces the powerful "complement search" pattern used in many array problems!*
