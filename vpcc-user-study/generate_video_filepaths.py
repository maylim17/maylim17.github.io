import os
import glob

video_folders = ['videos/blackbg/test', 'videos/greybg/test']

for folder in video_folders:
    pathlist = glob.glob(folder + '/*.mp4')
    print()
    print(pathlist)

