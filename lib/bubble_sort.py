from lib.abstract_strategy import SortAlgorithm


class BubbleSort(SortAlgorithm):

    def __init__(self, target_list: list):
        super().__init__(target_list)

    def sort(self) -> None:
        n = len(self._target_list)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self._target_list[j] > self._target_list[j + 1]:
                    buff = self._target_list[j]
                    self._target_list[j] = self._target_list[j + 1]
                    self._target_list[j + 1] = buff
