
from tdd_test import *

# manual test runner:
TestCaseTest(lambda fixture: fixture.test_running).run()
TestCaseTest(lambda fixture: fixture.test_set_up).run()
