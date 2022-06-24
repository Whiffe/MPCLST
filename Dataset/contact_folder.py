import os
import shutil
import sys
import argparse
import pickle
import numpy as np
import csv
import random

parser = argparse.ArgumentParser()

parser.add_argument('--DatasetXX_dir', default='./',type=str)

arg = parser.parse_args()

DatasetXX_dir=arg.DatasetXX_dir


#遍历./DatasetXX_dir中的video_crop
for filepath,dirnames,filenames in os.walk(DatasetXX_dir):
    if 'Dataset' in filepath:
        if len(filepath.split('/')) == 2:
            #print(filepath)
            frames_path = filepath + '/frames/*'
            os.system('cp -r ' + frames_path + ' ./rawframes')
        
