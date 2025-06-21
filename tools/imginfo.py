from PIL import Image
import sys

def image_info(path):
    try:
        with Image.open(path) as img:
            print(f"Dosya: {path}")
            print(f"Format: {img.format}")
            print(f"Boyut: {img.size[0]}x{img.size[1]} piksel")
            print(f"Mod: {img.mode}")
    except Exception as e:
        print(f"Hata: {e}")
