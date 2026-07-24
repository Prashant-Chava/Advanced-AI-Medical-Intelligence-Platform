import os
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

from app.services.model_loader import model


def generate_gradcam(image_path, save_path="reports/heatmap.png"):

    os.makedirs("reports", exist_ok=True)

    # Load image
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    img = np.array(image, dtype=np.float32)
    img = np.expand_dims(img, axis=0)

    # Get MobileNetV2 base model
    base_model = model.get_layer("mobilenetv2_1.00_224")

    # Automatically find the last convolution layer
    last_conv_layer = None

    for layer in reversed(base_model.layers):
        if isinstance(layer, tf.keras.layers.Conv2D):
            last_conv_layer = layer.name
            break

    print("Using Grad-CAM Layer:", last_conv_layer)

    # Build gradient model
    grad_model = tf.keras.models.Model(
        inputs=base_model.input,
        outputs=[
            base_model.get_layer(last_conv_layer).output,
            base_model.output,
        ],
    )

    with tf.GradientTape() as tape:

        # Forward pass through base model
        conv_output, features = grad_model(img)

        # Forward remaining layers manually
        x = model.layers[3](features)
        x = model.layers[4](x, training=False)
        predictions = model.layers[5](x)

        loss = predictions[:, 0]

    grads = tape.gradient(loss, conv_output)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_output = conv_output[0]

    heatmap = conv_output @ pooled_grads[..., tf.newaxis]

    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0)

    heatmap /= tf.reduce_max(heatmap) + 1e-8

    heatmap = heatmap.numpy()

    heatmap = cv2.resize(heatmap, (224, 224))

    heatmap = np.uint8(255 * heatmap)

    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    original = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    overlay = cv2.addWeighted(original, 0.6, heatmap, 0.4, 0)

    cv2.imwrite(save_path, overlay)

    return save_path