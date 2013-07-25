#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='django-autoslug',
      version='0.1',
      description='Automatic slugification on Django models.',
      long_description=readme,
      author='Patrick Jacobs',
      url='https://github.com/ceol/django-autoslug',
      license=license,
      packages=find_packages(),
     )