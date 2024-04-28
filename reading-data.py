from imutils import paths
import cv2

trainingpaths = list(paths.list_images("C:\Work\Hackathons\HackDavis24\fetal-head-ultrasound-DatasetNinja\train"))
testpaths = list(paths.list_images("C:\Work\Hackathons\HackDavis24\fetal-head-ultrasound-DatasetNinja\test"))

for trainingpath in trainingpaths:
    image = cv2.imread(trainingpath)
    cv2.imshow("Frame", image)
    cv2.waitKey()

cv2.destroyAllWindows()
