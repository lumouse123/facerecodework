import cv2
def close(cap):
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
    cap.release()#释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()
    print('Finished.')