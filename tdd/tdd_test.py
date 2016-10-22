
from tdd import *


class TestCaseTest(TestCase):

    def set_up(self):
        self.test = WasRun(lambda test: test.test_method)

    def test_template_method(self):
        self.test.run()
        assert self.test.log == ['set_up', 'test_method', 'tear_down']
