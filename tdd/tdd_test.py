
from tdd import *


class TestCaseTest(TestCase):

    def set_up(self):
        # we can also simplify the tests themselves, namely we create the `WasRun` object 
        # in here in `set_up` since each test method is run in a clean instance of `TestCaseTest`,
        # created by the runner, so there is no way the two tests can be coupled.
        self.test = WasRun(lambda test: test.test_method)

    def test_running(self):
        # skip the following `assert` since `was_run` is now created in `set_up` method, called by `run`:
        # assert not self.test.was_run 
        self.test.run()
        assert self.test.was_run

    def test_set_up(self):
        self.test.run()
        assert self.test.was_set_up
