import os
from PIL import Image


input_folder = "images"
output_folder = "cropped_images"


top_cut = 800
bottom_cut = 150
left_cut = 150
right_cut = 100


for filename in os.listdir(input_folder):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

       
        width, height = image.size

       
        crop_region = (left_cut, top_cut, width - right_cut, height - bottom_cut)

        
        cropped_image = image.crop(crop_region)

        
        os.makedirs(output_folder, exist_ok=True)

        
        output_path = os.path.join(output_folder, filename)
        cropped_image.save(output_path)