import os
import shutil
import unittest

from PIL import Image


class TestChangeChannels(unittest.TestCase):
    """
    Run tests for all functions
    the give image for testing is RGBA and RGB
    """

    def test_change_channels(self):
        filepath_read = "F:/tensorflow/sourcecode/cmshow/test/"
        filepath_save = "F:/tensorflow/sourcecode/cmshow/test/"
        # if (not os.path.isdir(filepath_save)):
        #     os.makedirs(filepath_save)
        # for filename in os.listdir(filepath_read):
        #     #print(filename)
        #     filename_read = filepath_read + filename
        #     filename_save = filepath_save + filename
        #     #print(filename_read)
        #     #print(filename_save)
        #     with open(filename_read, 'r+b') as f:
        #         with Image.open(f) as image:
        #             #print(image.mode)
        #             from channelchange.changechannels import change_image_channel
        #             change_image_channel(image, filename_save)
        from channelchange.changechannels import change_image_channels
        change_image_channels(filepath_read, filepath_save)

        #检查是是否存在图像通道不为3的情况
        # from channelchange.changechannels import image_channel_3
        # if(image_channel_3(filepath_save)):
        #     print("filepath_save 路径下图像全部是通道3")
        # else:
        #     print("filepath_save 路径下存在不为3的情况")

        # 将测试图像全部转化成通道3
        # with open("F:/tensorflow/sourcecode/cmshow/test/normal.937.png", 'r+b') as f:
        #     with Image.open(f) as image:
        #         print(image.mode)

        # from channelchange.changechannels import change_image_single_channel
        # change_image_single_channel("F:/tensorflow/sourcecode/cmshow/test/body.250.png")