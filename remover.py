import os
import glob
import shutil


files = glob.glob('./com/')

for f in files:
    shutil.rmtree(f)