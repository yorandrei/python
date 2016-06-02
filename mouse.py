import sys
pipe = open('/dev/input/mouse0', 'r')
while 1:
	for character in pipe.read(1):
		sys.stdout.write(repr(character))
		sys.stdout.flush()
