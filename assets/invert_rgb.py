# I can only use this script to invert neutrals or supporting colors. 
# Images that contain colors that matter, e.g. logos, have to be recolored by hand.

from pathlib import Path
from PIL import Image, ImageOps

dark_folder = Path("dark")
light_folder = Path("light")

for png_file in dark_folder.glob("*.png"):
    img = Image.open(png_file).convert("RGBA")

    # Split channels
    r, g, b, a = img.split()

    # Merge RGB only
    rgb = Image.merge("RGB", (r, g, b))

    # Invert RGB, preserve alpha
    inverted = ImageOps.invert(rgb)

    # Reattach alpha
    result = Image.merge("RGBA", (*inverted.split(), a))

    # Save
    output_path = light_folder / png_file.name
    result.save(output_path)

    print(f"Converted: {png_file.name}")

print("Done")