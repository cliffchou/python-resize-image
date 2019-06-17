import os
import shutil

import PIL
from PIL import Image


def change_image_channel(image, image_path):
     #4通道转3通道
    if image.mode == 'RGBA':
         r, g, b, a = image.split()
         image = Image.merge("RGB", (r, g, b))
         image.save(image_path)
     #1通道转3通道
    elif image.mode != 'RGB':
         image = image.convert("RGB")
         os.remove(image_path)
         image.save(image_path)
    return image

#通道转换(单张图片)，入参是单张图片路径
def change_image_single_channel(image_path):
    with open(image_path, 'r+b') as f:
        with Image.open(f) as image:
            change_image_channel(image, image_path)

#通道转换(批量)，入参是所有图片所在目录
def change_image_channels(path_read, path_save):
    #校验输入路径是否存在
    if(not os.path.isdir(path_read)):
        raise RuntimeError('path_read not exists')
    if(os.path.isdir(path_save)):
        print("path_save exists")
    else:
        os.makedirs(path_save)

    for filename in os.listdir(path_read):
        filename_read = path_read + filename
        filename_save = path_save + filename
        with open(filename_read, 'r+b') as f:
            with Image.open(f) as image:
                change_image_channel(image, filename_save)

#图片压缩
def image_compression(image, image_path):
    w, h = image.size
    print(w, h)
    image.thumbnail((int(w / 1.1), int(h / 1.1)))
    image.save(image_path)
    return image

#批量检查文件下的通道数，如果存在不为3的情况则返回false
def image_channel_3(path):
    for filename in os.listdir(path):
        filename_path = path + filename
        with open(filename_path, 'r+b') as f:
            with Image.open(f) as image:
                if(image != 'RGB'):
                    return False
    return True