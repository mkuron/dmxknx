import sys
import time
import usbdmx
import fhem
import time
from config import *

interfaces = usbdmx.scan()

if not interfaces:
    print "No interfaces found"
    sys.exit()

dmx = interfaces[0]
dmx.open()
dmx.mode(4)

suf = suffix_value
def suffix(val):
	if val < 128:
		return suffix_value
	else:
		return suffix_switch

def dmx_changed(channel, val):
	print "New value for channel %d: %d" % (channel+1, val)
	if last_change[channel] + min_pause > time.time():
		print "Not changing value"
		return False
	last_change[channel] = time.time()
	channel += 1
	if channels[channel] != '':
		knxchan = channels[channel] + suf
		if suf == suffix_value:
			fhem.set_value(knxchan, int(round(val/2.55)))
		elif val < 128:
			fhem.turn_off(knxchan)
		else:
			fhem.turn_on(knxchan)
	return True

last_change = [time.time()] * 512
dmx_old = [dmx.get_dmx(i) for i in range(512)] # TODO: manchmal null
print dmx_old

while True:
	for i in range(512):
		val = dmx.get_dmx(i)
		if i+1 == channel_switch:
			suf = suffix(val)
		if dmx_old[i] != val:
			if dmx_changed(i, val) == True:
				dmx_old[i] = val
	time.sleep(loop_pause)
