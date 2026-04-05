from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/location')
def location():
    return jsonify({
        "place": "Classroom",
        "latitude": 9.9312,
        "longitude": 76.2673
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
