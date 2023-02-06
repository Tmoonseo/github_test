import os
import cv2
import glob
import numpy as np
import pdb
import math

def UpsacaleAndxywh2xyxy4txt(txt_dir_old, txt_dir_new):
    txt_list = glob.glob(os.path.join(txt_dir_old, '*.txt'))

    for txt in txt_list:
        f = open(os.path.join(txt_dir_old, txt), 'r')
        line = f.readline()
        label = line.split(' ')[0]
        label_n = int(label) + 8
        # x_c = float(line.split(' ')[1]) * 800
        # y_c = float(line.split(' ')[2]) * 600
        # w_c_h = float(line.split(' ')[3]) * 400
        # h_c_h = float(line.split(' ')[4][:-1]) * 300
        # x1 = str(int(x_c - w_c_h))
        # y1 = str(int(y_c - h_c_h))
        # x2 = str(math.ceil(x_c + w_c_h))
        # y2 = str(math.ceil(y_c + h_c_h))
        f.close()
        # new_line = label + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + '\n'
        new_line = str(label_n) + line[1:]
        f_n = open(os.path.join(txt_dir_new, txt), 'w')
        f_n.write(new_line)
        f_n.close

# UpsacaleAndxywh2xyxy4txt('D:\\1001/test/right_label_', 'D:\\1001/test/right_label')
