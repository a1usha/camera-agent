import io
from base64 import encodebytes
from PIL import Image
import os
import random
from datetime import datetime, date
from json import dumps

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img

def get_random_image(full_path):
    images = os.listdir(full_path)
    return full_path + random.choice(images)

def get_current_date():
    return dumps(datetime.now(), default=json_serial)

def get_image(full_path):
    return get_response_image(get_random_image(full_path))

# TODO
def get_coords():
    return 320, 1800