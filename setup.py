#!/usr/bin/python   
from distutils.core import setup
import py2exe
import os, sys

CurrentPath = os.path.dirname(sys.argv[0])
setup(console=[str(CurrentPath) + 'spider.py'])
