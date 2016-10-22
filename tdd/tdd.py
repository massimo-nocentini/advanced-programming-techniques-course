

class TestCase:

    def __init__(self, getter):
        self.getter = getter

    def set_up(self): pass
    
    def run(self):
        self.set_up()
        method = self.getter(self)
        method()


class WasRun(TestCase):

    def test_method(self):
        self.was_run = True 
        self.log.append('test_method')
    
    def set_up(self):
        self.was_run = False

#       the simpleminded way to write the test for de-allocation is to introduce yet
#       another flag. All of those flags are starting to bug me, and they are missing
#       an important aspect of the methods, namely the order in which they are called:
#       `set_up` should be called before the test method is run, and `tear_down` is 
#       called afterward. So we maintain a log for calls, as a `list` object:
        self.log = []

#       finally, append that this method has been actually called:
        self.log.append('set_up')
