class YearMonth:
    MIN_MONTH = 1
    MAX_MONTH = 12

    def __init__(self, year, month):
        normalized_year, normalized_month = self._normalize(year, month)
        self.year = normalized_year
        self.month = normalized_month

    @classmethod
    def _normalize(cls, year, month):
        return cls._require_integer(year, "year"), cls._validate_month(month)

    @staticmethod
    def _require_integer(value, field_name):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{field_name} must be an integer")
        return value

    @classmethod
    def _validate_month(cls, month):
        normalized_month = cls._require_integer(month, "month")
        if normalized_month < cls.MIN_MONTH or normalized_month > cls.MAX_MONTH:
            raise ValueError("month must be between 1 and 12")
        return normalized_month

    def __repr__(self):
        return f"YearMonth(year={self.year}, month={self.month})"
