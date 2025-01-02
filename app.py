from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "You are welcome! this app. This  is a ml app"
if __name__ == '__main__':
    app.run()