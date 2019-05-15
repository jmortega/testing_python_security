from flask import Flask, request, redirect
from urllib.parse import urlparse
app = Flask(__name__)

#The following example code checks that a URL redirection will reach the example.com domain.
#The first two examples show unsafe checks that are easily bypassed. 
#In unsafe1 the attacker can simply add example.com anywhere in the url. For example, http://evil-example.net/example.com.
#In unsafe2 the attacker must use a hostname ending in example.com, but that is easy to do. For example, http://benign-looking-prefix-example.com.
#The second two examples show safe checks. 
#In safe1, a white-list is used. Although fairly inflexible, this is easy to get right and is most like to be safe.
#In safe2, urlparse is used to parse the URL, then the hostname is checked to make sure it ends with .example.com.

# Not safe, as "evil-example.net/example.com" would be accepted
@app.route('/some/path/bad1')
def unsafe1(request):
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)

# Not safe, as "benign-looking-prefix-example.com" would be accepted
@app.route('/some/path/bad2')
def unsafe2(request):
    target = request.args.get('target', '')
    if target.endswith("example.com"):
        return redirect(target)

#Simplest and safest approach is to use a white-list
@app.route('/some/path/good1')
def safe1(request):
    whitelist = [
        "example.com/home",
        "example.com/login",
    ]
    target = request.args.get('target', '')
    if target in whitelist:
        return redirect(target)

#More complex example allowing sub-domains.
@app.route('/some/path/good2')
def safe2(request):
    target = request.args.get('target', '')
    host = urlparse(target).hostname
    #Note the '.' preceding example.com
    if host and host.endswith(".example.com"):
        return redirect(target)