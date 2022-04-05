import os
import subprocess
import leafmap 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 


try:
    import leafmap
except ImportError:
    print('Installing leafmap ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'leafmap'])


import leafmap.foliumap as leafmap


m = leafmap.Map(center=(40, -100), zoom=4)

m
