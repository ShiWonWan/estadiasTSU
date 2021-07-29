# BLOCK CLASS IMPORT
from block import Block

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

# ARRAY OF BLOCKS
blocks = []
initial_block = Block("INITIAL BLOCK", datetime.now())

blocks.append(initial_block)

lastDocs = db.find()
for doc in lastDocs:
    blocks.append(Block(doc["prev data"], doc["data"]))

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
    id = db.insert({
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
    blocks.append(Block(lastHash, newHash))

    # RETURN JUST THE ID
    return jsonify(str(ObjectId(id)))

# GET ALL
@app.route('/all', methods=['GET'])
def getAll():
    return json.dumps([block.__dict__ for block in blocks])


if __name__ == '__main__':
    app.run(debug=1)