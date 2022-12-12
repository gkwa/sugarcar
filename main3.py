import codecs
import pathlib
import xml.dom.minidom

data = pathlib.Path("test.xml")

with open(data, "wb") as fh:
    fh.write(codecs.BOM_UTF16_LE)

with open(data, "a") as fh:
    fh.write("<hello><bye>stuff</bye></hello>")
    fh.write("\n")

dom = xml.dom.minidom.parse(str(data))

for elem in dom.getElementsByTagName("bye"):
    elem.setAttribute("Permanent", "yes")

print(dom.toprettyxml())
