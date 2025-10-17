# Weather Dashboard (Frontend + Backend)

This project contains a static frontend (`weather.html`) and a small Flask backend (`backend.py`) that proxies requests to OpenWeatherMap so the API key is not exposed in the browser.

Quick start (Windows PowerShell):

1. Create a virtual environment and install requirements:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install flask requests
```

2. Set your OpenWeather API key (recommended) and run the backend:

```powershell
$env:OPENWEATHER_API_KEY = "your_api_key_here"
python backend.py
```

3. Open http://127.0.0.1:5000/ in your browser. The frontend will call `/weather` to fetch data.

Notes:
- If `OPENWEATHER_API_KEY` is not set, `backend.py` will use a fallback key that was present in the repository. For production, always set your own key.
- The Flask app serves `weather.html` directly from the project root.
