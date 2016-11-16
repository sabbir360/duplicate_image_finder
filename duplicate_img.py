'''
Duplicate Image comparison
Ref: http://blog.iconfinder.com/detecting-duplicate-images-using-python/
'''

from PIL import Image
''''
IMG = Image.open('data/a.PNG')
WIDTH, HEIGHT = IMG.size
PIXELS = list(IMG.getdata())

DIFFERENCE = []

for row in range(HEIGHT):
    for col in range(WIDTH):
        if col != WIDTH:
            DIFFERENCE.append(PIXELS[col+row] > PIXELS[(col+row)+1])

for col in range(WIDTH-1):
    print(DIFFERENCE[col:col+(WIDTH-1)])
'''

def dhash(image, hash_size=8):
    '''
    return a list where fist string is hash and second one is path for image.
    '''
    image_path = image
    image = Image.open(image_path)
    # Grayscale and shrink the image in one step.
    image = image.convert('L').resize(
        (hash_size + 1, hash_size),
        Image.ANTIALIAS,
    )

    # pixels = list(image.getdata())

    # Compare adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)


'''
# examples
OLD = 'data/a.PNG'
NEW = 'data/b.PNG'

if dhash(OLD) == dhash(NEW):
    print("Same")
    print("delete :: " + OLD)
else:
    print("New")

'''
 