#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'blockbuffer',
    version = '0.0.1',
    description = 'Bufferand iterate over audio blocks of a fixed size, with overlap',
    author = 'Daniel Jones',
    author_email = 'dan-code@erase.net',
    url = 'https://github.com/ideoforms/python-blockbuffer',
    packages = ['blockbuffer'],
    install_requires = ['numpy'],
    keywords = ('buffer', 'data', 'dsp', 'audio'),
    classifiers = [
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers'
    ],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest']
)