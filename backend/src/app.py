from flask import Flask, request, jsonify
from flask.json import jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
import json
import hashlib
from datetime import datetime


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/blockChain'
mongo = PyMongo(app)

CORS(app)

db = mongo.db.datos

# TEST END POINT
@app.route('/')
def index():
    return json.loads('{"message":"Working ok"}')

# NEW ONE
@app.route('/new', methods=['POST'])
def createOne():
    # LAST BLOCK
    docTo = db.find().sort('date', -1).limit(1)
    for doc in docTo:
        last = doc
    lastHash = last['dato']
    newHash = hashlib.sha256(request.json['dato'].encode('utf-8')).hexdigest()

    # INSERT TO MONGO
    id = db.insert({
        'dato' : newHash,
        'last dato' : lastHash,
        'date': datetime.now()
    })

    # INSERT INTO .TXT FILE WITH THE ID NAME
    file = open('hashing.txt', 'a+')
    file.write("\n"+str({
        'dato' : newHash,
        'last dato' : lastHash,
        'date': datetime.now()
    })+',')
    file.close()

    # RETURN JUST THE ID
    return jsonify(str(ObjectId(id)))

# GET ALL
@app.route('/all', methods=['GET'])
def getAll():
    docs = []
    for doc in db.find():
        docs.append({
            '_id' : str(ObjectId(doc['_id'])),
            'dato' : doc['dato'],
            'last dato' : doc['last dato'],
            'date': doc['date']
        })
    return jsonify(docs[::-1])


if __name__ == '__main__':
    app.run(debug=1)