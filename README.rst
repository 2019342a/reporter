Logging Reporter
================
**Lightweight logger decorators for python**



.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

.. image:: https://github.com/2019342a/reporter/workflows/reporter/badge.svg
     :target: https://github.com/2019342a/reporter
     :alt: Tests


:License: MIT

What is this repository?
------------------------
Extends default python logging `module <https://docs.python.org/3/library/logging.html>`_ to make it easier to log actions before and after running functions and methods.
Usefull when debugging an application and you want to see the time a function takes or when the function was called.

Features
--------

- Display when a function was executed
- Display the result of a function
- Display a value before and after a fucntion was executed
- Display the execution time
- Display the :code:`str` and :code:`repr` method of an object before and after

How do I get set up?
--------------------

Use :code:`pip install git+ssh://git@github.com/2019342a/reporter` to install the library. Then you are good to go!


Dependencies
------------
logging-reporter requires `colorlog <https://github.com/borntyping/python-colorlog>`_ to add colour to the reporter logs.

Example
-------

.. code-block:: python

 from reporter.utils import create_reporter
 from reporter.decorators import report_execution

 # Initialise the logger
 create_reporter()

 @report_execution
 def add(a: int, b: int) -> int:
    return a + b


 add(1, 2)

You should then see in your terminal something like:

:code:`2021-05-15 11:05:53,114 - reporter - DEBUG - add was executed with args 1 2`

Contact
-------
If you have any questions, bugs or features please open a github issue.
