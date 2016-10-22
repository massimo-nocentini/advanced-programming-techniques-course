
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

    def test_failed_result(self):
        self.test = WasRun(lambda test: test.broken_test_method)
        result = self.test.run()
        assert "1 run, 1 failed" == result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert "1 run, 1 failed" == result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.append(WasRun(lambda test: test.test_method))
        suite.append(WasRun(lambda test: test.broken_test_method))
        result = suite.run()
        assert "2 run, 1 failed" == result.summary()
    
