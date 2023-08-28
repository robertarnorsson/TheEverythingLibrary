import random

class TELSorting():
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def bubble_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        WIP! Coming soon
        '''
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    def selection_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        WIP! Coming soon
        '''
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    def insertion_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        WIP! Coming soon
        '''
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def quick_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        WIP! Coming soon
        '''
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def merge_sort(self, arr: list[int | float]) -> list[int | float]:
        '''
        WIP! Coming soon
        '''
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
    
    def bogo_sort(self, arr: list[int | float]) -> list[int | float]:
        while not arr == sorted(arr):
            random.shuffle(arr)
        return arr

class TELSearching():
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def linear_search(self, arr: list[int | float], target: int | float):
        '''
        WIP! Coming soon
        '''
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def binary_search(self, arr: list[int | float], target: int | float):
        '''
        WIP! Coming soon
        '''
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
    
    def search(self, arr: list, target, comparison_func=None):
        '''
        WIP! Coming soon
        '''
        if comparison_func is None:
            comparison_func = lambda x, y: x == y

        for index, item in enumerate(arr):
            if comparison_func(item, target):
                return index
        return -1
