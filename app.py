# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os
import Embeddings
# import Gen_AI

# ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = './'

# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# creating a Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
@cross_origin()
def home():
    if(request.method == 'GET'):
        resp = jsonify({'message' : 'rendered successfully'})
        return resp
    
@app.route('/read',methods=['GET'])
@cross_origin()
def read_files():
        Embeddings.text_csv()
        return jsonify(200)
    
@app.route('/chat',methods=['GET'])
def chat_response():
    question = request.args.get("question")
    print("Question: "+question)
    resp = Embeddings.answer_question(question)
    return jsonify(resp)

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
# @app.route('/home', methods = ['GET'])
# def disp(num):
# 	return jsonify({})

# @app.route('/return-files/')
# def return_files_tut():
# 	try:
# 		return send_file('/SOP.pdf', attachment_filename='SOP.pdf')
# 	except Exception as e:
# 		return str(e)

# driver function
if __name__ == '__main__':
    CORS(app, support_credentials=True)
    app.run(debug = True)