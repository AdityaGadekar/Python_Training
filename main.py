"""
text=" yeah i am learning python"
print(text=='yeah')
print(text.startswith('yeah'))
print(text.endswith('python'))
"""
import re
text = "11/27/2021"
if re.match(r'\d+/\d+/\+d', text):
    print("yes")
else:
    print("no")

text2 = "Toady is 11/22/2021 python start on 3/13/2021"
regex_exp = re.compile(r'\d+/\d+/\d+')
#print(regex_exp.findall(text2))
m = regex_exp.match(11/22/2021)
print(m.group(0))