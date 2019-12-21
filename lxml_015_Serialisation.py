from lxml import etree

root = etree.XML('<root><a><b/></a></root>')
print(etree.tostring(root))
print(etree.tostring(root,xml_declaration=True))
print(etree.tostring(root,encoding='iso-8859-1'))
print(etree.tostring(root,pretty_print=True))
