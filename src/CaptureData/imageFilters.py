import cv2
class imageFilters:
    def __init__(self):
        pass

    def normal(self, image):
        return image
    
    def gray(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def cartoon(self, image):
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grey = cv2.medianBlur(grey, 5)
        edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 15)

        #cartoonize
        color = cv2.bilateralFilter(image, 9, 250, 250)
        image = cv2.bitwise_and(color, color, mask=edges)
        return image
    
    def pixel(self, image):
        height, width = image.shape[:2]
        w, h = (50, 50)
        temp = cv2.resize(image, (w, h))
        return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    
    def taupe(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
    
