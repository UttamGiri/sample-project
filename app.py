from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please subscribe, like, and comment for this argo cd demo-plan by tiger team-1-!!!'
