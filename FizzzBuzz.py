RULES = (
    (3, "3", "Fizz"),
    (5, "5", "Buzz"),
    (7, "7", "Whizz"),
)


def convert(number):
    _validate_number(number)

    number_text = str(number)
    matched_words = [
        word
        for divisor, digit, word in RULES
        if _matches_rule(number, number_text, divisor, digit)
    ]

    return "".join(matched_words) or number_text


def _validate_number(number):
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1:
        raise ValueError("number must be greater than 0")


def _matches_rule(number, number_text, divisor, digit):
    return number % divisor == 0 or digit in number_text


class FizzzBuzz:
    def convert(self, number):
        return convert(number)

    def say(self, number):
        return convert(number)

    def __call__(self, number):
        return convert(number)
