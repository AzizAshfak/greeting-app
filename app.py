from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "I am a Flask app!"
if __name__ == '__main__':
    app.run()