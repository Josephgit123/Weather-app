from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "your_openweather_api_key"  # Replace with your API key

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") != 200:
            weather = {"error": "City not found!"}
        else:
            weather = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"],
                "icon": response["weather"][0]["icon"]
            }
    
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
