import os
import random

# 定义文件夹路径
image_dir = '/home/maojianzeng/Play_phone_detection/YOLOv8-main/helmet_dataset/images'
label_dir = '/home/maojianzeng/Play_phone_detection/YOLOv8-main/helmet_dataset/labels'

# 获取所有图片文件名
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png') or f.endswith('.jpg')]

# 打乱文件列表
random.shuffle(image_files)

# 计算训练集和验证集的数量
total_images = len(image_files)
print(total_images)
train_size = int(total_images * 0.8)
val_size = total_images - train_size

# 划分训练集和验证集
train_images = image_files[:train_size]
val_images = image_files[train_size:]

# 生成train.txt和val.txt
with open('/home/maojianzeng/Play_phone_detection/YOLOv8-main/train.txt', 'w') as f:
    for image in train_images:
        f.write("{}\n".format(os.path.join(image_dir,image)))

with open('/home/maojianzeng/Play_phone_detection/YOLOv8-main/val.txt', 'w') as f:
    for image in val_images:
        f.write("{}\n".format(os.path.join(image_dir,image)))

print(f"生成了 {train_size} 个训练集样本和 {val_size} 个验证集样本。")
