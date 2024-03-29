import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('tets.jpg')
H_rows, W_cols= img.shape[:2]
print(H_rows, W_cols)

# 原图中书本的四个角点(左上、右上、左下、右下),与变换后矩阵位置
pts1 = np.float32([[350, 360], [538, 360], [20, 512], [880, 512]])
pts2 = np.float32([[346, 8],[527,8],[348, 535],[526,535]])

# 生成透视变换矩阵；进行透视变换
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (900,800))

cv2.imshow("original_img",img)
cv2.imshow("result",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()