import pathlib
import xml.dom.minidom

data = pathlib.Path("test.xml")

with open(data, "w") as fh:
    fh.write("\ufeff")
    fh.write("<hello><bye>stuff</bye></hello>")
    fh.write("\n")

dom = xml.dom.minidom.parse(str(data))

for elem in dom.getElementsByTagName("bye"):
    elem.setAttribute("Permanent", "yes")

print(dom.toprettyxml())
