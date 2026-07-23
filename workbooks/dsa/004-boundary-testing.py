def boundary_testing():
    """
    Practice careful index management:
    1. Safe subarray extraction
    2. Circular array access
    3. Window operations with bounds checking
    """
    
    def safe_subarray(arr, start, end):
        # TODO: Extract subarray from start to end (exclusive), handle invalid ranges
        pass
    
    def circular_access(arr, index):
        # TODO: Access array as if it were circular (index can be any integer)
        pass
    
    def sliding_window_sum(arr, k):
        # TODO: Return list of sums of all windows of size k
        pass
    
    def expand_around_center(arr, center):
        # TODO: Return the longest subarray centered at index 'center' 
        # where all elements are the same
        pass
    
    # Test cases
    test_arr = [1, 2, 3, 4, 5, 6]
    print(f"Subarray [1:4]: {safe_subarray(test_arr, 1, 4)}")  # [2, 3, 4]
    print(f"Subarray [10:20]: {safe_subarray(test_arr, 10, 20)}")  # []
    print(f"Circular access -1: {circular_access(test_arr, -1)}")  # 6
    print(f"Circular access 7: {circular_access(test_arr, 7)}")  # 2
    print(f"Window sums k=3: {sliding_window_sum(test_arr, 3)}")  # [6, 9, 12, 15]
    test_arr2 = [1, 1, 1, 2, 2, 2]
    print(f"Expand center=1: {expand_around_center(test_arr, 1)}")  

# Uncomment to test
boundary_testing()
