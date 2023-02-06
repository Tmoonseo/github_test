import os
import cv2
import glob
import numpy as np
import pdb
from PIL import Image
import natsort

####### 신성 데모 이미지 크랍용
####### 욜로 라벨을 불러와서 이미지에 라벨부분만 crop 하는 파일
####### i = roi 개수인데 이거는 보고해야할듯

# 경로 설정 / Left/Right 따로 해야되서 경로 바꿔주면서 해야함
# root = os.getcwd()

dir_path = 'D:\\1001/test/'

side = ['left', 'right']

# roi 폴더생성 / Left : 0~15 / Right : 16~30
repeat_num_dict = {'left': 8, 'right': 11}

for si in side:
    image0_paths = glob.glob(os.path.join(dir_path, si, '*.bmp'))
    image0_paths = natsort.natsorted(image0_paths)
    txt_paths = glob.glob(os.path.join(dir_path, si + '_label', '*.txt'))
    txt_paths =natsort.natsorted(txt_paths)
    roi_nums = len(txt_paths)

    repeat_num = repeat_num_dict[si]

    for i in range(roi_nums):
        if si == 'right':
            i += 8
        if not os.path.exists(os.path.join(dir_path, si + '_crop', 'r' + str(i))):
            os.mkdir(os.path.join(dir_path, si + '_crop', 'r' + str(i)))

    for idx in range(len(image0_paths)):
        img = Image.open(image0_paths[idx])
        txt = open(txt_paths[int(idx % repeat_num)])
        line = txt.readline()
        txt.close()
        cont = line.split(' ')
        cls = cont[0]
        x1 = int(cont[1])
        y1 = int(cont[2])
        x2 = int(cont[3])
        y2 = int(cont[4][:-1])

        crop_img = img.crop((x1, y1, x2, y2))
        # crop_img.show()

        temp0 = si + '_crop'
        temp1 = 'r' + str(int(idx % repeat_num))
        if si == 'right':
            temp1 = 'r' + str(int(idx % repeat_num) + 8)
        crop_img.save(os.path.join(dir_path, temp0, temp1, image0_paths[idx].split('\\')[-1]))