from PIL import Image


def resize_image(image_path: str, target_height: int):
    img = Image.open(image_path)
    width, height = img.size

    new_width = int((target_height/height)*width)
    img = img.resize((new_width, target_height))

    return img