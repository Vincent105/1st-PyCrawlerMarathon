from lxml import etree

root = etree.Element("root")
etree.SubElement(root, "child").text = "child 1"
etree.SubElement(root, "child").text = "child 2"
etree.SubElement(root, "another").text = "child 3"

print(etree.tostring(root, pretty_print=True))

for element in root.iter():
    print('%s - %s' % (element.tag, element.text))

for element in root.iter("child"):
    print('%s - %s' % (element.tag, element.text))

for element in root.iter("child", "another"):
    print('%s - %s' % (element.tag, element.text))

root.append(etree.Entity("#234"))
root.append(etree.Comment("some comment"))

for element in root.iter():
    if isinstance(element.tag, str):
        print('%s - %s' % (element.tag, element.text))
    else:
        print('%s - %s' % (element, element.text))

for element in root.iter(tag=etree.Element):
    print("%s - %s" % (element.tag, element.text))

for element in root.iter(tag=etree.Entity):
    print(element.text)