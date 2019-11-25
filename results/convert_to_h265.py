
# coding: utf-8
import sys, os
import threading
from multiprocessing import Pool

def convert_to_h265(item, ffmpeg_exec="ffmpeg"):
    ffmpeg = '{ffmpeg} -r 24000/1001 -i ../datasets/HDR/test/test_128_wTSA/HDR/{listfile}/%08d.png -pix_fmt yuv422p -vcodec libx265 -crf 6 ../datasets/HDR/test/test_128_wTSA/video/{outfile}.mp4 -y'.format(ffmpeg=ffmpeg_exec,
                                                                                    listfile=item,
                                                                                    infile=item,
                                                                                    outfile=item)
    f = os.popen(ffmpeg)
    ffmpegresult = f.readline()
    

rootdir = '../datasets/HDR/test/test_128_wTSA/HDR/'
all_dir_list = os.listdir(rootdir)

n_thread = 50
pool = Pool(n_thread)

for item in all_dir_list:
    pool.apply_async(convert_to_h265, args=(item,))

pool.close()
pool.join()
