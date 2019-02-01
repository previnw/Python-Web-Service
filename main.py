from flask import Flask, render_template, request, jsonify, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

# from pydub import AudioSegment
# from pydub.playback import play
# from random import sample

# def randomNumbers():
# 	nums = sample(range(1, 5), 2)
# 	# print(nums)
# 	return nums

# def assignNumbersToMp3(passNumbers):
# 	print(passNumbers)
# 	if passNumbers[0] == 1:
# 		# print(passNumbers[0])
# 		euros = AudioSegment.from_mp3("./mp3s/1euro.mp3")
# 		# euros = AudioSegment.from_file("./mp3s/1euro.mp3", format="mp3")

# 	elif passNumbers[0] == 2:
# 		# print(passNumbers[0])
# 		euros = AudioSegment.from_mp3("./mp3s/2euros.mp3")
# 		# euros = AudioSegment.from_file("./mp3s/2euros.mp3", format="mp3")

# 	elif passNumbers[0] == 3:
# 		# print(passNumbers[0])
# 		euros = AudioSegment.from_mp3("./mp3s/3euros.mp3")
# 		# euros = AudioSegment.from_file("./mp3s/3euros.mp3", format="mp3")

# 	elif passNumbers[0] == 4:
# 		# print(passNumbers[0])
# 		euros = AudioSegment.from_mp3("./mp3s/4euros.mp3")
# 		# euros = AudioSegment.from_file("./mp3s/4euros.mp3", format="mp3")

# 	elif passNumbers[0] == 5:
# 		# print(passNumbers[0])
# 		euros = AudioSegment.from_mp3("./mp3s/5euros.mp3")
# 		# euros = AudioSegment.from_file("./mp3s/5euros.mp3", format="mp3")

# 	andYo = AudioSegment.from_file("./mp3s/and.mp3", format="mp3")

# 	if passNumbers[1] == 1:
# 		# print(passNumbers[0])
# 		cents = AudioSegment.from_mp3("./mp3s/1cent.mp3")
# 		# cents = AudioSegment.from_file("./mp3s/1cent.mp3", format="mp3")

# 	elif passNumbers[1] == 2:
# 		# print(passNumbers[0])
# 		cents = AudioSegment.from_mp3("./mp3s/2cents.mp3")
# 		# cents = AudioSegment.from_file("./mp3s/2cents.mp3", format="mp3")

# 	elif passNumbers[1] == 3:
# 		# print(passNumbers[0])
# 		cents = AudioSegment.from_mp3("./mp3s/3cents.mp3")
# 		# cents = AudioSegment.from_file("./mp3s/3cents.mp3", format="mp3")

# 	elif passNumbers[1] == 4:
# 		# print(passNumbers[0])
# 		cents = AudioSegment.from_mp3("./mp3s/4cents.mp3")
# 		# cents = AudioSegment.from_file("./mp3s/4cents.mp3", format="mp3")

# 	elif passNumbers[1] == 5:
# 		# print(passNumbers[0])
# 		cents = AudioSegment.from_mp3("./mp3s/5cents.mp3")
# 		# cents = AudioSegment.from_file("./mp3s/5cents.mp3", format="mp3")

# 	ivr = euros + andYo + cents

# 	return ivr

# def mp3Play(mp3file):

# 	mp3file.export("./mp3s/ivr.mp3", format="mp3")
# 	datMoney = AudioSegment.from_file("./mp3s/ivr.mp3", format="mp3")
# 	play(datMoney)
# 	print("Done")


# # Initial manual mp3 testing
# # def mp3Concatenate():
	
# # 	twoEuros = AudioSegment.from_mp3("./mp3s/2euros.mp3")
# # 	andYo = AudioSegment.from_mp3("./mp3s/and.mp3")
# # 	twoCents = AudioSegment.from_mp3("./mp3s/2cents.mp3")
# # 	ivr = twoEuros + andYo + twoCents
# # 	ivr.export("./mp3s/ivr.mp3", format="mp3")
# # 	sound = AudioSegment.from_file("./mp3s/ivr.mp3", format="mp3")
# # 	play(sound)
	
# # 	print("Done")

# def main():
#     # mp3Concatenate()
#     p1 = randomNumbers()
#     p2 = assignNumbersToMp3(p1)
#     mp3Play(p2)

# if __name__ == '__main__':
#     main()