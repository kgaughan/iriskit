#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages
import re


def read(filename):
    with open(filename, 'r') as fh:
        return fh.read()


def get_metadata(module_path):
    """Extract the metadata from a module file."""
    matches = re.finditer(
        r"^__(\w+?)__ *= *'(.*?)'$",
        read(module_path),
        re.MULTILINE)
    return dict(
        (match.group(1), match.group(2).decode('unicode_escape'))
        for match in matches)


def read_requirements(requirements_path):
    """Read a requirements file, stripping out the detritus."""
    requirements = []
    with open(requirements_path, 'r') as fh:
        for line in fh:
            line = line.strip()
            if line != '' and not line.startswith(('#', 'svn+', 'git+')):
                requirements.append(line)
    return requirements


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
    zip_safe=True,
    install_requires=read_requirements('requirements.txt'),

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
    author_email=META['version']
)
