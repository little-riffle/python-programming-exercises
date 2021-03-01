import unittest

from repeating_numbers import find_repeating_numbers


class RepeatingNumbersTest(unittest.TestCase):
    def test_repeating_single_number(self):
        self.assertEqual(
            find_repeating_numbers(12, "9 31 38 5 62 44 38 17 19 38 50 74"), "38"
        )

    def test_two_repeating_numbers(self):
        self.assertEqual(
            find_repeating_numbers(12, "9 31 38 5 62 44 38 17 19 38 50 31"), "31 38"
        )

    def test_no_repeating_numbers(self):
        self.assertEqual(
            find_repeating_numbers(12, "4 3 14 15 18 39 56 89 101 150 165 187"), "0"
        )

    def test_another_repeating_single_number(self):
        self.assertEqual(
            find_repeating_numbers(9, "131 132 135 134 135 136 137 138 140"), "135"
        )

    def test_three_repeating_numbers(self):
        self.assertEqual(
            find_repeating_numbers(12, "9 20 38 5 62 4 38 17 19 38 5 20"), "5 20 38"
        )


if __name__ == "__main__":
    unittest.main()
