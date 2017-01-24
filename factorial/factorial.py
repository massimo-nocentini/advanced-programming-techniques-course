
class Factorial(object):

    def __call__(self, i):
        if i < 0: raise ValueError

        result = 1
        while i:
            result *= i
            i -= 1

        return result
