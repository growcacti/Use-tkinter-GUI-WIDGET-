import cv2
import os
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory

file= askopenfilename(filetypes=[("img file", "*.png"),("Image Files Files", "*.txt"),('All Files', '*.*')])



cv2.imread(file)
   
 
color_image = cv2.imread(file)
# cv2.waitKey()
# cv2.destroyAllWindows()

cartoon_style_selection = input(
    "This script currently has 2 sytles. Please type 1 or 2.   "
)

if cartoon_style_selection == "1":
    cartoon_image_style_1 = cv2.stylization(color_image,
                                            sigma_s=150, sigma_r=0.25)
    cv2.imshow("cartoon_1", cartoon_image_style_1)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif cartoon_style_selection == "2":
    cartoon_image_style_2 = cv2.stylization(color_image,
                                            sigma_s=60, sigma_r=0.5)
    cv2.imshow("cartoon_2", cartoon_image_style_2)
    cv2.waitKey()
    cv2.destroyAllWindows()

else:
    print("Invalid style selection.")
