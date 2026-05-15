import unittest

from YearMonth import YearMonth


class YearMonthTest(unittest.TestCase):
    def test_given_valid_year_and_month_when_creating_year_month_then_store_them(self):
        # Given
        year = 2026
        month = 5

        # When
        year_month = YearMonth(year, month)

        # Then
        self.assertEqual(2026, year_month.year)
        self.assertEqual(5, year_month.month)

    def test_given_month_less_than_one_when_creating_year_month_then_raise_value_error(self):
        # Given
        year = 2026
        month = 0

        # When / Then
        with self.assertRaisesRegex(ValueError, "month must be between 1 and 12"):
            YearMonth(year, month)

    def test_given_month_greater_than_twelve_when_creating_year_month_then_raise_value_error(self):
        # Given
        year = 2026
        month = 13

        # When / Then
        with self.assertRaisesRegex(ValueError, "month must be between 1 and 12"):
            YearMonth(year, month)

    def test_given_non_integer_year_when_creating_year_month_then_raise_type_error(self):
        # Given
        year = "2026"
        month = 5

        # When / Then
        with self.assertRaisesRegex(TypeError, "year must be an integer"):
            YearMonth(year, month)

    def test_given_non_integer_month_when_creating_year_month_then_raise_type_error(self):
        # Given
        year = 2026
        month = "5"

        # When / Then
        with self.assertRaisesRegex(TypeError, "month must be an integer"):
            YearMonth(year, month)


if __name__ == "__main__":
    unittest.main()
