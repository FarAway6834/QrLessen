from conv2mylib import *
def core(file, url, scale):
	png(makeQRObj(url), file, scale)

def cores(file, url, scale = 3):
	core(file, url, scale)

def main():
	cores(input('f : '), input('url : '))

if __name__ == "__main__": main()