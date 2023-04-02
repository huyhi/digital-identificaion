import pickle

from sklearn.svm import SVC

"""
MINST official website: http://yann.lecun.com/exdb/mnist/

TRAINING SET LABEL FILE (train-labels-idx1-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  60000            number of items
0008     unsigned byte   ??               label
0009     unsigned byte   ??               label
........
xxxx     unsigned byte   ??               label
The labels values are 0 to 9.

TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  60000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     unsigned byte   ??               pixel
0017     unsigned byte   ??               pixel
........
xxxx     unsigned byte   ??               pixel
Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
"""

IMG_PIXEL_NUM = 28 * 28


# MINST handwritten dataset was organized in a binary file, need to write a simple script to read the data
def read_image():
    result = []
    with open('./train-images-idx3-ubyte', 'rb') as image_f:
        image_f.read(16)
        for i in range(60000):
            result.append([int(b) / 255 * 0.99 + 0.01 for b in image_f.read(IMG_PIXEL_NUM)])

    return result


def read_label():
    result = []
    with open('./train-labels-idx1-ubyte', 'rb') as label_f:
        label_f.read(8)
        for i in range(60000):
            result.append(int(label_f.read(1)[0]))

    return result


def train_svm_model():
    x_train = read_image()
    y_train = read_label()
    # Train a SVM model with default kernel
    clf = SVC(kernel='rbf')
    clf.fit(x_train, y_train)

    with open('./svm.model', 'wb') as model_f:
        pickle.dump(clf, model_f)


if __name__ == '__main__':
    train_svm_model()
