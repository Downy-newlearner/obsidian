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
    for bbox, class_id, confidence in zip(predictions["boxes"], predictions["classes"], predictions["confidence"]):
        bbox = bbox[:4]  # Ensure only the first 4 values (x, y, w, h) are used
        x, y, w, h = bbox
        x1, y1 = int(x - w / 2), int(y - h / 2)
        x2, y2 = int(x + w / 2), int(y + h / 2)
        detections.append(((x1, y1, x2, y2), confidence, class_id))

    # Draw bounding boxes on the image
    detection_image = self.draw_bounding_boxes(image, detections)
    return detection_image, detections
