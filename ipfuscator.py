#!/usr/bin/env python

from argparse import ArgumentParser
import struct
import re, random


__version__ = '0.1.0'


def get_args():
	parser = ArgumentParser()
	parser.add_argument('ip', help='The IP to perform IPFuscation on')
	parser.add_argument('-o', '--output', help='Output file')
	return parser.parse_args()

def banner():
 	print(
	'''
IPFuscator
Author: Vincent Yiu (@vysecurity)
https://www.github.com/vysec/IPFuscator
Version: {}

    '''.format(__version__))

def checkIP(ip):
	m = re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\Z',ip)
	
	if m:
		# Valid IP format
		parts = ip.split('.')
		if len(parts) == 4:
			# Valid IP
			for i in parts:
					if int(i) > 255 or int(i) < 0:
						return False
			return True
		else:
			 return False
	else:
		return False

def printOutput(ip):
	parts = ip.split('.')

	decimal = int(parts[0]) * 16777216 + int(parts[1]) * 65536 + int(parts[2]) * 256 + int(parts[3])
	#hexadecimal = "0x%02X%02X%02X%02X" % (int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]))
	#octal = oct(decimal)
	print(
    '''
Decimal:\t{}
Hexadecimal:\t{}    
Octal:\t\t{}

IPv4 in IPv6: [::ffff:{}]
IPv4 in IPv6: [0:0:0:0:0:ffff:{}]
	'''.format(decimal, 
	            hex(decimal), 
			    oct(decimal),
				ip,
				ip))

	hexparts = []
	octparts = []

	for i in parts:
		hexparts.append(hex(int(i)))
		octparts.append(oct(int(i)))

	print(
	'''
Full Hex:\t{}
Full Oct:\t{}
	'''.format('.'.join(hexparts),
	('.'.join(octparts))))

	print("Random Padding: ")

	randhex = ""

	for i in hexparts:
		randhex += i.replace('0x','0x' + '0' * random.randint(1,30)) + '.'

	randhex = randhex[:-1]
	print("Hex:\t{}".format(randhex))

	randoct = ""
	for i in octparts:
		randoct += '0' * random.randint(1,30) + i + '.'

	randoct = randoct[:-1]

	print("Oct:\t{}".format(randoct))

	print("")
	print("Radom base:")

	randbase = []

	count = 0
	while count < 5:
		randbaseval = ""
		for i in range(0,4):
			val = random.randint(0,2)
			if val == 0:
				# dec
				randbaseval += parts[i] + '.'
			elif val == 1:
				# hex
				randbaseval += hexparts[i] + '.'
			else:
				randbaseval += octparts[i] + '.'
				# oct
		randbase.append(randbaseval[:-1])
		print("#{}:\t{}".format(count+1, randbase[count]))
		count += 1

	print("")
	print("Random base with random padding:")

	randbase = []

	count = 0
	while count < 5:
		randbaseval = ""
		for i in range(0,4):
			val = random.randint(0,2)
			if val == 0:
				# dec
				randbaseval += parts[i] + '.'
			elif val == 1:
				# hex
				randbaseval += hexparts[i].replace('0x', '0x' + '0' * random.randint(1,30)) + '.'
			else:
				randbaseval += '0' * random.randint(1,30) + octparts[i] + '.'
				# oct
		randbase.append(randbaseval[:-1])
		print("#{}:\t{}".format(count+1, randbase[count]))
		count += 1


def main():
	banner()

	args = get_args()

	if checkIP(args.ip):
		print("IP Address:\t{}".format(args.ip))
		printOutput(args.ip)
	else:
		print("[!] Invalid IP format: {}".format(args.ip))


if __name__ == '__main__':
	main()
