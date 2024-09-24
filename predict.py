import cv2
from ultralytics import YOLO

# 加载模型
model = YOLO(model="airplane.pt")

# 摄像头编号
camera_nu = 0

# 打开摄像头
cap = cv2.VideoCapture(camera_nu)

# 设置窗口大小
cv2.namedWindow("YOLOV8", cv2.WINDOW_NORMAL)  # 创建一个可调整大小的窗口
cv2.resizeWindow("YOLOV8", 800, 600)  # 设置窗口大小为800x600像素

while cap.isOpened():
    # 获取图像
    res, frame = cap.read()
    # 如果读取成功
    if res:
        # 正向推理
        results = model(frame)
        # 绘制结果
        annotated_frame = results[0].plot()
        # 显示图像
        cv2.imshow(winname="YOLOV8", mat=annotated_frame)
        # 按ESC退出
        if cv2.waitKey(1) == 27:
            break
# 释放连接
cap.release()
cv2.destroyAllWindows()
