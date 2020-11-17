from stats import get_current_date, get_coords, get_image
import requests
import time

SLEEP_INTERVAL = 5  # Refresh rate in seconds
URL = ''            # URL to post data
IMAGE_DIR = ''      # Directory with images

def create_post_dict() -> dict:
    x, y = get_coords()
    image = get_image(IMAGE_DIR)
    floor = 4 # TODO
    date = get_current_date()
    post_dict = {
        'xCoord': x,
        'yCoord': y,
        'floor': floor,
        'image': image,
        'date': date
    }
    return post_dict

if __name__ == '__main__':
    try:
        while True:
            post_dict = create_post_dict()
            print(post_dict)
            response = requests.post(URL, json=post_dict)
            print(response)
            time.sleep(SLEEP_INTERVAL)
    except KeyboardInterrupt:
        print('Finished')