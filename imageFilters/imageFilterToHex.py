from collections import Counter
from sklearn.cluster import KMeans
import numpy as np
import cv2
import os

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (550, 250), interpolation=cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img

def color_analysis(img):
    clf = KMeans(n_clusters=5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    return hex_colors

folder_path = "cropped_images"

all_colors = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg"):
        file_path = os.path.join(folder_path, file_name)
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        modified_image = prep_image(image)
        hex_colors = color_analysis(modified_image)
        all_colors.extend(hex_colors)


with open("all_colors.txt", "w") as f:
    for hex_color in all_colors:
        f.write(hex_color + "\n")
