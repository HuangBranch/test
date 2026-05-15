import unittest

from FizzzBuzz import FizzzBuzz


class FizzzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.converter = FizzzBuzz()

    def test_given_numbers_when_converting_then_return_expected_result(self):
        test_cases = (
            (1, "1"),
            (6, "Fizz"),
            (10, "Buzz"),
            (15, "FizzBuzz"),
            (13, "Fizz"),
            (52, "Buzz"),
            (53, "FizzBuzz"),
            (14, "Whizz"),
            (17, "Whizz"),
            (37, "FizzWhizz"),
            (572, "BuzzWhizz"),
            (21, "FizzWhizz"),
            (70, "BuzzWhizz"),
            (105, "FizzBuzzWhizz"),
            (537, "FizzBuzzWhizz"),
            (101, "101"),
        )

        for number, expected in test_cases:
            with self.subTest(number=number):
                # Given
                # When
                result = self.converter.convert(number)

                # Then
                self.assertEqual(expected, result)

    def test_given_invalid_numbers_when_converting_then_raise_expected_error(self):
        test_cases = (
            (0, ValueError, "number must be greater than 0"),
            (-1, ValueError, "number must be greater than 0"),
            ("3", TypeError, "number must be an integer"),
            (True, TypeError, "number must be an integer"),
        )

        for number, error_type, message in test_cases:
            with self.subTest(number=number):
                # Given
                # When / Then
                with self.assertRaisesRegex(error_type, message):
                    self.converter.convert(number)

    def test_given_supported_entry_points_when_converting_then_return_expected_result(self):
        test_cases = (
            ("say", 5, "Buzz"),
            ("__call__", 7, "Whizz"),
        )

        for entry_point, number, expected in test_cases:
            with self.subTest(entry_point=entry_point, number=number):
                # Given
                # When
                if entry_point == "__call__":
                    result = self.converter(number)
                else:
                    result = getattr(self.converter, entry_point)(number)

                # Then
                self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
