#!/Users/[user]/anaconda/bin/python

import os

def main():
	with open('/Users/[user]/usage.txt') as f:
		for line in f:
			if "Usage (Last 24 hours)" in line:
				iend = line.find('G inbound')
				istart = iend -4
				numstring = line[istart:iend]
				num = float(numstring)
				if num >= 6.70:
					cmd = """osascript -e 'tell app "Finder" to display dialog "If you watch any more Netflix, you are going to be put in INTERNET JAIL!!"'"""
					os.system(cmd)
				else:
					return 0
main()
