
class Factorial(object):

    def __call__(self, i):
        if i < 0: raise ValueError
        return i*self(i-1) if i else 1
