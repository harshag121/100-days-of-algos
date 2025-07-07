# Day 3: Reverse String 📝

**Topic**: String Basics  
**Difficulty**: Easy  
**Time to Complete**: 45-60 minutes

## 📋 Problem Description

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

### Examples

**Example 1:**
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Example 3:**
```
Input: s = ["A"]
Output: ["A"]
```

**Example 4:**
```
Input: s = []
Output: []
```

## 📥 Input/Output Format

**Input:**
- `s`: List of characters (0 ≤ s.length ≤ 10⁵)

**Output:**
- Modify `s` in-place (no return value needed)

## 🔍 Constraints and Edge Cases

### Constraints:
- 0 ≤ s.length ≤ 10⁵
- s[i] is a printable ASCII character

### Edge Cases:
1. **Empty string**: `[]`
2. **Single character**: `["A"]`
3. **Two characters**: `["A", "B"]`
4. **Palindrome**: `["a", "b", "a"]`
5. **All same characters**: `["a", "a", "a"]`
6. **Mixed case**: `["A", "b", "C"]`
7. **Special characters**: `["!", "@", "#"]`

## 💡 Solution Approaches

### Method 1: Two Pointers (Optimal) ⭐
Use two pointers from opposite ends, swapping characters.

**Algorithm:**
1. Initialize left pointer at start, right pointer at end
2. While left < right:
   - Swap characters at left and right positions
   - Move left forward, right backward
3. Continue until pointers meet

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

### Method 2: Stack Approach
Use a stack to reverse the order (educational, not optimal for this problem).

**Algorithm:**
1. Push all characters onto a stack
2. Pop characters back into the array

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

### Method 3: Recursion
Recursively swap characters from outside in.

**Algorithm:**
1. Base case: if left >= right, return
2. Swap characters at left and right
3. Recursively call for inner substring

**Time Complexity**: O(n)  
**Space Complexity**: O(n) due to recursion stack

## 🔧 Step-by-Step Solution Walkthrough

Let's trace through Example 1: `s = ["h","e","l","l","o"]`

### Two Pointers Approach:
```
Initial: ["h","e","l","l","o"]
         ↑               ↑
       left=0          right=4

Step 1: Swap s[0] and s[4]
        ["o","e","l","l","h"]
             ↑       ↑
           left=1  right=3

Step 2: Swap s[1] and s[3]
        ["o","l","l","e","h"]
                 ↑
            left=2=right=2

Step 3: left >= right, so stop
Final:  ["o","l","l","e","h"]
```

## 📊 Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Two Pointers | O(n) | O(1) | Optimal, in-place | None |
| Stack | O(n) | O(n) | Educational | Uses extra memory |
| Recursion | O(n) | O(n) | Elegant | Call stack overhead |

## 🎨 Visual Representation

```
Two Pointers Technique:
["h", "e", "l", "l", "o"]
  ↑                   ↑     Step 1: Swap
 left               right

["o", "e", "l", "l", "h"]
      ↑           ↑         Step 2: Move inward & swap
    left        right

["o", "l", "l", "e", "h"]
          ↑                 Step 3: Pointers meet, done!
      left=right

Think of it as:
- Two people walking toward each other
- They swap items as they pass
- When they meet in the middle, they're done
```

## 🚀 Optimization Tips

1. **Early termination**: If length ≤ 1, no reversal needed
2. **Pointer arithmetic**: Use `left` and `right = len(s) - 1 - left`
3. **XOR swap**: For integers, can use XOR to swap without temp variable
4. **String vs List**: Remember Python strings are immutable

## 🔗 Related Problems

- **Reverse Words in String**: Reverse word order, not characters
- **Valid Palindrome**: Check if string reads same forwards/backwards
- **Reverse String II**: Reverse every 2k characters
- **Reverse Words in String III**: Reverse each word individually

## 💭 Follow-up Questions

1. How would you reverse only alphabetic characters?
2. What if you need to reverse words instead of characters?
3. How to reverse a string recursively?
4. Can you reverse without using extra variables?

## 🎯 Practice Challenges

### Challenge 1: Reverse Only Letters
Reverse only alphabetic characters, keeping others in place.
```
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

### Challenge 2: Reverse Words
Reverse the order of words in a sentence.
```
Input: "the sky is blue"
Output: "blue is sky the"
```

### Challenge 3: Palindrome Check
Check if a string is a palindrome using the two-pointer technique.

## 📚 Key Takeaways

1. **Two pointers** is a fundamental technique for array/string problems
2. **In-place algorithms** save memory and are often preferred
3. **String manipulation** often involves character-by-character operations
4. **Edge cases** like empty or single-character strings are important

## 🧠 Pattern Recognition

The two-pointer technique used here appears in many problems:
- Checking palindromes
- Finding pairs that sum to a target
- Removing duplicates from sorted arrays
- Merging sorted arrays

---

**Next**: Proceed to [Day 4: Valid Palindrome](../day_04/) to learn two-pointer techniques!

**Previous**: Return to [Day 2: Array Rotation](../day_02/) or [Course Schedule](../course_schedule.md).

---
*💡 Master Pattern: Two pointers moving toward each other is one of the most elegant and efficient patterns in programming. You'll use this technique throughout your DSA journey!*
