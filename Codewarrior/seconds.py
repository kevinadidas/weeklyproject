def make_readable(seconds):

	minute_b = seconds // 60
	minute_r = seconds % 60 

	hour_b = minute_b // 60 
	hour_r = minute_b % 60 

	print("%02d:%02d:%02d"  % (hour_b, hour_r, minute_r))
