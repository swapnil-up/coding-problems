def solve_basic_array_ops():
    """
    Given an array, implement basic operations:
    1. Access element at index i (with bounds checking)
    2. Find the sum of all elements
    3. Find the maximum element
    4. Count occurrences of a specific value
    """
    
    def safe_access(arr, index):
        try:
            return arr[index]  
        except IndexError:
            return None
    
    def array_sum(arr):
        return sum(arr) if arr else None
    
    def find_max(arr):
        return max(arr) if arr else None
    
    def count_occurrences(arr, target):
        return arr.count(target)
    
    # Test cases
    test_arr = [1, 3, 5, 3, 7, 3]
    print(f"Access index 2: {safe_access(test_arr, 2)}")  # Should be 5
    print(f"Access index 10: {safe_access(test_arr, 10)}")  # Should be None
    print(f"Sum: {array_sum(test_arr)}")  # Should be 22
    print(f"Max: {find_max(test_arr)}")  # Should be 7
    print(f"Count of 3: {count_occurrences(test_arr, 3)}")  # Should be 3

# Uncomment to test
solve_basic_array_ops()