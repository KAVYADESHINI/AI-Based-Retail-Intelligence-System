import cv2
from ultralytics import YOLO
import supervision as sv
import time
import tempfile
import os

model = YOLO("yolov8n.pt")

tracker = sv.ByteTrack()

# Separate annotators (important!)
box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()


def process_video(uploaded_video):
    """
    uploaded_video → file object (from Streamlit file_uploader)
    """

    # ✅ Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_video.read())
        temp_video_path = temp_file.name

    cap = cv2.VideoCapture(temp_video_path)

    id_entry_time = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO inference
        results = model(frame)[0]

        # Convert to supervision detections
        detections = sv.Detections.from_ultralytics(results)

        # Filter only persons (class_id = 0)
        if len(detections) > 0:
            detections = detections[detections.class_id == 0]

            # Tracking
            detections = tracker.update_with_detections(detections)

            # Store entry time
            for tracker_id in detections.tracker_id:
                if tracker_id is not None and tracker_id not in id_entry_time:
                    id_entry_time[tracker_id] = time.time()

            # Create labels safely
            labels = [
                f"ID {tracker_id}"
                if tracker_id is not None else ""
                for tracker_id in detections.tracker_id
            ]

            # Draw boxes
            frame = box_annotator.annotate(
                scene=frame,
                detections=detections
            )

            # Draw labels separately (IMPORTANT FIX)
            frame = label_annotator.annotate(
                scene=frame,
                detections=detections,
                labels=labels
            )

        cv2.imshow("Retail AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Delete temp file
    os.remove(temp_video_path)

    return id_entry_time
