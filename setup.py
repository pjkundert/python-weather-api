#!/usr/bin/env python

from distutils.core import setup

__author__ = 'qetzal@gmail.com'
__version__ = '0.2.1'


setup(name='pywapi',
    version=__version__,
    description='A python wrapper around the Yahoo! Weather, Google Weather and NOAA APIs',
    author='Eugene Kaznacheev',
    author_email='qetzal@gmail.com',
    url='http://code.google.com/p/python-weather-api/',
    py_modules=['pywapi'],
    license='MIT',
    keywords = 'weather api yahoo noaa google',
)
