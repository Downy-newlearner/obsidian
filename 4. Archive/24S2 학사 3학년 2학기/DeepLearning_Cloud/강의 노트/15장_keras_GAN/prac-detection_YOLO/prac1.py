import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import keras_cv
import keras
import cv2
import numpy as np

# Define PascalVOC classes
PASCALVOC_CLASSES = [
    "Aeroplane", "Bicycle", "Bird", "Boat", "Bottle",
    "Bus", "Car", "Cat", "Chair", "Cow",
    "Diningtable", "Dog", "Horse", "Motorbike", "Person",
    "Pottedplant", "Sheep", "Sofa", "Train", "Tvmonitor"
]

class ObjectDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Load a pretrained YOLOv8 model
        self.model = keras_cv.models.YOLOV8Detector.from_preset(
            "yolo_v8_m_pascalvoc", bounding_box_format="xywh"
        )

    def initUI(self):
        self.setWindowTitle('Object Detection with YOLOv8')
        self.setGeometry(100, 100, 1200, 600)

        # Load button
        self.load_button = QPushButton('Load', self)
        self.load_button.setGeometry(10, 10, 120, 40)
        self.load_button.clicked.connect(self.load_image)

        # Image display labels
        self.image_label_original = QLabel(self)
        self.image_label_original.setGeometry(10, 70, 580, 300)
        self.image_label_original.setStyleSheet("border: 1px solid black;")

        self.image_label_result = QLabel(self)
        self.image_label_result.setGeometry(600, 70, 580, 300)
        self.image_label_result.setStyleSheet("border: 1px solid black;")

        # Result display label
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 380, 1170, 200)
        self.result_label.setWordWrap(True)
        self.result_label.setStyleSheet("border: 1px solid black; padding: 10px;")
        self.result_label.setText("Results will be displayed here.")

    def load_image(self):
        # Open file dialog to select an image
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)

        if file_path:
            # Display original image
            pixmap = QPixmap(file_path).scaled(580, 300, aspectRatioMode=1)
            self.image_label_original.setPixmap(pixmap)

            # Run YOLOv8 model on the image
            results = self.detect_objects(file_path)

            # Display detection results
            detection_image, detections = results
            self.display_result_image(detection_image)
            self.display_detections(detections)

    def detect_objects(self, file_path):
        # Load image and preprocess
        image = keras.utils.load_img(file_path)
        image = np.array(image)

        # Resize image for inference
        inference_resizing = keras_cv.layers.Resizing(
            640, 640, pad_to_aspect_ratio=True, bounding_box_format="xywh"
        )
        image_batch = inference_resizing([image])

        # Run prediction
        predictions = self.model.predict(image_batch)

        # Extract detections
        detections = []
        for bbox_array, class_id_array, confidence_array in zip(predictions["boxes"], predictions["classes"], predictions["confidence"]):
            # bbox_array and confidence_array are 2D arrays
            for bbox, class_id, confidence in zip(bbox_array, class_id_array, confidence_array):
                # Ignore invalid bounding boxes or confidence scores
                if np.all(bbox == -1) or confidence == -1:
                    continue
                
                # Extract x, y, w, h from bbox
                x, y, w, h = bbox[:4]
                x1, y1 = int(x - w / 2), int(y - h / 2)
                x2, y2 = int(x + w / 2), int(y + h / 2)

                # Append valid detections
                detections.append(((x1, y1, x2, y2), float(confidence), class_id))

        # Draw bounding boxes on the image
        detection_image = self.draw_bounding_boxes(image, detections)
        return detection_image, detections

    def draw_bounding_boxes(self, image, detections):
        for bbox, confidence, class_id in detections:
            x1, y1, x2, y2 = bbox
            conf = round(confidence, 2)  # Confidence is already a scalar
            label_name = PASCALVOC_CLASSES[int(class_id)]  # Get class name
            text = f"{label_name} {conf}"

            # Draw bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # Put label and confidence
            cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    def display_result_image(self, detection_image):
        # Convert OpenCV image to QPixmap and display
        h, w, ch = detection_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(detection_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image).scaled(580, 300, aspectRatioMode=1)
        self.image_label_result.setPixmap(pixmap)

    def display_detections(self, detections):
        # Format detection results for display
        results_text = "Detection Results:\n"
        for bbox, confidence, class_id in detections:
            conf = round(confidence, 2)
            label_name = PASCALVOC_CLASSES[int(class_id)]
            results_text += f"Label: {label_name}, Confidence: {conf}\n"

        self.result_label.setText(results_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ObjectDetectionApp()
    main_window.show()
    sys.exit(app.exec_())
