import sys
import cv2

img = cv2.imread("./assets/cat.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

cv2.imshow("이미지 뷰어", img)
cv2.waitKey()
cv2.destroyAllWindows()
