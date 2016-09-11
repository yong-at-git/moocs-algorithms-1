import unittest
from solution.inversion_counter import InversionCounter


class InversionCounterTestCase(unittest.TestCase):
    def test_sort_and_count_empty_input(self):
        self.assertEqual(InversionCounter.sort_and_count([]), 0)

    def test_sort_and_count_one_element(self):
        self.assertEqual(InversionCounter.sort_and_count([1]), 0)

    def test_sort_and_count_example_input(self):
        inverted = [1, 3, 5, 2, 4, 6]
        inversions = 3  # (3,2), (5,2), (5,4)

        self.assertEqual(InversionCounter.sort_and_count(inverted), inversions)

    def test_count_default_input_file(self):
        inversion_counter = InversionCounter()
        inversions = 2407905288
        input_file = './input_array.txt'

        self.assertEqual(inversion_counter.count(input_file), inversions)


if __name__ == "__main__":
    unittest.main()
