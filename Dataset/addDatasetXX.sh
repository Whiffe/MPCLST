# bash addDatasetXX.sh Dataset02 

#newDataset是创建新的Dataset，如：Dataset02
newDataset=$1

mkdir -p ${newDataset}

touch ${newDataset}/cutVideos.txt
