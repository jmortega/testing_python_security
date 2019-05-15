from flask import Flask, request, redirect
import re

#The following example code checks that a URL redirection will reach the example.com domain, or one of its subdomains.

#The unsafe check is easy to bypass because the unescaped . allows for any character before example.com, 
#effectively allowing the redirect to go to an attacker-controlled domain such as wwwXexample.com.

#The safe check closes this vulnerability by escaping the . so that URLs of the form wwwXexample.com are rejected.

app = Flask(__name__)

UNSAFE_REGEX = re.compile("(www|beta).example.com/")
SAFE_REGEX = re.compile(r"(www|beta)\.example\.com/")

@app.route('/some/path/bad')
def unsafe(request):
    target = request.args.get('target', '')
    if UNSAFE_REGEX.match(target):
        return redirect(target)
		
@app.route('/some/path/good')
def safe(request):
    target = request.args.get('target', '')
    if SAFE_REGEX.match(target):
        return redirect(target)