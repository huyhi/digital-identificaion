from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    file = request.files.get('file')
    if file is None:
        return err("file param required")
    return success("ok")


def err(msg):
    return '''
{{
  success: false,
  data: null
  errMsg: "{}"
}}
'''.format(msg)


def success(data):
    return '''
{{
  success: true,
  data: "{}"
  errMsg: null
}}
'''.format(data)
