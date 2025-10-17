from flask import Flask, send_from_directory, jsonify, request
import requests
import os

# Serve the static `weather.html` from the project root and proxy OpenWeather requests.
app = Flask(__name__, static_folder='.')

# Prefer environment variable for API key, fall back to the one that was in the repo for convenience.
API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'aadd85ed5845b4f5427252a2cd26d855')


@app.route('/')
def index():
    # Return the frontend file (served from project root)
    return send_from_directory('.', 'weather.html')


@app.route('/weather', methods=['GET'])
def weather():
    lat = request.args.get('lat', default='28.6139')
    lon = request.args.get('lon', default='77.2090')

    current_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

    try:
        cur_r = requests.get(current_url, timeout=6)
        cur_r.raise_for_status()
        current = cur_r.json()

        f_r = requests.get(forecast_url, timeout=6)
        f_r.raise_for_status()
        forecast = f_r.json()
    except requests.RequestException as e:
        return jsonify({
            'error': 'failed to fetch from OpenWeather',
            'details': str(e)
        }), 502

    return jsonify({
        'current': current,
        'forecast': forecast
    })


if __name__ == '__main__':
    # Debug mode for local development only
    app.run(debug=True)
