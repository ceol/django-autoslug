#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='django-autoslug',
      version='0.1',
      description='Automatic slugification of Django models.',
      long_description=open('README.md').read(),
      author='Patrick Jacobs',
      url='https://github.com/ceol/django-autoslug',
      packages=['autoslug'],
     )