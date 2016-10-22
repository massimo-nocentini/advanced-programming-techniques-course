
from tdd import *

test = WasRun("testMethod")
print(test.was_run) # we expect to see `False` printed out

# next we need to use our real interface `run()`, instead
# of calling the test method directly:
test.run()

print(test.was_run) # we expect to see `True` printed out
