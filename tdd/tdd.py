
class WasRun:

    # Now class `WasRun` is doing two distinct jobs: one is keeping track whether
    # a method was invoked or not, and the other is (dynamically) invoking the method.

    def __init__(self, getter):
        self.was_run = False
        self.getter = getter

    def test_method(self):
        self.was_run = True 
    
    def run(self):
        method = self.getter(self)
        method()
