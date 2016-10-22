
from tdd import *


# we're getting tired of looking to see that `False` and `True` booleans
# are printed every time. Using the mechanism we just built, we can now write:

class TestCaseTest(TestCase):

    def test_running(self):
        """
        This test method allows us to ensure that `test_method` is actually called.
        """
        test = WasRun(lambda test: test.test_method)
        assert not test.was_run 
        test.run()
        assert test.was_run

