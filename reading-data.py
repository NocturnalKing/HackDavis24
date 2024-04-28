from imutils import paths
#from CVPregnancy import *
from ShapeDetector import *
import cv2
import ShapeDetector

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

trainingDataCarousel()

for trainingFilePath in trainingpaths:
    image = cv2.imread(trainingFilePath)
    gsblur(image)


test = ShapeDetector()