import cv2

def getjpg(max_num, num, color, classifier, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度化
    faceRects = classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32)
    )

    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 捕捉到的图片的名字，这里用到了格式化字符串的输出
            image_name = (
                "C:/Users/Dell/Desktop/Before Graduation project/workspace/images/%s%d.jpg"
                % ("test", num)
            )
            # 加上扩展名,path_name为命名前缀
            image = frame[
                y : y + h, x : x + w
            ]  # 将当前帧含人脸部分保存为图片，注意这里存的还是彩色图片，前面检测时灰度化是为了降低计算量；这里访问的是从y位开始到y+h-1位
            success = cv2.imwrite(image_name, image)
            if not success:
                print("Error saving image")
            num += 1
            # 超过指定最大保存数量则退出循环
            if num >= max_num:
                return num  # 返回更新后的 num
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)  # 画出矩形框
            font = cv2.FONT_HERSHEY_SIMPLEX  # 获取内置字体
            # cv2.putText(
            #     frame, ("%d" % num), (x + 30, y + 30), font, 1, (255, 0, 255), 4
            # )  # 显示当前捕捉到多少张图片

    return num  # 返回未变化的 num


if __name__ == "__main__":  # 主程序
    window_name = "window_name"  # 窗口名称
    cv2.namedWindow(window_name)  # 创建窗口
    cap = cv2.VideoCapture(0)  # 打开摄像头
    classifier = cv2.CascadeClassifier(
        "E:/conda/envs/py310/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
    )  # 加载分类器
    color = (0, 255, 0)  # 人脸矩形框的颜色
    num = 0  # 记录存储的图片数量
    max_num = 5  # 每次捕捉5张图片

    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break

        num = getjpg(max_num, num, color, classifier, frame)  # 捕捉人脸并更新 num

        # 如果 num 达到 max_num（5），则重置 num 为 0 进入下一轮捕捉
        if num >= max_num:
            print(f"Captured {max_num} images, restarting...")
            num = 0  # 重置为 0，准备下一轮捕捉

        cv2.imshow(window_name, frame)  # 显示捕捉到的帧

        c = cv2.waitKey(10)  # 等待按键
        if c & 0xFF == ord("q"):  # 按下 'q' 键退出
            break
        elif c & 0xFF == 27:  # 按下 'Esc' 键退出
            break

    cap.release()  # 释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()  # 销毁窗口
    print("Finished.")
