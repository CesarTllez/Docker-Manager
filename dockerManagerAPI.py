from flask import Flask, jsonify, request
from flask_cors import CORS
import connectionDB as db
import os

app = Flask(__name__)
CORS(app)

#CRUD containers
@app.route('/containers/add', methods=['POST'])
def add():
    container = {
            'id': request.json['id'],
            'name': request.json['name']
        }
    data = (container['id'], container['name'])

    db.cursor.execute(db.sqlCommands['insertSQL'], data)
    db.connectionDB.commit()

    return jsonify({
        "message": "Container added successfully."
    })

@app.route('/containers/getAll', methods=['GET'])
def getAll():
    db.cursor.execute(db.sqlCommands['selectAllSQL'])
    tupleContainers = db.cursor.fetchall()
    diccionaryFormat = {
        "containers": []
    }
    for idC, nameC in tupleContainers:
        diccionaryFormat['containers'].append({
            'id': idC,
            'name': nameC
        })
        
    return diccionaryFormat

@app.route('/containers/update', methods=['PUT'])
def updateById():
    container = {
        'id': request.json['id'],
        'name': request.json['name']
    }
    data = (container['name'], container['id'])
    db.cursor.execute(db.sqlCommands['updateSQL'], data)
    db.connectionDB.commit()

    return ''

@app.route('/containers/delete/<string:idC>', methods=['DELETE'])
def deleteById(idC):
    db.cursor.execute(db.sqlCommands['deleteSQL'], [idC])
    db.connectionDB.commit()

    return ''

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
    
    if container['id'] == 'b4678c82b159':
        return jsonify({
            "message": "Can't pause database."
        })

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

if __name__ == '__main__':
    app.run(
        debug = True,
        host = "192.168.0.3"
    )