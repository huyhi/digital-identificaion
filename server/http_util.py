from flask import jsonify


def err(msg):
    return jsonify(success=False, data=None, msg=msg)


def success(data):
    return jsonify(success=True, data=data, msg=None)
