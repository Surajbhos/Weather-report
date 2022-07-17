import requests
from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/results', methods=['POST'])
def search_city():

	#cityName = request.form['location']
    API_KEY = '9d14771c3de6d6095ae39fd27925e69f'# initialize your key here
    city = request.form['location']
    nation = request.form['country']
    #city = request.args.get('q')  # city name passed as argument

    # call API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&{nation}&APPID={API_KEY}'
    response = requests.get(url).json()

    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    # get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    current_city = response['name']
    territory = response['sys']['country']
    damp = response.get('main', {}).get('humidity')
    current_weather = response['weather'][0]['description']
    Wind = response.get('wind', {}).get('speed')
    if current_temperature:
        temp_celsius = round(current_temperature - 273.15, 2)
        return render_template('results.html',current_weather=current_weather, temp_celsius=temp_celsius,current_city=current_city, territory=territory,damp=damp,Wind=Wind)
    else:
        return f'Error getting temperature for {city.title()}'
     
    #return current_weather 

@app.route('/weather')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)