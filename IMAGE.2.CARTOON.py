#--
#-- ************************************************************************************************************:
#-- ********************************************** PHTO 2 CARTOON **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   IMAGE.2.CARTOON.py                                                                                :
#-- Purpose:  A python script that converts a photo to a cartoon image.                                         :
#-- Class:    python -m PIP INSTALL opencv-python; python3 -m PIP INSTALL opencv-python                         :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- *************************************************:
#-- DEFINE PARAMS, CONFIG PATHS, IMPORT CLASSES      :
#-- *************************************************:
import cv2
#--
def convert_to_cartoon(image_path, output_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.medianBlur(gray_img, 5)
    edges = cv2.Laplacian(gray_img, cv2.CV_8U, ksize=5)
    _, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    cartooned_img = cv2.bitwise_and(img, img, mask=mask)
    cartooned_img = cv2.medianBlur(cartooned_img, 5)
    cv2.imwrite(output_path, cartooned_img)
#--
if __name__ == "__main__":
    input_image_path = "img.jpg"
    output_image_path = "cartooned.jpg"
    convert_to_cartoon(input_image_path, output_image_path)
#--
#-- *************************************************:
#-- END OF SCRIPT                                    :
#-- *************************************************: