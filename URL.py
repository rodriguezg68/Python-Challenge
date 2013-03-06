import webbrowser

#the hint was 2^38...2 to the 38th power...
site = 'http://www.pythonchallenge.com/pc/def/0.html'

print site

power = 2
count = 0
array = []

while count < 37:
	power *= 2
	count += 1

for number in str(power):
	array.append(chr(ord(number)))

string = ''.join(array)
newsite = site.replace('0', string)

print newsite

webbrowser.open(newsite)
