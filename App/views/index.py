from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('login.html')

@index_views.route('/images/<path:filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory('/workspaces/Info3604_Project/images', filename)
