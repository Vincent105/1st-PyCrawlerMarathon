from lxml import etree

root = etree.Element("root")
root.text = "TEXT"

print(root.text)
print(etree.tostring(root))

html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

print(etree.tostring(html))

br = etree.SubElement(body, "br")
