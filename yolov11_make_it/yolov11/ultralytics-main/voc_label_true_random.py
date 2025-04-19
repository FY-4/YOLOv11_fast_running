import shutil
import os
import random

# 原始路径
image_original_path = "data/images/"
label_original_path = "data/Annotations/"

cur_path = os.getcwd()
# cur_path = 'D:/image_denoising_test/denoise/'
# 训练集路径
train_image_path = os.path.join(cur_path, "datasets/images/train/")
train_label_path = os.path.join(cur_path, "datasets/labels/train/")

# 验证集路径
val_image_path = os.path.join(cur_path, "datasets/images/val/")
val_label_path = os.path.join(cur_path, "datasets/labels/val/")

# 测试集路径
test_image_path = os.path.join(cur_path, "datasets/images/test/")
test_label_path = os.path.join(cur_path, "datasets/labels/test/")

# 训练集目录
list_train = os.path.join(cur_path, "datasets/train.txt")
list_val = os.path.join(cur_path, "datasets/val.txt")
list_test = os.path.join(cur_path, "datasets/test.txt")

train_percent = 0.8
val_percent = 0.1
test_percent = 0.1


def del_file(path):
    for i in os.listdir(path):
        file_data = path + "\\" + i
        os.remove(file_data)


def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    else:
        del_file(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)
    else:
        del_file(train_label_path)

    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path)
    else:
        del_file(val_image_path)
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path)
    else:
        del_file(val_label_path)

    if not os.path.exists(test_image_path):
        os.makedirs(test_image_path)
    else:
        del_file(test_image_path)
    if not os.path.exists(test_label_path):
        os.makedirs(test_label_path)
    else:
        del_file(test_label_path)


def clearfile():
    if os.path.exists(list_train):
        os.remove(list_train)
    if os.path.exists(list_val):
        os.remove(list_val)
    if os.path.exists(list_test):
        os.remove(list_test)


def main():
    mkdir()
    clearfile()

    file_train = open(list_train, 'w')
    file_val = open(list_val, 'w')
    file_test = open(list_test, 'w')

    total_txt = os.listdir(label_original_path)
    num_txt = len(total_txt)

    # 新增：随机打乱文件顺序
    random.shuffle(total_txt)  # 关键修改点

    # 计算精确划分数量
    train_count = int(num_txt * train_percent)
    val_count = int(num_txt * val_percent)
    test_count = num_txt - train_count - val_count  # 确保总数正确

    # 分配文件
    for i, filename in enumerate(total_txt):
        name = filename[:-4]
        srcImage = os.path.join(image_original_path, name + '.jpg')
        srcLabel = os.path.join(label_original_path, filename)

        if i < train_count:
            dest_path_img = train_image_path
            dest_path_lbl = train_label_path
            file_train.write(os.path.join(dest_path_img, name + '.jpg') + '\n')
        elif i < train_count + val_count:
            dest_path_img = val_image_path
            dest_path_lbl = val_label_path
            file_val.write(os.path.join(dest_path_img, name + '.jpg') + '\n')
        else:
            dest_path_img = test_image_path
            dest_path_lbl = test_label_path
            file_test.write(os.path.join(dest_path_img, name + '.jpg') + '\n')

        # 复制文件
        shutil.copy(srcImage, os.path.join(dest_path_img, name + '.jpg'))
        shutil.copy(srcLabel, os.path.join(dest_path_lbl, filename))

    file_train.close()
    file_val.close()
    file_test.close()


if __name__ == "__main__":
    main()
