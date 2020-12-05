import threading
from PIL import ImageGrab
import random
import string


def take_scrren_shot():
    
    threading.Timer(5.0, take_scrren_shot).start()
    im = ImageGrab.grab()
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(6))
    pic_name = (result_str+'.png')
    im.save(pic_name)
take_scrren_shot()