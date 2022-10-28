from flask import Flask, json

details =  {"slackUsername": "Samjero02", "backend": True, "age": 28, "Bio": "An engineer and a tech enthusiast"}

api = Flask(__name__)

@api.route('/details', methods=['GET'])
def get_details():
  return json.dumps(details)

if __name__ == '__main__':
    api.run()
