file = open("./orc.txt", "r")
search = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
array = []
for line in file:
	string = line
	for char in string:
		for letter in search:
			if char == letter:
				array.append(char)
answer = ''.join(array)
print answer	
