# !/usr/bin/env python
# L0V3R IN MY@NM@R
def c2t(c):
	# if 31 < int(c) < 128:
	if int(c) in range(32,128):
		print c + " chr is convert to ascii text = '" + chr(int(c)) + "'"
def main():
	number = raw_input("Type any word to convert! : ")
	if number == '' :
		return main()
	if number.isdigit():
		c2t(number)
	else:
		print "Type a number!"
if __name__ == '__main__':
	main()