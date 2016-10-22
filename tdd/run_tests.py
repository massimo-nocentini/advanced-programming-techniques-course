
from tdd_test import *

# manual test runner:
TestCaseTest(lambda fixture: fixture.test_template_method).run()
TestCaseTest(lambda fixture: fixture.test_result).run()
TestCaseTest(lambda fixture: fixture.test_failed_result_formatting).run()
#TestCaseTest(lambda fixture: fixture.test_failed_result).run()
