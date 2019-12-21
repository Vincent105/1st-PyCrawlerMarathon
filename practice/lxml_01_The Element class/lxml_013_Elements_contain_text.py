from lxml import etree

root = etree.Element("root")
root.text = "TEXT"

print(root.text)
print(etree.tostring(root))

html = etree.Element("html")
body = etree.SubElement(html, "body")

# two properties .text and .tail
body.text = "TEXT"
print(etree.tostring(html))

br = etree.SubElement(body, "br")
print(etree.tostring(html))

br.tail = 'TAIL'
print(etree.tostring(html))

print(etree.tostring(br))
print(etree.tostring(br, with_tail=False))

print(etree.tostring(html, method="text"))
'''
Using XPath to find text
'''
print(html.xpath("string()"))   # lxml.etree only!
print(html.xpath("//text()"))   # lxml.etree only!

# Another way to extract the text content of a tree is XPath
build_text_list = etree.XPath("//text()") # lxml.etree only!
print(build_text_list(html))

texts = build_text_list(html)
print(texts[0])
print(texts[0].getparent().tag)
print(texts[1])
print(texts[1].getparent().tag)
print(texts[0].is_text)
print(texts[1].is_text)
print(texts[0].is_tail)
print(texts[1].is_tail)