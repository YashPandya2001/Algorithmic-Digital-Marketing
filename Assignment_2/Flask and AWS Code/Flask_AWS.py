from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import url_for
from flask_pymongo import PyMongo
import base64
import boto3
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Team5'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Assignment_2'
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('trailbucket12345678')
mongo = PyMongo(app)
@app.route('/category/<cid>', methods=['GET'])
def get_all_stars(cid):
  output =[]
  s=""
  pre ="Categories/"+cid
  for object_summary in my_bucket.objects.filter(Prefix=pre):
     print(object_summary.key)
     output.append(object_summary.key)
  for  out in output:
      fileO = "https://trailbucket12345678.s3.amazonaws.com/"+out
      s = s+ f"<img src='{fileO}' />"
  return s 
if __name__ == '__main__':
    app.run(debug=True)