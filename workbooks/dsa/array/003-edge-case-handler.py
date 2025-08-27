def handle_edge_cases():
    """
    Write functions that gracefully handle all corner cases:
    1. Empty arrays
    2. Single element arrays
    3. All elements the same
    4. Two element arrays
    """
    
    def robust_max(arr):
        try:
            return max(arr)
        except:
            return None
    
    def robust_second_largest(arr):
        if len(arr)<2:
            return None
        unique_arr = sorted(list(set(arr)), reverse = True)
        if len(unique_arr)<2:
            return None
        return unique_arr[1]
    
    def robust_remove_duplicates(arr):
        # TODO: Remove duplicates while preserving order, handle all edge cases
        return list(dict.fromkeys(arr))
        pass
    
    def robust_reverse_pairs(arr):
        # TODO: Return pairs (arr[i], arr[j]) where i < j, handle small arrays
        pairs = []
        n = len(arr)

        if n < 2:
            return pairs

        for i in range(n):
            for j in range(i + 1, n):  # Start j from i + 1 to ensure i < j
                pairs.append((arr[i], arr[j]))
        return pairs
        pass
    
    # Test all edge cases
    test_cases = [
        [],                    # Empty
        [5],                   # Single element
        [3, 3, 3],            # All same
        [1, 2],               # Two elements
        [5, 1, 5, 3, 1, 5]    # Normal case
    ]
    
    for i, arr in enumerate(test_cases):
        print(f"\nTest case {i+1}: {arr}")
        print(f"Max: {robust_max(arr)}")
        print(f"Second largest: {robust_second_largest(arr)}")
        print(f"Remove duplicates: {robust_remove_duplicates(arr)}")
        print(f"Pairs: {robust_reverse_pairs(arr)}")

# Uncomment to test
handle_edge_cases()