import os
from contextlib import contextmanager

from PIL import Image

from resizeimage import resizeimage

"""
with open('test.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [150, 150])
        cover.save('test-image-cover.jpeg', image.format)
"""


if __name__ == '__main__':

    """
    读取指定路径下的所有图片并进行resize_crop
    原始图片像素为 1080x1920
    调整之后像素为 400x1100
    注意: open()方法入参需要目标图片的绝对路径
    """

    filepath_read = "F:/tensorflow/CMshow/error_picture/test_data/"
    filepath_save = "F:/tensorflow/CMshow/error_picture/resize_crop/"
    """
    for filename in os.listdir(r"F:/tensorflow/CMshow/error_picture/test_data"):
        print(filename)  # 所有图片文件名
        filename_read = filepath_read + filename
        filename_save = filepath_save + filename
        with open(filename_read, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_crop(image, [400, 1100])
                cover.save(filename_save, image.format)
    """

    """
    补单张缺失图片
    with open("F:/tensorflow/CMshow/error_picture/test_data/abnormal.001.png", 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_crop(image, [400, 1100])
            cover.save("F:/tensorflow/CMshow/error_picture/resize_crop/abnormal.001.png", image.format)

    """

    """
    此时图片像素依旧过大()，需要单独rersize
    """
    filepath_read = "F:/tensorflow/CMshow/error_picture/resize_crop/"
    filepath_save = "F:/tensorflow/CMshow/error_picture/resize/"
    for filename in os.listdir(filepath_read):
        print(filename)  # 所有图片文件名
        filename_read = filepath_read + filename
        filename_save = filepath_save + filename
        with open(filename_read, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_contain(image, [28, 28])
                cover.save(filename_save, image.format)

