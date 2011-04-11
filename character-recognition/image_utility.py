# Image utility functions
import PythonMagick


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

    image.pixelColor(x, y, color);

# image - PythonMagickImage
# x - x coordinate of pixel
# y - y coordinate of pixel
#
# Returns
# r - r channel 0-255
# g - g channel 0-255
# b - b channel 0-255
def get_color(image, x, y):

    color = image.pixelColor(x, y)

    r = int((float(color.redQuantum()) / 65536.0) * 256.0)
    g = int((float(color.greenQuantum()) / 65536.0) * 256.0)
    b = int((float(color.blueQuantum()) / 65536.0) * 256.0)

    return [r, g, b]

def format_hex_number(hex_number):
    number = str(hex(hex_number))
    number = number[2:]
    if len(number) < 2:
        number = "0" + number

    return number

# Credit to ftp://ftp.imagemagick.org/pub/ImageMagick/python/README.txt
def resize(image, w, h):
    image = PythonMagick.Image(image) # copy
    size = "!%sx%s" % (w, h)
    image.sample(size)
    return image
