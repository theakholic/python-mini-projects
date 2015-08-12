"""
---add_bullets.py---
Add bullets to text copied to clipboard and copy the bulleted text to clipboard.
"""
import pyperclip

print('Accepted text to be copied.')
text = pyperclip.paste().decode()
#3print("TEXT = \n "+text)
lines = text.split('\n')

res = []
for line in lines:
	res.append('\t* ' + line)

##print("LINES:\n")
##print(res[:2])

##print("\n\n\n")
bulleted_text = '\n'.join(res)
pyperclip.copy(bulleted_text)
##print(bulleted_text)
print('Copying complete.')