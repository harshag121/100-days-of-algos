"""
Day 65: Number of Islands
Topic: DFS in Graphs
Difficulty: Medium

Problem: Implement solution for Number of Islands using Depth-first search.

Author: 100 Days DSA Course
Date: Day 65
"""

def solution_brute_force(data):
    """
    Brute force approach for Number of Islands.
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    
    Args:
        data: Input data for the problem
        
    Returns:
        Result based on problem requirements
        
    Example:
        >>> solution_brute_force([example_input])
        [expected_output]
    """
    # TODO: Implement brute force solution
    # This should be the most straightforward approach
    pass


def solution_optimized(data):
    """
    Optimized approach using Depth-first search.
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    
    This is the preferred implementation demonstrating Depth-first search.
    """
    # TODO: Implement optimized solution
    # This should use the key concepts for this day
    pass


def main_solution(data):
    """
    Main solution function for Number of Islands.
    
    This implements the optimal approach using Depth-first search.
    
    Args:
        data: Input data for the problem
        
    Returns:
        Solution result
        
    Example:
        >>> main_solution([example_input])
        [expected_output]
    """
    # Input validation
    if not data:
        return []  # or appropriate default
    
    # TODO: Implement main solution logic
    # Use the concepts: Depth-first search
    pass


def demonstrate_solution(data):
    """
    Educational function showing step-by-step solution process.
    """
    print(f"Solving Number of Islands with input: {data}")
    print("Key concepts: Depth-first search")
    print("Steps:")
    
    # TODO: Add step-by-step demonstration
    print("1. [Step description]")
    print("2. [Step description]")
    print("3. [Step description]")
    
    result = main_solution(data)
    print(f"Final result: {result}")
    return result


if __name__ == "__main__":
    # Test cases for Number of Islands
    test_cases = [
        # (input_data, expected_result, description)
        ([1, 2, 3], [1, 2, 3], "Basic case"),
        ([], [], "Empty input"),
        ([1], [1], "Single element"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Larger input"),
    ]
    
    print("Testing Number of Islands Solutions...")
    print("=" * 60)
    
    for i, (input_data, expected, description) in enumerate(test_cases, 1):
        result = main_solution(input_data)
        
        print(f"Test Case {i}: {description}")
        print(f"  Input: {input_data}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {'✅ PASS' if result == expected else '❌ FAIL'}")
        print()
    
    # Demonstrate the solution
    print("\nStep-by-Step Demonstration:")
    print("=" * 60)
    demonstrate_solution([1, 2, 3, 4, 5])
    
    print("\n🎯 Key Concept: Depth-first search")
    print("💡 Remember: Understanding the pattern is more important than memorizing!")