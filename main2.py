import cv2
import find_write_face
from collections import Counter  # 导入 Counter 模块


def initialize_camera():
    """初始化摄像头和分类器"""
    window_name = "window_name"
    cv2.namedWindow(window_name)  # 创建窗口
    cap = cv2.VideoCapture(0)  # 打开摄像头
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()
    classifier = cv2.CascadeClassifier(
        "haarcascade_frontalface_alt2.xml"
        #  "E:/conda/envs/py310/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"

    )  # 加载分类器
    return cap, classifier, window_name


def process_frame(frame, classifier, num, max_num, color):
    """处理每一帧，进行人脸检测和图像保存"""
    num = find_write_face.getjpg(max_num, num, color, classifier, frame)  # 捕捉人脸并更新 num
    # 当捕捉到的图像数量达到 max_num 时，录入检测到的人脸
    if num >= max_num:
        num = 0  # 重置为 0，准备下一轮捕捉
    return num


def main2():
    print("按esc关闭")
    cap, classifier, window_name = initialize_camera()
    color = (0, 255, 0)  # 人脸矩形框的颜色
    num = 0  # 记录存储的图片数量
    max_num = 5  # 每次捕捉5张图片

    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            print("Error: Failed to capture image.")
            break
        # 处理当前帧并更新 num
        num = process_frame(frame, classifier, num, max_num, color)

        # 只在每个循环周期结束后显示捕捉到的帧
        cv2.imshow(window_name, frame)
        
        c = cv2.waitKey(10)  # 等待 10ms
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:#如果窗口被关闭
            break
        # 等待按键处理：如果按下 'Esc' 键退出
        if c & 0xFF == 27:  # 按下 'Esc' 键退出
            break

    cap.release()  # 释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()
    print("Finished.")


if __name__ == "__main__":
    main2()
