#hint: K -> M, O -> Q, E -> G

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

array = []

for letter in message:
	if letter == 'y' or letter == 'z':
		array.append(chr(ord(letter) - 24))
	elif letter == '.' or letter == "'" or letter == '(' or letter == ')':
		array.append(letter)
	else:
		array.append(chr(ord(letter) + 2))
string = ''.join(array)
split = string.split('"')
string = ' '.join(split)
print string
