import cv2
import os
from multiprocessing import Pool

videos_src_path = '../../datasets/HDR/test/SDR_540p'
videos_save_path = '../../datasets/HDR/test/sequences_540k'

def read_image_worker(each_video):
    # print(each_video)
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '/' + each_video_name)
    # exit(0)
    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
    each_video_full_path = os.path.join(videos_src_path, each_video)
    print(each_video_full_path)
    cap = cv2.VideoCapture(each_video_full_path)
    print(cap, cap.isOpened())
    frame_count = 0
    # exit(0)
    while (1):
        print(frame_count)
        success, frame = cap.read()
        if not success:
            break
        cv2.imwrite(each_video_save_full_path + "%08d.png" % frame_count, frame)
        frame_count += 1
    cap.release()


# videos = os.listdir(videos_src_path)
# count = 0

n_thread = 10
pool = Pool(n_thread)

videos = os.listdir(videos_src_path)
# videos = [videos_src_path]
count = 0
print(videos)
for each_video in videos:
    print(count, each_video)
    # exit(0)
    count+=1
    pool.apply_async(read_image_worker, args=(each_video,))

# read_image_worker('15420198.mp4')

pool.close()
pool.join()
    # exit(0)
