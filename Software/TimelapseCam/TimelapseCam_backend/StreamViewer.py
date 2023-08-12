# 调用 OpenCV 库
import cv2

# 定义摄像头地址
camera_url = "http://192.168.31.203:81/stream"

# 创建VideoCapture对象
cap = cv2.VideoCapture(camera_url)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法连接到摄像头。请检查摄像头地址或网络连接。")
    exit()

while True:
    # 读取帧
    ret, frame = cap.read()

    # 检查帧是否成功读取
    if not ret:
        print("无法获取帧。")
        break

    # 显示预览画面
    cv2.imshow('Camera Preview', frame)

    # 按下 'q' 键退出预览
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
