import face_recognition
from PIL import Image, ImageDraw
import numpy as np
unknown_image = face_recognition.load_image_file("bigfacetest.jpg")
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)

    name = "Unknown"
    adjustment_side = (right-left)/6.45
    adjustment_top = (bottom-top)/ 1.6125
    # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face

    # Draw a box around the face using the Pillow module
    # draw.rectangle((left-adjustment_side, top-adjustment_top, right+adjustment_side, bottom+adjustment_side), outline=(0, 255, 0))
    draw.rectangle((0, 0, left-adjustment_side, 3072), fill=(0,0,255))  # left fill
    draw.rectangle((0, 0, 5472, top-adjustment_top), fill=(0, 0, 255))  # upper fill
    draw.rectangle((0, bottom+adjustment_side, 5472, 3072), fill=(0, 0, 255))  # bottom fill
    draw.rectangle((right+adjustment_side, 0, 5472, 3072), fill=(0, 0, 255))  # right fill
    # Draw a label with a name below the face
    # text_width, text_height = draw.textsize(name)
    # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    # draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw
print(face_encodings)
print(left, top, bottom, right)
# Display the resulting image
pil_image.show()
