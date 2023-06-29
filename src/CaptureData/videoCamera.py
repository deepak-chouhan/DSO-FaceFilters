import cv2
import threading
from . import imageFilters

class VideoCamera(imageFilters.imageFilters):
    def __init__(self):
        super().__init__()
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        self.filter = "normal"

    def __del__(self):
        self.video.release()

    def getFrame(self):
        image = self.frame
        image = cv2.flip(image, 1)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    def setFilter(self, filter):
        self.filter = filter
        print(f"New Filter: {filter}")
        print(f"Assigned Filter: {self.filter}")
        return self.filter

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            self.frame = self.addFilter(self.frame)
    
    def addFilter(self, image):
        if self.filter == "normal":
            return self.normal(image)
        if self.filter == "gray":
            return self.gray(image)
        if self.filter == "cartoon":
            return self.cartoon(image)
        if self.filter == "pixel":
            return self.pixel(image)

