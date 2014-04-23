#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='haste-client',
    version='1.0.1',
    url='https://github.com/jirutka/haste-client',
    description='CLI client for Haste server (hastebin.com) written in Python.',
    long_description=read_md('README.md'),
    author='Jakub Jirutka',
    author_email='jakub@jirutka.cz',
    license='MIT',
    scripts=['haste'],
    install_requires=[
        'requests',
        'docopt'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ]
)
