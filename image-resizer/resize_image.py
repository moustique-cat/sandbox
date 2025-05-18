from PIL import Image
import os

resize_factor = 0.5

input_folder = "imageInput"
output_folder = "imageOutput"

os.makedirs(output_folder, exist_ok=True)

valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        
        with Image.open(input_path) as img:
            original_height = img.height
            new_height = (int(original_height * resize_factor))
            resized_img = img.resize(new_height)
            resized_img.save(output_path)
            print(f"Resized {filename} from {original_size} to {new_size} in {output_path}.")