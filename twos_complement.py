#two's complement.


#I have an integer, if its postive cool.
NUM_BITS = 8
opposite = {"0": "1", "1": "0"} #X TO X+1 MOD 2
pad = lambda s, PAD_MAX: '0'*(PAD_MAX - len(s)) + s 
def two_complement(n):
	assert abs(n) < 2**(NUM_BITS - 1)
	if n >= 0:
		return pad(bin(n)[2:],8)
	#if its negative use ~x + 1
	first_part = bin(abs(n))[2:]
	second = ''.join(map(lambda x:opposite[x],first_part))
	return bin_add(second, bin(1)[2:],NUM_BITS)
