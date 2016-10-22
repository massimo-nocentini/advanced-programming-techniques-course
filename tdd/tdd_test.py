
from tdd import *


class TestCaseTest(TestCase):

    def set_up(self):
        self.test = WasRun(lambda test: test.test_method)

    def test_template_method(self):
        self.test.run()
        assert self.test.log == ['set_up', 'test_method', 'tear_down']

    def test_result(self):
        result = self.test.run()
        assert "1 run, 0 failed" == result.summary()
