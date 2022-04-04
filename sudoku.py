from typing import List


def main():
    assert is_correct([1, 2, 8, 9, 3, 5, 6, 7, 4]) == True
    assert is_correct([1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert is_correct([1, 1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert is_correct([]) == False

def is_correct(sudoku_list : List[int]):
    sudoku_correct = {1,2,3,4,5,6,7,8,9}
    sudoku_set = set(sudoku_list)
    
    return True if sudoku_correct.difference(sudoku_set) == set() else False



if __name__ == "__main__":
    print(main())
    