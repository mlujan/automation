
import os
from sst.actions import *
from sst import runtests

#Load Our custom Functions
execfile("_functions/importCsv.py")
path = os.path.dirname(os.path.abspath(__file__))
data = loadmain(path +"/_data/testdata.csv")
sleep(10)
