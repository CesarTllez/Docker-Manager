from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import json_util
import os

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dockerDB"
mongo = PyMongo(app)

@app.route('/containers/add', methods=['POST'])
def add():
    container = {
        'id': request.json['id'],
        'name': request.json['name']
    }
    mongo.db.containers.insert_one({
        'id': container['id'],
        'name': container['name']
    })
    response = jsonify({
        'message': 'Container added successfully.'
    })
    response.status_code = 201
    return response

@app.route('/containers/updateById/<string:id>', methods=['PATCH'])
def updateById(id):
    name = request.json['name']
    mongo.db.containers.update_one(
        {'id': id}, 
        {'$set': {
            'name': name
        }})
    return ''

@app.route('/containers/getAll', methods=['GET'])
def getAll():
    containers = mongo.db.containers.find()
    return json_util.dumps(containers)

@app.route('/containers/deleteById/<string:id>', methods=['DELETE'])
def deleteById(id):
    mongo.db.containers.delete_many({'id': id})
    response = jsonify()
    response.status_code = 204
    return response

@app.route('/containers/unpause', methods=['POST'])
def unpauseById():
    container = {
        'id': request.json['id']
    }
    os.system('docker unpause '+container['id'])
    return jsonify({
        "message": "Unpaused container."
    })

@app.route('/containers/pause', methods=['POST'])
def pauseById():
    container = {
        'id': request.json['id']
    }
    os.system('docker pause '+container['id'])

    return jsonify({
        "message": "Paused container."
    })

@app.route('/containers/start', methods=['POST'])
def startById():
    container = {
        'id': request.json['id']
    }
    os.system('docker start '+container['id'])
    return jsonify({
        "message": "Started container."
    })

@app.route('/containers/stop', methods=['POST'])
def stopById():
    container = {
        'id': request.json['id']
    }
    os.system('docker stop '+container['id'])
    return jsonify({
        "message": "Stopped container."
    })

#Errors handler
@app.errorhandler(404)
def notFound(error=None):
    wrapper = jsonify({
        'message': 'This resource does not exist',
        'url': request.url,
        'status': '404 NOT FOUND'
    })
    wrapper.status_code = 404
    return wrapper

if __name__ == '__main__':
    app.run(
        debug = True,
        host = '192.168.0.3'
    )