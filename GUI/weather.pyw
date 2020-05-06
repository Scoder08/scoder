import requests
api_key = "677f3a393bd163dce7f3daf4802157f1"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
inp=input()
complete_url = base_url + "appid=" + api_key + "&q=" + ''.join(inp)

response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
print(x['coord'])
