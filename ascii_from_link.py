import requests
from PIL import Image
from io import BytesIO
import os

# Direktori output
output_dir = "hasil"
os.makedirs(output_dir, exist_ok=True)

# Input URL
link = input("Masukkan URL gambar (.jpg/.png): ")

try:
    # Download gambar
    response = requests.get(link)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content))
    img = img.convert("L")  # ubah jadi grayscale
    img = img.resize((100, 50))  # resize agar tidak terlalu besar

    chars = "@%#*+=-:. "
    ascii_art = ""

    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            ascii_art += chars[pixel // 25]
        ascii_art += "\n"

    output_path = os.path.join(output_dir, "ascii.txt")
    with open(output_path, "w") as f:
        f.write(ascii_art)

    print(f"✅ ASCII berhasil disimpan di '{output_path}'")

except Exception as e:
    print(f"❌ Gagal memproses gambar: {e}")
