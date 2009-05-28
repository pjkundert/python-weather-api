#!/usr/bin/env python

from distutils.core import setup

__author__ = 'qetzal@gmail.com'
__version__ = '0.2'


setup(name='pywapi',
    version=__version__,
    description='A python wrapper around the Yahoo! Weather, Google Weather, NOAA and GisMeteo APIs',
    author='Eugene Kaznacheev',
    author_email='qetzal@gmail.com',
    url='http://code.google.com/p/python-weather-api/',
    py_modules=['pywapi'],
    keywords = 'weather api yahoo noaa google gismeteo',
)
