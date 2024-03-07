#this will serve one file i.e when i will aks for the file it will return the file, the response should have a file
#from inside the json structure.
from flask import Flask, request, jsonify
from helperMethods import getDataFromPath

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/getFile')
def hello():
    path = request.args.get('path', None)
    response_data = {}
    if path:
        status,isZip,fileName,fileData = getDataFromPath(path)
        response_data['isZip'] = isZip
        response_data['fileName'] = fileName
        response_data['fileData'] = fileData
    return jsonify(response_data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)