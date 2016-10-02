#! /usr/bin/env python3

from solution.list_utils import ListUtils


class MergeSorter:
    @staticmethod
    def sort(numbers):
        if len(numbers) <= 1:
            return numbers
        else:
            first_half = ListUtils.get_first_half(numbers)
            first_half_sorted = MergeSorter.sort(first_half)

            second_half = ListUtils.get_second_half(numbers)
            second_half_sorted = MergeSorter.sort(second_half)

            return MergeSorter._merge(first_half_sorted, second_half_sorted)

    @staticmethod
    def _merge(first_sorted_half, second_sorted_half):
        merged = []

        first_list_idx = 0
        second_list_idx = 0
        total_idx = 0

        while total_idx < len(first_sorted_half) + len(second_sorted_half):
            if first_list_idx == len(first_sorted_half):
                merged.append(second_sorted_half[second_list_idx])
                second_list_idx += 1
            elif second_list_idx == len(second_sorted_half):
                merged.append(first_sorted_half[first_list_idx])
                first_list_idx += 1
            elif first_sorted_half[first_list_idx] <= second_sorted_half[second_list_idx]:
                merged.append(first_sorted_half[first_list_idx])
                first_list_idx += 1
            else:
                merged.append(second_sorted_half[second_list_idx])
                second_list_idx += 1

            total_idx += 1

        return merged
