
from tdd import *


class TestCaseTest(TestCase):

    def set_up(self):
        self.test = WasRun(lambda test: test.test_method)
        self.result = TestResult()

    def test_template_method(self):
        self.test.run(self.result)
        assert self.test.log == ['set_up', 'test_method', 'tear_down']

    def test_result(self):
        self.test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def test_failed_result(self):
        self.test = WasRun(lambda test: test.broken_test_method)
        self.test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert "1 run, 1 failed" == self.result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.append(WasRun(lambda test: test.test_method))
        suite.append(WasRun(lambda test: test.broken_test_method))
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()
    
