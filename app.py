from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	# flask cant return dictionries but strings only.
	# jsonify function is converting the dictionery into a valid json string
	return jsonify({'message':'Hello, world!'})

if __name__=='__main__':
	app.run()
