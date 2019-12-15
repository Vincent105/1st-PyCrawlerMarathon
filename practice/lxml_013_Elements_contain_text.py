from lxml import etree

root = etree.Element("root")
root.text = "TEXT"

print(root.text)
print(etree.tostring(root))
