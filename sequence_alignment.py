#sequence alignment of DNA
import sys
sys.setrecursionlimit(10000)

def LCS(s1, s2):
	"""Use it or lose it, longest common substring."""
	if not s1 or not s2:
		return (0,'')
	if s1[0] == s2[0]:
		x = LCS(s1[1:], s2[1:])
		return (1 + x[0], s1[0] + x[1])
	
	x1,ans1 = LCS(s1[1:], s2)
	
	x2, ans2 = LCS(s1,s2[1:])
	return (x1,ans1) if x1 > x2 else (x2,ans2)


def fancyLCS(s1, s2):
	"""
	Take two strings S1 and S2 as input and return a list with three items:
	A number indicating the length of the longest common subsequence of these two strings,
	A copy of S1 and S2, but with the symbols that are
	      not used in the longest common subsequence replaced by # symbols

	>>> fancyLCS("human", "chimpanzee")
	[4, 'h#man', '#h#m#an###']
	"""
	if not s1:
		return (0, "","#"*len(s2))
	if not s2:
		return (0,"#"*len(s1), "")
	if s1[0] == s2[0]:
		lngth, curr_str1, curr_str2 = fancyLCS(s1[1:], s2[1:])
		return (lngth+1, s1[0]+curr_str1, s2[0]+curr_str2)

	len1, str11, str12  =  fancyLCS(s1[1:], s2)
	len2, str21,str22 = fancyLCS(s1,s2[1:])
	return (len1,"#" + str11, str12) if len1 > len2 else (len2, str21,"#" + str22)


def align(s1, s2):
	"""
	Align s1 and s2 using "-" characters.
	Return the length of the longest common subsequence and aligned strings
	>>> align("hi", "ship")
	(2, '-hi-', 'ship')
	"""

	if not s1:
		ans = (0, '-'*len(s2), s2)
		#print "returning: ", str(ans)
		return ans
	if not s2:
		ans = (0, s1, '-'*len(s1))
		#print "returning: ", str(ans)
		return ans

	if s1[0] == s2[0]:
		nxt_ln, nxt_s1, nxt_s2 = align(s1[1:], s2[1:])
		ans = (1+nxt_ln, s1[0]+nxt_s1, s2[0]+nxt_s2)
		#print "returning: ", str(ans)
		return ans

	#drop the second element.
	o1_len, o1_s1, o1_s2 = align(s1,s2[1:])

	#drop the first element
	o2_len, o2_s1, o2_s2 = align(s1[1:], s2)

	ans = (o1_len,'-'+o1_s1,s2[0]+o1_s2) if o1_len > o2_len else (o2_len, s1[0]+o2_s1,'-'+o2_s2)
	#print "returning: ", str(ans)
	return ans