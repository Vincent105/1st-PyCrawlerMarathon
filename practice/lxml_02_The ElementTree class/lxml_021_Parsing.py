from lxml import etree
root = etree.XML('''\
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
    <a>&tasty;</a>
</root>
''')

tree = etree.ElementTree(root)
print(tree.docinfo.xml_version)
