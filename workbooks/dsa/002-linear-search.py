def linear_search_variations():
    """
    Implement different types of linear search:
    1. Find first occurrence index
    2. Find all occurrence indices
    3. Find if element exists
    4. Find element closest to target
    """
    
    def find_first(arr, target):
        try:
            return arr.index(target)
        except:
            return -1
        pass
    
    def find_all(arr, target):
        return [i for i, x in enumerate(arr) if target == x]
        pass
    
    def exists(arr, target):
        return target in arr
    
    def find_closest(arr, target):
        return min(arr, key=lambda x: abs(target-x))
        pass
    
    # Test cases
    test_arr = [1, 5, 3, 5, 7, 5, 9]
    print(f"First 5 at: {find_first(test_arr, 5)}")  # Should be 1
    print(f"All 5s at: {find_all(test_arr, 5)}")  # Should be [1, 3, 5]
    print(f"Exists 7: {exists(test_arr, 7)}")  # Should be True
    print(f"Closest to 6: {find_closest(test_arr, 6)}")  # Should be 5 or 7

# Uncomment to test
linear_search_variations()