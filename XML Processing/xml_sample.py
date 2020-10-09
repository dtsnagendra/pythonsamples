
import xml.etree.ElementTree as et

xml_data = et.parse('d:/sample/pythonsamples/XML Processing/country.xml')
root = xml_data.getroot()
#print(root)

#for child in root:
#    print(child.tag)
#    print(child.attrib)
#    print(child.get('name'))

#for child in root.findall('country'):
#    print(child.find('rank').text)
#    print(child.find('year').text)
#    print(child.get('name'))
'''
for r in root.iter('rank'):
    print(r.text)

for y in root.iter('year'):
    print(y.text)
'''

#reading xml file - select
# removing data from xml - delete
'''
for c in root.findall('country'):
    r = int(c.find('rank').text)
    if r > 50:
        print("removing rank",r)
        c.remove(c.find('rank'))

xml_data.write('d:/sample/pythonsamples/XML Processing/removed.xml')
'''
# update xml file
for c in root.findall('country'):
    r = int(c.find('rank').text)
    print(c.find('rank').text)
    c.find('rank').text = str(r + 1)
    
xml_data.write('d:/sample/pythonsamples/XML Processing/modified.xml')

'''
<books>
   <book name='' author =''>
      <price>5000</price>
      <publisheddate>24-Jul-2000</publisheddate>
      <noofpages>6500</noofpages>
   </book>
</books>
'''


