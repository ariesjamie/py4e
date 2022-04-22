#Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475 '
#Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

'''
input: a string 
output: the portion of the string as required 
'''

str = 'X-DSPAM-Confidence: 0.8475 '
colon = str.find(":")
print(colon)

sub_str = str[colon + 1:]
print(len(sub_str))
print(sub_str)
sub_str = sub_str.strip()
print(len(sub_str))
print(sub_str)
print(type(sub_str))
f_sub_str = float(sub_str)
print(f_sub_str)
print(type(f_sub_str))

