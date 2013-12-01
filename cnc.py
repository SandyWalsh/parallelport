import parallel
import time

p = parallel.Parallel()     # open LPT1
data = 0b11000000
while True:
	print "Setting HIGH"
	p.setData(data)  # Enable D7 (9), D6 (8)
	p.setAutoFeed(1) # Enable pin 14

	step = 0b11111111
	for x in range(100):
		p.setData(step)
		time.sleep(.01)
		p.setData(data)

	print "Setting LOW"
	p.setData(0)     # Turn it all off.
	p.setAutoFeed(0)

	time.sleep(2)
	# and repeat