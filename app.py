from flask import Flask, request, jsonify
from Excel import *
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
	twitter_account = request.files['twitter_account']
	gmail_account = request.files['gmail_account']
	twitter_account.save("./uploads/" + "twitter.xlsx")
	gmail_account.save("./uploads/" + "gmail.xlsx")
	rows = getSheet(fileName="./uploads/twitter.xlsx")
	return rows

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
