from flask import Flask , request , make_response

# using escape function
from flask import escape

app = Flask(__name__)

@app.route ('/XSS_param',methods =['GET' ])
def XSS():
	param = escape(request.args.get('param','not set'))
	html = open('templates/XSS_param.html ').read()
	resp = make_response(html.replace('{{ param}}',param))
	return resp

if __name__ == ' __main__ ':
	app.run(debug = True)
