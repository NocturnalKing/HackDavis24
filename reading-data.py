from imutils import paths
import cv2

trainingpaths = list(paths.list_images("C:\Work\Hackathons\HackDavis24\\fetal-head-ultrasound-DatasetNinja\\train\img"))
testpaths = list(paths.list_images("C:\Work\Hackathons\HackDavis24\\fetal-head-ultrasound-DatasetNinja\\test\img"))

print(trainingpaths)

def trainingDataCarousel():
    for trainingFilePath in trainingpaths:
        image = cv2.imread(trainingFilePath)
        cv2.imshow("Frame", image)
        cv2.waitKey()
    cv2.destroyAllWindows()
    
def testDataCarousel():
    for testFilePath in testpaths:
        image = cv2.imread(testFilePath)
        cv2.imshow("Frame", image)
        cv2.waitKey()
    cv2.destroyAllWindows()

class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, c):
        # initialize the shape name and approximate the contour
        shape = "undefined"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

# if the shape is a triangle, it will have 3 vertices
if len(approx) == 3:
    shape = "triangle"
# if the shape has 4 vertices, it is either a square or
# a rectangle
# bounding box to compute the aspect ratio
	(x, y, w, h) = cv2.boundingRect(approx)
	ar = w / float(h)
	# a square will have an aspect ratio that is approximately
	# equal to one, otherwise, the shape is a rectangle
	shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
	
    # if the shape is a pentagon, it will have 5 vertices
	elif len(approx) == 5:
	    shape = "pentagon"
	
    # otherwise, we assume the shape is a circle
    else:
		shape = "circle"
		# return the name of the shape
		return shape



