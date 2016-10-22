
from tdd_test import *

# manual test runner:
print(TestCaseTest(lambda fixture: fixture.test_template_method).run().summary())
print(TestCaseTest(lambda fixture: fixture.test_result).run().summary())
print(TestCaseTest(lambda fixture: fixture.test_failed_result_formatting).run().summary())
print(TestCaseTest(lambda fixture: fixture.test_failed_result).run().summary())
