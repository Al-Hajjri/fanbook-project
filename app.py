from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient('mongodb+srv://alhajjri:SamsungA7@cluster0.g8buonf.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)