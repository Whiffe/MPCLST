import sys
import os
import json
import pickle
import argparse
import csv
import cv2
import json

parser = argparse.ArgumentParser()

parser.add_argument('--pkl_dir', default='./Dataset03/choose_frames_middle/',type=str, help="label_dir")
parser.add_argument('--csv_dir', default='./Dataset03/train_personID.csv',type=str, help="label_dir")

arg = parser.parse_args()

train_personID = []
with open(arg.csv_dir, 'r') as f:
    reader = csv.reader(f)
    temp_key = ''
    for row in reader:
        train_personID.append(row)
print("len(train_personID):",len(train_personID))
count1 = 0
new_json = {}
for root, dirs, files in os.walk(arg.pkl_dir, topdown=False):
    for name in files:
        if '_proposal_s.json' in name and 'checkpoint' not in name:
            json_path = os.path.join(root, name)
            with open(json_path,'r',encoding='utf8')as fp:
                json_data = json.load(fp)
                new_json = json_data
                for image_data in json_data['metadata']:
                    fileID = image_data.split("_")[0].split('image')[-1]
                    fname = json_data['file'][fileID]['fname']
                    
                    imgDir = os.path.join(root, fname)
                    img = cv2.imread(imgDir)  #读取图片信息
                    #sp = img.shape[0:2]     #截取长宽啊
                    sp = img.shape #[高|宽|像素值由三种原色构成]
                    img_w = sp[1] #宽度
                    img_h = sp[0] #高度
                    
                    videoID = fname.split("_")[0]
                    frameID = fname.split("_")[1].split('.')[0]
                    frameID2 = int((int(frameID) - 1)/30)
                    xy = json_data['metadata'][image_data]['xy'].copy()
                    xy[1] = xy[1]/img_w
                    xy[2] = xy[2]/img_h
                    xy[3] = xy[3]/img_w + xy[1]
                    xy[4] = xy[4]/img_h + xy[2]
                    for personIdData in train_personID:
                        #同一个视频  同一帧
                        if int(videoID) == int(personIdData[0]):
                            if frameID2 == int(personIdData[1]):
                                if abs(xy[1]-float(personIdData[2]))<0.005 and abs(xy[2]-float(personIdData[3]))<0.005 and abs(xy[3]-float(personIdData[4]))<0.005 and abs(xy[4]-float(personIdData[5]))<0.005:
                                    new_image_data = image_data.split('_')[0] + '_'  + str(int(personIdData[6])+100)
                                    #print("personIdData[6]:",personIdData[6],"new_image_data:",new_image_data)
                                    new_json_string = json.dumps(new_json,ensure_ascii=False,indent=2)
                                    new_json_string_replace = new_json_string.replace('"'+image_data +'"', '"'+new_image_data+'"')
                                    new_json = json.loads(new_json_string_replace)
                                    
                                    count1 = count1 + 1
                                    break
                new_json_path = '.'+json_path.split('.')[1]+'_ID.json'
                print("new_json_path",new_json_path)
                new_json_file = open(new_json_path, 'w')
                new_json_file.write(json.dumps(new_json,ensure_ascii=False,indent=2))
                new_json_file.close()
                #input()
                    #new_json['metadata'][]
                    
print("count1:",count1)
