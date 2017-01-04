
# Description

A repo to collect work while attending classes of [Advanced Programming
Techniques][course] course, taught by prof [Lorenzo Bettini][bettini] @
University of Florence.

[bettini]:https://github.com/LorenzoBettini
[course]:https://e-l.unifi.it/course/view.php?id=2215

# Content

First of all some links about structuring a project for a *healthy* development
cycle:
- http://docs.python-guide.org/en/latest/writing/structure/
- https://docs.python.org/3/reference/datamodel.html
- https://www.python.org/dev/peps/pep-0008/
- http://learnvimscriptthehardway.stevelosh.com/

## TDD: `factorial`

In folder [`factorial`][fact:dir] there's some code about *Test Driven
Development*, in particular it collects the port in Python of the code seen in
class, which was implemented in Java, of coding the `factorial` function $n!$.
If you're using VIM, evaluate the command `:source commands.vim`, being in that
directory, in order to map `<F3>` key to run test cases instead of typing
`!make` command each time. We collect the following links:
- [`unittest` module][doc:unittest] official documentation
- [original paper][beck] by Kent Beck on TDD
- [BDD][bdd]


[doc:unittest]:https://docs.python.org/3/library/unittest.html
[beck]:https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm
[fact:dir]:https://github.com/massimo-nocentini/apt-unifi-course/tree/master/factorial
[bdd]:http://pythonhosted.org/behave/tutorial.html

## TDD: bootstrapping a test framework

In folder [`tdd`][tdd:folder] there's the bootstrap of a tiny test framework,
*driven by test-first*, in the spirit of [Kent Beck][tdd:beck]. We record a
commit for each interesting point, in order to be able to look at the history
as a learning process about the derivation of a simple but working unit-test
framework driven by tests, it's a kind of self-brain surgery ;)

[tdd:beck]:https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=pd_sim_14_6?_encoding=UTF8&psc=1&refRID=P274Z8V81HKRP4S2YHHS
[tdd:folder]:https://github.com/massimo-nocentini/advanced-programming-techniques-course/tree/master/tdd

## Mocking: `payroll`

In folder [`payroll`][payroll:dir] there's some code about *mocking* concepts,
applied to implementing a payroll example.  The official documentation of
`unittest.mock` module is comprehensive with useful sample code, moreover we
find interesting the following resources,  also:
- [`unittest.mock` module][doc:unittest:mock] official documentation
- https://www.toptal.com/python/an-introduction-to-mocking-in-python
- https://realpython.com/blog/python/testing-third-party-apis-with-mocks/
- https://blog.fugue.co/2016-02-11-python-mocking-101.html
- http://wesmckinney.com/blog/spying-with-python-mocks/

### Coverage

We use module [`coverage`][cov] in order to spot regions of code not stressed
by tests. Remember to install such module with `sudo pip3 install coverage`.

[doc:unittest:mock]:https://docs.python.org/3/library/unittest.mock.html
[payroll:dir]:https://github.com/massimo-nocentini/apt-unifi-course/tree/master/payroll
[cov]:https://coverage.readthedocs.io/en/coverage-4.2/index.html

## Dependency Injection

Some links:
- https://github.com/google/pinject
- http://www.aleax.it/yt_pydi.pdf

# Continuous Integration

![build-status-flag]
(https://travis-ci.org/massimo-nocentini/advanced-programming-techniques-course.svg?branch=master)

We've set up a link with [Travis CI][travis] and this repository in order to
have automatic builds for our code, `factorial` and `payroll` exercises in
particular. More info here: https://docs.travis-ci.com/user/customizing-the-build/

[travis]:https://travis-ci.org/massimo-nocentini/advanced-programming-techniques-course
