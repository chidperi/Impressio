# File name: main.py
# Copyright 2017 Chidambaram Periakaruppan
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

from flask import Flask, current_app, request, jsonify
import io
import model
import base64
import logging

app = Flask(__name__)
@app.route('/', methods=['POST'])
def predict():
    data = {}
    try:
        data = request.get_json()['data']
    except Exception:
        return jsonify(status_code='400', msg='Bad Request'), 400

    data = base64.b64decode(data)

    image = io.BytesIO(data)
    predictions = model.predict(image)
    current_app.logger.info('Predictions: %s', predictions)
    return jsonify(predictions=predictions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)