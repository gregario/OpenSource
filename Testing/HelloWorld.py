import time
import sys

counter = 0
while True:
	print "hello world"
	time.sleep(1)
	print "count: " + str(counter)
	counter = counter + 1
	if counter >10:
		sys.exit(0)
