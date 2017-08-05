from flask import Flask
from flask import request
from ballot_api import get_representatives
from flask import Response

app = Flask(__name__)


@app.route("/representatives", methods=['POST'])
def representatives():
    data = request.get_json()
    address = data['address']
    levels = data['levels']
    response = Response(get_representatives(address,
                        levels))
    response.headers = {'Content-Type': 'application/json'}
    return response

if __name__ == "__main__":
    app.run()
