

class TestCase:

    def __init__(self, getter):
        self.getter = getter

    def run(self):
        method = self.getter(self)
        method()


class WasRun(TestCase):

    def __init__(self, getter):
        TestCase.__init__(self, getter)
        self.was_run = False

    def test_method(self):
        self.was_run = True 
    
