import os
import yaml

user_input = input()

with open(user_input) as exploit_file:
	contents = yaml.safe_load(exploit_file) #ok