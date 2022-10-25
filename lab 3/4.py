def build_xml_element(tag, content, **other):
    ans = '<'
    ans += tag
    ans += ' '
    for index, element in enumerate(other.items()):
        ans += element[0]
        ans += ' = \\"'
        ans += element[1]
        ans += '\\ \"'
    ans += '> ' + content + ' </'
    ans += tag
    ans += '>'
    return ans


print(build_xml_element("a", "Hello there", href=" http://python.org ",
                        _class=" my-link ", id=" someid "))
