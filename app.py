from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from PatternDAO import patternDAO

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    return render_template('testing.html')

###### Pattern Routes
# Get all patterns
@app.route('/patterns', methods = ['GET'])
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

# Find by patterns by userID
@app.route('/userID/<userID>')
def findByUserID(userID):
    return jsonify(patternDAO.findByUserID(userID))


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
        "format": request.json["format"],
        "userID": request.json["userID"]
    }
    return jsonify(patternDAO.create(pattern)), 201


# Update a pattern
@app.route('/patterns/<patternID>', methods=['PUT'])
def update_pattern(patternID):
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
    if 'format' in request.json:
        currentPattern['format'] = request.json['format']
    if 'userID' in request.json:
        currentPattern['userID'] = request.json['userID']
    patternDAO.update(currentPattern)
    return jsonify(currentPattern)


#  Delete
@app.route('/patterns/<patternID>', methods=['DELETE'])
def delete(patternID):
    patternDAO.delete(patternID)
    return jsonify({"done": True})


######## User Routes
@app.route('/users', methods = ['GET'])
def get_all_users():
    return jsonify(patternDAO.get_all_users())







######## Borrow Routes


if __name__ == "__main__":
    app.run(debug=True)
