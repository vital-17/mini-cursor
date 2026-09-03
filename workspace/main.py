def calculate_sum(start: int, end: int) -> int:
    """
    Calculate the sum of integers from start to end (inclusive).
    
    Args:
        start: The starting integer (inclusive)
        end: The ending integer (inclusive)
    
    Returns:
        The sum of all integers in the range [start, end]
    
    Raises:
        ValueError: If start > end or if inputs are not integers
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError("start must be less than or equal to end")
    
    return sum(range(start, end + 1))


if __name__ == "__main__":
    # Compute sum from 1 to 100
    result = calculate_sum(1, 100)
    
    # Verify against Gauss formula: n*(n+1)//2 where n = 100
    expected = 100 * 101 // 2
    
    # Assert correctness
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Output the result
    print(f"Sum from 1 to 100 = {result}")