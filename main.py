from flask import Flask, json

from Db import FirestoreDB

app = Flask(__name__)

@app.route('/sharedPassword/<uid>')
def getSharedPass(uid):
    db = FirestoreDB()
    passDict = db.getCopiedPassword(uid)
    return json.dumps(passDict, indent = 4)

if __name__ == "__main__":
    app.run()



