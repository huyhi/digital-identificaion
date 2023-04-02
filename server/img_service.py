import io
import os.path
import pickle

from PIL import Image
from urllib import request

from conf import ROOT_DIR

PIXEL_WIDTH = 28
PIXEL_HEIGHT = 28
svm_model = None


def load_model():
    global svm_model
    with open(os.path.join(ROOT_DIR, 'svmtraining', 'svm.model'), 'rb') as model_f:
        svm_model = pickle.load(model_f)


def grayscale_and_resize(img: Image):
    img = img.convert('LA')
    img = img.resize((PIXEL_WIDTH, PIXEL_HEIGHT))
    return img


def img_2_byte_array(img: Image) -> list[int]:
    res = []
    img_size_x, img_size_y = img.size
    pixel_access = img.load()
    for y in range(img_size_y):
        for x in range(img_size_x):
            res.append(pixel_access[x, y][1])
    return res


def predict(x) -> int:
    if predict is None:
        raise Exception('model not loaded')
    return svm_model.predict([x])[0].item()


def img_from_data_url(data_url):
    with request.urlopen(data_url) as resource:
        return Image.open(io.BytesIO(resource.read()))
