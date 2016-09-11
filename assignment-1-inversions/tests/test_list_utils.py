import unittest
from solution.list_utils import ListUtils


class ListUtilsTestCase(unittest.TestCase):

    even_list = [1, 2, 3, 4]
    even_first_half = [1, 2]
    even_second_half = [3, 4]

    odd_list = [1, 2, 3, 4, 5]
    odd_first_half = [1, 2]
    odd_second_half = [3, 4, 5]

    def test_empty(self):
        self.assertEqual(ListUtils.get_first_half([]), [])
        self.assertEqual(ListUtils.get_second_half([]), [])

    def test_get_first_half_odd(self):
        self.assertEqual(ListUtils.get_first_half(self.odd_list), self.odd_first_half)

    def test_get_second_half_odd(self):
        self.assertEqual(ListUtils.get_second_half(self.odd_list), self.odd_second_half)

    def test_get_first_half_even(self):
        self.assertEqual(ListUtils.get_first_half(self.even_list), self.even_first_half)

    def test_get_second_half_even(self):
        self.assertEqual(ListUtils.get_second_half(self.even_list), self.even_second_half)

if __name__ == '__main__':
    unittest.main()
