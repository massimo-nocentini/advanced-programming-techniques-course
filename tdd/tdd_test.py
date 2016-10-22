
from tdd import *


class TestCaseTest(TestCase):

    def set_up(self):
        self.test = WasRun(lambda test: test.test_method)

    def test_template_method(self):
#       now this test is doing the work of `test_running` too, so get rid of it, 
#       and rename this method, formely for `set_up`.
        self.test.run()
        assert self.test.log == ['set_up', 'test_method']
