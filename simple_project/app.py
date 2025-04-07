from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from PatternDAO import patternDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return 'Welcome'


# Get all patterns
@app.route('/users')
def getAll():
    return jsonify(patternDAO.getAll())