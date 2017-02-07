# -*- coding: utf8 -*-
import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'mobile',
    version = "0.3.3",
    author = "Johannes Gorset",
    author_email = "jgorset@gmail.com",
    description = "Simple, easy to use sms app with support for pluggable backends",
    license = "MIT",
    keywords = ['sms', 'django',],
    long_description=read('README.md'),
    install_requires = [
        'suds==0.4',
        'twilio==5.7.0'
    ],
    packages = [
        'mobile',
        'mobile.backends',
        'mobile.migrations'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Framework :: Django",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
