from flask import  Flask
from  flask_restful import Resource,Api
# from .models import Entry

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)
