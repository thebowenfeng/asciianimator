import cv2
import os
import time

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "

im_gray = cv2.imread('test3.jpg', cv2.IMREAD_GRAYSCALE)
#im_gray = cv2.bitwise_not(im_gray)
height, width = im_gray.shape

ratio = height / width
new_height = 64
new_width = int(64 * (1 / ratio))

resized = cv2.resize(im_gray, (new_width, new_height), interpolation= cv2.INTER_AREA)

#cv2.imshow("image", resized)
#cv2.waitKey(10000)
#cv2.destroyWindow("image")


ascii_img = []

for row_index, row in enumerate(resized):
    ascii_row = []
    for pix_index, pix in enumerate(row):
        avg_lum = int(pix / 255 * 66)
        ascii_row.append(gscale1[avg_lum] + " ")
    ascii_img.append(ascii_row)

for row in ascii_img:
    print(''.join(row))







