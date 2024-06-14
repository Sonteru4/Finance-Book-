''' controller and routes for users '''
import json
import uuid

import logger
from app import app, mongo
from bson import json_util
from flask import request, jsonify, flash, redirect, send_file
from werkzeug.utils import secure_filename

from .data import *

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = os.path.join(ROOT_PATH, 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def user():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find_one(query)
        return jsonify(data), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('name', None) is not None and data.get('email', None) is not None:
            mongo.db.users.insert_one(data)
            return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        if data.get('email', None) is not None:
            db_response = mongo.db.users.delete_one({'email': data['email']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        if data.get('query', {}) != {}:
            mongo.db.users.update_one(
                data['query'], {'$set': data.get('payload', {})})
            return jsonify({'ok': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400


@app.route('/ticker', methods=['GET'])
def get_summary_data_by_ticker():
    if request.method == 'GET':
        ticker = request.args
        cursor = mongo.db.summary_data.find({"ticker": ticker})
        json_docs = []
        for doc in cursor:
            print("in doc")
            json_doc = json.dumps(doc, default=json_util.default)
            json_docs.append(json_doc)
        return jsonify(json_docs), 200


@app.route('/ticker_fin', methods=['GET'])
def get_finance_by_ticker():
    if request.method == 'GET':
        ticker = request.args.get('ticker', type=str)
        LOG.info("ticker : %s " % ticker)
        balance = get_company_data(ticker)
        return jsonify(balance), 200


@app.route('/upload_pdf', methods=['POST'])
def save_files():
    print("uploaded")
    if request.method == 'POST':
        print(request.files)
        print(request.files.keys)
        # check if the post request has the file part
        if 'statement_fill' not in request.files:
            LOG.info("statement_fill not in request.files")
            flash('No file part')
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
        file = request.files['statement_fill']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            LOG.info("no selected file")
            flash('No selected file')
            return redirect(request.url)
        if file:
            LOG.info("save file")
            filename = secure_filename(file.filename).encode('UTF-8')
            flash('file {} saved'.format(filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'ok': True,
                            'file_name': file.filename,
                            'message': 'success to save file',
                            'id': str(uuid.uuid4()),
                            'originalName': file.filename,
                            'url': request.url_root + UPLOAD_FOLDER + "/" + file.filename
                            }), 200
    return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400


@app.route('/uploads/<path:path>', methods=['GET'])
def get_pdf_file(path):
    LOG.info("get pdf request : %s" % path)
    dir_list = os.listdir(app.config['UPLOAD_FOLDER'])
    print(dir_list)
    for i in dir_list:
        if path == i:
            LOG.info("found the relevant pdf to send")
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'], i), attachment_filename=path, as_attachment=True,
                             mimetype="application/pdf")
    return jsonify({'ok': False, 'message': 'Cant find the pdf'}), 400
