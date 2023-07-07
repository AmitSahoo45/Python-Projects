from rembg import remove
from PIL import Image

input_path = "alonso.jpg"
output_path = "alonso-no-bg.png"

img = Image.open(input_path)
output = remove(img)
output.save(output_path, "PNG")