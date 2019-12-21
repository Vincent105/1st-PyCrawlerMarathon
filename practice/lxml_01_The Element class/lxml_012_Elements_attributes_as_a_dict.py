from lxml import etree

root = etree.Element("root", interesting="totally")
print(etree.tostring(root))

print(root.get("interesting"))
print(root.get("hello"))
root.set("hello", "vincent")
print(root.get("hello"))
print(sorted(root.keys()))
for name, value in sorted(root.items()):
    print('%s = %r' % (name, value))

attributes = root.attrib
print(attributes['interesting'])
print(attributes.get("no-such-attribute"))
print(attributes.get("interesting"))

attributes["hello"] = "vin105"
print(attributes["hello"])
print(root.get("hello"))
print(attributes.get("hello"))

d = dict(root.attrib)
print(sorted(d.items()))
