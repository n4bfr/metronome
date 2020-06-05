#0.6 - Web display work

from datetime import datetime
import time
import cgitb

cgitb.enable()

count = 0
while (count < 60):
	count=count + 1

	clock = datetime.now()

	hour = clock.strftime("%H")
	minute = clock.strftime("%M")
	second  = clock.strftime("%S")
	micro = clock.strftime("%f")
	ms = round((float(micro)/10000))

	xms = round(10-(ms/10))

	xsec = round(59-float(second))
	if xsec < 10:
		xsec = "0" + str(xsec)

	xmin = round(59-float(minute))
	if xmin < 10:
		xmin = "0" + str(xmin)

	xhr = round(23-float(hour))
	if xhr < 10:
		xhr = "0" + str(xhr)

start_response('200 OK', [('Content-Type', 'text/html')])
#print("HR   MN   SE   MS   XMS  XS  XMIN  XHR")
	print(hour, minute, second, ms, xms, xsec, xmin, xhr)

#print('\nFormatted:',
#      time.strftime("%a %b %d %H:%M:%S:%f %Y"))

	time.sleep(.1)
