from lxml import etree

root = etree.XML('<root><a><b/></a></root>')

print(etree.tostring(root, xml_declaration=True))
print(etree.tostring(root, encoding='iso-8859-1'))
print(etree.tostring(root, pretty_print=True))

root = etree.XML('<html><head/><body><p>Hello<br/>World</p></body></html>')

print(etree.tostring(root))
print(etree.tostring(root, method='xml'))
print(etree.tostring(root, method='html'))
print(etree.tostring(root, method='html', pretty_print=True))
print(etree.tostring(root, method='text'))
print(etree.tostring(root, encoding='unicode', method='text'))

