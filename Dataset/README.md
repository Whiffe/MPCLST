
## addDatasetXX.sh
addDatasetXX.sh的作用是创建DatasetXX，及DatasetXX下面的文件夹和文件<br>
每一个新添加的DatasetXX，代表新增的视频，也即后续视频的标注<br>
最后将所有的DatasetXX的视频、裁剪视频、抽帧、标注文件拼在一起<br>

## cutVideos.sh
cutVideos.sh的作用是将DatasetXX/videos文件夹下的视频按照DatasetXX/cutVideos.txt的内容裁剪位多个15秒的视频，并将裁剪的视频放在DatasetXX/video_crop文件夹下。
## cutVideos.txt
cutVideos.txt中存储了视频名及视频裁剪的起始点，如：10002.mp4 1340 2165 2710 2746，代表视频10002.mp4从第1340秒、第2165秒、第2710秒、第2746秒开始裁剪，裁剪长度为15秒，裁剪长度为15秒。
