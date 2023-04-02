"""
deplay flask app reference: https://spacewander.github.io/explore-flask-zh/13-deployment.html
"""
from flask import Flask, request

from server.http_util import err, success
from server.img_service import load_model, img_from_data_url, grayscale_and_resize, img_2_byte_array, predict


def start():
    load_model()
    return Flask(__name__)


app = start()


@app.route('/predict', methods=['POST'])
def predict_img():
    img_data_url = request.form.get('img_data_url')
    if img_data_url is None:
        return err("img_data_url param required")

    img = img_from_data_url(img_data_url)
    img = grayscale_and_resize(img)
    predict_res = predict(img_2_byte_array(img))
    return success(predict_res)


# global server internal exception handler
@app.errorhandler(Exception)
def handle_bad_request(e):
    return err(str(e))


if __name__ == '__main__':
    app.run()
