#base_conversion

#convert integer N to base B
numberToBaseB = lambda N, B: nTB(N,B,'') #iterative process
nTB = lambda N,B, CURR:  nTB(N//B, B, str(N%B) + CURR) if N > 0 else CURR

#convert from base B string to integers
bTN = lambda S, B, CURR: bTN(S[1:], B, int(S[0]) + B*CURR) if S else CURR
baseBtoN = lambda S, B: bTN(S,B,0) #iterative process

#convert from base B1 to base B2
b1tob2 = lambda B1,B2,STR_B1: numberToBaseB(baseBtoN(STR_B1,B1),B2)

#add two binary numbers
add_binary = lambda s1, s2: numberToBaseB(baseBtoN(s1,2) + baseBtoN(s2,2), 2)


#convert from b1 to b2 where b1, b2  < 30
#use A to Z for 10, ... 30
#so 10 goes to A
x1 = {i:str(i) for i in range(10)}
x2 = {i : chr(ord("A") + i - 10) for i in range(10,31)}
x1.update(x2)
digits = x1
reverse_digits = {v:k for k,v in digits.items()}

def convert(b1_str,b1,b2):
	return convert_to_base_b(convert_dec(b1_str,b1),b2)

def c_dec(b_str, b, curr):
	if not b_str:
		return curr
	return c_dec(b_str[1:], b, reverse_digits[b_str[0]] + b*curr)

def convert_dec(b_str,b):
	"""Convert a string in base b, b < 30 to decimal."""
	return c_dec(b_str, b, 0)

def c_to_b(n,b, curr):
	if n < 1:
		return curr
	return c_to_b(n//b,b,digits[n%b]+curr)

def convert_to_base_b(n,b):
	"""Convert a decimal to base b string."""
	return c_to_b(n,b,'')




