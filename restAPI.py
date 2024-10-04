from flask import Flask, request, json
from flask_restful import Resource, Api
from flask_cors import CORS
import json

App = Flask(__name__)

CORS(App)

api = Api(App)

class main(Resource):
    def get(self):
        return "Hello world!", 201

class add_data(Resource):
    def post(self):

        messages = open("./data.json", "r")

        messages = messages.read()

        messages = json.loads(messages)

        json_data = request.get_json()

        contact = f"{json_data.get('contact')}"
        description = f"{json_data.get('description')}"

        if not isinstance(contact, str) or not isinstance(description, str):
            return {"error": "Contact and description must be strings."}, 400

        if (len(contact) > 20 or len(contact) < 3) or (len(description) > 1000 or len(description) < 50):
            return {"error": "Insufficient information or information has exceeded limit!."}, 400

        messages[contact] = description

        new_msg = open("./data.json", "w")

        msg = ""

        for char in str(messages):
            if char == "'":
                msg = msg + '"'
                continue
            msg = msg + char

        new_msg.write(msg)

        return {"message": "Request was successful!"}, 201
class get_data(Resource):
    def get(self):
        messages = open("./data.json", "r")

        messages = messages.read()

        print(messages)

        del_msg = open("./data.json", "w")

        del_msg.write("{}")

        return messages, 201

api.add_resource(main, "/")
api.add_resource(add_data, "/add_data")
api.add_resource(get_data, "/get_data")

App.run(debug=True)