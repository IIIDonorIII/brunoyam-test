import unittest
import random
import functools
from largest_number import largest_number

def compare(x, y):
    return int(x + y) - int(y + x)

def largest_number(nums):
    nums_str = list(map(str, nums))
    max_length = max(map(len, nums_str))
    
    nums_str.sort(key=functools.cmp_to_key(compare), reverse=True)
    
    return ''.join(nums_str)

class TestLargestNumberSorting(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_number([]), "")

    def test_single_element(self):
        self.assertEqual(largest_number([42]), "42")

    def test_multiple_elements(self):
        self.assertEqual(largest_number([56, 9, 11, 2]), "956211")
        self.assertEqual(largest_number([3, 81, 5]), "8153")

    def test_equal_elements(self):
        self.assertEqual(largest_number([111, 1111, 11, 11111]), "111111111111")

    def test_large_numbers(self):
        self.assertEqual(largest_number([99, 555, 33, 7777]), "9977755533")

    def test_random_arrays(self):
        for _ in range(10):
            nums = [random.randint(1, 1000) for _ in range(random.randint(1, 20))]
            self.assertEqual(
                largest_number(nums),
                ''.join(sorted(map(str, nums), key=functools.cmp_to_key(compare), reverse=True))
            )

if __name__ == '__main__':
    unittest.main()