import tkinter as tk

root = tk.Tk()
root.title("水平居中排列按钮")

# 创建按钮
button1 = tk.Button(root, text="按钮 1")
button2 = tk.Button(root, text="按钮 2")
button3 = tk.Button(root, text="按钮 3")

# 使用 grid() 方法进行水平排列并居中
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)

# 配置列的权重，确保按钮水平居中
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
