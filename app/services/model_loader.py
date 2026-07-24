import json
import os
import tempfile
import zipfile

from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join("saved_models", "best_pneumonia_model_v2.keras")


def _strip_quantization_config(obj):
    if isinstance(obj, dict):
        cleaned = {}
        for key, value in obj.items():
            if key == "quantization_config":
                continue
            cleaned[key] = _strip_quantization_config(value)
        return cleaned
    if isinstance(obj, list):
        return [_strip_quantization_config(item) for item in obj]
    return obj


def _load_model(path):
    if os.path.exists(path):
        try:
            return load_model(path, compile=False)
        except Exception:
            with zipfile.ZipFile(path, "r") as archive:
                data = {name: archive.read(name) for name in archive.namelist()}

            if "config.json" not in data:
                raise

            config = json.loads(data["config.json"].decode("utf-8"))
            patched_config = _strip_quantization_config(config)

            tmp_fd, tmp_path = tempfile.mkstemp(suffix=".keras")
            os.close(tmp_fd)

            try:
                with zipfile.ZipFile(tmp_path, "w") as patched_archive:
                    for name, content in data.items():
                        if name == "config.json":
                            patched_archive.writestr(name, json.dumps(patched_config))
                        else:
                            patched_archive.writestr(name, content)

                return load_model(tmp_path, compile=False)
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

    raise FileNotFoundError(f"Model file not found: {path}")


model = _load_model(MODEL_PATH)