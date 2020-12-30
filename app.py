# app.py

import os

import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

CHURCHES_TABLE = os.environ['CHURCHES_TABLE']
client = boto3.client('dynamodb')

# dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name="eu-west-2")
# churches_table = dynamodb.Table(CHURCHES_TABLE)

# AWS_ACCESS_KEY = os.getenv('KOS_AK')
# AWS_SECRET_ACCESS_KEY = os.environ.get('KOS_SAK')

# c = boto3.dynamodb2.connect_to_region(aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name="eu-west-2")
# churches_table = Table(CHURCHES_TABLE,connection=c)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/churches", methods=["POST"])
def create_church():
    church_id = request.json.get('churchId')
    church_name = request.json.get('name')
    if not church_id or not church_name:
        return jsonify({'error': 'Please provide userId and name'}), 400

    resp = client.put_item(
        TableName=CHURCHES_TABLE,
        Item={
            'churchId': {'S': church_id },
            'name': {'S': church_name }
        }
    )

    return jsonify({
        'churchId': church_id,
        'name': church_name
    })

  #  https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb
  # get all churches