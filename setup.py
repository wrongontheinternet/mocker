#!/usr/bin/env python

from distutils.core import setup
import mocker

setup(
    name='Mocker',
    version=mocker.__version__,
    description='Python example implementation of the Docker engine',
    author='Anthony Shaw',
    author_email='unknown@jto.id.au',
    url='https://github.com/tonybaloney/mocker/',
    packages=['mocker'],
    scripts=['scripts/mocker'])
