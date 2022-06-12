# bash addDatasetXX.sh Dataset02 

#newDataset是创建新的Dataset，如：Dataset02
newDataset=$1

mkdir -p ${newDataset}
mkdir -p ${newDataset}/videos
mkdir -p ${newDataset}/video_crop
mkdir -p ${newDataset}/frames
mkdir -p ${newDataset}/choose_frames_all

touch ${newDataset}/cutVideos.txt
