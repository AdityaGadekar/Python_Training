import xml.etree.ElementTree as ET
mytree = ET.parse('xmlexample/x1.xml')
myroot = mytree.getroot()
# print(myroot)
# print(myroot.tag)
# print(myroot.attrib)
# print(myroot[0].tag)
#
# for x in myroot[0]:
#     print(x.tag, x.attrib)
#
# for x in myroot[0]:
#     print(x.text)
#
# for x in myroot.findall('food'):
#     item = x.find('item').text
#     price = x.find('price').text
#     des = x.find('description').text
#     cal = x.find('calories').text
#     print(item,price,des,cal)

# XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
# <States>
#     <state name ="TELANGANA">
#         <rank>1</rank>
#         <neighbor name ="ANDHRA" language ="Telugu"/>
#         <neighbor name ="KARNATAKA" language ="Kannada"/>
#     </state>
#     <state name ="GUJARAT">
#         <rank>2</rank>
#         <neighbor name ="RAJASTHAN" direction ="N"/>
#         <neighbor name ="MADHYA PRADESH" direction ="E"/>
#     </state>
#     <state name ="KERALA">
#         <rank>3</rank>
#         <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
#     </state>
# </States>
# '''
#
# root = ET.fromstring(XMLexample_stored_in_a_string)
# # for neighbor in root.iter('neighbor'):
# #     print(neighbor.attrib)
# for state in root.findall('state'):
#     rank = state.find('rank').text
#     name = state.find('name')
#     print(rank, name)

for prices in myroot.iter('price'):
    prices.text = str(float(prices.text)+10)
    prices.set('newprices','yes')

ET.SubElement(myroot[0],"tasty")

for x in myroot.findall('food'):
    ET.SubElement(x,"Tasty")
for temp in myroot.iter('tasty'):
    temp.text = str("YES")

print(myroot.remove(myroot[1]))

#poping element
print(myroot[1][0].attrib.pop('name'))

mytree.write('modified.xml')