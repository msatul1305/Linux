- Practice SQL query questions
  - indexing also
- Design Patterns
- Implement a Python function that finds the shortest path between two nodes in a weighted directed graph using Dijkstra's algorithm.
- Problem: Implement a Python function that checks if a given number is a power of two (e.g., 1, 2, 4, 8, 16, ...). using binary digits
  - def is_power_of_two(n):
    # Check if n is positive and has only one '1' bit in its binary representation
    return n > 0 and (n & (n - 1)) == 0

    # Test the function
    numbers_to_test = [1, 2, 4, 8, 16, 3, 5, 6, 7, 9]
    
    for num in numbers_to_test:
    if is_power_of_two(num):
    print(f"{num} is a power of two.")
    else:
    print(f"{num} is not a power of two.")
- 