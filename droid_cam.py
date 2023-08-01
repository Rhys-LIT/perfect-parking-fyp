"""Open CV."""
from cv2 import destroyAllWindows, imshow, INTER_CUBIC, Mat, resize, VideoCapture, waitKey

print("Download and install DroidCam on your phone from the App Store.")
print("https://apps.apple.com/ie/app/droidcam-webcam-obs-camera/id1510258102")
print("https://play.google.com/store/apps/details?id=com.dev47apps.droidcam")
print("You should see a URL with the IP address of your phone and port 4747 displayed on your screen.")

image_dimensions:tuple = (480, 640)

zoom_factor:float = 1

display_dimensions:tuple = (int(image_dimensions[0] * zoom_factor),
                                      int(image_dimensions[1] * zoom_factor))


url:str = 'http://192.168.188.64:4747/video' # YOUR IP ADDRESS MAY BE DIFFERENT
video_capture:VideoCapture = VideoCapture(url)
window_name:str = "DroidCam"


while True:
    is_open:bool = False
    video_frame:Mat = None
    is_open, video_frame = video_capture.read()

    if not is_open:
        print("Unable to open camera")
        break

    display_video_frame:Mat = resize(video_frame, display_dimensions, interpolation = INTER_CUBIC)
    imshow(window_name, display_video_frame)

    if waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
destroyAllWindows()
