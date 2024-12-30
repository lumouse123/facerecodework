import cv2
import numpy as np
import configparser

def record(image, config):
    name = ""
    images = []
    labels = []
    names = []

    # 读取所有配置的图像路径、标签和名称
    i = 1
    while True:
        # 尝试读取图像路径
        img_path = config.get('Images', f'image{i}', fallback=None)
        if img_path is None:  # 如果没有更多的图像路径，跳出循环
            break
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
        else:
            print(f"Error: Image {img_path} not found!")

        # 尝试读取标签
        label = config.getint('Labels', f'label{i}', fallback=None)
        if label is None:
            break
        labels.append(label)

        # 尝试读取名称
        name = config.get('Names', f'name{i}', fallback=None)
        if name is None:
            break
        names.append(name)

        i += 1

    # 确保有图像和标签进行训练
    if len(images) == 0 or len(labels) == 0:
        print("No images or labels to train on!")
        return None, None, None

    recognizer = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
    recognizer.train(images, np.array(labels))

    # 进行预测
    predict_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # 对比
    label, confidence = recognizer.predict(predict_image)

    # 根据标签找到对应的名字
    if label > 0 and label <= len(names):
        name = names[label - 1]  # 标签从 1 开始，列表索引从 0 开始

    return label, confidence, name


if __name__ == "__main__":  # 主程序
    print("Recording...")

    # 创建 ConfigParser 对象并读取配置文件，指定编码为 utf-8
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    # 调用 record 函数，传入图像路径和配置
    label, confidence, name = record("recordface/hjk.jpg", config)

    print(f"Label: {label}\nConfidence: {confidence}\nName: {name}")
