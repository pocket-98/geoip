#!/usr/bin/python3

import os
import sys
import argparse
import json
from urllib.request import urlopen

version = "1.0"
url = "http://freegeoip.net/json/"
sep = ":  "

def pretty(snake_case):
	capitalize = lambda word: word[0].upper() + word[1:]
	snake_case = snake_case.replace("ip", "IP")
	words = [capitalize(word) for word in snake_case.split("_")]
	prettified = " ".join(words)
	return prettified

def get_term_width():
	return int(os.popen('stty size', 'r').read().split()[1])

def get_ip_info(ip):
	info = {}
	try:
		info = json.loads(urlopen(url + ip).read().decode("utf-8"))
	except Exception as e:
		print("error: couldn't load info for '" + ip + "'", file=sys.stderr)
	return info

def main(argv):
	parse = argparse.ArgumentParser(description="Extract IP or domain information using freegeoip.net")
	parse.add_argument("-v", "--version", action="version", version="%(prog)s " + version)
	parse.add_argument("ips", metavar="<ip>", nargs="+", help="ip address or domain")
	args = parse.parse_args(argv)

	for ip in args.ips:
		print()
		info = get_ip_info(ip)
		half_width = get_term_width() // 2
		for property, value in info.items():
			print("%*s" % (half_width, pretty(property) + sep) + str(value))
		print()

if __name__ == "__main__":
	main(sys.argv[1:])
