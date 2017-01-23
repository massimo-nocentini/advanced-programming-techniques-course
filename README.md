
# Description

A repo to collect work while attending classes of [Advanced Programming
Techniques][course] course, taught by prof [Lorenzo Bettini][bettini] @
University of Florence; although the course targets Java-like languages,
our aim is to port and implement concepts using the _Python_ language.

Three toy projects have been implemented, as described in the following sections.

[bettini]:https://github.com/LorenzoBettini
[course]:https://e-l.unifi.it/course/view.php?id=2215

## TDD: `factorial`

In folder [`factorial`][fact:dir] there is some code written sticking to the
*Test Driven Development* methodology; in particular, it collects the port of
the tutorial seen in classes about the coding of the `factorial` function `n!`.
If you're using VIM, evaluate the command `:source commands.vim`, after moving
into the project directory: key `<F3>` is mapped to run test cases, avoiding to
type the `:!make` command each time. We collect the following links:
- [`unittest` module][doc:unittest] official documentation;
- [original paper][beck] by Kent Beck on TDD;
- [BDD][bdd], in the style of [`rspec`][rspec].

[doc:unittest]:https://docs.python.org/3/library/unittest.html
[beck]:https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm
[fact:dir]:https://github.com/massimo-nocentini/apt-unifi-course/tree/master/factorial
[bdd]:http://pythonhosted.org/behave/tutorial.html
[rspec]:http://rspec.info/

## TDD: `bootstrapping` a test framework

In folder [`tdd`][tdd:folder] we bootstrap a tiny test framework, *driven by
test-first*, in the spirit of [Kent Beck][tdd:beck]. We record a commit for
each interesting step, in order to be able to look at the history as a learning
process about the derivation of a simple, eventually working, unit-test
framework -- "...it's a kind of self-brain surgery", in Kent's words ;)

[tdd:beck]:https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=pd_sim_14_6?_encoding=UTF8&psc=1&refRID=P274Z8V81HKRP4S2YHHS
[tdd:folder]:https://github.com/massimo-nocentini/advanced-programming-techniques-course/tree/master/tdd

## Mocking: `payroll`

In folder [`payroll`][payroll:dir] there is some code about *mocking* concepts,
applied to the `payroll` case study.  The official documentation of
`unittest.mock` module is comprehensive with useful sample code; moreover, we
find of interest the following resources too:
- [`unittest.mock` module][doc:unittest:mock] official documentation
- https://www.toptal.com/python/an-introduction-to-mocking-in-python
- https://realpython.com/blog/python/testing-third-party-apis-with-mocks/
- https://blog.fugue.co/2016-02-11-python-mocking-101.html
- http://wesmckinney.com/blog/spying-with-python-mocks/

## Continuous Integration: `travis-ci`

[![Build Status](https://travis-ci.org/massimo-nocentini/advanced-programming-techniques-course.svg?branch=master)](https://travis-ci.org/massimo-nocentini/advanced-programming-techniques-course)

We have set up a link with [Travis CI][travis] and this repository in order to
have automatic builds for our code, `factorial` and `payroll` exercises in
particular. More info here: https://docs.travis-ci.com/user/customizing-the-build/

[travis]:https://travis-ci.org/massimo-nocentini/advanced-programming-techniques-course

# Misc

In the following sections we collect heterogeneous stuff, mainly to bookmark them
for further work. 

## Refs

Some links about structuring a project for a *healthy* development cycle:
- http://docs.python-guide.org/en/latest/writing/structure/
- https://docs.python.org/3/reference/datamodel.html
- https://www.python.org/dev/peps/pep-0008/
- http://learnvimscriptthehardway.stevelosh.com/

### Coverage

We use module [`coverage`][cov] in order to spot regions of code not stressed
by tests. Remember to install such module with `sudo pip3 install coverage`.

[doc:unittest:mock]:https://docs.python.org/3/library/unittest.mock.html
[payroll:dir]:https://github.com/massimo-nocentini/apt-unifi-course/tree/master/payroll
[cov]:https://coverage.readthedocs.io/en/coverage-4.2/index.html

## Dependency Injection

Just some links:
- https://github.com/google/pinject
- http://www.aleax.it/yt_pydi.pdf
