import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel, iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.25 * dist_transform.max(), 250, 0)

print('Number of white pixels:', np.sum(sure_fg > 220))
print('Number of black pixels:', np.sum(sure_fg < 220))

cv2.imshow('image', sure_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
