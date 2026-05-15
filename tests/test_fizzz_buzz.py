import unittest

from FizzzBuzz import FizzzBuzz


class FizzzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.converter = FizzzBuzz()

    def test_given_plain_number_when_converting_then_return_number_itself(self):
        # Given
        number = 1

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("1", result)

    def test_given_multiple_of_three_when_converting_then_return_fizz(self):
        # Given
        number = 6

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("Fizz", result)

    def test_given_multiple_of_five_when_converting_then_return_buzz(self):
        # Given
        number = 10

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("Buzz", result)

    def test_given_multiple_of_three_and_five_when_converting_then_return_fizz_buzz(self):
        # Given
        number = 15

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("FizzBuzz", result)


if __name__ == "__main__":
    unittest.main()
