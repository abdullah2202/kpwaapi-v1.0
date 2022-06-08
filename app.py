from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def home_page():
   return '<div>Hello World!</div>'






if __name__ == '__main__':
   port = int(os.environ.get("POST", 5000))
   app.run(debug=True, host='0.0.0.0', port=port)