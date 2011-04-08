# Image utility functions

# image - PythonMagickImage
# x - x coordinate of pixel
# y - y coordinate of pixel
# r - r channel 0-255
# g - g channel 0-255
# b - b channel 0-255
def set_color(image, x, y, r, g, b):

    r_hex = format_hex_number(r)
    g_hex = format_hex_number(g)
    b_hex = format_hex_number(b)

    color = "#" + r_hex + g_hex + b_hex

    print color
    image.pixelColor(x, y, color);


def format_hex_number(hex_number):
    number = str(hex(hex_number))
    number = number[2:]
    if len(number) < 2:
        number = "0" + number

    return number