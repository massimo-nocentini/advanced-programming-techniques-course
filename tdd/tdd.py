

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
    
    def set_up(self):
        self.was_run = False
        self.was_set_up = True
