import cv2
import numpy as np
import time
import os

nframes = 500  # 拍摄多少张照片
interval = 0.00001  # 间隔时间（秒）

# 需要改为你的 ESP32 的 IP 地址
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("延时相机启动")
for i in range(nframes):
    # 捕获图像帧
    ret, img = cap.read()
    # 保存图像文件
    if img is None:
        print("无法获取图像")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # 等待一段时间
    time.sleep(interval)
    print("照片编号：", i)

# 定义照片文件夹路径
photos_path = "temp_destination/photos/"
# 如果文件夹不存在，则创建文件夹
os.makedirs(photos_path, exist_ok=True)
# 获取照片文件名列表
photos = os.listdir(photos_path)
# 按名称对照片进行排序
photos.sort()
# 创建视频写入对象
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# 遍历照片
for photo in photos:
    # 读取照片作为图像
    image = cv2.imread(photos_path + photo)
    # 调整图像大小以适应视频帧大小
    image = cv2.resize(image, (1280, 720))
    # 将图像写入视频
    video.write(image)

# 释放视频写入对象
video.release()
print("延时摄影视频生成完成")
