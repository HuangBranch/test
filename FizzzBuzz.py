def convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


class FizzzBuzz:
    def convert(self, number):
        return convert(number)

    def say(self, number):
        return convert(number)

    def __call__(self, number):
        return convert(number)
