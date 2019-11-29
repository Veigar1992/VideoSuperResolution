import os, sys

png_path = './SDR_4K/'

video_list =  os.listdir(png_path)

for video_idx in video_list:
	curr_png_path = os.path.join(png_path, video_idx)
	png_list = os.listdir(curr_png_path)
	for i in range(1,len(png_list)+1):
		origin_idx = '{:08d}.png'.format(i)
		target_idx = '{:08d}.png'.format(i-1)
		# print(origin_idx, target_idx)
		origin_name = os.path.join(curr_png_path, origin_idx)
		target_name = os.path.join(curr_png_path, target_idx)
		os.rename(origin_name,target_name)
