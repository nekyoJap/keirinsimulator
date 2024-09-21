from flask import Flask, render_template
app = Flask(__name__)

# 駒の情報
racers = [
    {'number': 1, 'color': 'white', 'x': 300, 'y': 400},
    {'number': 2, 'color': 'black', 'x': 400, 'y': 400},
    {'number': 3, 'color': 'red', 'x': 500, 'y': 400},
    {'number': 4, 'color': 'blue', 'x': 600, 'y': 400},
    {'number': 5, 'color': 'yellow', 'x': 700, 'y': 400},
    {'number': 6, 'color': 'green', 'x': 800, 'y': 400},
    {'number': 7, 'color': 'orange', 'x': 900, 'y': 400},
    {'number': 8, 'color': 'pink', 'x': 1000, 'y': 400},
    {'number': 9, 'color': 'purple', 'x': 1100, 'y': 400}
]

@app.route('/')
def index():
    return render_template('index.html', racers=racers)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='0.0.0.0', port=5000, debug=True)
