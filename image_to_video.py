import cv2
import os

def create_video_from_png(png_folder, output_path, fps=30):
    # 获取所有 PNG 图片的路径
    png_files = sorted([os.path.join(png_folder, file) for file in os.listdir(png_folder) if file.endswith('.png')])

    # 读取第一张 PNG 图片，获取图像尺寸
    img = cv2.imread(png_files[0])
    height, width, _ = img.shape

    # 创建视频编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 逐帧写入视频
    for index,png_file in enumerate(png_files) :
        print('index = ', index)
        img = cv2.imread(png_file)
        video_writer.write(img)

    # 释放资源
    video_writer.release()

# 指定 PNG 图片所在的文件夹路径、输出视频的路径和帧率
png_folder = '/mmsegmentation/outputs/vis'
output_path = '/mmsegmentation/outputs/output_video.mp4'
video_fps = 10  # 修改为你想要的帧率

# 调用函数创建视频
print('\n~ ~ ~ ~ ~ ~ ~ ~ ~Start ~ ~ ~ ~ ~ ~ ~ ~ ~')
create_video_from_png(png_folder, output_path, fps=video_fps)

print('~ ~ ~ ~ ~ ~ ~ ~ ~Finish ~ ~ ~ ~ ~ ~ ~ ~ ~')