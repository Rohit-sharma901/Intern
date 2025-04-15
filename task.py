from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson import ObjectId

app = Flask(__name__)

# Replace the following with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')
db = client['Task']
collection = db['Task_collection']

@app.route('/data/<object_id>', methods=['GET'])
def get_data(object_id):
    # Query to fetch data ordered by timestamp
    object_id = ObjectId(object_id)
    # data = collection.find({}, {'timestamp': 1, 'Frequency.value': 1, 'Active_Power.value': 1}).sort('timestamp', -1)
    data1 = collection.find_one({'_id': object_id})
    # Removing _id key from data1 since it is not serializable
    data1.pop('_id')
    # Return JSON response
    return jsonify(data1)

if __name__ == '__main__':
    app.run(debug=True)
