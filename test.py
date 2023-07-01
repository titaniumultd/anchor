import os
import shutil
from PIL import Image, ImageDraw, ImageFont

icon_folder = r'C:\Users\titni\Downloads\1'
output_folder = r'C:\Users\titni\Downloads\output'
catalog_image_path = r'C:\Users\titni\Downloads\icon_catalog.jpg'

# Copy icons to output folder
for file in os.listdir(icon_folder):
    if file.endswith('.ico'):
        shutil.copy(os.path.join(icon_folder, file), output_folder)

# Load icons as images
icon_images = []
icon_filenames = []
for file in os.listdir(output_folder):
    if file.endswith('.ico'):
        icon_images.append(Image.open(os.path.join(output_folder, file)))
        icon_filenames.append(file)

# Create the icon catalog image
icon_size = (64, 64)
icons_per_row = 10
num_rows = (len(icon_images) + icons_per_row - 1) // icons_per_row
text_height = 20

canvas_width = icon_size[0] * icons_per_row
canvas_height = (icon_size[1] + text_height) * num_rows
canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))
draw = ImageDraw.Draw(canvas)

# Load a font for the file names (You can replace 'arial.ttf' with a path to a font file)
font = ImageFont.truetype('arial.ttf', 12)

for i, icon_image in enumerate(icon_images):
    row = i // icons_per_row
    col = i % icons_per_row
    x = col * icon_size[0]
    y = row * (icon_size[1] + text_height)

    # Draw the icon with a white background
    resized_icon = icon_image.resize(icon_size, Image.ANTIALIAS)
    white_background = Image.new('RGBA', icon_size, (255, 255, 255, 255))
    white_background.paste(resized_icon, mask=resized_icon)
    canvas.paste(white_background, (x, y))

    # Draw the file name below the icon
    file_name = icon_filenames[i]
    text_width, _ = draw.textsize(file_name, font=font)
    text_x = x + (icon_size[0] - text_width) // 2
    text_y = y + icon_size[1]
    draw.text((text_x, text_y), file_name, font=font, fill=(0, 0, 0))

# Save the catalog image as JPEG with quality setting
canvas = canvas.convert('RGB')  # Convert the image to RGB format
canvas.save(catalog_image_path, 'JPEG', quality=85)

print('Icon catalog image created successfully.')
