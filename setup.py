#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='mesoscope',
    version=version,
    description='process data from the two-photon random access mesoscope',
    author='sofroniewn',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/sofroniewn/mesoscope',
    packages=find_packages(),
    install_requires=required,
    entry_points = {"console_scripts": ['mesoscope = mesoscope.cli:cli']},
    long_description='See ' + 'https://github.com/sofroniewn/mesoscope',
    license='MIT'
)
