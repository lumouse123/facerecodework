import os
import shutil
def changefile(new_file_name, old_file_path):
    # 定义原文件路径和目标路径
    new_dir = 'recordface'       # 目标文件夹
    # 创建目标目录（如果它不存在的话）
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    # 定义新的完整文件路径
    new_file_path = os.path.join(new_dir, new_file_name)
    # 移动并重命名文件
    shutil.copy(old_file_path, new_file_path)
    print(f"文件已从 {old_file_path} 复制并重命名为 {new_file_path}")
    return new_dir
if __name__ == "__main__":  # 主程序
    changefile("testtesttest.jpg",'images/test0.jpg')