from PIL import Image
import binascii
import hashlib

from .models import PatientSteggedDetails

def rgb2hex(r, g, b):
	hexCode = '#%02x%02x%02x' % (r, g, b)
	# print(hexCode)
	return hexCode

def hex2rgb(hexcode):
	return tuple(map(ord, hexcode[1:].decode('hex')))

def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

def bin2str(binary):
	message = binascii.unhexlify('%x' % int('0b'+binary,2))
	# print(str(message))
	return message.decode('utf-8')

def encode(hexcode, digit):
	if hexcode[-1] in ('0','1', '2', '3', '4', '5'):
		hexcode = hexcode[:-1] + digit
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

def retr(filename):
	img = Image.open(filename)
	binary = ''

	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		# print(img)
		datas = img.getdata()
		# print(datas)

		for item in datas:

			digit = decode(rgb2hex(item[0],item[1],item[2]))
			if digit == None:
				pass
			else:
				binary = binary + digit
				if (binary[-16:] == '1111111111111110'):
					#print "Success"
					# print(binary[:-16])
					return bin2str(binary[:-16])

		return bin2str(binary)
	return 1

def hide(filename, message):
	img = Image.open(filename)
	binary = str2bin(message) + '1111111111111110'
	# print(binary) - check
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()

		newData = []
		digit = 0
		# temp = ''
		for item in datas:
			# print(item) - check
			if digit < len(binary):
				newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
				# print(newpix)
				if newpix is None:
					newData.append(item)
				else:
					r, g, b = hex2rgb(newpix)
					newData.append((r,g,b,255))
					digit += 1
			else:
				# print(newData)
				newData.append(item)
		# print(newData)
		img.putdata(newData)
		#randNum = rand()
		#keyNum = randNum[random.randint(0,10)]
		#keyPic = filename[:len(filename) - 4] + str(keyNum) + ".png"
		img.save(filename[:len(filename)-4] + "-key.png", "PNG")
		# print("Picture key is saved @ location " + filename + " .")
		#print "Please rename the picture file, removing the pin, for safety!"
		#print "Your pin number is " + str(keyNum)
		return 0

	return 1
