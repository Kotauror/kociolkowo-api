# app.py

import os

import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

CHURCHES_TABLE = os.environ['CHURCHES_TABLE']
client = boto3.client('dynamodb')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(CHURCHES_TABLE)

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

@app.route("/churches", methods=["GET"])
def get_all_churches():
    resp = table.scan()

    return resp