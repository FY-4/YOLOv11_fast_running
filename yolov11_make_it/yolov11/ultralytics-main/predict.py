import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('F:\YOLO\yolov11_make_it\yolov11\\ultralytics-main\\best.pt')
    model.predict(source='0',
                  imgsz=640,
                  device='0',

                  )

