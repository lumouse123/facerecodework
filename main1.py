import time
import keyboard
import configrecord
import configparser
def process_frame(path):
    """处理，进行人脸检测"""
    label = None
    confidence = None
    name = None
    
    image = "images/test0.jpg"  # 假设图像路径
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    # 调用 record 函数，传入图像路径和配置
    label, confidence, name = configrecord.record(image, config)

    if confidence <= 80: # type: ignore
        print("Record Successed!")
        print("label=", label)
        print("name=", name)
        print("confidence=", confidence)
        print("-------------------------------")
    else:
        print("confidence=", confidence)
        print("Unkonw Face")
        print("-------------------------------")


def main1():
    path = "images"
    # 获取目录中的所有文件
    while 1:
        # 处理当前帧并更新 num
        start_time = time.time()
        process_frame(path)
        while time.time() - start_time < 4:  # 休眠2s，期间检测按键
            if keyboard.is_pressed("esc"):
                break
        time.sleep(0.01)
        # 如果按下 'Esc' 键退出
        if keyboard.is_pressed("esc"):
            print("程序退出")
            # try:
            #     for filename in os.listdir(path):
            #         file_path = os.path.join(path, filename)
                    # if os.path.isfile(file_path):  # 确保是文件而不是子目录
                    #     os.remove(file_path)  # 删除文件
            # except FileNotFoundError:
                # break
            break
    print("Finished.")

if __name__ == "__main__":
    main1()
