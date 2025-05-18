# Image Resizer (Python)

This is a simple script to batch resize images in a folder using Python and Pillow.

```
image-resizer/
├── imageInput/ # Drop your original images here
├── imageOutput/ # Resized images will be saved here
```

## Setup Instructions

1. Create a virtual environment
```shell
cd image-resizer
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies
```shell
pip install pillow
```

3. Add images to imageInput/
Supported formats: .jpg, .jpeg, .png, .bmp, .gif

4. Run the script

```shell
python resize_image.py
```

5. Find resized images in imageOutput/

You can change the resize_factor in resize_image.py to adjust the scaling:
```python
resize_factor = 0.5  # 50% of original size
```
