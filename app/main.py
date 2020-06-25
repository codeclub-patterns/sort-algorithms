from lib.sort_manager import SortManager
from lib.bubble_sort import BubbleSort
from random import randint


if __name__ == '__main__':

    target_list = [randint(10, 99) for k in range(12)]
    print(target_list)
    select_algorithm = BubbleSort(target_list)

    sort_manager = SortManager(select_algorithm)
    sort_manager.execute()
    print(target_list)
