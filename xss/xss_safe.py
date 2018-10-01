from flask import Flask
from flask import request, render_template_string, render_template

app = Flask(__name__)

TEMPLATE = '''
<html>
<head><title> Hello {{ person.name | e }} </title></head>
<body> Hello {{ person.name | e }} </body>
</html>
'''

@app.route('/render_template')
def render_template():
	person = {'name':"world", 'secret':
	'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}

	if request.args.get('name'):
		person['name'] = request.args.get('name')
	
	return render_template_string(TEMPLATE, person=person)

if __name__ == "__main__":
	app.run(debug=True)
