# BLOCK CLASS IMPORT AND POW
from block import Block
from pow import PoW

# SERVER IMPORTS
from flask import Flask, request, jsonify
from flask.json import jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

# LANGUAGE IMPORTS
import json
import hashlib
from datetime import datetime

# SERVER AND DB CONFIG
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/blockChain'
mongo = PyMongo(app)
CORS(app)
db = mongo.db.datos

# CPUS

myPc = 3 * ['myPc'] # 3 cpu units
anotherPc = 2 * ['anotherPc'] # 2 cpu units
AlfonsoPc = 4 * ['AlfonsoPc'] # 4 cpu units
sisPc = 2 * ['sisPc'] # 2 cpu units

cpus = [myPc, anotherPc, AlfonsoPc, sisPc]

# ARRAY OF BLOCKS

blocks = []
initial_block = Block("GENESIS BLOCK", datetime.now())
PoW(cpus, initial_block)

blocks.append(initial_block)

lastDocs = db.find()
for doc in lastDocs:
    NewBlock = Block(doc["prev data"], doc["data"])
    PoW(cpus, NewBlock)
    blocks.append(NewBlock)

# TEST END POINT
@app.route('/')
def index():
    return json.loads('{"message":"Working ok"}')

# NEW ONE
@app.route('/new', methods=['POST'])
def createOne():

    # LAST BLOCK
    lastHash = blocks[-1].block_hash
    newHash = request.json['data']

    # INSERT TO MONGO
    id = db.insert_one({
        'data' : newHash,
        'prev data' : lastHash,
    })

    # INSERT INTO .TXT FILE WITH THE ID NAME
    file = open('hashing.txt', 'a+')
    file.write("\n"+str({
        'data' : newHash,
        'prev data' : lastHash,
    })+',')
    file.close()

    # ADD THE NEW BLOCK TO THE LIST
    NewBlock = Block(lastHash, newHash)
    PoW(cpus, NewBlock)
    blocks.append(NewBlock)

    # RETURN JUST THE ID
    return jsonify(str(ObjectId(id.inserted_id)))

# GET ALL
@app.route('/all', methods=['GET'])
def getAll():
    return json.dumps([block.__dict__ for block in blocks])


if __name__ == '__main__':
    app.run(debug=1)