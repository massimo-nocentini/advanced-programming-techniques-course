
from tdd_test import *

# manual test runner:
suite = TestSuite()
suite.append(TestCaseTest(lambda fixture: fixture.test_template_method))
suite.append(TestCaseTest(lambda fixture: fixture.test_result))
suite.append(TestCaseTest(lambda fixture: fixture.test_failed_result_formatting))
suite.append(TestCaseTest(lambda fixture: fixture.test_failed_result))
suite.append(TestCaseTest(lambda fixture: fixture.test_suite))

result = TestResult()
suite.run(result)

print(result.summary()) # should print "5 run, 0 failed" on the console

