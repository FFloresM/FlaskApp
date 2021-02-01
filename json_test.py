import json

try:
	with open('data/data.json') as f:
		data = json.load(f)
		print(data["usuario"])
except:
	raise "error al abrir archivo"