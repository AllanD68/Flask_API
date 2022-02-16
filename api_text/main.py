from email import message
from flask import Flask, request
from flask_restful import Api, Resource, abort
from numpy import delete
from utils.crud_scraping import wikiScraping
import os

app = Flask(__name__)
api = Api(app)


class Text(Resource):
    def get(self,test):
        return wikiScraping(test)

    def delete(self,test):
        if os.path.isfile('JsonDB/' + test + '.json') == True:
            os.remove(f"JsonDB/{test}.json")
            return 200
        else:
            abort (404,message="la ressource n'existe pas")


class All_text(Resource):
    def get(self):
        return 'hello'



api.add_resource(Text,"/text/<test>") 
api.add_resource(All_text,"/All_text/")

if __name__ == "__main__":
    app.run(debug=True)

#def objet to json

#def save_to_db

# @app.route("/text" , method=['POST'])
# def create_text():