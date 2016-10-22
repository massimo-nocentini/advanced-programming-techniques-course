
from tdd import *

test = WasRun(lambda sut: sut.test_method)

print(test.was_run) # we expect to see `False` printed out

test.run()

print(test.was_run) # we expect to see `True` printed out
