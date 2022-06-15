# bash addDatasetXX.sh Dataset02 

#newDataset是创建新的Dataset，如：Dataset02
newDataset=$1

mkdir -p ${newDataset}
mkdir -p ${newDataset}/videos
mkdir -p ${newDataset}/video_crop
mkdir -p ${newDataset}/frames
mkdir -p ${newDataset}/choose_frames_all
mkdir -p ${newDataset}/choose_frames
mkdir -p ${newDataset}/annotations
mkdir -p ${newDataset}/choose_frames_middle

touch ${newDataset}/cutVideos.txt
touch ${newDataset}/annotations/train_excluded_timestamps.csv
touch ${newDataset}/annotations/val_excluded_timestamps.csv
touch ${newDataset}/annotations/included_timestamps.txt
touch ${newDataset}/annotations/action_list.pbtxt
