import cv2

try:
    img = cv2.imread("lenna.png")

    height, width = img.shape[0:2]

    starRow = int(height * .15)
    starCol = int(width * .15)
    endRow = int(height * .85)
    endCol = int(width * .85)

    croppedImage = img[starRow:endRow, starCol:endCol]
    cv2.imshow('Original Image', img)
    cv2.imshow('Cropped Image', croppedImage)
    cv2.waitKey(0)

finally:
    cv2.destroyAllWindows()
