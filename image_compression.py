#run length image compression
PENGUIN_IMG = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
SMILE = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
FIVE = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
PAD_MAX = 6# Because 64 is max so 6 bits
other = {"0": "1", "1": "0"}

def cmpress(binary_str,to_find="1"):
	"""Compress a binary_str of length 64 using run-length encoding."""
	if not binary_str:
		return []
	zero = 0
	one = binary_str.find(to_find)
	#why is there a zero!
	#can one = zero?
	if one == -1: #it's till the end
		one = len(binary_str) #eg "00" 2-0 = 9
	return [one-zero]+cmpress(binary_str[one:], other[to_find])

def left_pad(s,max_pad):
	return '0'*(max_pad-len(s)) + s
def compress(binary_str):
	#A better solution might be to transmit k, the number of bits of each term in the run-length sequence.
	# Now k<6 so the first 6 bits can be k.
	temp = map(lambda x: bin(x)[2:], cmpress(binary_str))
	
	return ''.join(map(lambda x: left_pad(x,PAD_MAX), temp))


def dc(cl,curr):
	if not cl:
		return ''
	return cl[0]*curr + dc(cl[1:],other[curr])

def to_list(compressed_str,PAD_MAX):
	if not compressed_str:
		return []
	return [int(compressed_str[:8],2)]+to_list(compressed_str[8:],PAD_MAX)


def decompress(compressed_str):
	#make the compressed_str into compressed_list
	assert len(compressed_str)%PAD_MAX == 0, "Illegal compressed str"
	compressed_list = to_list(compressed_str,PAD_MAX)
	return dc(compressed_list,'0')

