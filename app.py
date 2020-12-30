# app.py

import os

import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

CHURCHES_TABLE = os.environ['CHURCHES_TABLE']
client = boto3.client('dynamodb')


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/churches")
def get_all_churches():
    resp = client.get_item(
        TableName=CHURCHES_TABLE,
        Key={
            'churchId': { 'S': churchId }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'No churches found'}), 404

    return jsonify({
        'churchId': item.get('churchId').get('S'),
        'name': item.get('name').get('S')
    })

  #  https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb
  # get all churches