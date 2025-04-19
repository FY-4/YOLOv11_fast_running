import os


def rename_files_in_directory(directory, increment):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为图片文件（这里假设图片文件以 .jpg 结尾）
        if filename.endswith('.jpg'):
            # 分离文件名和扩展名
            name, ext = os.path.splitext(filename)

            # 检查文件名是否以 'photo_' 开头并且后面跟着数字
            if name.startswith('photo_'):
                try:
                    # 提取数字部分
                    number = int(name[len('photo_'):])
                    # 增加指定的数字
                    new_number = number + increment
                    # 构造新的文件名
                    new_filename = f'photo_{new_number}{ext}'
                    # 构造完整的旧文件路径和新文件路径
                    old_file_path = os.path.join(directory, filename)
                    new_file_path = os.path.join(directory, new_filename)
                    # 重命名文件
                    os.rename(old_file_path, new_file_path)
                    print(f'Renamed: {filename} to {new_filename}')
                except ValueError:
                    print(f'Skipping file {filename}: Invalid number format')


# 使用示例
directory_path = 'F:\YOLO\垃圾分类\有害垃圾\药丸\photos'  # 替换为你的目录路径
increment_value = 819
rename_files_in_directory(directory_path, increment_value)
