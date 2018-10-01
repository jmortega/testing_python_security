import os
import cPickle
import yaml

user_input = input()
cPickle.loads(user_input) #violation

with open(user_input) as exploit_file:
	contents = yaml.load(exploit_file) #violation