#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages
from buildkit import *


META = get_metadata('iriskit/__init__.py')


setup(
    name='iriskit',
    version=META['version'],
    description='Internet Registry Information Service (IRIS) client',
    long_description=read('README'),
    url='https://github.com/kgaughan/iriskit/',
    platforms=['any'],
    license='MIT',
    packages=find_packages(exclude='tests'),
    zip_safe=False,
    install_requires=read_requirements('requirements.txt'),
    include_package_data=True,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],

    author=META['author'],
    author_email=META['email'],
)
