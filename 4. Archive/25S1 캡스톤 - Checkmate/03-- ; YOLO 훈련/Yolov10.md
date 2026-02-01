**Train**
yolo task=detect mode=train epochs=50 batch=16 device=0,1,2,3 plots=True model= '/home/jdh251425/2025_DKU_Capstone/AI/yolov10/weights/yolov10m.pt' data='/home/jdh251425/2025_DKU_Capstone/AI/yolov10/data.yaml'

**Inference**
yolo task=detect mode=predict model='/home/jdh251425/2025_DKU_Capstone/AI/yolov10/runs/detect/train2/weights/best.pt' source='/home/jdh251425/2025_DKU_Capstone/AI/dataset/labels/inference' device=0

yolo task=detect mode=predict model='/home/jdh251425/2025_DKU_Capstone/AI/Algorithm/yolov10/trained_model/best.pt' source='/home/jdh251425/2025_DKU_Capstone/AI/Algorithm/yolov10/test_data' device=0


yolo task=detect mode=predict model='/home/jdh251425/2025_DKU_Capstone/AI/Algorithm/yolov10/trained_model/best.pt' source="/home/jdh251425/2025_DKU_Capstone/AI/Algorithm/OCR/prac_data_0513/signals_and_systems_example.jpeg" device=0
