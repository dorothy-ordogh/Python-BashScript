#!/Users/dorothyordogh/anaconda/bin/python

import os

def main():
	with open('/Users/dorothyordogh/netusage.txt') as f:
		for line in f:
			if "Usage (Last 24 hours)" in line:
				istart = line.find('G inbound')
				numstring = istart - 4
				num = float(numstring)
				if num >= 6.70:
					cmd = """osascript -e 'tell app "Finder" to display dialog "If you watch any more Netflix, you are going to be put in INTERNET JAIL!!"'"""
					os.system(cmd)
				else:
					return 0
main()