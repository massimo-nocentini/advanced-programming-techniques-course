
from tdd import *

test = WasRun("testMethod")
print(test.was_run) # we expect to see `False` printed out
test.test_method()
print(test.was_run) # we expect to see `True` printed out
