#!/usr/bin/env python

from argparse import ArgumentParser
import re, random


__version__ = '1.0.0'


def get_args():
	parser = ArgumentParser()
	parser.add_argument('ip', help='The IP to perform IPFuscation on')
	parser.add_argument('-o', '--output', help='Output file')
	return parser.parse_args()


def banner():
	print("IPFuscator")
	print("Author: Vincent Yiu (@vysecurity)")
	print("https://www.github.com/vysecurity/IPFuscator")
	print("Version: {}".format(__version__))
	print("")


def check_ip(ip):
	m = re.fullmatch('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip)

	if m:
		parts = ip.split('.')
		if len(parts) == 4 and all(0 <= int(p) <= 255 for p in parts):
			return True
	return False


def print_output(ip):
	parts = ip.split('.')

	decimal = int(parts[0]) * 16777216 + int(parts[1]) * 65536 + int(parts[2]) * 256 + int(parts[3])
	print("\nDecimal:\t{}".format(decimal))
	print("Hexadecimal:\t{}".format(hex(decimal)))
	print("Octal:\t\t{}".format(oct(decimal)))

	hexparts = [hex(int(i)) for i in parts]
	octparts = [oct(int(i)) for i in parts]

	print ("\nFull Hex:\t{}".format('.'.join(hexparts)))
	print ("Full Oct:\t{}".format('.'.join(octparts)))

	print ("\nRandom Padding: ")

	randhex = '.'.join([i.replace('0x','0x' + '0' * random.randint(1,30)) for i in hexparts])
	print ("Hex:\t{}".format(randhex))

	randoct = '.'.join(['0' * random.randint(1,30) + i for i in octparts])
	print ("Oct:\t{}".format(randoct))

	print ("\nRandom base:")

	randbase = []
	for _ in range(5):
		randbaseval = []
		for i in range(4):
			choices = [parts[i], hexparts[i], octparts[i]]
			randbaseval.append(random.choice(choices))
		randbase.append('.'.join(randbaseval))

	for i, base in enumerate(randbase):
		print("#{}:\t{}".format(i+1, base))

	print ("\nRandom base with random padding:")

	randbase = []
	for _ in range(5):
		randbaseval = []
		for i in range(4):
			val = random.choice([0, 1, 2])
			if val == 0:
				randbaseval.append(parts[i])
			elif val == 1:
				randbaseval.append(hexparts[i].replace('0x', '0x' + '0' * random.randint(1,30)))
			else:
				randbaseval.append('0' * random.randint(1,30) + octparts[i])
		randbase.append('.'.join(randbaseval))

	for i, base in enumerate(randbase):
		print("#{}:\t{}".format(i+1, base))


def main():
	banner()

	args = get_args()

	if check_ip(args.ip):
		print("IP Address:\t{}".format(args.ip))
		print_output(args.ip)
	else:
		print("[!] Invalid IP format: {}".format(args.ip))


if __name__ == '__main__':
	main()
