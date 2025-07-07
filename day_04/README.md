# Day 4: Valid Palindrome 🔄

**Topic**: Two Pointers  
**Difficulty**: Easy  
**Time to Complete**: 45-60 minutes

## 📋 Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## 📥 Input/Output Format

**Input:**
- `s`: String (1 ≤ s.length ≤ 2 × 10⁵)

**Output:**
- Boolean: `true` if palindrome, `false` otherwise

## 🔍 Constraints and Edge Cases

### Constraints:
- 1 ≤ s.length ≤ 2 × 10⁵
- s consists only of printable ASCII characters

### Edge Cases:
1. **Empty after cleaning**: `".,"`
2. **Single character**: `"a"`
3. **All non-alphanumeric**: `"!@#$%"`
4. **Mixed case**: `"Aa"`
5. **Numbers included**: `"A1B2b1a"`
6. **Spaces only**: `"   "`

## 💡 Solution Approaches

### Method 1: Create Clean String (Naive)
Clean the string first, then check if it equals its reverse.

**Algorithm:**
1. Remove non-alphanumeric characters and convert to lowercase
2. Compare string with its reverse

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

### Method 2: Two Pointers (Optimal) ⭐
Use two pointers without creating a new string.

**Algorithm:**
1. Initialize left and right pointers
2. Skip non-alphanumeric characters
3. Compare characters at valid positions
4. Move pointers inward

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

## 🔧 Step-by-Step Solution Walkthrough

Let's trace through Example 1: `s = "A man, a plan, a canal: Panama"`

### Two Pointers Approach:
```
Original: "A man, a plan, a canal: Panama"
Clean conceptually: "amanaplanacanalpanama"

left=0, right=31 (last char)
1. s[0]='A' -> 'a', s[31]='a' -> 'a' ✓ Match
2. Skip non-alphanumeric until s[2]='m', s[29]='m' ✓ Match
3. Continue pattern...
4. Pointers meet in middle -> palindrome confirmed
```

## 📊 Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Clean String | O(n) | O(n) | Simple logic | Extra memory |
| Two Pointers | O(n) | O(1) | Optimal space | Slightly complex |

## 🎨 Visual Representation

```
Two Pointers on "A man, a plan, a canal: Panama":

A   m a n ,   a   p l a n ,   a   c a n a l :   P a n a m a
↑                                                         ↑
left                                                    right

Skip non-alphanumeric, compare 'A'↔'a' (case-insensitive)
Move inward, continue until pointers meet or mismatch found.
```

## 🚀 Optimization Tips

1. **Character validation**: Use `isalnum()` for checking
2. **Case conversion**: Use `lower()` for comparison
3. **Early termination**: Return false immediately on mismatch
4. **Skip efficiently**: Increment pointers in one operation

## 🔗 Related Problems

- **Palindrome Number**: Check if integer is palindrome
- **Longest Palindromic Substring**: Find longest palindromic substring
- **Palindrome Linked List**: Check if linked list is palindrome
- **Valid Palindrome II**: Allow one character deletion

## 💭 Follow-up Questions

1. What if we allow one character to be different?
2. How to find the longest palindromic substring?
3. What about checking palindromes in other languages?
4. How to handle Unicode characters?

## 🎯 Practice Challenges

### Challenge 1: Palindrome Number
Check if an integer is a palindrome without converting to string.

### Challenge 2: Case-Sensitive Palindrome
Check palindrome considering case and all characters.

### Challenge 3: Longest Palindrome
Find the longest palindromic substring in a string.

## 📚 Key Takeaways

1. **Two pointers** technique is perfect for palindrome problems
2. **Character filtering** can be done on-the-fly
3. **Space optimization** often possible with clever pointer usage
4. **String processing** frequently involves character validation

---

**Next**: Proceed to [Day 5: Sliding Window](../day_05/) to learn sliding window patterns!

**Previous**: Return to [Day 3: Reverse String](../day_03/) or [Course Schedule](../course_schedule.md).

---
*💡 Key Pattern: Two pointers with character filtering - a powerful combination for string validation problems!*
