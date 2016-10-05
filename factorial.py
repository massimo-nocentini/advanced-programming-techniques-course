
class Factorial(object):

    def __call__(self, i):
        return i*self(i-1) if i else 1
