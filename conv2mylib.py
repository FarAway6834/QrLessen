from pyqrcode import makeQRObj
def gen(func):
	return lambda obj, f, scale : getattr(obj, func)(f, scale=scale)
def terminal(quiet_zone):
	return qrcode.terminal(quiet_zone=quiet_zone)
svg, eps = gen('svg'), gen('eps'), png('png')