import xml.etree.ElementTree as ET
import os


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id, classes, input_folder='data/Annotations', output_folder='data/Annotations'):
    # 打开对应的XML文件
    in_file_path = os.path.join(input_folder, f'{image_id}.xml')
    if not os.path.exists(in_file_path):
        print(f"Warning: XML file {in_file_path} does not exist.")
        return

    with open(in_file_path, encoding='UTF-8') as in_file:
        # 创建或打开对应的TXT文件准备写入
        out_file_path = os.path.join(output_folder, f'{image_id}.txt')
        with open(out_file_path, 'w') as out_file:
            # 解析XML文件
            tree = ET.parse(in_file)
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            for obj in root.iter('object'):
                # 检查对象是否在我们感兴趣的类中，以及是否被标记为困难
                difficult = obj.find('difficult')
                if difficult is None:
                    difficult = '0'
                else:
                    difficult = difficult.text

                cls = obj.find('name').text
                if cls not in classes or int(difficult) == 1:
                    continue

                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                     float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))

                # 边界框坐标修正
                b = tuple(min(max(coord, 0), dim - 1) for coord, dim in zip(b, [w, w, h, h]))

                bb = convert((w, h), b)
                out_file.write(f"{cls_id} {' '.join([f'{a:.6f}' for a in bb])}\n")


def process_all_annotations(classes, input_folder='data/Annotations', output_folder='data/Annotations'):
    # 确保输出目录存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历所有XML文件
    for xml_file in os.listdir(input_folder):
        if xml_file.endswith('.xml'):
            image_id = os.path.splitext(xml_file)[0]
            convert_annotation(image_id, classes, input_folder, output_folder)
            print(f"Converted {xml_file} to {image_id}.txt")


# 示例调用
classes = ['其他垃圾', '可回收垃圾','厨余垃圾','有害垃圾']
process_all_annotations(classes)