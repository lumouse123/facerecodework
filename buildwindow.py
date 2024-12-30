import cv2
def open(window_name, camera_id): # path_name是图片存储目录，max_num是需要捕捉的图片数量
    cv2.namedWindow(window_name) # 创建窗口
    cap = cv2.VideoCapture(camera_id) # 打开摄像头
    return cap