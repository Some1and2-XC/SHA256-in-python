#!/usr/bin/env python



# Moves to the Right
def SHR(inputNumber, it):
	return "0" * (it) + inputNumber[0:- it]


# Circular moves to the right
def ROTR(inputNumber, it):
	return str(inputNumber)[- it:-1] + str(inputNumber[-1]) + str(inputNumber)[0:- it]


# Exclusive or
def XOR(inputNumber1, inputNumber2):
	outNo = ""
	inputNumber1 = str(inputNumber1)
	inputNumber2 = str(inputNumber2)
	for i in range(len(inputNumber1)):
		if inputNumber1[i] == inputNumber2[i]:
			outNo += "0"
		else:
			outNo += "1"
	return outNo


# Adds binary
def ADD(inputNumber1, inputNumber2):
	carry = 0
	length = len(inputNumber1)
	outStr = ""
	inputNumber1 = inputNumber1[::-1]
	inputNumber2 = inputNumber2[::-1]

	for i in range(length):
		no = int(inputNumber1[i]) + int(inputNumber2[i]) + carry

		if no == 3:
			outStr += "1"
			carry = 1
		elif no == 2:
			outStr += "0"
			carry = 1
		elif no == 1:
			outStr += "1"
			carry = 0
		elif no == 0:
			outStr += "0"
			carry = 0
	return outStr[::-1]


def CHOICE(inputNumber1, inputNumber2, inputNumber3):
	outStr = ""
	inputNumber1 = str(inputNumber1)
	inputNumber2 = str(inputNumber2)
	inputNumber3 = str(inputNumber3)

	for i in range(len(inputNumber1)):
		if inputNumber1[i] == 0:
			outStr += inputNumber2[i]
		else:
			outStr += inputNumber3[i]

	return outStr


def MAJOR(inputNumber1, inputNumber2, inputNumber3):
	outStr = ""
	inputNumber1 = str(inputNumber1)
	inputNumber2 = str(inputNumber2)
	inputNumber3 = str(inputNumber3)
	for i in range(len(inputNumber1)):
		if int(inputNumber1[i]) + int(inputNumber2[i]) + int(inputNumber3[i]) >= 2:
			outStr += "1"
		else:
			outStr += "2"
	return outStr


# zeroSplit just asks if the number should be seperated by 0's
def makeBin(inputList, zeroSplit):
	outStr = ""
	for i in range(len(inputList) - 1, -1, -1):
		quo = inputList[i]
		while True:
			outStr += str(quo % 2)
			quo = int(quo / 2)
			if quo == 0:
				if zeroSplit:
					outStr += "0"
				break
	return outStr[::-1]

def makeOneBin(inputNo):
	outStr = ""
	quo = int(inputNo)
	while True:
		outStr += str(quo % 2)
		quo = int(quo / 2)
		if quo == 0:
			break
	return outStr[::-1]


	return outStr[::-1]


def line():
	print("-" * 50)
	return


def o0(input):
	list = [input]
	list.append(ROTR(list[0], 7))
	list.append(ROTR(list[0], 18))
	list.append(SHR(list[0], 3))
	list.append(XOR(list[1], list[2]))
	list.append(XOR(list[3], list[4]))
	# for i in range(0, len(list)):
	#	print(list[i] + " " + str(i))
	list = list[5]
	return list


def o1(input):
	list = [input]
	list.append(ROTR(list[0], 17))
	list.append(ROTR(list[0], 19))
	list.append(SHR(list[0], 10))
	list.append(XOR(list[1], list[2]))
	list.append(XOR(list[3], list[4]))
	# for i in range(0, len(list)):
	# 	print(list[i] + " " + str(i))
	list = list[5]
	return list


def O0(input):
	list = [input]
	list.append(ROTR(list[0], 2))
	list.append(ROTR(list[0], 13))
	list.append(ROTR(list[0], 22))
	list.append(XOR(list[1], list[2]))
	list.append(XOR(list[3], list[4]))
	# for i in range(0, len(list)):
	# 	print(list[i] + " " + str(i))
	list = list[5]
	return list

def O1(input):
	list = [input]
	list.append(ROTR(list[0], 6))
	list.append(ROTR(list[0], 11))
	list.append(ROTR(list[0], 25))
	list.append(XOR(list[1], list[2]))
	list.append(XOR(list[3], list[4]))
	# for i in range(0, len(list)):
	# 	print(list[i] + " " + str(i))
	list = list[5]
	return list


def fixLen(input, exLen):
	return "0" * (exLen - len(str(input))) + str(input)


