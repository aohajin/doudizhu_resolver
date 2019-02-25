# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license = f.read()

setup(
    name='doudizhu_resolver',
    version='0.1.1',
    description='doudizhu puzzle resolver',
    long_description=readme,
    url='https://github.com/aohajin/doudizhu_resolver',
    author='aohajin',
    author_email='maohaijian@xiimoon.com',
    packages=['doudizhu_resolver'],
    data_files=[("", ["LICENSE"])],
    license=license,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ], )
