from distutils.core import setup

import wpactrl as mod

setup(
    name='wpactrl',
    version=mod.__version__,
    description='Fast and simple WSGI-framework for small web-applications.',
    long_description=mod.__doc__,
    author=mod.__author__,
    author_email='apps@outernet.is',
    url='https://github.com/Outernet-Project/wpactrl',
    py_modules=['wpactrl'],
    license='GPL',
)
