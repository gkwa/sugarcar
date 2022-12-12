import pathlib
import xml.dom.minidom

data = pathlib.Path("test.xml")

with open(data, "w") as fh:
    fh.write("\ufeff")
    fh.write("<hello><bye>stuff</bye></hello>")
    fh.write("\n")

# strip bom
s = open(str(data), mode="r", encoding="utf-8-sig").read()
open(str(data), mode="w", encoding="utf-8").write(s)

dom = xml.dom.minidom.parse(str(data))

for elem in dom.getElementsByTagName("bye"):
    elem.setAttribute("Permanent", "yes")

print(dom.toprettyxml())
