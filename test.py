import matplotlib.pylab as plt
import cv2
import numpy as np
import math

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def process(image):

    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width/2, height/1.7),
        (width, height)
    ]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cv2.imwrite('canny2.png', canny_image)
    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32),)
    lines = cv2.HoughLinesP(cropped_image,
                            rho=1,
                            theta=np.pi/180,
                            threshold=40,
                            lines=np.array([]),
                            minLineLength=1,
                            maxLineGap=25)
    cor_lines = []
    for x in lines:
        y = x[0]
        dx = abs(y[0]-y[2])
        yx = abs(y[1]-y[3])
        angle = math.atan(yx/dx)
        if (angle > math.pi * 0.3 ):
            print (angle)
        if (yx > 20):
            if (angle > math.pi * 0.15 and angle < math.pi * 0.85):
                cor_lines.append(x)
        

    image_with_lines = draw(image, cor_lines)
    #print (lines[0])
    return image_with_lines

cap = cv2.VideoCapture('video.mp4')
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 20, (640,360))

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    out.write(frame)
    cv2.imshow('frame', frame)
    #cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()