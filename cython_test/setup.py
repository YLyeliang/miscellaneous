from setuptools import setup
from Cython.Build import cythonize

setup(name='version2',ext_modules=cythonize('version2.pyx'))