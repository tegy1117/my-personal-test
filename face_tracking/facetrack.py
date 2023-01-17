import cv2
import mediapipe as mp

def overlay(image, x, y, w, h, overlay_image):# overlay_image는 4채널이미지 image는 3채널 이미지
    alpha = overlay_image[:, :, 3]
    mask_image = alpha / 255
    for i in range(0, 3):
        image[y-h:y+h, x-w:x+w, i] = (overlay_image[:, :, i] * mask_image) + (image[y-h:y+h, x-w:x+w, i] * (1-mask_image))


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
# IMAGE_FILES = []
# with mp_face_detection.FaceDetection(
#     model_selection=1, min_detection_confidence=0.5) as face_detection:
#   for idx, file in enumerate(IMAGE_FILES):
#     image = cv2.imread(file)
#     # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
#     results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     # Draw face detections of each face.
#     if not results.detections:
#       continue
#     annotated_image = image.copy()
#     for detection in results.detections:
#       print('Nose tip:')
#       print(mp_face_detection.get_key_point(
#           detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
#       mp_drawing.draw_detection(annotated_image, detection)
#     cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)

# For webcam input:
cap = cv2.VideoCapture(1)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections: #detection은 6개(우좌 눈, 코 끝, 입 중심, 우좌 이주)
        #mp_drawing.draw_detection(image, detection)
        keypoints = detection.location_data.relative_keypoints
        r_eye = keypoints[0]
        l_eye = keypoints[1]
        nose = keypoints[2]
        h, w, _ = image.shape
        print(r_eye)
        r_eye = int(r_eye.x*w), int(r_eye.y*h)
        l_eye = int(l_eye.x*w), int(l_eye.y*h)
        nose = int(nose.x*w), int(nose.y*h)
        


        cv2.circle(image, r_eye, 50 ,(255, 0, 0), 10, cv2.LINE_AA)
        cv2.circle(image, l_eye, 50 ,(0, 0, 255), 10, cv2.LINE_AA)
        cv2.circle(image, nose, 50 ,(0, 255, 255), 10, cv2.LINE_AA)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    if cv2.waitKey(5) == ord('q'):
      break
cap.release()