from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, Integer
from flask.ext.restless import APIManager
import datetime

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///akwaaba.db'
db = SQLAlchemy(app)


class PhotoAdd(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(PhotoAdd, methods=['GET', 'DELETE', 'POST', 'PUT'])


@app.route('/')
def index():
    return app.send_static_file('index.html')

app.debug = True

if __name__ == '__main__':
    app.run()
