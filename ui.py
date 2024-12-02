from flask import Flask, render_template, request
from app import main as get_weather
from app import api_key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        data = get_weather(city, api_key)
    return render_template('index.html', data = data)


if __name__ == "__main__":
    app.run(debug=True, port=4996)






