import pickle
import numpy as np
import csv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--DatasetXX_dir', default='Dataset01',type=str, help="DatasetXX_dir")
parser.add_argument('--dense_proposals_dir', default='dense_proposals_train.pkl',type=str, help="dense_proposals_train.pkl or dense_proposals_val.pkl")

arg = parser.parse_args()

pkl_dir = '../../Dataset/' + arg.DatasetXX_dir + '/annotations/' + arg.dense_proposals_dir

f = open(pkl_dir,'rb')
info = pickle.load(f, encoding='iso-8859-1') 
dense_proposals_train = {}


for i in info:
    tempArr = np.array(info[i])
    dicts = []
    for index1,temp in enumerate(tempArr):
        temp = temp.astype(np.float64)
        for index2,x in enumerate(temp):
            if x < 0:
                temp[index2]=0.0
            if x > 1:
                temp[index2]=1.0
        dicts.append(temp)
    dense_proposals_train[i] = np.array(dicts)
# 保存为pkl文件
with open(pkl_dir,"wb") as pklfile: 
    pickle.dump(dense_proposals_train, pklfile)
