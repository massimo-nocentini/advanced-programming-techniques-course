

class TestCase:

    def __init__(self, getter):
        self.getter = getter

    def set_up(self): pass

    def tear_down(self): pass
    
    def run(self):
        self.set_up()
        method = self.getter(self)
        method()
        self.tear_down()


class WasRun(TestCase):

    def test_method(self):
        self.was_run = True 
        self.log.append('test_method')
    
    def set_up(self):
        self.was_run = False
        self.log = []
        self.log.append('set_up')

    def tear_down(self):
        self.log.append('tear_down')
