import cv2
import threading
from . import imageFilters

class VideoCamera(imageFilters.imageFilters):
    def __init__(self):
        super().__init__()
        self.video = cv2.VideoCapture(0)
        self.filter = "normal"
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def getFrame(self):
        image = self.frame
        image = cv2.flip(image, 1)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    def setFilter(self, filter):
        self.filter = filter
        return self.filter

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            self.frame = self.addFilter(self.frame)
    
    def addFilter(self, image):
        filters = {
            "normal": self.normal,
            "gray": self.gray,
            "cartoon": self.cartoon,
            "pixel": self.pixel,
            "taupe": self.taupe
        }
        return filters.get(self.filter, self.pixel)(image)

