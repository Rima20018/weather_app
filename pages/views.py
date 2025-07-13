from django.shortcuts import render

weather_data = {
  'amman': {'city': 'Amman', 'country': 'Jordan', 'temp': '30°C', 'status': 'Sunny'},
  'cairo': {'city': 'Cairo', 'country': 'Egypt', 'temp': '33°C', 'status': 'Sunny'},
  'paris': {'city': 'Paris', 'country': 'France', 'temp': '22°C', 'status': 'Rainy'},
  'irbid': {'city': 'Irbid', 'country': 'Jordan', 'temp': '29°C', 'status': 'Cloudy'},
  'london': {'city': 'London', 'country': 'UK', 'temp': '20°C', 'status': 'Cloudy'}
}

def weather_search(request):
  result = None
  if (request.method == "GET"):
    query = request.GET.get('city')
    if (query):
      city_key = query.lower ()
      if city_key in weather_data:
        result = weather_data[city_key]
  return render (request, 'pages/temp_pages.html', {'result': result})ult})