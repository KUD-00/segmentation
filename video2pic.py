import cv2
import os

# Set the path of the video file
video_path = "/media/dl-station/disk2/img-proc/交差点空撮.mp4"

# Set the path of the output folder to save the frames
output_folder = "./input_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file using OpenCV
video = cv2.VideoCapture(video_path)

# Get the frame rate of the video
fps = int(video.get(cv2.CAP_PROP_FPS))

# Set the number of frames to capture per second (in this case, 24)
frames_per_second = 24

# Set the frame interval based on the frame rate and desired frames per second
frame_interval = fps // frames_per_second

# Set a counter to keep track of the frames captured
frame_count = 0

# Set the time interval to capture frames (in this case, the first minute)
time_interval = fps * 60

# Loop through the video frames and extract the frames at the desired rate
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Check if it's time to stop capturing frames based on the time interval
    if frame_count >= time_interval:
        break

    # Check if it's time to capture a frame based on the frame interval
    if frame_count % frame_interval == 0:
        # Set the file name for the output frame
        filename = f"{output_folder}/frame{frame_count}.jpg"

        # Save the frame as an image
        cv2.imwrite(filename, frame)

    # Increment the frame counter
    frame_count += 1

# Release the video object
video.release()