from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolo11n.pt')  # 地址改成自己的
    model.train(data='data.yaml',
                #cache=False,
                imgsz=640,
                epochs=100,
                #single_cls=False,  # 是否是单类别检测
                batch=8,
                #close_mosaic=10,
                #workers=0,
                device='0',
                #optimizer='SGD',
                #amp=True,
                project='runs/train',
                name='exp',
                )