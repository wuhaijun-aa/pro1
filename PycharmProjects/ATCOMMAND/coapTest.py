import os
import sys
import unittest
from pathlib import Path
import

class caseTest(unittest.testcase):
    def __init__(self,name,namepath):
        self.name = os.path.basename(sys.argv[0].replace(".py",""))
        self.namepath = Path("d:\\test\\test")
    def setup(self):
        self.ser = serial