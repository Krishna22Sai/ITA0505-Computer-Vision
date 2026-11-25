import cv2
import pytesseract

# Set Tesseract path (change only if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_video():

    cap = cv2.VideoCapture("video-1.mp4")

    if not cap.isOpened():
        print("Error: Cannot open video")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract text from frame
        text = pytesseract.image_to_string(gray)

        if text.strip() != "":
            print("Detected Text:")
            print(text)
            print("----------------")

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


extract_text_from_video()