Weather Forecast API Website

**Overview**
This is a weather forecast website built using Django and Django Rest Framework (DRF). It allows users to enter a city name and get the current weather information along with a forecast. The website uses the OpenWeatherMap API to fetch weather data.

**Features**
Search for current weather conditions by city.
View weather forecast.
Weather icons representing different weather conditions.
Responsive design using Bootstrap 4.

**Setup Instructions**

Prerequisites
Python 3.6+
Django 3.2+
Django Rest Framework
OpenWeatherMap API key

**Installation**

Clone the repository:

bash
git clone https://github.com/yourusername/weather-forecast-website.git
cd weather-forecast-website
Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
**Install the required packages:**

bash
pip install -r requirements.txt
Add your OpenWeatherMap API key to your Django settings:

python
# settings.py
OPENWEATHERMAP_API_KEY = 'your_api_key_here'
Run the Django server:

bash
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000 to view the website.

API Endpoints
The website provides an API endpoint to get weather information for a specific city. The API can be tested using the Postman tool.

Endpoint
GET /api/weather/<city>/: Get the current weather and forecast for the specified city.

Using **Postman** to Test the API
Install Postman: Download and install the Postman tool from the official website.

Create a new request:

Open Postman and create a new request.
Set the request type to GET.
Enter the API endpoint URL: http://127.0.0.1:8000/api/weather/<city>/ (replace <city> with the desired city name).
Send the request:

Click the Send button to send the request.
View the response in the Postman interface.
Example Usage
To get the weather information for "London", you can use the following URL in Postman:

ruby
GET http://127.0.0.1:8000/api/weather/London/
You should receive a JSON response with the current weather and forecast for London.

Project Structure
weather_project/: Main project directory.
weather/: App directory containing views, serializers, and templates.
templates/weather_form.html: HTML template for the weather form.
static/css/styles.css: CSS file for styling the webpage.

**Future Enhancements**
Improve UI/UX with more interactive features.
Add user authentication and profiles.
Save favorite cities for users.
Display additional weather information such as humidity, wind speed, etc.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing
**Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
