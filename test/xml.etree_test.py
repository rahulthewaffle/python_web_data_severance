import xml.etree.ElementTree as ET

countrydata = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

root = ET.fromstring(countrydata)

# Top-level elements
print('\n')
print(root.findall("."))
print('\n')
# All 'neighbor' grand-children of 'country' children of the top-level elements
print(root.findall("./country/neighbor"))
print('\n')
# Nodes with name='Singapore' that have a 'year' child
print(root.findall(".//year/..[@name='Singapore']"))
print('\n')
# 'year' nodes that are children of nodes with name='Singapore'
print(root.findall(".//*[@name='Singapore']/year"))
print('\n')
print(root.findall(".//[@name='Singapore']/year"))
print('\n')
# All 'neighbor' nodes that are the second child of their parent
print(root.findall(".//neighbor[2]"))
print('\n')
