import cv2
import matplotlib.pyplot as plt
import numpy as np

import Predictor


def extract(image):
    image = cv2.imread(image)
    img = image.copy()
    img_orig = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blured_img = cv2.medianBlur(gray_img, 21)

    # edges = cv2.Canny(blured_img, 30, 80, apertureSize=3)

    circles_detected = cv2.HoughCircles(blured_img, cv2.HOUGH_GRADIENT, 1, 120,
                                        param1=80, param2=30, minRadius=10, maxRadius=300)

    total_euro_val = 0
    total_mad_val = 0

    if circles_detected is not None:
        for (x, y, r) in circles_detected[0]:
            x, y, r = int(x), int(y), int(r)
            extracted_coin = img_orig[(y - r):(y +r), (x - r):(x + r)]
            if extracted_coin is not None and extracted_coin.size > 0:
                extracted_coin = cv2.resize(extracted_coin, (150, 150))
                predictedVal = Predictor.predict(extracted_coin)

                intVal, currency = Predictor.convertLabelToInt(predictedVal)

                if currency == 'Euro':
                    total_euro_val += intVal
                elif currency == 'Mad':
                    total_mad_val += intVal

                cv2.circle(img_orig, (x, y), r, (0, 255, 0), 4, 4)
                cv2.putText(img_orig, str(predictedVal), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    return img_orig, total_mad_val, total_euro_val
