def linear_search_variations():
    """
    Implement different types of linear search:
    1. Find first occurrence index
    2. Find all occurrence indices
    3. Find if element exists
    4. Find element closest to target
    """
    
    def find_first(arr, target):
        # TODO: Return index of first occurrence, -1 if not found
        pass
    
    def find_all(arr, target):
        # TODO: Return list of all indices where target appears
        pass
    
    def exists(arr, target):
        # TODO: Return True if target exists, False otherwise
        pass
    
    def find_closest(arr, target):
        # TODO: Return element closest to target value
        pass
    
    # Test cases
    test_arr = [1, 5, 3, 5, 7, 5, 9]
    print(f"First 5 at: {find_first(test_arr, 5)}")  # Should be 1
    print(f"All 5s at: {find_all(test_arr, 5)}")  # Should be [1, 3, 5]
    print(f"Exists 7: {exists(test_arr, 7)}")  # Should be True
    print(f"Closest to 6: {find_closest(test_arr, 6)}")  # Should be 5 or 7

# Uncomment to test
# linear_search_variations()