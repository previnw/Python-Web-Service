from random import sample
from pydub import AudioSegment
from pydub.playback import play
import json

nums = sample(range(1,5), 2)

initial_string = {"numbers": nums}
json_data = json.dumps(initial_string)

temp_dict = {}
filtered_str = json_data.replace(" ", "")
filtered_str = filtered_str.strip("}").strip("{").strip('"numbers"').strip(":").strip("]").strip("[")
euros_str,cents_str = filtered_str.split(",")
# output_str = euros_str + " euros and " + cents_str + " cents"
# print(type(output_str))
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
print(euros, "euros and", cents, "cents")

ivr.export("./mp3s/ivr.mp3", format="mp3")
datMoney = AudioSegment.from_file("./mp3s/ivr.mp3", format="mp3")
play(datMoney)
print("Done")



# print(json_data)



