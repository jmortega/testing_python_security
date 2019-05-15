from flask import Flask
from flask import request, render_template_string, render_template
app = Flask(__name__)

TEMPLATE = '''
<html>
<head><title> Hello {{ person.name }} </title></head>
<body> Hello FOO </body>
</html>
'''
@app.route('/hello-flask')
def hello_flask():
	person = {'name':"world", 'secret':'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	# Replace FOO with person's name
	template = TEMPLATE.replace("FOO", person['name'])
	return render_template_string(template, person=person)

if __name__ == "__main__":
	app.run(debug=True)

#The URL used for this attack is: http://127.0.0.1:5000/hello-flask?name=Tom<script>alert("You are under attack!")</script>