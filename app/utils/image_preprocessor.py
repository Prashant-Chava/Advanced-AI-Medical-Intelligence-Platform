import numpy as np
from PIL import Image

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    # Keep raw pixel values (0-255)
    image = np.array(image, dtype=np.float32)

    image = np.expand_dims(image, axis=0)

    return image