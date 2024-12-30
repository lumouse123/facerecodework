import  cv2

def facedetect(windowname,camera_id):
#命名和打开摄像头
    cv2.namedWindow(windowname) # 创建一个已windowname为名字的窗口
    cap=cv2.VideoCapture(camera_id) # camera_id为设备摄像头的id，默认是0，如果有usb摄像头可能会变为1
    classfier=cv2.CascadeClassifier('E:/conda/envs/py310/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml') 
    # 加载分类器，分类器位置可以自行更改，注意这里用opencv库文件夹下的绝对路径也不行，在库文件夹里找到这个文件复制到这个程序的同目录下，参考：https://blog.csdn.net/GAN_player/article/details/77993872

    color=(0,225,0)#人脸框的颜色，采用rgb模型，这里表示g取255，为绿色框
    while cap.isOpened():
        ok,frame=cap.read() # 读取一帧数据，ok表示摄像头读取状态，frame表示摄像头读取的图像矩阵mat类型
        if not ok:
            break
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#图像灰度化，cv2.cvtColor(input_image, flag) where flag determines the type of conversion.
         # detectMultiScale完成人脸探测工作，returns the positions of detected faces as Rect(x,y,w,h)，x、y是左上角起始坐标，h、w是高和宽
        # grey是要识别的图像数据，scaleFactor图像缩放比例，minSize为需要检测的有效点数
        faceRects=classfier.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32)) 

        if len(faceRects)>0:#大于0则检测到人脸     
            for faceRect in faceRects:# 可能检测到多个人脸，用for循环单独框出每一张人脸
                x,y,w,h=faceRect#获取框的左上的坐标，框的长宽
                
                
                # cv2.rectangle()完成画框的工作，外扩了10个像素
                # cv2.rectangle()函数,颜色，粗细程度。
                cv2.rectangle(frame,(x-10,y-10),(x+w-10,y+h-10),color,2)

        cv2.imshow(windowname,frame) # 显示图像

        c=cv2.waitKey(10)
        if c&0xFF==ord('q'): # 退出条件
            break

    cap.release()#释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':#主程序
    print ('face detecting... ')
    facedetect('facedetect',0)

