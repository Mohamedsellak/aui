from flask import Flask, request, jsonify
from flask_cors import CORS
from calculeDistance import calculeDistance

app = Flask(__name__)
# to allow the cros origin request
CORS(app)

@app.route('/', methods = ['POST','GET'])
def search():
    # recuperer les location a partir de Leaflet js Map
    data = request.get_json()
    results = {'data': data}

    # calculer les distance entre chaque point et les autre points
    les_distances = calculeDistance(data['locations'])
    return jsonify(results)

if __name__ == '__main__':
    app.run()