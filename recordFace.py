import cv2
import numpy as np


def record(image):
    name = ""
    images = []
    images.append(cv2.imread("ye2.jpg", cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread("wang1.jpg", cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread("hjk.jpg", cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread("luimage/lu1.jpg", cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread("luimage/lu2.jpg", cv2.IMREAD_GRAYSCALE))
    labels = [1, 2, 4, 3, 3]
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
    # recognizer.train(images, np.array(labels))
    recognizer.train(images, np.array(labels))
    predict_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # 对比
    label, confidence = recognizer.predict(predict_image)
    # print("label=", label)
    # print("confidence=", confidence)
    # print("Record Successed!")
    if label == 1:
        name = "叶"
    elif label == 2:
        name = "王"
    elif label == 3:
        name = "卢"
    elif label == 4:
        name = "胡"
    return label, confidence, name

    # return recognizer,labels,images


if __name__ == "__main__":  # 主程序
    print("Recording...")
    label, confidence, name = record("luimage/lu2.jpg")
    print(label, confidence, name)
