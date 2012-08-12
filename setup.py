#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='iriskit',
    version='0.1.0',
    description='Internet Registry Information Service (IRIS) client',
    long_description=open('README').read(),
    url='https://github.com/kgaughan/iriskit/',
    license='MIT',
    packages=find_packages(exclude='tests'),
    zip_safe=True,
    install_requires=[line.rstrip() for line in open('requirements.txt')],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: System :: Networking',
    ],

    author='Keith Gaughan',
    author_email='k@stereochro.me'
)
