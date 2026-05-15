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

    def test_given_invalid_month_when_creating_year_month_then_raise_value_error(self):
        test_cases = (0, 13)

        for month in test_cases:
            with self.subTest(month=month):
                # Given
                year = 2026

                # When / Then
                with self.assertRaisesRegex(ValueError, "month must be between 1 and 12"):
                    YearMonth(year, month)

    def test_given_non_integer_year_when_creating_year_month_then_raise_type_error(self):
        test_cases = ("2026", True)

        for year in test_cases:
            with self.subTest(year=year):
                # Given
                month = 5

                # When / Then
                with self.assertRaisesRegex(TypeError, "year must be an integer"):
                    YearMonth(year, month)

    def test_given_non_integer_month_when_creating_year_month_then_raise_type_error(self):
        test_cases = ("5", True)

        for month in test_cases:
            with self.subTest(month=month):
                # Given
                year = 2026

                # When / Then
                with self.assertRaisesRegex(TypeError, "month must be an integer"):
                    YearMonth(year, month)

    def test_given_year_month_when_rendering_repr_then_return_debug_friendly_text(self):
        # Given
        year_month = YearMonth(2026, 5)

        # When
        result = repr(year_month)

        # Then
        self.assertEqual("YearMonth(year=2026, month=5)", result)


if __name__ == "__main__":
    unittest.main()
