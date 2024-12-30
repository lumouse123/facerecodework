import tkinter as tk
import configparser
import newfacefile
import main2
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk


def on_button_click(old_file_path):
     
    if len(entry.get()) == 0:
        label1.config(text="录入失败，请输入姓名")
    else:
        config = configparser.ConfigParser()
        config.read("config.ini", encoding="utf-8")
        label1.config(text=entry.get() + " 录入成功")

        keys = config.options("Images")
        # 找出最后一个数字的 key 名称
        max_key_num = 0
        for key in keys:
            num = int(key[5:])  # 'key' 后面的数字
            if num > max_key_num:
                max_key_num = num
        # 生成新的 key 和 value

        new_label_label = f"label{max_key_num + 1}"  # 新的键是原有最大数字加 1
        new__label_value = f"{max_key_num + 1}"  # 新的值可以是自定义的
        new_name_label = f"name{max_key_num + 1}"  # 新的键是原有最大数字加 1
        new_name_value = entry.get()
        new_image_label = f"image{max_key_num + 1}"  # 新的键是原有最大数字加 1
        
        new_dir = newfacefile.changefile(f"{new_image_label}.jpg",old_file_path)
        new_image_value = f"{new_dir}/image{max_key_num + 1}.jpg"

        config.set("Labels", new_label_label, new__label_value)
        with open("config.ini", "w", encoding="utf-8") as configfile:
            config.write(configfile)
        config.set("Names", new_name_label, new_name_value)
        with open("config.ini", "w", encoding="utf-8") as configfile:
            config.write(configfile)
        config.set("Images", new_image_label, new_image_value)
        with open("config.ini", "w", encoding="utf-8") as configfile:
            config.write(configfile)


def showcamerapic():
    global old_file_path 
    new_image = Image.open("images/test0.jpg")
    new_photo = ImageTk.PhotoImage(new_image)  # 转换为 tk.PhotoImage 格式

    label2.config(image=new_photo)  # type: ignore
    label2.image = new_photo  # type: ignore # 保持对图像的引用，防止被垃圾回收
    old_file_path = 'images/test0.jpg'
    print(old_file_path)
    return old_file_path

def showfilepic():
    global old_file_path 
    old_file_path = filedialog.askopenfilename()
    new_image = Image.open(old_file_path)
    new_image = new_image.resize((200, 200))
    new_photo = ImageTk.PhotoImage(new_image)  # 转换为 tk.PhotoImage 格式
    # 更新 label2 显示的新图片
    label2.config(image=new_photo)  # type: ignore
    label2.image = new_photo  # type: ignore # 保持对图像的引用，防止被垃圾回收
    print(old_file_path)
    return old_file_path

# 创建主窗口
root = tk.Tk()
root.title("新增加人脸")
root.geometry("400x600")

# 创建标签
label1 = tk.Label(root, text="输入名字")
label1.grid(row=0, column=1, padx=10, pady=10)

# 创建文本框
entry = tk.Entry(root)
entry.grid(row=1, column=1, padx=10, pady=10)

image = Image.open("images/test0.jpg")
photo = ImageTk.PhotoImage(image)  # 转换为 tk.PhotoImage 格式
# 创建标签，并将图片显示在标签上
w_box = 200
h_box = 200
label2 = tk.Label(root, image=photo, width=200, height=200)  # type: ignore
label2.grid(row=2, column=1, padx=10, pady=10)

old_file_path = 'images/test0.jpg'
print(old_file_path)
# 创建按钮，点击按钮时更新标签文本

button2 = tk.Button(root, text="打开摄像头(esc关闭)", command=main2.main2)  # 重写
button3 = tk.Button(root, text="刷新图片", command=showcamerapic)
button4 = tk.Button(root, text="本地图片",command=showfilepic )
button1 = tk.Button(root, text="录入人脸", command=lambda:on_button_click(old_file_path))
# 使用 grid() 方法进行水平排列并居中
button1.grid(row=3, column=0, padx=5, pady=10)
button2.grid(row=3, column=1, padx=5, pady=10)
button3.grid(row=3, column=2, padx=5, pady=10)
button4.grid(row=3, column=3, padx=5, pady=5)
# 配置列的权重，确保按钮水平居中
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=6)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.mainloop()
