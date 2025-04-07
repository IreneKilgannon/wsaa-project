from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from PatternDAO import patternDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return render_template('index.html')


# Get all patterns
@app.route('/')
def getAll():
    return jsonify(patternDAO.getAll())


# Find By patternID
@app.route('/patterns/<patternID>', methods = ['GET'])
def findByID(patternID):
    return jsonify(patternDAO.findByID(patternID))


# Find by Brand
@app.route('/brand/<brand>', methods = ['GET'])
def findByBrand(brand):
    return jsonify(patternDAO.findByBrand(brand))

# Find by Category
@app.route('/category/<category>', methods = ['GET'])
def findByCategory(category):
    return jsonify(patternDAO.findByCategory(category))

# Find by Fabric Type
@app.route('/fabric_type/<fabric_type>')
def findByFabric(fabric_type):
    return jsonify(patternDAO.findByFabric(fabric_type))

# Find by Patterns belonging to a specific owner by name
@app.route('/name/<name>')
def findByOwner(name):
    return jsonify(patternDAO.findByOwner(name))

# Create a pattern
@app.route('/patterns', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    pattern = {
        "patternID": request.json["patternID"],
        "brand": request.json["brand"],
        "category": request.json["category"],
        "fabric_type": request.json["fabric_type"],
        "description": request.json["description"],
        "ownerID": request.json["ownerID"]
    }
    return jsonify(patternDAO.create(pattern))


# Update a pattern
@app.route('/patterns/<patternID>', methods=['PUT'])
def update_age(patternID):
    foundPattern = patternDAO.findByID(patternID)
    print (foundPattern)
    if foundPattern == {}:
        return jsonify({}), 404
    currentPattern = foundPattern
    if 'patternID' in request.json:
        currentPattern['patternID'] = request.json['patternID']
    if 'brand' in request.json:
        currentPattern['brand'] = request.json['brand']
    if 'category' in request.json:
        currentPattern['category'] = request.json['category']
    if 'fabric_type' in request.json:
        currentPattern['fabric_type'] = request.json['fabric_type']
    if 'description' in request.json:
        currentPattern['description'] = request.json['description']
    if 'ownerID' in request.json:
        currentPattern['ownerID'] = request.json['ownerID']
    patternDAO.update(currentPattern)
    return jsonify(currentPattern)


#  Delete
@app.route('/patterns', methods=['DELETE'])
def delete(patternID):
    patternDAO.delete(patternID)
    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)
