import os
import sys
import shutil
import cv2
from PIL import Image


filedir = '/home/lym/下载/siftmatching/orb'
thisdir = '/home/lym/下载/aaa'
thumbb = '/home/lym/下载/siftmatching/thumb'

def dir(fileDir):
    photo_list = []
    for a in os.walk(fileDir):
        #print(type(a[0]))
        for b in a[2]:
            photo_path=a[0]+"/"+str(b)
            photo_list.append(photo_path)
    return photo_list


def copy_all_to_onedir(path_new):
    all_path = dir(filedir)
    for each_dir_path in all_path:
        shutil.copy(each_dir_path, path_new)

def rename():
    all_pic = dir(thisdir)
    index = 0
    for each_pic in all_pic:
        index = index+1

        (filepath,tempfilename) = os.path.split(each_pic)
        (filename,extension) = os.path.splitext(tempfilename)
        if extension=='.jpg':
            shutil.move(each_pic,filepath+'/'+"image_"+str(index).zfill(5)+'.jpg')
        elif extension=='.JPG':
            shutil.move(each_pic,filepath+'/'+"image_"+str(index).zfill(5)+'.jpg')
        else:
            os.unlink(each_pic)

def del_pic():
    all_path = dir(thumbb)
    for each in all_path:
        try:
            fp = open(each, 'rb')
            img = Image.open(fp)
        except:
            fp.close()
            print(each)
            os.remove(each)
        else:
            continue

def delgray():
    all_path = dir(thisdir)
    for each in all_path:
        print(each)
        scr = cv2.imread(each)
        shape = scr.shape
        #print(shape)
        a = shape[2]
        b = shape[1]
        c = shape[0]
        #print(a)
        if a != 3 | b<100 | c < 100:
            print(each)
            os.remove(each)



def delsize():
    all_path = dir(thisdir)
    for each in all_path:
        a=os.path.getsize(each)
        if a<1000:
            print(each)
            os.remove(each)


#a1067 = cv2.imread('/home/lym/1067.jpg')
#print(a1067.shape)
#cv2.imshow(a1067)

'''
path = '/home/lym/aaa/test.jpg'
(filepath,tempfilename) = os.path.split(path)
(filename,extension) = os.path.splitext(tempfilename)try:
                        fp = open(os.path.join(parent, filename), 'rb')
                        img = Image.open(fp)
                    except:
                        fp.close()
                        os.remove(os.path.join(parent, filename))
                    else:
                        continue
print(tempfilename,filepath,extension)
'''

#photo_path = print(dir(filedir))
#copy_all_to_onedir(thisdir)
#delgray()
#del_pic()
#delsize()





