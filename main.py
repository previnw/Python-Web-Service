from flask import Flask, render_template, url_for, jsonify, request, redirect, send_file, send_from_directory
from random import sample
import requests
import json
import sys
import ffmpeg
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__, static_folder="static")

# @app.route('/numbers')
# def numbers():
#     return jsonify({'numbers' : sample(range(1,5), 2)})

@app.route('/')
def get():
	
	# uri = 'http://127.0.0.1:5000/numbers'
	# uri = jsonify({'numbers' : sample(range(1,5), 2)})
	# uResponse = requests.get(uri)
	# Jresponse = uResponse.text
	# data = json.loads(Jresponse)
	# jsonData = json.dumps(data)

	nums = sample(range(1,5), 2)
	initial_string = {"numbers": nums}
	json_data = json.dumps(initial_string)

	filtered_str = json_data.replace(" ", "")
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
		euros_mp3 = AudioSegment.from_mp3("static/1euro.mp3")
		# euros = AudioSegment.from_file("./mp3s/1euro.mp3", format="mp3")

	elif euros == 2:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("static/2euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/2euros.mp3", format="mp3")

	elif euros == 3:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("static/3euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/3euros.mp3", format="mp3")

	elif euros == 4:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("static/4euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/4euros.mp3", format="mp3")

	elif passNumbers[0] == 5:
		# print(passNumbers[0])
		euros_mp3 = AudioSegment.from_mp3("static/5euros.mp3")
		# euros = AudioSegment.from_file("./mp3s/5euros.mp3", format="mp3")

	and_mp3 = AudioSegment.from_file("static/and.mp3", format="mp3")

	if cents == 1:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("static/1cent.mp3")
		# cents = AudioSegment.from_file("./mp3s/1cent.mp3", format="mp3")

	elif cents == 2:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("static/2cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/2cents.mp3", format="mp3")

	elif cents == 3:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("static/3cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/3cents.mp3", format="mp3")

	elif cents == 4:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("static/4cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/4cents.mp3", format="mp3")

	elif cents == 5:
		# print(passNumbers[0])
		cents_mp3 = AudioSegment.from_mp3("static/5cents.mp3")
		# cents = AudioSegment.from_file("./mp3s/5cents.mp3", format="mp3")

	ivr = euros_mp3 + and_mp3 + cents_mp3

	with counter.get_lock():
		counter.value += 1

	# return jsonify(count=counter.value)

	temp = str(counter.value)
	ivr_id = "ivr" + temp + ".mp3"
	ivr_url = "static/" + ivr_id 

	ivr.export(ivr_url, format="mp3")
	# datMoney = AudioSegment.from_file("./mp3s/ivr.mp3", format="mp3")
	# play(datMoney)

	return send_from_directory(app.static_folder, ivr_id)

	# return jsonify(value=ivr_url)

# @app.route('/app')
# def app():
# 	return render_template('index.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.run(debug=True)