def bin2char(inputNo):
	chars = "0123456789abcdef"
	inputNo = str(inputNo)
	out = []
	for i in range(0, len(inputNo), 4):
		out.append(chars[int(inputNo[i:i + 4], 2)])
	return out

#-----------------------------------------------------------------

# line()

text = input("Message:")
print("-" * 50)
text = [ord(text[i]) for i in range(len(text))]
print("Bytes: " + str(text))
text = makeBin(text, True)
print("Message: " + text)
input()

line()
# Adds a "1" to the data for a seperator for the 0 padding
text += "1"
print("Padding: " + str(len(text)))
print("Has to make message 512 long minus 64 bits for encoding message length: ")
line()
lengthToAdd = makeBin([len(text)], False)
if lengthToAdd[-1] == "0":
	lengthToAdd = lengthToAdd[0:-1] + "1"
else:
	lengthToAdd = lengthToAdd[0:-1] + "0"
amntOfBlocks = int((len(text) + 64) / 512) + 1

text += "0" * (512 * amntOfBlocks - len(text) - len(lengthToAdd))
text += lengthToAdd

tempStr = text
text = []
for i in range(amntOfBlocks):
	text.append(tempStr[512 * i:512 * (i + 1)])
del tempStr
del amntOfBlocks

print(text)
input()

# Splits text into blocks of 16 Characters
for j in range(len(text)):
	text[j] = [text[j][32 * i:32 * (i + 1)] for i in range(16)]

if False:
	for i in range(len(text)):
		print(str(i), end="\r")
		line()
		for j in range(16):
			print(text[i][j] + " " + str(j))
	line()
for i in range(len(text)):
	for j in range(16, 64):
		if j >= 16:
			text[i].append(ADD(ADD(text[i][j - 16], o0(text[i][j - 15])), ADD(o1(text[i][j - 2]), text[i][j - 7])))
if False:
	for i in range(len(text)):
		line()
		print(str(i) * 10)
		line()
		for j in range(64):
			print(text[i][j] + " " + str(j))
	line()

# Adds Constants (Squares of Primes)
dataReg = []
i = 2
constants = []
while len(constants) < 64:
	isPrime = True

	for j in range(2, i):
		if int(i / j) == i / j and i != j:
			isPrime = False
			break
	if isPrime is True:
		constants.append(i ** (1/3))
	i += 1
for i in range(len(constants)):
	constants[i] = makeOneBin(str(int(float("0" + str(constants[i])[1:]) * 2 ** 32)))
	constants[i] = "0" * (32 - len(constants[i])) + constants[i]

while len(dataReg) < 8:
	isPrime = True

	for j in range(2, i):
		if int(i / j) == i / j and i != j:
			isPrime = False
			break
	if isPrime is True:
		dataReg.append(i ** (1/2))
	i += 1
print(dataReg)
line()
# Remove First Number (only works if number is less than 10)
for i in range(len(dataReg)):
	dataReg[i] = makeOneBin(str(int(float("0" + str(dataReg[i])[1:]) * 2 ** 32)))
	dataReg[i] = "0" * (32 - len(dataReg[i])) + dataReg[i]
	print(dataReg[i] + " | " + str(len(dataReg[i])))
line()
# Compression
"""
T1 = fixLen(ADD(ADD(ADD(CHOICE(dataReg[4], dataReg[5], dataReg[6]), O1(dataReg[4])), dataReg[7]), constants[0]), 32)
T2 = fixLen(ADD(MAJOR(dataReg[0], dataReg[1], dataReg[2]), O0(dataReg[0])), 32)
del dataReg[7]
dataReg.insert(0, ADD(T1, T2))
dataReg[4] = ADD(dataReg[4], T1)
"""
for i in range(len(text)):
	for j in range(len(text[0])):
		T1 = fixLen(ADD(ADD(ADD(ADD(CHOICE(dataReg[4], dataReg[5], dataReg[6]), O1(dataReg[4])), dataReg[7]), text[i][j]), constants[j]), 32)
		T2 = fixLen(ADD(MAJOR(dataReg[0], dataReg[1], dataReg[2]), O0(dataReg[0])), 32)
		del dataReg[7]
		dataReg.insert(0, ADD(T1, T2))
		dataReg[4] = ADD(dataReg[4], T1)


text = []
for i in range(len(dataReg)):
	text.append(bin2char(dataReg[i]))
input(text)
line()
text = "".join("".join(str(text[i][j]) for j in range(len(text[i]))) for i in range(len(text)))
input(text)
print(dataReg)

# /home/some1and2/Desktop/In\ development/Pass
# need to make all the constants start to exist! need to add constant to T1
