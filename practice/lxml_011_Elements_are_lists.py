from lxml import etree

# The Element class
root = etree.Element("root")
print(root.tag)

root.append(etree.Element("child1"))
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

print(etree.tostring(root, pretty_print=True))

'''
# Elements are lists
'''

child = root[0]
print(child.tag)
print(len(root))
print(root.index(root[1]))  # lxml.etree only!

childs = list(root)
for child in childs:
    print(child.tag)

root.insert(0, etree.Element("child0"))

childs = list(root)
for child in childs:
    print(child.tag)

start = root[:1]
end = root[-1:]
print(start[0].tag)
print(end[0].tag)
print(end[0].tag)

print(etree.iselement(root))
if len(root):   # this no longer works!
    print("The root element has children")

for child in root:
    print(child.tag)

root[0] = root[-1]  # this moves the element in lxml.etree!

for child in root:
    print(child.tag)

l = [0, 1, 2, 3]
l[0] = l[-1]
print(l)

print(root is root[0].getparent())

#   copy an element to a different position
from copy import deepcopy
element = etree.Element("neu")
element.append(deepcopy(root[1]))
print(element[0].tag)
print([c.tag for c in root])


print(root[0] is root[1].getprevious())
print(root[1] is root[0].getnext())