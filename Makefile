
FACTORIAL_DIR=factorial/
PAYROLL_DIR=payroll/

tests:
	# https://www.gnu.org/software/make/manual/html_node/Recursion.html
	$(MAKE) tests -C $(FACTORIAL_DIR)
	$(MAKE) tests -C $(PAYROLL_DIR)

tests-local:
	# https://www.gnu.org/software/make/manual/html_node/Recursion.html
	$(MAKE) tests-local -C $(FACTORIAL_DIR)
	$(MAKE) tests-local -C $(PAYROLL_DIR)
