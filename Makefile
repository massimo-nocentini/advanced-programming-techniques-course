
FACTORIAL_DIR=factorial/
PAYROLL_DIR=payroll/

tests:
	# https://www.gnu.org/software/make/manual/html_node/Recursion.html
	$(MAKE) -C $(FACTORIAL_DIR)
	$(MAKE) -C $(PAYROLL_DIR)
