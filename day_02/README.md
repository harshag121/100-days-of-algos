# Day 2: Array Rotation 🔄

**Topic**: Array Manipulation  
**Difficulty**: Medium  
**Time to Complete**: 60-75 minutes

## 📋 Problem Description

Given an array of integers and a number `k`, rotate the array to the right by `k` steps. Modify the array in-place with O(1) extra memory.

### Examples

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation: 
rotate 1 step to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 step to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

**Example 3:**
```
Input: nums = [1], k = 1
Output: [1]
```

## 📥 Input/Output Format

**Input:**
- `nums`: List of integers (1 ≤ nums.length ≤ 10⁵)
- `k`: Non-negative integer (0 ≤ k ≤ 10⁵)

**Output:**
- Modify `nums` in-place (no return value needed)

## 🔍 Constraints and Edge Cases

### Constraints:
- 1 ≤ nums.length ≤ 10⁵
- -2³¹ ≤ nums[i] ≤ 2³¹ - 1
- 0 ≤ k ≤ 10⁵

### Edge Cases:
1. **Single element**: `[1]` with any k
2. **k = 0**: No rotation needed
3. **k > length**: `k = 10` with array length 3 (use k % length)
4. **k = length**: Full rotation (same as original)
5. **Empty array**: Not possible per constraints
6. **Negative numbers**: Mixed positive/negative values

## 💡 Solution Approaches

### Method 1: Extra Array (Naive)
Create a new array and place elements in rotated positions.

**Algorithm:**
1. Create new array of same size
2. Place each element at position (i + k) % n
3. Copy back to original array

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

### Method 2: Cyclic Replacements
Move elements one by one to their final positions.

**Algorithm:**
1. Calculate how many cycles we need
2. For each cycle, move elements to their correct positions
3. Handle the case where gcd(n, k) > 1

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

### Method 3: Reverse Method (Optimal) ⭐
Use three reversal operations to achieve rotation.

**Algorithm:**
1. Reverse the entire array
2. Reverse the first k elements
3. Reverse the remaining n-k elements

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

## 🔧 Step-by-Step Solution Walkthrough

Let's trace through Example 1: `nums = [1,2,3,4,5,6,7]`, `k = 3`

### Reverse Method:
```
Original: [1,2,3,4,5,6,7]
Step 1: Reverse entire array
        [7,6,5,4,3,2,1]

Step 2: Reverse first k=3 elements
        [5,6,7,4,3,2,1]

Step 3: Reverse remaining 4 elements
        [5,6,7,1,2,3,4]
```

**Why this works:**
- After full reversal: last k elements are at the beginning (but reversed)
- First reversal of k elements: puts them in correct order
- Second reversal: puts remaining elements in correct order

## 📊 Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Extra Array | O(n) | O(n) | Simple to understand | Uses extra memory |
| Cyclic | O(n) | O(1) | In-place, optimal | Complex implementation |
| Reverse | O(n) | O(1) | In-place, elegant | Requires insight |

## 🎨 Visual Representation

```
Array Rotation by k=3:
[1,2,3,4,5,6,7] → [5,6,7,1,2,3,4]

Think of it as:
- Take last 3 elements: [5,6,7]
- Move them to front: [5,6,7,_,_,_,_]
- Fill rest with remaining: [5,6,7,1,2,3,4]

Reverse Method Visualization:
Original:     [1,2,3,4,5,6,7]
Reverse All:  [7,6,5,4,3,2,1]
              ↑ ↑ ↑ ↑ ↑ ↑ ↑
Reverse k=3:  [5,6,7,4,3,2,1]
              ✓ ✓ ✓ ↑ ↑ ↑ ↑
Reverse rest: [5,6,7,1,2,3,4]
              ✓ ✓ ✓ ✓ ✓ ✓ ✓
```

## 🚀 Optimization Tips

1. **Handle k > n**: Use `k = k % n` to avoid unnecessary rotations
2. **Early return**: If `k == 0` or `n == 1`, no rotation needed
3. **Choose method**: Use reverse method for best space complexity
4. **Validate input**: Check for valid k and non-empty array

## 🔗 Related Problems

- **Rotate String**: Check if one string is rotation of another
- **Reverse Words in String**: Similar reversal technique
- **Circular Array Loop**: Detect loops in rotated arrays
- **Search in Rotated Sorted Array**: Binary search in rotated arrays

## 💭 Follow-up Questions

1. How would you rotate left instead of right?
2. What if you need to rotate a 2D matrix?
3. How to find the minimum number of rotations needed?
4. Can you rotate only a subarray?

## 🎯 Practice Challenges

### Challenge 1: Rotate Left
Modify the solution to rotate left by k positions.

### Challenge 2: Find Rotation Count
Given a rotated sorted array, find how many times it was rotated.

### Challenge 3: 2D Matrix Rotation
Rotate a 2D matrix 90 degrees clockwise.

## 📚 Key Takeaways

1. **Modular arithmetic** is crucial for cyclic operations
2. **Reversal technique** is a powerful pattern for array manipulation
3. **In-place algorithms** save memory but require more thought
4. **Edge cases** like k > n must be handled properly

---

**Next**: Proceed to [Day 3: String Basics](../day_03/) to explore string manipulation!

**Previous**: Return to [Day 1: Two Sum](../day_01/) or [Course Schedule](../course_schedule.md).

---
*💡 Key Pattern: The "reverse" technique appears in many array manipulation problems. Master this pattern as it's both elegant and efficient!*
