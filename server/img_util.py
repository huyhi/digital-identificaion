import pickle

from PIL import Image


def resize(img: Image):
    img = img.convert('L')
    img = img.resize((28, 28))
    return img


def img_2_byte_array(img: Image) -> list[int]:
    res = []
    img_size_x, img_size_y = img.size
    pixel_access = img.load()
    for y in range(img_size_y):
        for x in range(img_size_x):
            res.append(255 - pixel_access[x, y])
    return res


def predict(x) -> int:
    with open('../svmtraining/svm.model', 'rb') as model_f:
        model = pickle.load(model_f)
    return model.predict(x)[0]
