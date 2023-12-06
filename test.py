# !/bin/bash/python
# Class: CIS 440-0900
# Comment: Simple Script to test Flask Web Interface

from flask import Flask

app = Flask(__name__)
host = '127.0.0.1'
port = 80

@app.route('/')

def home_page():
       return 'You have landed on the Home Page!'

if __name__ == "__main__":
          app.runn(debug=True,host=host, port=port)


