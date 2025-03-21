**Train**
yolo task=detect mode=train epochs=50 batch=16 device=0,1,2,3 plots=True model= '/home/jdh251425/2025_DKU_Capstone/AI/yolov10/weights/yolov10m.pt' data='/home/jdh251425/2025_DKU_Capstone/AI/yolov10/data.yaml'

**Inference**
yolo task=detect mode=predict epochs=50 batch=16 device=0,1,2,3 plots=True model= '/home/jdh251425/2025_DKU_Capstone/AI/yolov10/runs/detect/train2/weights/best.pt' data='/home/jdh251425/2025_DKU_Capstone/AI/yolov10/data.yaml'

yolo task=detect mode=predict model='/home/elicer/yolov10/runs/detect/train16/weights/best.pt' source='/home/elicer/yolov10/data/test/images/' device=0