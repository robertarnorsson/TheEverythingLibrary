import random

class TELSorting:
    '''
    ## Sorting
    ---
    This class provides utility functions for searching lists.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self) -> None:
        pass

    @staticmethod
    def bubble_sort(arr: list[int | float]) -> list[int | float]:
        '''
        ## Bubble Sort
        ---
        ### Description
        Sorts a list using the bubble sort algorithm. Use only for fun!\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to be sorted.\n
        ---
        ### Return
            - The sorted list.\n
        ---
        ### Exceptions
            - If an error occurs during sorting.\n
        '''
        try:
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    @staticmethod
    def selection_sort(arr: list[int | float]) -> list[int | float]:
        '''
        ## Selection Sort
        ---
        ### Description
        Sorts a list using the selection sort algorithm.\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to be sorted.\n
        ---
        ### Return
            - The sorted list.\n
        ---
        ### Exceptions
            - If an error occurs during sorting.\n
        '''
        try:
            n = len(arr)
            for i in range(n):
                min_index = i
                for j in range(i+1, n):
                    if arr[j] < arr[min_index]:
                        min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]
            return arr
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    @staticmethod
    def insertion_sort(arr: list[int | float]) -> list[int | float]:
        '''
        ## Insertion Sort
        ---
        ### Description
        Sorts a list using the insertion sort algorithm.\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to be sorted.\n
        ---
        ### Return
            - The sorted list.\n
        ---
        ### Exceptions
            - If an error occurs during sorting.\n
        '''
        try:
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return arr
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def quick_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        ## Quick Sort
        ---
        ### Description
        Sorts a list using the quick sort algorithm.\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to be sorted.\n
        ---
        ### Return
            - The sorted list.\n
        ---
        ### Exceptions
            - If an error occurs during sorting.\n
        '''
        try:
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return self.quick_sort(left) + middle + self.quick_sort(right)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def merge_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        ## Merge Sort
        ---
        ### Description
        Sorts a list using the merge sort algorithm.\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to be sorted.\n
        ---
        ### Return
            - The sorted list.\n
        ---
        ### Exceptions
            - If an error occurs during sorting.\n
        '''
        try:
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                self.merge_sort(left_half)
                self.merge_sort(right_half)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1
                return arr
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def bogo_sort(arr: list[int | float]) -> list[int | float]:
        '''
        ## Bogo Sort
        ---
        ### Description
        Sorts a list using the bogo sort algorithm.\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to be sorted.\n
        ---
        ### Return
            - The sorted list.\n
        ---
        ### Exceptions
            - If an error occurs during sorting.\n
        '''
        try:
            while not arr == sorted(arr):
                random.shuffle(arr)
            return arr
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

class TELSearching:
    '''
    ## Search
    ---
    This class provides utility functions for searching lists.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self) -> None:
        pass

    @staticmethod
    def linear_search(arr: list[int | float], target: int | float):
        '''
        ## Linear Search
        ---
        ### Description
        Searches for a target element in a list using linear search algorithm.\n
        ---
        ### Arguments
            - `arr`: The list of integers or floats to search.
            - `target`: The element to search for.\n
        ---
        ### Return
            - The index of the target element if found, otherwise -1.\n
        ---
        ### Exceptions
            - If an error occurs during searching.\n
        '''
        try:
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
            return -1
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    @staticmethod
    def binary_search(arr: list[int | float], target: int | float):
        '''
        ## Binary Search
        ---
        ### Description
        Searches for a target element in a sorted list using binary search algorithm.\n
        ---
        ### Arguments
            - `arr`: The sorted list of integers or floats to search.
            - `target`: The element to search for.\n
        ---
        ### Return
            - The index of the target element if found, otherwise -1.\n
        ---
        ### Exceptions
            - If an error occurs during searching.\n
        '''
        try:
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    @staticmethod
    def search(arr: list, target, comparison_func=None):
        '''
        ## Generic Search
        ---
        ### Description
        Searches for a target element in a list using a custom comparison function.\n
        ---
        ### Arguments
            - `arr`: The list to search.
            - `target`: The element to search for.
            - `comparison_func`: A custom function to compare elements. Default is equality comparison.\n
        ---
        ### Return
            - The index of the target element if found, otherwise -1.\n
        ---
        ### Exceptions
            - If an error occurs during searching.\n
        '''
        try:
            if comparison_func is None:
                comparison_func = lambda x, y: x == y

            for index, item in enumerate(arr):
                if comparison_func(item, target):
                    return index
            return -1
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
