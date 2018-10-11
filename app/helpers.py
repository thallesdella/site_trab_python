import datetime

def date_now(pattern = '%d/%m/%Y %H:%M:%S'):
	str = '{{0:{}}}'.format(pattern)
	return str.format(datetime.datetime.now())