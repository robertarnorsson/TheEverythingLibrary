class TELMath():
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def add(self, x: int | float | str, y: int | float | str) -> float:
        return float(x + y)

    def add_list(self, arr: list[int | float | str]) -> float:
        result = 0.0
        clean_numbers = []
        for num in arr:
            if type(num) == str:
                clean_numbers.append(''.join(char for char in num if char.isdigit()))
            else:
                clean_numbers.append(num)
        if type(clean_numbers) == list:
            for num in clean_numbers:
                try:
                    result += float(num)
                except ValueError as msg:
                    print(f"{num} is a {type(num)} which is not able to be added!\n{msg}")
                except Exception as msg:
                    print(f"An error occured!\n{msg}")
            return float(result)
        else:
            return float(result)
    
    def subtract(self, x: int | float | str, y: int | float | str) -> float:
        return float(x - y)

    def subtract_list(self, arr_x: list[int | float | str], arr_y: list[int | float | str]) -> float:
        x = self.add_list(arr=arr_x)
        y = self.add_list(arr=arr_y)

        try:
            return float(x - y)
        except ValueError as msg:
            print(f"{x} or {y} is a {type(x)} or {type(y)} which is not able to be subtracted!\n{msg}")
        except Exception as msg:
            print(f"An error occured!\n{msg}")
    
    def average(self, arr: list[int | float | str]) -> float:
        length = len(arr)
        _sum = self.add_list(arr=arr)

        try:
            return float(_sum / length)
        except ValueError as msg:
            print(f"{_sum} is not able to be averaged!\n{msg}")
        except Exception as msg:
            print(f"An error occured!\n{msg}")