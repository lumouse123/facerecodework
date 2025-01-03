import tkinter as tk


from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import sys, os

currentDir = os.path.dirname(os.path.abspath(__file__))
upper_dir = os.path.dirname(currentDir)
sys.path.append(upper_dir)

import configparser
import newfacefile
import main2


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

def on_button_click(old_file_path):
     
    if len(entry_1.get("1.0", "end-1c")) == 0:
        
        # 插入新内容
        canvas.itemconfig(text2, text="请输入有效的姓名")
    else:
        config = configparser.ConfigParser()
        config.read("config.ini", encoding="utf-8")
        text2=canvas.delete("all")
        text2=canvas.create_text(
            120.0,
            60.0,
            anchor="nw",
            text="成功",
            fill="#D30F0F",
            font=("Inter", 20 * -1)
            
        )

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
    label2.image = ne w_photo  # type: ignore # 保持对图像的引用，防止被垃圾回收
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


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Users/Dell/Desktop/gui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

image = Image.open("images/test0.jpg")
photo = ImageTk.PhotoImage(image)  # 转换为 tk.PhotoImage 格式
old_file_path = 'images/test0.jpg'
print(old_file_path)

window.geometry("413x604")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 604,
    width = 413,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    413.0,
    604.0,
    fill="#E3E3E3",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    206.0,
    237.0,
    image=photo
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    273.0,
    39.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=197.0,
    y=27.0,
    width=152.0,
    height=23.0
)

text1=canvas.create_text(
    49.0,
    27.0,
    anchor="nw",
    text="输入你的名字",
    fill="#000000",
    font=("Inter", 20 * -1)
)
text2=canvas.create_text(
    120.0,
    60.0,
    anchor="nw",
    text=" ",
    fill="#D30F0F",
    font=("Inter", 20 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))#打开摄像头
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=main2.main2,
    relief="flat"
)
button_1.place(
    x=44.0,
    y=437.0,
    width=157.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))#刷新图片
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=showcamerapic,
    relief="flat"
)
button_2.place(
    x=206.0,
    y=437.0,
    width=157.0,
    height=48.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))#录入人脸
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(old_file_path),
    relief="flat"
)
button_3.place(
    x=206.0,
    y=495.0,
    width=157.0,
    height=48.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))#本地照片
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: showfilepic,
    relief="flat"
)
button_4.place(
    x=44.0,
    y=495.0,
    width=157.0,
    height=48.0
)

window.resizable(False, False)
window.mainloop()