import cv2
import random

# Load input video
video = cv2.VideoCapture("sample.mp4")

# Get video properties
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID'
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Get frame dimensions
    height, width, _ = frame.shape

    # Random position for text
    x = random.randint(50, width - 300)
    y = random.randint(50, height - 100)

    # Add main text
    cv2.putText(
        frame,
        "Automotive Technology",
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Add bottom black bar
    cv2.rectangle(frame, (0, height - 40), (width, height), (0, 0, 0), -1)

    # Add bottom text
    cv2.putText(
        frame,
        "python assignment, version 0",
        (20, height - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # ✅ Save the frame to output video
    out.write(frame)

    # Show video
    cv2.imshow("Python Assignment - Part 0", frame)

    # Exit on ESC key
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Release everything
video.release()
out.release()
cv2.destroyAllWindows()