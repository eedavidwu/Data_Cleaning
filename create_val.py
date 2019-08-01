import os
from os import listdir, getcwd
from os.path import join

wd = getcwd()
#For validation images path:
val_folder_path = os.path.join(wd,'images')
val_file_list = os.listdir(val_folder_path)
num=len(val_file_list)
print ('Val:'+str(num))
val_path = open('Val_Path.txt', 'w')

for file_obj in val_file_list:
    file_path = os.path.join(val_folder_path, file_obj)
    print(file_path)
    val_path.write(file_path + '\n')
val_path.close()

'''
#For train images path:
train_folder_path=os.path.join(wd,'images')
train_file_list = os.listdir(train_folder_path)
num=len(train_file_list)
print ('Train:'+str(num))
train_path = open('Train_Path.txt', 'w')

for file_obj in train_file_list:
    file_path = os.path.join(train_folder_path, file_obj)
    print(file_path)
    train_path.write(file_path + '\n')
train_path.close()
'''
