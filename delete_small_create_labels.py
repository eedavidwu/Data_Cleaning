#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys, pdb, numpy
from PIL import Image, ImageChops, ImageOps, ImageDraw
from os import listdir, getcwd
import shutil

wd=getcwd()
input_path=os.path.join(wd,'images')
in_label_path=os.path.join(wd,'labels')

output_path=os.path.join(wd,'out_images')
out_label_path=os.path.join(wd,'out_labels')


if __name__ == "__main__":
    file_name = [name for name in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, name))]

    print(len(file_name))
    count_big=0
    count_small=0


    for k in file_name:
        img_input_path = os.path.join(input_path, k)
        #label_input_path = os.path.join(in_label_path, k).replace('.jpg', '.txt')
        label='0 0'
        #print(img_input_path)
        #print(label_input_path)
        image = Image.open(img_input_path)
        
        w, h = image.size
        if w>30 and h>30:
            count_big = count_big+1
            out_label=os.path.join(out_label_path, '%s' % (k)).replace('.jpg','.txt')
            label_out_file = open(out_label, 'w')
            label_out_file.write(label)
            label_out_file.close()
            shutil.move(img_input_path,'/home/wuhaotian/image_aug/Big/')
            #shutil.move(label_input_path, '/home/wuhaotian/image_aug/out_labels/')
        else:
            count_small=count_small+1
            #shutil.move(img_input_path, '/home/wuhaotian/image_aug/Small/')
    print('big:',count_big,'small:', count_small)
    print ('Finished:\n','labels store in:',out_label_path)


