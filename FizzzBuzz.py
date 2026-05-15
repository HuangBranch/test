def convert(number):
    _validate_number(number)

    fizz = _is_fizz(number)
    buzz = _is_buzz(number)

    if fizz and buzz:
        return "FizzBuzz"
    if fizz:
        return "Fizz"
    if buzz:
        return "Buzz"
    return str(number)


def _validate_number(number):
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1 or number > 100:
        raise ValueError("number must be between 1 and 100")


def _is_fizz(number):
    return number % 3 == 0 or "3" in str(number)


def _is_buzz(number):
    return number % 5 == 0 or "5" in str(number)


class FizzzBuzz:
    def convert(self, number):
        return convert(number)

    def say(self, number):
        return convert(number)

    def __call__(self, number):
        return convert(number)
