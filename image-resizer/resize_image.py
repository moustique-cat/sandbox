#script to resize images

#run in venv
from PIL import Image

# Load the image
img = Image.open("input.jpg")

# Resize it
new_height = 600
resized_img = img.thumbnail((new_height))

# Save it
resized_img.save("output.jpg")

print("Image resized and saved as output.jpg")