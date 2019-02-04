from flask import Flask, render_template, url_for, jsonify, request, redirect
from random import sample
import requests
import json
import sys
from pydub import AudioSegment
from pydub.playback import play
app = Flask(__name__)

@app.route('/numbers')
def numbers():
    return jsonify({'numbers' : sample(range(1,5), 2)})

@app.route('/get')
def get():
	uri = 'http://127.0.0.1:5000/numbers'
	uResponse = requests.get(uri)
	Jresponse = uResponse.text
	data = json.loads(Jresponse)
	jsonData = json.dumps(data)

	filtered_str = jsonData.replace(" ", "")
	filtered_str = filtered_str.strip("}").strip("{").strip('"numbers"').strip(":").strip("]").strip("[")
	euros_str,cents_str = filtered_str.split(",")

	# for thing in filtered_str:
	# 	key, value = thing.split(":")
	# 	temp_dict[key] = value

	output_str = euros_str + " euros and " + cents_str + " cents"

	euros = int(euros_str)
	cents = int(cents_str)

	if euros == 1:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("./mp3s/1euro.mp3")
		# euros = AudioSegment.from_file("./mp3s/1euro.mp3", format="mp3")

	elif euros == 2:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("./mp3s/2euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/2euros.mp3", format="mp3")

	elif euros == 3:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("./mp3s/3euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/3euros.mp3", format="mp3")

	elif euros == 4:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("./mp3s/4euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/4euros.mp3", format="mp3")

	elif passNumbers[0] == 5:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("./mp3s/5euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/5euros.mp3", format="mp3")

	and_mp3 = AudioSegment.from_file("./mp3s/and.mp3", format="mp3")

	if cents == 1:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("./mp3s/1cent.mp3")
		# cents = AudioSegment.from_file("./mp3s/1cent.mp3", format="mp3")

	elif cents == 2:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("./mp3s/2cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/2cents.mp3", format="mp3")

	elif cents == 3:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("./mp3s/3cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/3cents.mp3", format="mp3")

	elif cents == 4:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("./mp3s/4cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/4cents.mp3", format="mp3")

	elif cents == 5:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("./mp3s/5cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/5cents.mp3", format="mp3")

	ivr = euros_mp3 + and_mp3 + cents_mp3

	ivr.export("./mp3s/ivr.mp3", format="mp3")
	datMoney = AudioSegment.from_file("./mp3s/ivr.mp3", format="mp3")
	play(datMoney)

	return output_str

if __name__ == '__main__':
    app.run(debug=True)