
# Description

A repo to collect work while attending classes of *Advanced Programming Techniques* taught by 
prof [Lorenzo Bettini][bettini] @ University of Florence.

[bettini]:https://github.com/LorenzoBettini

# Content

First of all some links about structuring a project for a *healthy* development cycle:
- http://docs.python-guide.org/en/latest/writing/structure/
- https://docs.python.org/3/reference/datamodel.html
- https://www.python.org/dev/peps/pep-0008/
- http://learnvimscriptthehardway.stevelosh.com/

## TDD: `factorial`

In folder [`factorial`][fact:dir] there's some code about *Test Driven Development*, in particular it collects 
the port in Python of the code seen in class, which was implemented in Java, of coding the `factorial` function $n!$.
If you're using VIM, evaluate the command `:source commands.vim`, being in that directory, in order to map
`<F3>` key to run test cases instead of typing `!make` command each time. We collect the following links:
- [`unittest` module][doc:unittest] official documentation
- [original paper][beck] by Kent Beck on TDD
- [BDD][bdd]


[doc:unittest]:https://docs.python.org/3/library/unittest.html
[beck]:https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm
[fact:dir]:https://github.com/massimo-nocentini/apt-unifi-course/tree/master/factorial
[bdd]:http://pythonhosted.org/behave/tutorial.html

## Mocking: `payroll`

In folder [`payroll`][payroll:dir] there's some code about *mocking* concepts, applied to implementing a payroll example.
The official documentation of `unittest.mock` module is comprehensive with useful sample code, moreover we find interesting
the following resources,  also:
- [`unittest.mock` module][doc:unittest:mock] official documentation
- https://www.toptal.com/python/an-introduction-to-mocking-in-python
- https://realpython.com/blog/python/testing-third-party-apis-with-mocks/
- https://blog.fugue.co/2016-02-11-python-mocking-101.html
- http://wesmckinney.com/blog/spying-with-python-mocks/

### Coverage

We use module [`coverage`][cov] in order to spot regions of code not stressed by tests. Remember to 
install such module with `sudo pip3 install coverage`.

[doc:unittest:mock]:https://docs.python.org/3/library/unittest.mock.html
[payroll:dir]:https://github.com/massimo-nocentini/apt-unifi-course/tree/master/payroll
[cov]:https://coverage.readthedocs.io/en/coverage-4.2/index.html

## Dependency Injection

Some links:
- https://github.com/google/pinject
- http://www.aleax.it/yt_pydi.pdf
