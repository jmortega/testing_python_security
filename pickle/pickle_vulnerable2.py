import os
import pickle
import yaml

user_input = input()
pickle.loads(user_input) #violation

with open(user_input) as exploit_file:
	contents = yaml.load(exploit_file) #violation