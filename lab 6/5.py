import xml.etree.ElementTree as ET


def f(path, attrs):

    tree = ET.parse(path)
    root = tree.getroot()

    res = []
    for elem in root.iter():
        if any(elem.attrib.get(key) == value for key, value in attrs.items()):
            res.append(elem)

    return res


print(f("xml.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
