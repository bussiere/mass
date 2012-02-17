#!/usr/bin/env python

from setuptools import setup

setup(
    name='jswatchr',
    version='0.0.1',
    description='Watches your javascript',
    author='Jack Boberg & Alex Padgett',
    author_email='developer@topicdesign.com',
    url='https://github.com/jackboberg/jswatchr',
    packages=['jswatchr'],
    scripts=['jswatchr/scripts/jswatchr'],
    install_requires=['jsmin','macfsevents','argparse'],
    zip_safe = False
)
