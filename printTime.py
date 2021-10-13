from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():    
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

