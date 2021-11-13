from flask import Flask, json

from app.Db import FirestoreDB

app = Flask(__name__)

@app.route('/sharedPassword/<uid>')
def getSharedPass(uid):
    db = FirestoreDB()
    passDict = db.getCopiedPassword(uid)
    return json.dumps(passDict, indent = 4)
