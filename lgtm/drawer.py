from PIL import Image, ImageDraw, ImageFont
from typing import IO

# The ratio of the message drawable area to the entire image
MAX_RATIO = 0.8

# Font-related constants
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

# Change the path according to the execution environment
FONT_NAME = "/Library/Fonts/Arial Bold.ttf"
FONT_COLOR_WHITE = (255, 255, 255, 0)

# Output-related constants
OUTPUT_NAME = "output.png"
OUTPUT_FORMAT = "PNG"


def save_with_message(fp: IO[bytes], message: str):
    with Image.open(fp) as image:
        draw = ImageDraw.Draw(image)
        # The size of the area where message can be drawn
        # Calculate each element of the tuple
        image_width, image_height = image.size
        message_area_width = image_width * MAX_RATIO
        message_area_height = image_height * MAX_RATIO

        # Decrement to find the best font-size
        for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
            font = ImageFont.truetype(FONT_NAME, font_size)
            # Required size for drawing
            text_width, text_height = draw.textsize(message, font=font)
            w = message_area_width - text_width
            h = message_area_height - text_height

            # Use values within the drawable area for both width and height
            if w > 0 and h > 0:
                position = (
                    (image_width - text_width) / 2,
                    (image_height - text_height) / 2
                )
                draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
                break

        image.save(OUTPUT_NAME, OUTPUT_FORMAT)
