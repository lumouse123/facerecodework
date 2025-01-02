import cv2
def build():
    window_name = "window_name"
    cv2.namedWindow(window_name)  # 创建窗口
    cap = cv2.VideoCapture(0)  # 打开摄像头
    while cap.isOpened():
        ok, frame = cap.read()
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)  # 等待 10ms
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
        if c & 0xFF == 27:  # 按下 'Esc' 键退出
            break
    cap.release()  # 释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()
    print("Finished.")
    
if __name__ == "__main__":
    build()
