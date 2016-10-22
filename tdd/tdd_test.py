
from tdd import *


class TestCaseTest(TestCase):

    def test_running(self):
        test = WasRun(lambda test: test.test_method)
        assert not test.was_run 
        test.run()
        assert test.was_run

    def test_set_up(self):
        test = WasRun(lambda test: test.test_method)
        test.run()
        assert test.was_set_up
