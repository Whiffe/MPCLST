import json
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--DatasetXX_dir', default='Dataset01',type=str, help="DatasetXX_dir")

arg = parser.parse_args()

choose_frames_middle_dir = './' + arg.DatasetXX_dir + '/choose_frames_middle'

# 通过循环与判断来找出via的json标注文件
for root, dirs, files in os.walk(choose_frames_middle_dir, topdown=False):
    for file in files:
        #via的json标注文件以_proposal.json结尾
        if "_finish.json" in file:
            jsonPath = root+'/'+file
            #读取标注文件
            with open(jsonPath, encoding='utf-8') as f:
                line = f.readline()
                viaJson = json.loads(line)
                for metadata in viaJson['metadata']:
                    #对标注文件中所有av进行修改，av就是当前选中的标注值
                    #下面的1，2，3代表3种多选，如头部、身体、四肢三个部位的行为
                    # 这里的值应动态获取，时间关系，先固定成这样
                    # 这里需要根据手动设置
                    viaJson['metadata'][metadata]["av"] = [{'1': '1','2': '5,6','3': '','4': '','5': '29','6': '34','7': '44,45,46','8': '49','9': '64','10': '71'}]
                #修改后的文件名
                newName = file.split(".")[0]+'_s'+'.json'
                
                f2 = open(root+'/'+newName, 'w')
                f2.write(json.dumps(viaJson))
                f2.close()
                
                f.close()
