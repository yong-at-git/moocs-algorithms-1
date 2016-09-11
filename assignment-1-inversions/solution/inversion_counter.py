
import array
from solution.list_utils import ListUtils
from solution.quicksorter import QuickSorter


class InversionCounter:

    def count(self, input_file_path):
        original_numbers = self._read_input_numbers(input_file_path)
        return InversionCounter.sort_and_count(original_numbers)

    @staticmethod
    def sort_and_count(numbers):

        if len(numbers) <= 1:
            return 0
        else:
            first_half = ListUtils.get_first_half(numbers)
            first_half_result = InversionCounter.sort_and_count(first_half)

            second_half = ListUtils.get_second_half(numbers)
            second_half_result = InversionCounter.sort_and_count(second_half)

            split_inversion_result = InversionCounter.count_split_inversion(first_half, second_half)

        return first_half_result + second_half_result + split_inversion_result

    @staticmethod
    def count_split_inversion(first_half, second_half):

        inversions = []

        first_list_idx = 0
        second_list_idx = 0
        total_idx = 0

        first_half_sorted = QuickSorter.sort(first_half)
        second_half_sorted = QuickSorter.sort(second_half)

        while total_idx < len(first_half) + len(second_half):
            if first_list_idx == len(first_half):
                return sum(inversions)
            elif second_list_idx == len(second_half):
                return sum(inversions)
            elif first_half_sorted[first_list_idx] < second_half_sorted[second_list_idx]:
                first_list_idx += 1
            else:
                inversions.append(len(first_half) - first_list_idx)
                second_list_idx += 1

            total_idx += 1

        return sum(inversions)

    def _read_input_numbers(self, input_file_path):
        f = open(input_file_path)

        original_numbers = array.array('i')

        for line in f:
            original_numbers.append(int(line))

        return original_numbers
