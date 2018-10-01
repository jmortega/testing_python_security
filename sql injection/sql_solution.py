import sqlite3
from rest_framework.decorators import api_view


def customSinkFunction(query):
	connection = sqlite3.connect("add some args here");
	return connection.execute(query) # sink

@api_view()
def customSourceFunction(request):
	user_input = request.GET['query']
	return user_input

def function():
	source = customSourceFunction()
	sanitizedQuery = source.replace("'", "''") # neutralization
	customSinkFunction(sanitizedQuery) # OK