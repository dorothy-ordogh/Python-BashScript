#!/Users/[user]/anaconda/bin/python
#Import os so a finder pop up can notify me
import os

def main():
	#Open file that contains usage levels
	with open('~/usage.txt') as f:
		for line in f:
			#If the line contains the usage level, then parse number and
			#compare to preset number (threshold)
			if "Usage (Last 24 hours)" in line:
				iend = line.find('G inbound')
				istart = iend -4
				numstring = line[istart:iend]
				num = float(numstring)
				if num >= 6.70:
					#Finder pop up to notify me of my internet usage with a funny message
					cmd = """osascript -e 'tell app "Finder" to display dialog "If you watch any more Netflix, you are going to be put in INTERNET JAIL!!"'"""
					os.system(cmd)
				else:
					return 0
main()
