class TELMath:
    '''
    ## Math
    ---
    This class provides utility functions for math.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self) -> None:
        pass

    def add(self, x: int | float | str, y: int | float | str) -> float:
        '''
        ## Addition
        ---
        ### Description
        Adds two numbers.\n
        ---
        ### Arguments
            - `x`: The first number.
            - `y`: The second number.\n
        ---
        ### Return
            - The sum of the two numbers.\n
        ---
        ### Exceptions
            - If an error occurs during addition.\n
        '''
        try:
            return float(x + y)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def add_list(self, arr: list[int | float | str]) -> float:
        '''
        ## Addition of List
        ---
        ### Description
        Adds all the numbers in a list.\n
        ---
        ### Arguments
            - `arr`: The list of numbers.\n
        ---
        ### Return
            - The sum of the numbers in the list.\n
        ---
        ### Exceptions
            - If an error occurs during addition.\n
        '''
        try:
            result = 0.0
            clean_numbers = []
            for num in arr:
                if type(num) == str:
                    clean_numbers.append(''.join(char for char in num if char.isdigit()))
                else:
                    clean_numbers.append(num)
            if type(clean_numbers) == list:
                for num in clean_numbers:
                    result += float(num)
                return float(result)
            else:
                return float(result)
        except ValueError as e:
            print(f"{num} is a {type(num)} which is not able to be added!\n{e}")
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def subtract(self, x: int | float | str, y: int | float | str) -> float:
        '''
        ## Subtraction
        ---
        ### Description
        Subtracts one number from another.\n
        ---
        ### Arguments
            - `x`: The first number.
            - `y`: The second number.\n
        ---
        ### Return
            - The result of subtracting `y` from `x`.\n
        ---
        ### Exceptions
            - If an error occurs during subtraction.\n
        '''
        try:
            return float(x - y)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def subtract_list(self, arr_x: list[int | float | str], arr_y: list[int | float | str]) -> float:
        '''
        ## Subtraction of Lists
        ---
        ### Description
        Subtracts the sum of one list from the sum of another list.\n
        ---
        ### Arguments
            - `arr_x`: The first list of numbers.
            - `arr_y`: The second list of numbers.\n
        ---
        ### Return
            - The result of subtracting the sum of `arr_y` from the sum of `arr_x`.\n
        ---
        ### Exceptions
            - If an error occurs during subtraction.\n
        '''
        try:
            x = self.add_list(arr=arr_x)
            y = self.add_list(arr=arr_y)

            return float(x - y)
        except ValueError as e:
            print(f"{x} or {y} is a {type(x)} or {type(y)} which is not able to be subtracted!\n{e}")
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def average(self, arr: list[int | float | str]) -> float:
        '''
        ## Average
        ---
        ### Description
        Calculates the average of numbers in a list.\n
        ---
        ### Arguments
            - `arr`: The list of numbers.\n
        ---
        ### Return
            - The average of the numbers in the list.\n
        ---
        ### Exceptions
            - If an error occurs during calculation.\n
        '''
        try:
            length = len(arr)
            _sum = self.add_list(arr=arr)
            return float(_sum / length)
        except ValueError as e:
            print(f"{_sum} is not able to be averaged!\n{e}")
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def median(self, arr: list[int | float | str]) -> float:
        '''
        ## Median
        ---
        ### Description
        Calculates the median of numbers in a list.\n
        ---
        ### Arguments
            - `arr`: The list of numbers.\n
        ---
        ### Return
            - The median of the numbers in the list.\n
        ---
        ### Exceptions
            - If an error occurs during calculation.\n
        '''
        try:
            sorted_numbers = sorted(arr)
            length = len(sorted_numbers)
            
            if length % 2 == 1:
                median = sorted_numbers[length // 2]
            else:
                middle1 = sorted_numbers[length // 2 - 1]
                middle2 = sorted_numbers[length // 2]
                median = (middle1 + middle2) / 2
            
            return median
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")