def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    # Example usage
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    sorted_list = bubble_sort(sample_list.copy())
    print("Sorted list:", sorted_list)


class inheritance:
    """
    A simple class to demonstrate inheritance.
    """
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"