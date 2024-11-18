# coding=utf-8

# 将Windows的屏幕截图重命名成时间
# v1.0 zyyme 20241029

import os, datetime

# 切换到脚本所在的目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

listdir = os.listdir('.')

names = {i:1 for i in listdir}
for file_path in listdir:
    if os.path.isfile(file_path) and file_path.startswith('屏幕截图('):
        # 获取文件的  ctime创建时间 修改时间mtime
        modified_time = os.path.getmtime(file_path)
        modified_time_obj = datetime.datetime.fromtimestamp(modified_time)
        # 格式化修改时间为字符串
        modified_time_str = modified_time_obj.strftime("%Y-%m-%d_%H-%M-%S")
        # 获取原始文件名和扩展名
        basename = os.path.basename(file_path)
        name, ext = os.path.splitext(basename)
        # 新的文件名
        new_name = f"{modified_time_str}{ext}"
        if new_name in names.keys():
            names[new_name] += 1
            new_name = f"{modified_time_str}_{names[new_name]}{ext}"
        # 重命名文件
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        print(basename, '->', new_name)
        os.rename(file_path, new_path)