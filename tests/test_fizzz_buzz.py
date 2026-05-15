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

    def test_given_number_contains_three_when_converting_then_return_fizz(self):
        # Given
        number = 13

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("Fizz", result)

    def test_given_number_contains_five_when_converting_then_return_buzz(self):
        # Given
        number = 52

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("Buzz", result)

    def test_given_number_contains_three_and_five_when_converting_then_return_fizz_buzz(self):
        # Given
        number = 53

        # When
        result = self.converter.convert(number)

        # Then
        self.assertEqual("FizzBuzz", result)

    def test_given_number_less_than_one_when_converting_then_raise_value_error(self):
        # Given
        number = 0

        # When / Then
        with self.assertRaisesRegex(ValueError, "number must be between 1 and 100"):
            self.converter.convert(number)

    def test_given_number_greater_than_one_hundred_when_converting_then_raise_value_error(self):
        # Given
        number = 101

        # When / Then
        with self.assertRaisesRegex(ValueError, "number must be between 1 and 100"):
            self.converter.convert(number)

    def test_given_non_integer_number_when_converting_then_raise_type_error(self):
        # Given
        number = "3"

        # When / Then
        with self.assertRaisesRegex(TypeError, "number must be an integer"):
            self.converter.convert(number)

    def test_given_valid_number_when_using_say_then_return_expected_result(self):
        # Given
        number = 5

        # When
        result = self.converter.say(number)

        # Then
        self.assertEqual("Buzz", result)

    def test_given_valid_number_when_calling_instance_then_return_expected_result(self):
        # Given
        number = 3

        # When
        result = self.converter(number)

        # Then
        self.assertEqual("Fizz", result)


if __name__ == "__main__":
    unittest.main()
